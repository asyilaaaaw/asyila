# FUNGSI
print("=======================================================") 
print("                        FUNGSI")
print("=======================================================")

print("\n====>        Membuat Fungsi      <====") 
def halo_wak() : 
    # untuk menampilkan instruksi halo wak
    print("Halo Wak, Assalamualaikum wr wb")
    print("Terimakasih sudah klik video ini!")
    print("Cerita kali ini dikirim oleh wawak kita dari untid")

halo_wak()

print("\n====>        Fungsi Dengan Argumen      <====") 
# def nama_fungsi(argumen)
#        badan fungsi

print("-----    Contoh 1    -----")
def halo_maba(nama) :
    # fungsi hai_ganteng untuk menerima
    print(f"Selamat Datang di Untidar, {nama}")

halo_maba("Jake")

print("-----    Contoh 2    -----")
def tambah (angka1, angka2) :
    # kita bisa juga menggunakan operasi matematika
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(6,7)

print("-----    Contoh 3    -----")
def sambutan(list_peserta):
    data_peserta = list_peserta.copy()
    for peserta in data_peserta :
        print(f"Selamat Datang di Untidar, {peserta}")

mahasiswa = ["Jake", "Arin", "Martin", "Sutopo"]
sambutan(mahasiswa)

print("\n====>        Fungsi Dengan Return       <====")
# def nama_fungsi(argumen)
#       badan fungsi
#       return output

print("-----    Contoh 1    -----")
def Kuadrat(Input_Angka) :
    Hasil_Kuadrat = Input_Angka ** 2
    return Hasil_Kuadrat

Angka = Kuadrat(7)
print(Angka)

print(Kuadrat(44))

Operasi_1 = 10 - Kuadrat(3)
print(f"{Operasi_1}")

print("-----    Contoh 2    -----")
def fungsi_tambah (Angka_1, Angka_2) :
    # Fungsi return dengan multi input
    return Angka_1 + Angka_2

Operasi = fungsi_tambah(10,8)
print(Operasi)

print("-----    Contoh 3    -----")
def operasi_matematika(Angka_1, Angka_2) :
    tambah  = Angka_1 + Angka_2
    kurang  = Angka_1 - Angka_2
    kali    = Angka_1 * Angka_2
    bagi    = Angka_1 / Angka_2
    return tambah, kurang, kali, bagi

A, B, C, D = operasi_matematika(6,7)
print(f"Hasil Tambah    = {A}")
print(f"Hasil Kurang    = {B}")
print(f"Hasil Kali      = {C}")
print(f"Hasil Bagi      = {D}")

print("\n====>        Default Argumen    <====")
# def fungsi(argument):
# def fungsi(argument = nilai default):

print("-----    Contoh 1    -----")
def hai_mgl(nama = "Jake"):
    print(f"Selamat datang ke Magelang, {nama}")

hai_mgl("James")
hai_mgl()

print("-----    Contoh 2    -----")
def sapaan(nama, pesan = "Good Meowning!"):
    print(f"hai {nama}, {pesan}")

sapaan("Jake", "Selamat Pagi!")
sapaan("Budi")

print("-----    Contoh 2    -----")
def operasi_pangkat(Angka, Pangkat):
    hasil = Angka**Pangkat
    return hasil

print(operasi_pangkat(3,4))

print("-----    Contoh 4    -----")
def operasi_faktorial(input_1 = 1, input_2 = 2, input_3 = 3, input_4 = 4):
    hasil = input_1 * input_2 * input_3 * input_4
    return hasil

print(operasi_faktorial())
print(operasi_faktorial(input_3 = 6))

print("\n=======================================================")






















