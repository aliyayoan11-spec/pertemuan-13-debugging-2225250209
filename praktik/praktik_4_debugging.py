def hitung_rata_rata(nilai):
    # Perbaikan B01: Mencegah ZeroDivisionError jika list kosong dan 
    # memperbaiki pembagi agar menyesuaikan panjang data (tidak hardcode /5)
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status(nilai):
    # Perbaikan B02: Memperbaiki operator pembanding batas kelulusan dari '>' menjadi '>='
    if nilai >= 60:
        return "Lulus"
    return "Tidak lulus"

def nilai_tertinggi(nilai):
    # Perbaikan B03: Mencegah error jika list kosong dan memperbaiki logika pencarian nilai max (< menjadi >)
    if len(nilai) == 0:
        return None
    tertinggi = nilai[0]
    for x in nilai[1:]:
        if x > tertinggi:
            tertinggi = x
    return tertinggi

# Pengujian Program
nilai = [80, 60, 90, 70]
print("Rata-rata:", hitung_rata_rata(nilai))
print("Status 60:", status(60))
print("Tertinggi:", nilai_tertinggi(nilai))