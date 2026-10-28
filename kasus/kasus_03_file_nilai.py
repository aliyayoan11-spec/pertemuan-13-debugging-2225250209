# Simulasi pembacaan file nilai atau data list mahasiswa
data_nilai = [80, 60, 90, 70, 85]

def proses_data(nilai_list):
    if len(nilai_list) == 0:
        return "Data kosong"
    return f"Jumlah data: {len(nilai_list)}, Rata-rata: {sum(nilai_list)/len(nilai_list)}"

print(proses_data(data_nilai))