print(">***=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=***<")
print("                     MANIPULASI DAN OPERASI LIST")
print(">***=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=***<")
print("\n")
# 1. Diberikan list berikut: 
Kendaraan = ['motor', 'mobil', 'sepeda', 'bus']
print(f"1. Diketahui list berikut! \n{Kendaraan}")

print("\na. Tambahkan 'truk' di akhir list") 
Kendaraan.append('truk')
print(Kendaraan)

print("\nb. Sisipkan becak' pada index ke-1") 
Kendaraan.insert(1, 'becak')
print(Kendaraan)

print("\nc. Hapus data yang berada paling belakang dari list tersebut.") 
Kendaraan.pop()
print(Kendaraan)

print("\nd. Ubah elemen 'sepeda' menjadi 'skuter'.") 
Kendaraan[2] = 'skuter'
print(Kendaraan)
print("\ne. Tampilkan informasi jumlah total data di dalam list tersebut")
Jumlah_Data = len(Kendaraan)
print(f"Jumlah data pada list adalah {Jumlah_Data}")
print("------------------------------------------------------------------")

# 2. Diberikan list berikut: 
Angka = [75, 80, 90, 75, 85, 100, 65]
print(f"\n2. Diberikan list berikut:\n{Angka}") 

print("\na. Cari tahu di indeks ke berapa skor 100 berada.")
Index_100 = Angka.index(100)
print(f"Skor 100 berada di index ke {Index_100}")

print("\nb. Hitung ada berapa banyak siswa yang mendapatkan skor 75.")
Jumlah_Skor75 = Angka.count(75)
print(f"Siswa yang mendapatkan skor 75 sebanyak {Jumlah_Skor75}")

print("\nc. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar.")
Angka.sort()
print(f"Skor urut adalah {Angka}")

print("\nd. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.")
Angka.reverse
print(f"Urutan skor dari terbesar ke terkecil adalah \n{Angka}")
print("------------------------------------------------------------------")

# 3. Gabungkan menu_tambahan ke dalam menu_utama menggunakan fungsi, 
# kemudian tampilkan hasil dari data gabungan tersebut. 
print("\n3. Gabungkan dan tampilkan menu tambahan ke dalam menu utama!")
Menu_Utama = ["Nasi Goreng", "Mie Ayam"]
print(f"Diketahui list menu utama       : \n{Menu_Utama}")
Menu_Tambahan = ["Kerupuk", "Es Teh"] 
print(f"Diketahui list menu tambahan    : \n{Menu_Tambahan}")

Menu_Utama.extend(Menu_Tambahan)
print(f"Menu utama dan menu tambahan adalah {Menu_Utama}")
print("------------------------------------------------------------------")

# 4. Diberikan data nested list berupa informasi nama barang dan harganya: 
Data_Barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]
print(f"\n 4. Diketahui data barang dengan nested list berikut ini: \n{Data_Barang}") 

print("\na. Tampilkan harga dari \"Pensil\" (yaitu 2000)") 
print("dengan memanggil indeks baris dan kolom yang spesifik dari list tersebut.")
Harga_Pensil = Data_Barang[1][1]  
print(f"Harga Pensil    : {Harga_Pensil}")

print("\nb. Gunakan perulangan untuk membaca data satu per satu,")
print("lalu tampilkan output dengan format: \"Nama: [nama barang], Harga: [harga]\" untuk setiap elemen di dalamnya.")
for barang in Data_Barang :
    print(f"Nama    : {barang[0]}")
    print(f"Harga   : {barang[1]}\n")

print(">***=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=***<")
















