---
workflow: general-video
flow: automation
storyboard: no
message: "Saya sendiri ada gout — jumpa Jus Gout, boleh dapatkan dekat beg kuning"
destination: tiktok
aspect: 1080x1920
language: ms
length: 53s
angle: testimonial-ugc
---

## Intent

Edit video talking-head (A-roll) tentang Jus Gout guna Hyperframes. Transcribe dulu,
buang ayat berulang, pause janggal dan gangguan, cari hook yang kuat, letak animation,
motion graphics dan sound FX di tempat yang patut. "Jangan render dulu final file.
Preview dulu."

## Assets

- assets/v1.mp4 — VID_20261012_171246.mp4 (Drive), A-roll talking head, 3:53, dirakam ter-mirror (kamera depan) → di-flip dalam composition
- assets/v2.mp4 — VID_20261012_172341.mp4 (Drive), B-roll produk tanpa suara; "Gunakan video 2 tu untuk jadikan overlay dalam video 1"

## Customizations

- Captions perkataan-demi-perkataan, kata kunci kuning (warna label produk)
- Hook kinetik "SIAPA DEKAT SINI / YANG ADA / GOUT?" + punch-in + impact
- Grafik: tag pengalaman sendiri, nota "rawatan & ubat doktor tetap penting", nama produk, cip bahan (Bromelain, Milk Thistle), "semak dulu", beg kuning, lencana harga promo, butang CTA check out
- SFX dari pustaka bundled HyperFrames (whoosh, pop, impact, chime, sparkle, ping, click)

## Notes

- Tiada muzik latar (katalog BGM perlukan akaun HeyGen); boleh tambah kemudian.
- Ayat "untuk sembuhkan gout" dikekalkan dalam audio seperti asal — perlu semakan pemilik sebelum iklan (dakwaan kesihatan).
- Cut list: data/edl.json → tools/build.py menjana index.html + compositions/.
