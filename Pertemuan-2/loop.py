def input_stok_barang():
    # Inisialisasi dictionary untuk menyimpan stok berdasarkan kategori rak
    stok_barang = {}

    print("Masukkan data stok barang (ketik 'selesai' untuk mengakhiri):")

    while True:
        nama_barang = input("Masukkan nama barang: ")

        # Periksa apakah pengguna ingin mengakhiri input
        if nama_barang.lower() == 'selesai':
            break

        kategori_rak = input("Masukkan kategori rak: ")
        stok = int(input("Masukkan stok barang: "))

        # Perbarui stok barang dalam dictionary
        if kategori_rak in stok_barang:
            if nama_barang in stok_barang[kategori_rak]:
                stok_barang[kategori_rak][nama_barang] += stok
            else:
                stok_barang[kategori_rak][nama_barang] = stok
        else:
            stok_barang[kategori_rak] = {nama_barang: stok}

    return stok_barang

def tampilkan_stok_barang(stok_barang):
    # Menampilkan hasil stok barang untuk setiap kategori rak
    print("\nDaftar Barang Berdasarkan Kategori Rak dan Jumlah Unit:")
    for kategori, barang in stok_barang.items():
        print(f"\nKategori Rak: {kategori}")
        for nama_barang, jumlah_unit in barang.items():
            print(f"{nama_barang}: {jumlah_unit} unit")

# Program utama
while True:
    data_stok = input_stok_barang()
    tampilkan_stok_barang(data_stok)

    ulangi = input("\nApakah Anda ingin mengulangi program? (ya/tidak): ")
    if ulangi.lower() != 'ya':
        print("Terima kasih, program selesai.")
        break
