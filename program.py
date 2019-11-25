daftar = []
no = 1

# Perulangan
while True:
    # Input
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai_t = int(input("Nilai Tugas: "))
    nilai_uts = int(input( "Nilai UTS: " ))
    nilai_uas = int(input( "Nilai UAS: " ))
    # Menghitung persentase nilai
    a = nilai_t*30/100
    b = nilai_uts*35/100
    c = nilai_uas*35/100
    nilai_akhir = a+b+c
    # Menggabungkan variabel ke dalam bentuk list
    daftar.append([no, nama, nim, nilai_t, nilai_uts, nilai_uas, nilai_akhir])
    # Membuat nomor dalam tabel
    no += 1
    # Perintah untuk berhenti
    keluar = input("Lanjut? (Ya/Tidak): ")
    if keluar.lower() == "tidak":
        break

# Membuat tabel
print("|==================================================================|")
print("| No. |     Nama     |   NIM   |  Tugas  |  UTS  |  UAS  |  Akhir  |")
print("|==================================================================|")
# Perulangan
for x in daftar:
    print("| {no:3} | {nama:12} "
          "|  {nim:6} | {tugas:7} "
          "| {uts:5} | {uas:5} "
          "| {akhir:7.2f} |"
            # Format print
          .format(no=x[0], nama=x[1],
                  nim=x[2], tugas=x[3],
                  uts=x[4], uas=x[5],
                  akhir=x[6]))
print("|==================================================================|")