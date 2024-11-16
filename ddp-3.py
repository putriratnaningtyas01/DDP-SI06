# Soal 1, Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)
Nama = "Putri Ratnaningtyas"
NIM = "0110124152"
Rombel = "SI06"
NoTelepon = 6289614889141
Alamat = "Kp.Cipayung, RT04/RW06, No.71, Kel.Tengah, Kec.Cibinong, Kab.Bogor"
print ("Nama saya adalah :", Nama)
print ("NIM saya :", NIM)
print ("Saya dari rombel :", Rombel)
print ("Ini No Telepon saya :", NoTelepon)
print ("Saya tinggal di :", Alamat)
print ("=========================================")

# Soal 2, buat seperti no 1 tapi 1 nama teman kalian 
Nama = "Sinta"
NIM = "0110124056"
Rombel = "SI06"
NoTelepon = 6289655842419
Alamat = "Jl. BDB Manggis, RT01/RW15, Cilangkap, Tapos, Jawa Barat"
print (f"Nama saya adalah : {Nama} \n NIM saya : {NIM} \n Saya dari rombel : {Rombel} \n Ini No Telepon saya : {NoTelepon} \n Saya tinggal di : {Alamat}")
print ("=========================================")


# Soal 3, buat program python untuk mencari nilai berat badan ideal 
#input
TB = int(input("Masukkan tinggi badan anda? "))
#proses
bb_ideal = (TB - 100) - (TB - 100) * 0.15
#hasil
print("berat badan ideal adalah: ", (bb_ideal))
print ("=========================================")


#Soal 4, Nilai Konversi dari Celcius ke Fahreinheit
#input
celcius = float(input("Masukkan suhu celcius? "))
#proses
fahreinheit = (9/5 * celcius) + 32
#hasil
print(f"Suhu dalam fahreinheit adalah: {fahreinheit:.2f}")
print ("=========================================")


# Soal 5, buat program python untuk mencari luas dan keliling tabung
# input
JariJari = float(input("Masukkan jari-jari tabung? "))
Tinggi = float(input("Masukkan tinggi tabung? "))
# proses
Luas = 2*22/7*JariJari*(JariJari + Tinggi)
Keliling = 2*22/7*JariJari
# hasil
print(f"Luas tabung adalah:  {Luas:.2f}")
print(f"Keliling tabung adalah:  {Keliling:.2f}")
print ("=========================================")