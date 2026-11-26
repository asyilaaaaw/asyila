print("=======================================================")
print("                     LATIHAN FUNGSI")
print("=======================================================")


def persegi_panjang(panjang, lebar):
    luas_persegi_panjang = panjang * lebar
    return luas_persegi_panjang

def balok(panjang, lebar, tinggi):
    volume_balok = panjang * lebar * tinggi
    return volume_balok

def lingkaran(jari_jari):
    phi             = 3.14
    luas_lingkaran  = phi * (jari_jari ** 2)
    return luas_lingkaran

def bola(jari_jari):
    phi = 3.14
    volume_bola = (4/3) * phi * (jari_jari ** 3)
    return volume_bola

# PROGRAM UTAMA
while True:
    print("\n================================")
    print("       PROGRAM KALKULATOR")
    print("================================")
    print("1. Luas Persegi Panjang")
    print("2. Volume Persegi Panjang (Balok)")
    print("3. Luas Lingkaran")
    print("4. Volume Bola")
    print("5. Keluar")
    print("================================")

    pilihan = input("Pilih perhitungan (1-5): ")

    if pilihan == "1":
        print("\n--- LUAS PERSEGI PANJANG ---")
        panjang     = float(input("Masukkan panjang : "))
        lebar       = float(input("Masukkan lebar   : "))

        hasil = persegi_panjang(panjang, lebar)
        print(f"Luas Persegi Panjang = {hasil:.2f}")

    elif pilihan == "2":
        print("\n--- VOLUME BALOK ---")
        panjang     = float(input("Masukkan panjang : "))
        lebar       = float(input("Masukkan lebar   : "))
        tinggi      = float(input("Masukkan tinggi  : "))

        hasil = balok(panjang, lebar, tinggi)
        print(f"Volume Balok = {hasil:.2f}")

    elif pilihan == "3":
        print("\n--- LUAS LINGKARAN ---")
        jari_jari   = float(input("Masukkan jari-jari: "))

        hasil = lingkaran(jari_jari)
        print(f"Luas Lingkaran = {hasil:.2f}")

    elif pilihan == "4":
        print("\n--- VOLUME BOLA ---")
        jari_jari   = float(input("Masukkan jari-jari: "))

        hasil = bola(jari_jari)
        print(f"Volume Bola = {hasil:.2f}")

    elif pilihan == "5":
        print("\nTerima kasih sudah menggunakan program!")
        break

    else:
        print("\nPilihan tidak tersedia. Silakan coba lagi!")



print("\n=======================================================")












