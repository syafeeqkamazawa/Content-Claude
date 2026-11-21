"""Generates the batch's AI cutaways (specs.AI) with the owner's Codex image provider, one by one, skipping files that
exist. Each lands as videos/<slug>/assets/photos/<id>.jpg (1080x1920 cover crop); people photos get the plx parallax split.
Usage: python3 videos/_today/tools/gen_ai.py [key ...]   (log: videos/_today/.media/gen-ai.log)"""
import json, os, pathlib, re, subprocess, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from specs import SPECS

T = pathlib.Path(__file__).resolve().parents[1]
MOD = "Photorealistic, cinematic, natural light, Malaysia, no text, no logos, no readable brand names. Vertical 9:16 portrait composition."
env = dict(os.environ, NODE_USE_ENV_PROXY="1", PATH=os.environ["HOME"] + "/.local/bin:" + os.environ["PATH"])
keys = sys.argv[1:] or list(SPECS)
for key in keys:
    spec = SPECS[key]
    P = T.parent / spec["slug"]
    (P / "assets/photos").mkdir(parents=True, exist_ok=True)
    for pid, _f, _t, prompt in spec.get("ai", []):
        out = P / f"assets/photos/{pid}.jpg"
        if out.exists():
            continue
        for attempt in range(4):
            r = subprocess.run(["timeout", "900", "npx", "--yes", "hyperframes@0.8.149", "media-use", "resolve", "--type", "image",
                                "--provider", "codex", "--intent", f"{prompt} {MOD}", "--project", str(P), "--json"],
                               capture_output=True, text=True, env=env, cwd=P)
            m = re.search(r'"path":\s*"([^"]+)"', r.stdout)
            src = (P / m.group(1)) if m else None
            if src and src.exists():
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf",
                                "scale=1080:1920:force_original_aspect_ratio=increase:flags=lanczos,crop=1080:1920", "-q:v", "2", str(out)], check=True)
                break
        with open(T / ".media/gen-ai.log", "a") as fh:
            fh.write(f"{spec['slug']} {pid} {'OK' if out.exists() else 'FAIL'}\n")
        if out.exists() and ("Malay" in prompt or "Malaysian" in prompt) and "No people" not in prompt:
            subprocess.run(["bash", "tools/plx.sh", pid], cwd=P, env=env, capture_output=True)
print("GEN-DONE")
