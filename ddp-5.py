# Soal 1
# buat variabel list dengan value : [nama kendaraan, jenis kendaraan, cc kendaraan, warna kendaraan, roda kendaraan]
transportasi = ["nama kendaraan", "jenis kendaraan", "cc kendaraan", "warna kendaraan", "roda kendaraan"]
print(transportasi)

# tambahkan list di belakang dengan value : [harga kendaraan, tipe kendaraan]
transportasi.append("harga kendaraan")
transportasi.append("tipe kendaraan")
print(transportasi)

# tambahkan setelah jenis kendaraan dengan value : [merk kendaraan]
transportasi.insert(2, "merk kendaraan")
print(transportasi)

# Soal 2
# Menghitung luas bangun datar dengan match case

pilih = int(input("""Selamat datang diaplikasi menghitung
1. Untuk menghitung luas persegi
2. Untuk menghitung luas lingkaran
3. Untuk menghitung luas segitiga

Masukkan pilihan anda: """))

match pilih:
    case 1 :
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("Masukkan sisi persegi: "))
        luaspersegi = sisi*sisi 
        print("Luas persegi yang sisinya",sisi,"adalah", luaspersegi)
    case 2 :
        print("Kamu memilih 2 untuk menghitung luas lingkaran")
        jarijari = int(input("Masukkan jari-jari lingkaran: "))
        luaslingkaran = 3.14 * jarijari * jarijari 
        print("Luas lingkaran yang jari-jarinya",jarijari,"adalah", luaslingkaran)
    case 3 :
        print("Kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("Masukkan alas segitiga: "))
        tinggi = int(input("Masukkan tinggi segitiga: "))
        luassegitiga = 0.5 * alas * tinggi 
        print("Luas segitiga dengan alas",alas,"dan tinggi",tinggi,"adalah", luassegitiga)
    case _ :
        print("Anda salah pilih")