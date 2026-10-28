# Pertemuan 13 - Debugging dan Testing
Nama: Aliya Yoan Ramadhani
NIM: 2225250209
Kelas: 3 B

## Kasus
Praktik 4 berfokus pada investigasi, identifikasi, dan perbaikan tiga bug utama pada fungsi pengolahan nilai mahasiswa (penghitungan rata-rata, penentuan status kelulusan, dan pencarian nilai tertinggi).

## Test Case & Retest
| ID | Target | Input | Expected | Actual Awal | Status Awal | Status Akhir (Retest) |
|---|---|---|---|---|---|---|
| T1 | rata-rata | [80, 60, 90, 70] | 75.0 | 60.0 | FAIL | PASS |
| T2 | rata-rata | [100, 80] | 90.0 | 36.0 | FAIL | PASS |
| T3 | status | 60 | Lulus | Tidak lulus | FAIL | PASS |
| T4 | status | 59 | Tidak lulus | Tidak lulus | PASS | PASS |
| T5 | tertinggi | [80, 60, 90, 70] | 90 | 0 | FAIL | PASS |

## Bug Report

### Bug 1 (B01) - Rata-rata Tidak Akurat
- **Gejala:** Hasil rata-rata untuk list `[80, 60, 90, 70]` bernilai `60.0` (seharusnya `75.0`) karena pembagi di-hardcode dengan angka `5`.
- **Lokasi:** Fungsi `hitung_rata_rata`, baris `return sum(nilai) / 5`.
- **Akar Penyebab:** Pembuat kode menggunakan pembagi tetap `5` alih-alih menyesuaikan dengan panjang data (`len(nilai)`).
- **Perbaikan:** Mengganti penyebut dengan `len(nilai)` serta menambahkan validasi list kosong.

### Bug 2 (B02) - Bug Batas Status Kelulusan
- **Gejala:** Input nilai tepat `60` menghasilkan `"Tidak lulus"`.
- **Lokasi:** Fungsi `status`, baris `if nilai > 60:`.
- **Akar Penyebab:** Penggunaan operator strict inequality (`>`) alih-alih inclusive inequality (`>=`) untuk nilai batas kelulusan.
- **Perbaikan:** Mengubah operator menjadi `if nilai >= 60:`.

### Bug 3 (B03) - Kesalahan Logika Nilai Tertinggi
- **Gejala:** Fungsi selalu mengembalikan nilai `0` karena inisialisasi variabel `tertinggi = 0` dan kesalahan arah operator perbandingan (`<`).
- **Lokasi:** Fungsi `nilai_tertinggi`.
- **Akar Penyebab:** Variabel pembanding diinisialisasi dengan angka `0` (yang lebih kecil dari elemen list positif) dan kondisi `if x < tertinggi` mencari nilai terkecil bukan terbesar.
- **Perbaikan:** Mengubah inisialisasi ke elemen pertama list (`nilai[0]`) dan membalik operator menjadi `if x > tertinggi`.

## Cara Menjalankan
```bash
python3 praktik/praktik_4_debugging.py