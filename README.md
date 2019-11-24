 <h1 align=center>Praktikum 4

## <p align=center>Buat program sederhana untuk <br>menambahkan data kedalam sebuah list<br> dengan rincian sebagai berikut:
• Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
• Tampilkan pertanyaan untuk menambah data (y/t?), 
apabila jawaban
t (Tidak), maka program akan menampilkan daftar datanya. 
• Nilai Akhir diambil dari perhitungan 3 komponen nilai 
(tugas: 30%, uts: 35%, uas: 35%)
• Buat flowchart dan penjelasan programnya pada README.md. • Commit dan push repository ke github.

**Flowchart :**

![Flowchart](https://github.com/antonmartinus72/Praktikum_4/blob/master/img/Flowchart.png)

**Kode :**

    daftar = []
    no = 1
Kode di atas digunakan untuk mendeklarasikan list daftar yang nanti akan di isi. `no = 1` adalah variabel nomor.

**Kode :**
Disini saya menggunakan perulangan `While True:` agar perulangan terus terjadi.
**Kode :**

    while True:  
	    nama = input("Nama: ")  
	    nim = input("NIM: ")  
	    nilai_t = int(input("Nilai Tugas: "))  
	    nilai_uts = int(input( "Nilai UTS: " ))  
	    nilai_uas = int(input( "Nilai UAS: " ))

Untuk Perhitungan persentase dilakukan seperti ini :
**Kode :** 

    a = nilai_t*30/100  
    b = nilai_uts*35/100  
    c = nilai_uas*35/100  
    nilai_akhir = a+b+c
Hasil dari operator `a`, `b`, dan `c` akan di jumlahkan ke dalam variabel `nilai_akhir`.

Selanjutnya memasukan variabel ke dalam fungsi **list**.
**Kode :**

    daftar.append([no, nama, nim, nilai_t, nilai_uts, nilai_uas, nilai_akhir])
List ini akan digabung ke dalam variabel `daftar`  yang nantinya akan dibuat menjadi tabel.

Perintah ini digunakan untuk menambah variabel nomor dengan 1 setiap ada perulangan agar setiap perulangan memiliki nomor yang berbeda.
**Kode :**
   

    no += 1
 
Perintah di bawah ini digunakan untuk menghentikan perulangan jika user menginput "tidak". Jika hasilnya adalah false maka perulangan akan terjadi kembali dengan menginputkan kembali data. `.lower`digunakan untuk mengubah input yang kita masukan menjadi huruf kecil dan tujuan didalam kode ini adalah untuk membuat ***case sensitive*** tidak berlaku saat melakukan input "TIdAK".
**Kode :**

    keluar = input("Lanjut? (Ya/Tidak): ")  
    if keluar.lower() == "tidak":  
        break
  
Selanjutnya list akan di print di dalam perulangan for.
**Kode :**

    for x in daftar:  
        print("| {no:3} | {nama:12} "  
		      "|  {nim:6} | {tugas:7} " 
		      "| {uts:5} |{uas:5} " 
		      "| {akhir:7.2f} |"  
		      .format(no=x[0], 
		      nama=x[1],nim=x[2], 
		      tugas=x[3],uts=x[4], 
		      uas=x[5],akhir=x[6]))
Perulangan `for x in daftar:` akan mengambil list dari setiap perulangan variabel `daftar` yang terjadi dan akan disimpan ke dalam variabel `x`, lalu `x` akan di format untuk meletakan data yang disimpan ke dalam placeholder `{}`yang terdapat pada string. `.2f` dalam string digunakan untuk menampilkan 2 angka float.

### Output yang didapat :

![Output](https://github.com/antonmartinus72/Praktikum_4/blob/master/img/Output.PNG)


<p align=center>
Anton Martinus A.A.Y
<br>
TI.19.A.1
<br>
<a>https://github.com/antonmartinus72/labpy03