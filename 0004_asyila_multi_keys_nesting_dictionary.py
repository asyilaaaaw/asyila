import datetime

# Template data buku
buku_template = {
    'judul_buku': '',
    'penulis': '',
    'tahun_terbit': 0,
    'tanggal_terakhir_pinjam': None,
    'status': ''
}

# Dictionary utama
data_perpustakaan = {}

while True:
    print("\n" + "="*45)
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^45}")
    print("="*45)

    # Membuat dictionary baru
    buku = dict.fromkeys(buku_template.keys())

    # Input data buku
    buku['judul_buku'] = input("Judul Buku       : ")
    buku['penulis'] = input("Nama Penulis     : ")
    buku['tahun_terbit'] = int(input("Tahun Terbit     : "))

    tanggal = input("Tanggal Terakhir Pinjam (DD-MM-YYYY): ")

    if tanggal == "-":
        buku['tanggal_terakhir_pinjam'] = None
    else:
        buku['tanggal_terakhir_pinjam'] = (
            datetime.datetime.strptime(tanggal, "%d-%m-%Y")
        )

    buku['status'] = input(
        "Status (Tersedia/Tidak): "
    ).capitalize()

    # Multi Keys menggunakan tuple
    KEY = (buku['judul_buku'], buku['penulis'])

    # Memasukkan data ke dictionary utama
    data_perpustakaan.update({KEY: buku})

    # Menampilkan seluruh data buku
    print("\n" + "="*100)
    print(f"{'DATA PERPUSTAKAAN':^100}")
    print("="*100)

    print(
        f"{'KEY':<25} {'JUDUL BUKU':<20} "
        f"{'PENULIS':<15} {'TAHUN':<8} "
        f"{'TERAKHIR PINJAM':<18} {'STATUS':<12}"
    )

    print("-"*100)

    for KEY in data_perpustakaan:

        JUDUL = data_perpustakaan[KEY]['judul_buku']
        PENULIS = data_perpustakaan[KEY]['penulis']
        TAHUN = data_perpustakaan[KEY]['tahun_terbit']

        tanggal = data_perpustakaan[KEY]['tanggal_terakhir_pinjam']

        if tanggal is None:
            PINJAM = "-"
        else:
            PINJAM = tanggal.strftime("%d-%m-%Y")

        STATUS = data_perpustakaan[KEY]['status']

        print(
            f"{str(KEY):<25} {JUDUL:<20} "
            f"{PENULIS:<15} {TAHUN:<8} "
            f"{PINJAM:<18} {STATUS:<12}"
        )

    print("-"*100)

    is_done = input("\nTambah buku lagi? (y/n): ").lower()

    if is_done == "n":
        break

print("\nProgram selesai. Terima kasih!")
