"""Electrova Waffle Maker #1 (13 Nov, folder "Elevtrova [sic] waffle maker dan Tepung waffle") — builds assets/a.mp4
from the owner's unboxing clip VID_20261113_090052 (src/090052.mp4: colours, weight, manual, the four plates, how
to swap them, timer, value, CTA) and the voiced cooking clip VID_20261113_092819 (src/092819.mp4: 'the moment of
truth', opens the maker on the square waffle), complete sentences ~0.5 s apart. assets/b.mp4 = the B-roll for the
cutaways (BROLL below, offsets saved in data/timeline.json).
Style (owner 12 Nov): motion overlay text + caption of the Jus Gout 'video contoh', visual overlays, talking kept.
"""
import json, pathlib, subprocess
P = pathlib.Path(__file__).resolve().parents[1]
PRE, POST, GAP_IN = 0.22, 0.32, 0.12
SRC = {"m": "src/090052.mp4", "r": "src/092819.mp4"}
CLIP = {"m": "090052", "r": "092819"}
# id, source, [(start, end) speech ranges], text
LINES = [
    ("M1", "m", [(5.02, 25.09)], "Pagi-pagi sarapan dengan anak-anak masak waffle sedap. Tepung dah beli, tapi mestilah ada tempat untuk masak dia. Yang ni aku boleh recommend untuk korang dapatkan dekat beg kuning, waffle maker daripada Electrova ni, memang mantap, memang padu."),
    ("M2", "m", [(31.36, 33.38)], "Ok, warna pun warna estetik guys."),
    ("M3", "m", [(70.14, 75.97), (76.29, 82.88)], "Dekat beg kuning guys, korang boleh pilih lah, ada dua kaler, satu kaler yang macam ni lah, satu lagi kaler merah. Ok, ikut kesesuaian tema rumah korang lah. Memang sangat lawa guys, serius, tak tipu korang."),
    ("M4", "m", [(83.71, 91.07)], "Oh lawa guys. Dia punya berat pun solid tau. Maknanya dia punya metal ni memang solid lah, berat."),
    ("M5", "m", [(92.26, 99.97)], "Buku manual ada, jangan risau. Korang boleh baca. Kalau korang malas baca takpe, aku cuba explain kat video ni."),
    ("M6", "m", [(114.21, 120.22)], "First kali guys, korang akan dapat tempat untuk masak waffle. Mantap guys."),
    ("M7", "m", [(128.90, 134.05), (134.94, 137.54), (139.39, 143.55), (145.25, 147.14)], "So bekas waffle ada, ada juga pattern ni, ni pattern bulat-bulat ya. Kalau korang nak buat bulat-bulat, korang boleh guna yang ni, acuan ni. Korang boleh juga guna ni. Banyak-banyak pattern guys, mantap. Ada empat pattern semua."),
    ("M8", "m", [(252.42, 253.98), (260.45, 263.23), (284.80, 293.89), (301.34, 304.03), (304.32, 307.23)], "Ini acuan yang pertama. Acuan kedua, ada jenis donat macam ni. Ok, seterusnya bentuk waffle ni guys. Bukan sahaja korang boleh buat waffle tau, korang boleh buat macam-macam bentuk sebenarnya. Lepas tu ni yang keempat, betul-betul bulat ni kan, biasa korang tengok kat gerai-gerai kan."),
    ("M9", "m", [(327.65, 331.81), (332.90, 334.50), (335.36, 337.44), (338.14, 339.49)], "Acuan ketiga dan acuan keempat guys, memang sangat lawa, banyak pilihan, sangat function."),
    ("M10", "m", [(344.03, 347.52), (380.80, 385.44), (386.21, 390.14), (391.74, 393.25), (402.85, 405.41), (405.76, 407.84), (409.41, 412.26), (417.41, 419.17), (425.73, 428.93)], "Tu macam mana cara nak ganti tempat acuan tu guys, aku tunjuk terus ke korang. Korang nak tukar acuan ni senang sahaja, korang tak ada button kat sini, korang tarik ke atas ataupun ke belakang, dah tercabut. So korang boleh tukar, contoh korang nak buat waffle kan, so korang hanya perlu masukkan sahaja dekat sini, dan tolak masuk ke dalam sampai bunyi. Pastikan dua ni masuk ke dalam. Nampak, so dah siap, cantik."),
    ("M11", "m", [(429.44, 430.62), (431.10, 433.70), (434.24, 439.74), (440.16, 441.86)], "Bila korang nak masak, korang boleh tutup sahaja, memang sangat lawa. Lepas tu ada timer kat sini, korang boleh set nak garing, nak crispy, nak garing, boleh set lama sikit lah."),
    ("R1", "r", [(3.90, 8.35), (11.78, 13.38), (14.37, 16.16)], "Okay guys, the moment of truth. Bismillah. Masya Allah, nampak sedap. Masya Allah."),
    ("M12", "m", [(448.48, 451.36), (455.01, 458.69)], "Harga ni pun mampu milik guys. Korang kata berbaloi lah dengan apa yang korang dapat ni, sangat berbaloi."),
    ("M13", "m", [(469.86, 471.42), (471.87, 473.66), (474.05, 475.74)], "Sampai dia melekat, dia lock kat sini. So guys, memang sangat kuat."),
    ("M14", "m", [(476.48, 484.60), (484.95, 487.40), (488.26, 492.45), (492.86, 493.60)], "Ok, berbaloi dengan barang dia, orang kata barang sampai dengan barang order tu sama kan, jangan risau insya Allah. Seller tengah buat harga promosi tu, sementara tengah ada diskaun, harga tengah murah tu, korang boleh beli awal-awal di beg kuning, insya Allah."),
]
DROPPED = ("090052: the repeated 'memang padap, memang padu' (28-30.6), 'jom buat ... sama-sama', the silent unboxing "
           "(36-70, 100-114, 121-128), 'ok' / 'ha' fillers, the long plate-counting stretch (147-252: 'satu, dua, tiga, "
           "kedua...'), the unclear 'ini memang dah pada ... sendiri' (254-259), the donut-plate fiddling and repeated "
           "plate names (263-284, 294-301, 308-327), the 'korang cungkih je, sekejap' tries (348-380), the repeated 'tarik ke "
           "belakang' and second swap demo (393-402, 413-425, 459-469), the unclear 'tak mahal ... hal virus' (452-454.6), "
           "'terima kasih' at the end; 092819: the pause before the lid opens (8.4-11.8)")
# B-roll for the cutaways, concatenated into assets/b.mp4 in this order: (clip, in, out)
BROLL = [("092000", 0.0, 82.3), ("092406", 0.0, 71.7), ("093613", 0.0, 43.5), ("095047", 0.0, 11.6), ("095121", 0.0, 11.2), ("095912", 100.0, 203.2)]

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
