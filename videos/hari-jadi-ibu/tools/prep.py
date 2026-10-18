"""Prepare the family photos: fix EXIF rotation, make a print-size copy and a
blurred, darkened 1080x1920 background plate for each (src/photos -> assets/photos)."""
import glob, os
from PIL import Image, ImageOps, ImageFilter, ImageEnhance

os.makedirs("assets/photos", exist_ok=True)
for f in sorted(glob.glob("src/photos/p*.jpg")):
    name = os.path.splitext(os.path.basename(f))[0]
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    pr = im.copy(); pr.thumbnail((1600, 1600), Image.LANCZOS)
    pr.save(f"assets/photos/{name}.jpg", quality=90)
    bg = ImageOps.fit(im, (540, 960), Image.LANCZOS).filter(ImageFilter.GaussianBlur(22))
    bg = ImageEnhance.Brightness(ImageEnhance.Color(bg).enhance(0.8)).enhance(0.55)
    bg.resize((1080, 1920), Image.LANCZOS).save(f"assets/photos/{name}-bg.jpg", quality=85)
    print(name, pr.size)
