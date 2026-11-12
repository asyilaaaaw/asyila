print("\n==========================================")
print("         1. Tuple dan Set")
print("==========================================")

# a. Buatlah sebuah Tuple bernama mahasiswa yang berisi 3 data diri: ("Nama", "NIM", "Prodi")
print("--- Bagian 1.a: Tuple ---")
mahasiswa = ("Asyila Wadda Nafi'ah", "240101001", "Teknologi Informasi")
print(f"Data Mahasiswa : {mahasiswa}")

# b. Tampilkan data NIM dan Prodi ke layar dengan cara mengakses indeksnya.
print("--- Bagian 1.b: Akses Tuple ---")
print(f"NIM   : {mahasiswa[1]}")
print(f"Prodi : {mahasiswa[2]}")

# c. Coba jalankan kode mahasiswa[2] = "Teknologi Informasi". Amati pesan error yang muncul, 
# lalu jelaskan mengapa hal tersebut terjadi.
print("\n--- Bagian 1.c: Immutable Tuple ---")
# mahasiswa[2] = "Teknologi Informasi"
print("Pesan Error: \'tuple\' object does not support item assignment")
print("Penjelasan: Tuple bersifat immutable (tidak dapat diubah setelah dibuat), "
    "\nsehingga elemen di dalamnya tidak bisa dimodifikasi atau diganti nilainya.")

# d. Buatlah sebuah Set bernama nilai_angka dari barisan angka berikut: 10, 4, 3, 2, 4, 10, 7, 5. 
# Cetak nilai_angka ke layar dan jelaskan apa yang terjadi pada angka 10 dan 4 yang ditulis dua kali!
print("\n--- Bagian 1.d: Set (Himpunan) ---")
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print(f"Isi nilai_angka: {nilai_angka}")
print("Penjelasan: Set secara otomatis menghilangkan duplikasi data. "
    "\nAngka 10 dan 4 yang ditulis dua kali hanya akan disimpan dan dicetak satu kali saja.")


print("\n==========================================")
print("        2. Manipulasi Dictionary")
print("==========================================")

# a. Buatlah dictionary bernama data_mahasiswa
print("a. Buatlah dictionary bernama data_mahasiswa")
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(f"Data Mahasiswa  : {data_mahasiswa}")

# b. Ubah nilai "prodi" menjadi "Sastra Mesin" sekaligus menambahkan key baru "angkatan" dengan nilai 2026.
print("\nb. Ubah nilai \"prodi\" menjadi \"Sastra Mesin\" sekaligus menambahkan key baru \"angkatan\" dengan nilai 2026.")
data_mahasiswa["prodi"] = "Sastra Mesin"
data_mahasiswa["angkatan"] = 2026
print(f"Setelah diubah & ditambah           : {data_mahasiswa}")

# c. Hapus data "nim", lalu tampilkan hasil akhir dictionary ke layar.
print("\nc. Hapus data \"nim\", lalu tampilkan hasil akhir dictionary ke layar.")
del data_mahasiswa["nim"]
print(f"Hasil akhir setelah 'nim' dihapus   : {data_mahasiswa}")


print("\n==========================================")
print("     3. Perulangan pada Dictionary")
print("==========================================")

# a. Buatlah dictionary bernama keranjang dengan data harga buah
keranjang = {
    "apel"  : 5000, 
    "pisang": 3000, 
    "jeruk" : 7000, 
    "anggur": 15000
}
print(keranjang)

# b. Gunakan perulangan untuk menampilkan setiap barang dan harganya dengan format: "Harga apel: Rp 5000"
print("Daftar Harga Buah:")
for buah, harga in keranjang.items():
    print(f"Harga {buah}   : Rp {harga}")

# c. Tampilkan total belanja (menjumlahkan seluruh nilai/harga pada dictionary)
total_belanja = sum(keranjang.values())
print(f"\nTotal belanja keseluruhan: Rp {total_belanja}")







