print(">=_=_=_=_=_=_=_=_=_=***=_=_=_=_=_=_=_=_=_=<")
print("        PERULANGAN DAN KONTROL ALUR")
print(">=_=_=_=_=_=_=_=_=_=***=_=_=_=_=_=_=_=_=_=<")

# Array itu sama seperti variabel, namun multi value dengan tipe data bisa beragam. 
# Pada list terdapat index dan value
# Index = urutan, diawali dengan angka 0
# Value = contoh a = [1, 2, 3] menggunakan kurung siku
# Array terdiri dari tuple, dictionary, and list)
#

print("\nPROGRAM 5.1")
print(">_=_=_=_=_FUNGSI FOR_=_=_=_=_<")
    # For (Inisialisasi, Kondisi, Pencacah)
angka = [1, 2, 3, 4, 5, 6]
for i in angka :
    print(f"Angka i sekarang -> {i}")
        # Bisa juga tanpa fungsi for
print(angka[3])
print("\n>_=_=_=_=_FUNGSI RANGE_=_=_=_=_<")
    # Fungsi Range
angka = range(7)    # Dengan integer
for i in angka :
    print(f"Angka -> {i}")
print("\n")
angka = range(1, 13)     # Dengan rentang angka
for i in angka :
    print(f"Angka -> {i}")
afirmasi_positif = "ASYILA CANTIK BENERRR!" # Dengan string
for i in afirmasi_positif :
    print(i)

print("\nPROGRAM 5.2")
print(">_=_=_=_=_WHILE LOOP_=_=_=_=_<")
"""
angka1 = 22
while angka1 > 4 :
   print("Some People Wadidaw")
"""
 #Jika di run, ini gak akan ada akhirnya
 #maka,
angka = 4
while angka < 10 :
    angka = angka + 1
    print("Titut ketawa")

print("\nPROGRAM 5.3")
print(">_=_=_=_=_CONTINUE, PASS, BREAK_=_=_=_=_<")
"""
print(">_=_=_=_=_Pass_=_=_=_=_<")
angka = 8
while angka < 10 :
    agka = angka + 1
    if angka == 6 :
        pass
    print(angka)

print("\n>_=_=_=_=_CONTINUE_=_=_=_=_<")
angka = 8
print(f"Angka -> {angka}")
while angka > 3 :
    angka = angka + 1
    print(f"Angka sekarang -> {angka}")
    if angka == 3 :
        print (f"Angka sekarang = {angka}")
        continue
    print("but i wadadidaw")
"""


print("\n>_=_=_=_=_Break_=_=_=_=_<")
angka = 6
print(f"Angka -> {angka}")
while angka < 2 :
    angka = angka + 1
    print(f"Angka sekarang adalah {angka}")
    if angka == 8 :
        print("Wokee dana masuk boskyuh!")
        break
    print("Bukti Tf")

print("Nipu kah?")














































