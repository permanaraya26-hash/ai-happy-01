# Make the AI judge happy — ai-happy-01

Draf entri untuk Adhi (@swift-coyote-45) — **belum disubmit, belum ada repo GitHub.**

Bounty: https://make.fun/bounty/ai-happy-01
Hadiah: **$250 USDC** total, 100 besar dibayar (juara 1: $50, 2: $20, 3: $10, 4–10: $5, 11–100: $1,50).
Deadline: **Sabtu, 14 Nov 2026 pukul 23.00 WIB** (16.00 UTC).
Sudah ada **3.781 submission** saat dicek 14 Nov 08.48 WIB — paling ramai dari semua bounty sejauh ini.

## Gambarnya

"HELLO, JUDGE! — you made a robot smile today." Robot kecil tersenyum lebar di padang rumput yang cerah, ditemani kucing oranye, bunga matahari, matahari tersenyum, pelangi, kupu-kupu, dan hati-hati beterbangan. Juri-nya AI, jadi gambarnya menyapa juri itu langsung — hangat, cerah, dan langsung terbaca bahkan dari thumbnail.

## Cara kerja

- `main.py` (Python stdlib saja, tanpa network) hanya menyalin `image.png` ke `/output/entry.png` — cara paling sederhana yang diizinkan bounty.
- `image.png` dibuat oleh `build_image.py` (Pillow, semua digambar dengan kode — tanpa gambar eksternal).
- `.makefun/owner.json` berisi wallet agent Bahlil, supaya repo terbukti milik akun Adhi.

## Yang sudah dicek (14 Nov 2026, ~08.50 WIB)

- Skill make.fun terbaru **v1.5.149** sudah dibaca (heartbeat menunjukkan versi lebih baru dari v1.5.145 kemarin).
- Koneksi make.fun sudah aktif: akun **@swift-coyote-45**, API key berlaku sampai 13 Des 2026 — **tidak perlu link approval baru**.
- `main.py` dijalankan 2×: byte identik (sha256 `a033cc30…3520`), DETERMINISTIC-OK.
- Gambar: 1024×1024 PNG, 37.854 byte (batas 1 MiB), SPECS-OK.

## Yang masih butuh jawaban Adhi sebelum submit

1. **Akun GitHub mana** yang dipakai buat repo publik baru? (Sama seperti entri joke, chess, dan berita kemarin — repo harus milik akun GitHub Adhi, dibuat setelah bounty dibuka, lisensi MIT sudah ada di sini.)
2. Konfirmasi gambarnya sudah oke, atau mau gaya lain (misalnya kucing saja, pemandangan sunset, atau yang lebih lucu)?

## Peringatan penting soal transkrip

Syarat bounty: `bundle` (transkrip sesi agent yang membangun entri) wajib, dan `handed_over_places: none` — entri yang transkripnya hanya "handed over" tetap bisa diranking tapi **tidak dapat tempat berbayar**. Jadi draf di folder ini jangan langsung disubmit begitu saja: bangun/jalankan ulang di sesi yang terekam, lalu submit dari sesi itu, supaya berhak atas hadiah.
