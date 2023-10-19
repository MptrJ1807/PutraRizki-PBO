import math

#program menghitung sederhana
print("selamat datang di program menghitung sederhana")

#pilihan menu
print("Pilih operasi :\n", "1. penjumlahan \n", "2. pengurangan \n", "3. perkalian \n", "4. pembagian \n")

pilihan = input("masukan nomor operasi (1/2/3/4) : ")

angka1 = float(input("Masukan angka pertama : \n"))
angka2 = float(input("Masukan angka kedua : \n"))
angka3 = float(input("Masukan angka ketiga : \n"))

if pilihan == '1':
    hasil = angka1 + angka2 + angka3
    print("Hasil penjumlahan:", hasil)
elif pilihan == '2':
    hasil = angka1 - angka2 - angka3
    print("Hasil pengurangan:", hasil)
elif pilihan == '3':
    hasil = angka1 * angka2 * angka3
    print("Hasil perkalian:", hasil)
elif pilihan == '4':
    if angka2 != 0:  # Mencegah pembagian oleh nol
        hasil = angka1 / angka2 / angka3
        print("Hasil pembagian:", hasil)
    else:
        print("Error: Tidak dapat melakukan pembagian oleh nol!")
else:
    print("Pilihan tidak valid. Silakan pilih nomor operasi yang benar (1/2/3/4).")