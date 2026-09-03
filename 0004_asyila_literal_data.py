print(">***=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=***<")
print("                         Literal Data")
print(">***=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=***<")

print("1. Membuat Program Menggunakan Variable yang Ditentukan")
nama    = "Asyila Wadda Nafi'ah"
umur    = 18
berat   = 50.5

print("Nama     :", nama)
print("Umur     :", umur, "Tahun")
print("Berat    :", berat, "KG")
print("\n")

print("2. Mengubah Tipe Data")
angka_string    = "123"
angka_float     = 45.67
angka_interger  = 89

    # 1. Konversi angka string menjadi interger
data_int    = int(angka_string)
print("Angka    =", data_int,   ", Tipe Data   :", type(data_int))
    # 2. Konversi angka float menjadi interger
data_int    = int(angka_float)
print("Angka    =", data_int,   ", Tipe Data  :", type(data_int))
    # 3. Konversi angka interger menjadi float
data_float  = float(angka_interger)
print("Angka    =", data_float, ", Tipe Data    :", type(data_float))
    # 4. Konversi angka interger menjadi string
data_str    = str(angka_interger)
print("Angka    =", data_str,   ", Tipe Data  :", type(data_str))
print("\n")

print("3. Membuat Program yang Menginput Usia, Tinggi Badan, Nama")
    # Input Usia
data_usia           = int(input("Masukkan Usia  :"))
print("Data Usia            =", data_usia, "Tahun" "\nTipe Data   :", type(data_usia))
    #Input Tinggi Badan 
data_tinggi_badan   = float(input("Masukan Tinggi Badan     :"))
print("Data Tinggi Badan    =", data_tinggi_badan, "CM", "\nTipe Data   :", type(data_tinggi_badan))
    #Input Nama
data_nama           = input("Masukan Nama   :")
print("Data Nama            =", data_nama, "\nTipe Data   :", type(data_nama))

print(">***=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=***<")