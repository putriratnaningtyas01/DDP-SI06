import math

def l_persegi(sisi):
    luas = sisi * sisi
    keliling = sisi * sisi * sisi * sisi
    print(f"Luas persegi {sisi} * {sisi} = {luas}")
    print (f"Keliling persegi {keliling}")

def l_persegi_panjang(panjang, lebar):
    luas = panjang * lebar   
    keliling = 2 * (panjang + lebar)
    print(f"Luas persegi panjang {panjang} * {lebar} = {luas}")
    print (f"keliling persegi panjang {keliling}")

def l_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi   
    keliling = 3 * alas
    print(f"Luas segitiga {0.5} * {alas} * {tinggi} = {luas}")
    print (f"keliling segitiga {keliling}")

def l_lingkaran(jari2):
    phi = 3.14
    luas = phi * jari2 * jari2
    keliling = 2 * jari2 * phi
    print(f"Luas plingkaran {phi} * {jari2} * {jari2} = {luas}")
    print (f"keliling lingkaran {keliling}")

def l_jajar_genjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = (2 * alas) + (2 * sisi_miring)
    print(f"Luas jajar genjang {alas} * {tinggi} = {luas}")
    print (f"Keliling jajar genjang {keliling}")

def l_belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print(f"luas belah ketupat {0.5} * {diagonal1} * {diagonal2}  = {luas}")
    print (f"keliling belah ketupat {keliling}")

def l_layang_layang(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = 0.5 * diagonal1 * diagonal2
    keliling= (2 * sisi_atas) + (2 * sisi_bawah)
    print(f"luas layang layang {0.5} * {diagonal1} * {diagonal2} = {luas}")
    print (f"keliling layang layang {keliling}")