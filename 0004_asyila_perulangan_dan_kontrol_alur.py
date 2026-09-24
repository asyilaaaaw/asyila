print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")
print("           Perulanagan dan Kontrol")
print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")

# Program menentukan bilangan ganjil dan genap dari 1 sampai 50
print("\n_=_=_=_ Menampilkan Bilangan Ganjil dan Genap (1-50) _=_=_=_")
Angka = range(1,51)
for i in Angka :
    if i % 2 == 0:
        print(f"{i} adalah bilangan GENAP")
    else:
        print(f"{i} adalah bilangan GANJIL")

# Program menentukan bilangan prima dari 1 sampai 100
print("\n_=_=_=_ Menampilkan Bilangan Prima (1-100) _=_=_=_")
Bilangan_Prima = range(1,101)
for h in Bilangan_Prima : 
    if h > 1 : 
        for i in range(2, h) :
            if (h % i) == 0 :
                break
        else:
            print(h)

print("_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_=_")