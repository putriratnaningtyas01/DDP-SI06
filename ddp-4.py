# Soal 1
# Buatlah program yang meminta pengguna untuk memasukkan sebuah bilangan bulat. Program harus menentukan apakah bilangan tersebut genap atau ganjil menggunakan if dan if else.

# angka = int(input("Masukkan bilangan bulat: "))

# if angka % 2 == 0:
#     print("Bilangan genap")
# elif angka % 2 != 0:
#     print("Bilangan ganjil")
# else:
#     print("Input tidak valid")

# print("===============")


# Soal 2
# Buatlah program yang meminta pengguna untuk memasukkan nilai ujian. Jika nilai lebih besar atau sama dengan 75, cetak "Lulus". Jika tidak, cetak "Tidak Lulus". Gunakan if dan if else.

# nilaiujian = int(input("Masukkan nilai ujian: "))

# if nilaiujian >= 75:
#     print("Lulus")
# else:
#     print("Tidak Lulus")

# print("===============")


# # Soal 3
# # Buatlah program yang meminta pengguna untuk memasukkan usia. Program harus mencetak "Dewasa" jika usia lebih besar atau sama dengan 18, dan "Anak-anak" jika kurang dari 18. Tambahkan kondisi untuk mencetak "Remaja" jika usia antara 13 dan 17 menggunakan if and.

# usia = int(input("Masukkan usia anda: "))

# if usia >= 18:
#     print("Dewasa")
# elif usia < 18 and usia > 12:
#     print("Remaja")
# else:
#     print("Anak-anak")

# print("===============")


# Soal 4
# Buatlah program yang meminta pengguna untuk memasukkan status keanggotaan (misalnya "gold", "silver", atau "bronze"). Jika statusnya "gold" atau "silver", cetak "Selamat! Anda mendapatkan diskon". Gunakan if or.

# statusanggota = input("Masukkan status anggota anda: ")

# if statusanggota == "gold" or statusanggota == "silver":
#     print("Selamat! Anda mendapatkan diskon")
# else:
#     print("Maaf anda tidak mendapat diskon")

# print("===============")


# Soal 5
# Buatlah program yang meminta pengguna untuk memasukkan jumlah pembelian. Jika jumlahnya lebih dari 100, beri diskon 10% menggunakan shorthand if. Cetak total harga setelah diskon jika ada, jika tidak, cetak total harga tanpa diskon.

jumlahpembelian = int(input("Masukkan jumlah pembelian: "))
hargaitem = 1000
hargadiskon = hargaitem * jumlahpembelian * (10/100)
hargatotal = hargaitem * jumlahpembelian 
total = hargatotal - hargadiskon

print(f"Anda mendapat diskon 10%, harga per item {hargaitem} jadi total yang harus dibayar {total}") if jumlahpembelian > 100 else print(f"Harga per item {hargaitem}, jadi total yang harus dibayar adalah {hargatotal}")

print("===============")

