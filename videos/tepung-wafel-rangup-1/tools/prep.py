"""Tepung Wafel Rangup #1 (13 Nov, folder "Elevtrova waffle maker dan Tepung waffle") — builds assets/a.mp4
from the owner's talking clip VID_20261113_084758 (src/084758.mp4: the flour pack, restock, how to mix, CTA) and the
voiced cooking clip VID_20261113_092656 (src/092656.mp4: opens the waffle maker on the finished waffle), complete
sentences ~0.5 s apart. assets/b.mp4 = the B-roll for the cutaways (BROLL below, offsets saved in data/timeline.json).
Style (owner 12 Nov): motion overlay text + caption of the Jus Gout 'video contoh', visual overlays, talking kept.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"t": "src/084758.mp4", "h": "src/092656.mp4"}
CLIP = {"t": "084758", "h": "092656"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("T1", "t", [(29.92, 36.64)], "Anak-anak aku, termasuk aku sekali, dah berebut-rebut bila dah buat waffle pakai tepung ni je."),
    ("T2", "t", [(6.32, 8.99)], "Korang tahu tak, ni tepung waffle."),
    ("T3", "t", [(19.42, 28.32)], "Ni masuk kali kedua aku dah restock tepung untuk buat waffle. Memang sedap sangat."),
    ("T4", "t", [(37.34, 42.28)], "Sekarang ni packaging dah makin cantik tau. Dulu nampak stiker je satu."),
    ("T5", "t", [(42.50, 49.90), (52.06, 53.20)], "Inilah tengok, menunjukkan betapa high demand, ramai sambutan yang sangat memberangsangkan orang beli tepung ni."),
    ("T6", "t", [(53.32, 59.68)], "Memang sedap, memang tak tipu korang. Ni orang tu beli tu, beli dua tu. Sebab memang sedap."),
    ("T7", "t", [(60.88, 62.58), (62.92, 66.10), (66.48, 72.18), (72.66, 75.82)], "Korang belilah. Cara ni mudah sahaja. Korang campur tepung ni, dekat sini pun dah ada tulis lah. Korang campur je tepung ni dengan air, minyak dan telur sahaja. Lepas tu korang kacau-kacau-kacau, dah boleh, dah boleh masak."),
    ("T8", "t", [(76.16, 80.92)], "Dah boleh letak dekat tempat acuan waffle ataupun dalam kuali pun tak masalah."),
    ("H1", "h", [(1.98, 6.02), (6.82, 12.00)], "Guys, hasil tepung dia guys, korang tengok eh. Bismillah. Masya Allah, masya Allah. Kalau korang nak garing lagi, korang boleh biar lama lah."),
    ("H2", "h", [(13.44, 15.97), (16.64, 21.76)], "Ni hasil guna tepung waffle yang tadi tu guys, korang tengok. Oh masya Allah, cantik guys."),
    ("T9", "t", [(82.14, 85.46)], "Tu korang belilah, memang anak-anak insya Allah memang suka."),
    ("T10", "t", [(90.68, 97.04)], "Siap boleh, anak-anak aku buat sarapan, buat bekal pergi sekolah pun boleh juga."),
    ("T11", "t", [(98.48, 99.34), (99.62, 100.50)], "Dengan coklat boleh, dengan kaya pun boleh."),
    ("H3", "h", [(25.82, 28.35), (28.66, 29.86)], "So jangan tunggu lagi, anak-anak sedang menunggu tu, untuk korang buat untuk dia orang."),
    ("T12", "t", [(118.92, 122.86), (123.04, 124.86), (125.56, 126.52), (127.08, 128.36)], "Guys, tengok dekat beg kuning, kalau ada voucher boleh claim. Kalau harga tengah murah tu, korang belilah awal-awal, sebelum harga ni naik balik."),
]
DROPPED = ("084758: 'ok aku dah' (2-3.5), the drawn-out 'masuk, masuk' before the restock line, the first 'anak-anak' "
           "(stutter), 'sambutan apa tu' (repeat), 'ok' fillers, the unclear 'anak-anak pun dah ...' tail (85.7-87.6), "
           "'ha?' / 'memang' / 'ok?' between lines, and the 'no gluten / free gluten, kita nak cari yang sihat, baik untuk "
           "badan' passage (101.8-117.7: health claim not shown on the pack — CLAUDE.md 5 Nov TikTok-risk rule); "
           "092656: 'ok' fillers, the long 'guys' (22-24.6) and the second CTA 'dapatkan di beg kuning, supaya harga masih "
           "dalam promosi' (30-34.2, repeats T12)")
# B-roll for the cutaways, concatenated into assets/b.mp4 in this order: (clip, in, out)
BROLL = [("091202", 0.0, 28.2), ("091251", 0.0, 47.4), ("091338", 0.0, 45.5), ("092709", 0.0, 5.2), ("095912", 0.0, 100.0)]

# (line, source time the shot starts or None = line start, clip, clip in, crop)
SHOTS = [(lid, None, CLIP[src], "sync", None) for lid, src, *_ in LINES]
VF = {None: "scale=1080:1920,setsar=1"}


def run(*a): subprocess.run(a, check=True)


def layout():
    t, out = 0.0, {}
    for lid, src, rng, txt in LINES:
        pieces = []
        for k, (a, b) in enumerate(rng):
            s0 = a - (PRE if k == 0 else GAP_IN)
            s1 = b + (POST if k == len(rng) - 1 else GAP_IN)
            pieces.append((round(s0, 3), round(s1, 3)))
        dur = sum(b - a for a, b in pieces)
        out[lid] = dict(src=src, pieces=pieces, e0=round(t, 3), e1=round(t + dur, 3), text=txt)
        t += dur
    return out, round(t, 3)


def e_of(L, lid, s):
    """source time inside line lid -> edit time"""
    acc = L[lid]["e0"]
    for a, b in L[lid]["pieces"]:
        if s <= b:
            return round(acc + max(0.0, s - a), 3)
        acc += b - a
    return round(acc, 3)


def main():
    L, TOTAL = layout()
    tmp = P / ".media/prep"; tmp.mkdir(parents=True, exist_ok=True)
    gain = {}
    for src, inp in SRC.items():
        rng = [p for d in L.values() if d["src"] == src for p in d["pieces"]]
        sel = "+".join(f"between(t,{a},{b})" for a, b in rng)
        r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(P / inp), "-vn", "-af",
                            f"aselect='{sel}',asetpts=N/SR/TB,highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,"
                            "loudnorm=I=-15:print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
        js = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
        gain[src] = round(-13.3 - float(js["input_i"]), 2)
    print("gain", gain)
    idx = {k: i for i, k in enumerate(SRC)}
    flt, parts, n = [], [], 0
    for lid, d in L.items():
        for a, b in d["pieces"]:
            dur = b - a
            flt.append(f"[{idx[d['src']]}:a]atrim={a}:{b},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=mono,"
                       f"highpass=f=75,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,volume={gain[d['src']]}dB,"
                       f"afade=t=in:d=0.03,afade=t=out:st={dur-0.05:.3f}:d=0.05[p{n}]")
            parts.append(f"[p{n}]"); n += 1
    flt.append("".join(parts) + f"concat=n={n}:v=0:a=1,alimiter=limit=0.89:level=false[a]")
    args = []
    for inp in SRC.values():
        args += ["-i", str(P / inp)]
    run("ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(flt), "-map", "[a]", "-ar", "48000", "-ac", "2",
        "-c:a", "pcm_s16le", str(tmp / "voice.wav"))
    # picture: synced shots follow the line's own pieces; others play straight
    segs = []
    for k, (lid, t, clip, cin, crop) in enumerate(SHOTS):
        a = L[lid]["e0"] if t is None else e_of(L, lid, t)
        b = (L[SHOTS[k + 1][0]]["e0"] if SHOTS[k + 1][1] is None else e_of(L, SHOTS[k + 1][0], SHOTS[k + 1][1])) if k + 1 < len(SHOTS) else TOTAL
        if cin == "sync":
            for pa, pb in L[lid]["pieces"]:
                segs.append((clip, pa, round(pb - pa, 3), crop))
        else:
            segs.append((clip, cin, round(b - a, 3), crop))
        print(f"{a:7.2f}-{b:7.2f}  {lid} {clip} @{cin}")
    lst = []
    for k, (clip, cin, dur, crop) in enumerate(segs):
        out = tmp / f"s{k:02d}.mp4"
        run("ffmpeg", "-v", "error", "-y", "-ss", str(cin), "-t", str(round(dur + 0.1, 3)), "-i", str(P / f"src/{clip}.mp4"),
            "-vf", f"{VF[crop]},fps=60,trim=duration={dur}", "-an",
            "-c:v", "libx264", "-preset", "fast", "-crf", "14", "-pix_fmt", "yuv420p", str(out))
        lst.append(f"file '{out}'")
    (tmp / "list.txt").write_text("\n".join(lst) + "\n")
    run("ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-i", str(tmp / "voice.wav"),
        "-map", "0:v", "-map", "1:a", "-c:v", "libx264", "-preset", "fast", "-crf", "15", "-r", "60", "-g", "30",
        "-c:a", "aac", "-b:a", "192k", str(P / "assets/a.mp4"))
    bidx, off, inp, fl = {}, 0.0, [], []
    for k, (clip, a, b) in enumerate(BROLL):
        inp += ["-ss", str(a), "-t", str(b - a), "-i", str(P / f"src/{clip}.mp4")]
        fl.append(f"[{k}:v]scale=1080:1920,setsar=1,fps=60,trim=duration={b - a},setpts=PTS-STARTPTS[v{k}]")
        bidx[clip] = {"offset": round(off, 3), "in": a}
        off += b - a
    fl.append("".join(f"[v{k}]" for k in range(len(BROLL))) + f"concat=n={len(BROLL)}:v=1:a=0[v]")
    run("ffmpeg", "-v", "error", "-y", *inp, "-filter_complex", ";".join(fl), "-map", "[v]", "-c:v", "libx264", "-preset", "fast",
        "-crf", "17", "-pix_fmt", "yuv420p", "-g", "30", str(P / "assets/b.mp4"))
    (P / "data/timeline.json").write_text(json.dumps({"lines": L, "total": TOTAL, "dropped": DROPPED, "broll": bidx}, indent=1, ensure_ascii=False))
    print("TOTAL", TOTAL)


if __name__ == "__main__":
    main()
