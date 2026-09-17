# Operasi Logika atau Boolean

    # not, or, and, xor
    
print(">_=_=_=_NOT_=_=_=_<")
# not adalah operator untuk menegasikan suatu fungsi
a = True
b = not a
print(b)
print("\n>_=_=_=_OR_=_=_=_<")
# Jika dua-duanya True, hasilnya True.
# Jika salah satu True atau benar, maka hasilnya true. 
# Jika keduanya salah maka hasilnya false.
a = False
b = True
c = a or b
print(c)
print("\n>_=_=_=_AND_=_=_=_<")
# Jika kedua nilai True, maka hasilnya True
# Jika salah satu false, maka False
a = True
b = False
c = a and b
print(c)
print("\n>_=_=_=_XOR_=_=_=_<")
# Akan bernilai True, jika salah satu True. Sisanya False
a =True
b = False
c = a ^ b
print(c)

    # Logika dan Komparasi
# Gabungan 
# Gabungan kurang dari 7 dan lebih dari 17
print(">_=_=_=_GABUNGAN_=_=_=_<")
# Gabungan angka < 7 atau Angka > 17

# Membuat Input User
Angka = float(input("Angka  :"))

  # Memeriksa Angka < 7
AngkaUser7 = Angka < 7
print(Angka, "<", 7, AngkaUser7)
  # Memeriksa Angka > 17
AngkaUser17 = Angka > 17
print(Angka, ">", 17, AngkaUser17)

# Hasil Gabungan
hasil = AngkaUser7 or AngkaUser17
print(hasil)

print(">_=_=_=_IRISAN_=_=_=_<")
# Gabungan angka > 7 dan Angka < 17

# Membuat Input User
Angka = float(input("Angka  :"))

  # Memeriksa Angka > 7
AngkaUser7 = Angka > 7
print(Angka, ">", 7, AngkaUser7)
  # Memeriksa Angka < 17
AngkaUser17 = Angka < 17
print(Angka, "<", 17, AngkaUser17)

# Hasil Irisan
hasil = AngkaUser7 and AngkaUser17
print(hasil)

    # IF and Else
# 1. If Inline
print("\n>_=_=_=_If Inline_=_=_=_<")
nama = input("Siapa kamu?")
if nama == "Asyila" : print("Ini pacarnya Jake ya?")

# 2. If Indentation
print("\n>_=_=_=_If Indentation_=_=_=_<")
nama = input("Siapa kamu?")
if nama == "Asyila" :
    print("WOW KEMBARANNYA DUA LIPA!")
    print("INI MAH BELLA HADID!")

# 3. Else Statement
print("\n>_=_=_=_Else Statement_=_=_=_<")
nama = input("Siapa kamu?")
if nama == "Asyila" :
    print("HAII SYILAA!")
else:
    print("Halo Jugaa!")

    # ELIF Statement
nama = input("Masukan Nama :")

if nama == "Asyila" :
    print("Halo Asyila dari Untidar")
elif nama == "Salsa" :
    print("Hallo Salsa dari Undip")
elif nama== "Zulfa":
    print("Hai Zulfa dari UNY")
else :
    print("Hallo")
