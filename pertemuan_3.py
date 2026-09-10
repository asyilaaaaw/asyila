# Program 3.1 Operasi Aritmatika dan Menampilkan Output 
    # Operasi aritmatika digunakan untuk melakukan perhitungan matematika
    # Menggunakan variabel hasil =

    # Operasi Tambah
a = 10
b = 12
hasil   = a + b
print(hasil)
hasil   = 6 + 7      
print(hasil)
    # Operasi Pengurangan
a = 50
b = 20
hasil   = a - b
print(hasil)
hasil   = 6 - 12    
print(hasil)
    # Operasi Perkalian
a = 33
b = 3
hasil   = a * b
print(hasil)
hasil   = 88 * 99   
print(hasil)
    # Operasi Pembagian
a = 44
b = 2
hasil   = a / b 
print(hasil)
hasil   = 20 / 8    
print(hasil)
    # Operasi Eksponen (pangkat)
a = 4
b = 2
hasil   = a ** b 
print(hasil)
hasil   = 26 ** 3   
print(hasil)
    # Operasi Modulus
a = 99
b = 2
hasil   = a % b 
print(hasil)
hasil   = 44 % 3    
print(hasil)
    # Floor Division
a = 67
b = 4
hasil   = a / b 
print(hasil)
hasil   = 88 // 26   
print(hasil)

# Program 3.2 Konversi Celcius ke Satuan Lain 
print("\n")
print("====================================================")
print("         Program Konversi Temperatur")
print("====================================================")
celcius     = float(input("Masukan Suhu dalam Celcius   :"))
print("Suhu   :", celcius, "Celcius")

    # Reamur 
reamur      = (4/5) * celcius
print("Suhu dalam Reamur        :", reamur, "Reamur")

    # Fahrenheit
fahrenheit  = (9/5) * celcius + 32
print("Suhu dalam Fahrenheit    :", fahrenheit, "Fahrenheit")

    # Kelvin
kelvin      = celcius + 273
print("Suhu dalam Kelvin        :", kelvin, "Kelvin")

# Program 3.3 Operasi Komparasi
print("\n")
print("====================================================")
print("                Operasi Komparasi")
print("====================================================")
    # Operasi Sama Dengan
a = 6
b = 8
hasil = a == 6
print(a, "=", 6, hasil)
hasil = a == b
print(a, "=", b,hasil)
    # Operasi Tidak Sama Dengan
a = 77
b = 99
hasil = a != b
print(a, "tidak sama dengan", b, "adalah", hasil)
hasil = b != 89
print(b, "tidak sama dengan", 89, "adalah", hasil)
    # Operasi Lebih Dari
a = 34
b = 54
hasil = a > b
print(a, ">", b, hasil)
hasil = b > a 
print(b, ">", a, hasil)
    # Operasi Kurang Dari
a = 98
b = 100
hasil = a < b
print(a, "<", b, hasil)
hasil = b < a
print(b, "<", a, hasil)
# Operator Lebih Besar Sama Dengan
a = 33
hasil = a >= 33
print(a, ">=", 33, hasil)
hasil = 22 >= a
print(22, ">=", a, hasil)
    # Operator Lebih Besar Sama Dengan
a = 33
hasil = a >= 33
print(a, ">=", 33, hasil)
hasil = 22 >= a
print(22, ">=", a, hasil)
    # is
a = 43
b = 43
hasil = a is b
print("a = b :", hasil)
    # is not
a = 43
b = 33
hasil = a is not b
print("a = b :", hasil)

print("====================================================")



