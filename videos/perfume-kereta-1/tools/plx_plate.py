#!/usr/bin/env python3
"""Layers for a moving overlay.

fg.png (from remove-background) is rewritten as the original photo masked by the cut-out
grown by a few pixels and feathered, so its edge carries real background texture; the plate
(out.jpg) has that same area filled with the colours of the surroundings (normalised-
convolution blur), so neither layer shows a ghost, glow or seam when they drift apart.
Usage: plx_plate.py photo.jpg fg.png out.jpg"""
import sys
import numpy as np
from PIL import Image, ImageFilter

src, fg, out = sys.argv[1:4]
img = np.asarray(Image.open(src).convert("RGB"), dtype=np.float32)
alpha = Image.open(fg).getchannel("A")
# grow the hole a little past the cut-out edge so no subject pixels stay in the plate
grown = alpha.filter(ImageFilter.MaxFilter(17))
hole = np.asarray(grown, dtype=np.float32) / 255.0
keep = 1.0 - np.clip(hole * 3.0, 0, 1)
# foreground layer: original pixels inside the grown cut-out, edge feathered
fg_alpha = grown.filter(ImageFilter.GaussianBlur(4))
Image.merge("RGBA", (*Image.open(src).convert("RGB").split(), fg_alpha)).save(fg)


def blur(a, r):
    """Large separable box blur (three passes ≈ gaussian) via cumulative sums."""
    for _ in range(3):
        for ax in (0, 1):
            c = np.cumsum(np.pad(a, [(r + 1, r) if i == ax else (0, 0) for i in range(a.ndim)], mode="edge"), axis=ax)
            hi = np.take(c, np.arange(2 * r + 1, c.shape[ax]), axis=ax)
            lo = np.take(c, np.arange(0, c.shape[ax] - 2 * r - 1), axis=ax)
            a = (hi - lo) / (2 * r + 1)
    return a


num = blur(img * keep[..., None], 40)
den = blur(keep, 40)[..., None]
fill = num / np.maximum(den, 1e-3)
# where the hole is very wide, the normalised blur can still be empty — fall back to a wider pass
num2, den2 = blur(img * keep[..., None], 120), blur(keep, 120)[..., None]
fill = np.where(den > 0.02, fill, num2 / np.maximum(den2, 1e-3))
w = np.clip(hole * 3.0, 0, 1)[..., None]
plate = img * (1 - w) + fill * w
Image.fromarray(np.clip(plate, 0, 255).astype(np.uint8)).save(out, quality=92)
