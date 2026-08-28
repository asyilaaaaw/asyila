# Program 2.1 Menampilkan Output ke Konsol
print("Hallo World")

# Program 2.2 Menampilkan Outpu ke Konsol
# Variable adalah tempat menyimpan nilai
# Tipe Data
    # 1. String             = data yang bisa menyimpan karakter
    # 2. Interger           = data yang hanya bisa menyimpan angka atau bilangan kecuali pecahan atau desimal (bilangan bulat)
    # 3. Double / Float     = data yang menyimpan bilangan desimal
    # 4. Boolean            = data yang hanya bisa menampung dua nilai, true atau false


# Tipe Data Pada Python
    # int x = 5 (nilai 5 adalah nilai x yang merupakan data interger)
    # Namun dalam Python tidak perlu penulisan jenis datanya, seperti
x = 5
y = 10 

print(x)
print("Nilai y adalah", y)

#Aturan Penamaan
nilai_y = 15        # menggunakan underscore
                    # tidak bisa diawali dengan angka
juta_19 = 19000000  # tidak perlu pakai titik, titik untuk mengganti koma pada data float 
nilaiZ = 17.5       

print("nilai y,", nilai_y) # Pemanggilan ke 1
nilai_y = 10
print("nilai y,", nilai_y) # Pemanggilan ke 2

# Program 2.3 Mengenal Tipe Data
a = 10      # a adalah variable dengan nilai 10
# Tipe Data Interger
data_interger = 1
print("Data     :", data_interger)
print("- bertipe", type(data_interger))

# Tipe Data Float
data_float  = 1.5
print("Data     :", data_float)
print("- bertipe", type(data_float))

# Tipe Data String
data_string = "Asyila"
print("Data     :", data_string)
print("- bertipe", type(data_string))

# Tipe Data Boolean
data_bool = True
print("Data     :", data_bool)
print("- bertipe", type(data_bool))

# Tipe Data Kompleks
data_complex = complex(5,6)
print("Data     :", data_complex)
print("- bertipe", type(data_complex))

# Tipe Data dari Bahasa C
    #from ctypes import c_double

# Program 2.4 Konversi Tipe Data
    # Kita mempelajari casting, yaitu merubah tipe data satu ke tipe data lainnya
    # Tipe data : int(), float(), str(), bool()

# 1. Konversi Data Interger
data_int    = 9
data_float  = float(data_int)
data_str    = str(data_int)
data_bool   = bool(data_int)

print("Data     =", data_float, "\t, Tipe   :", type(data_float))
print("Data     =", data_str,   "\t, Tipe   :", type(data_str))
print("Data     =", data_bool,  ", Tipe    :", type(data_bool))

# 2. Konversi Data Float
data_float  = 9.2
data_int    = int(data_float)
data_str    = str(data_float)
data_bool   = bool(data_float)

print("Data     =", data_int,   ", Tipe     :", type(data_int))
print("Data     =", data_str,   ", Tipe     :", type(data_str))
print("Data     =", data_bool,  ", Tipe     :", type(data_bool))

# 3. Konversi Data String
data_str    = "10"
data_int    = int(data_str)
data_float  = float(data_str)
data_bool   = bool(data_str)

print("")
print("")
print("")

# Program 2.5 Mengambil Input Data dari User
    # Input data user 
    # Data yang dimasukkan pasti string
data    = input("Masukan data  :")
print("Data     :", data,   "Tipe   :", type(data))

    #Jika ingin mengambil int, maka
angka   = int(input("Masukan angka   :"))
print("Data     :", angka, "Tipe    :", type(angka))


