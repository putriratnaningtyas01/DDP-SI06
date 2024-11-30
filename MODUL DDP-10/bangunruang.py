import bangunruang

def kubus(sisi):
    luas = 6 * sisi * sisi
    volume = sisi * sisi * sisi
    print(f"Luas kubus {6} * {sisi} * {sisi} = {luas}")
    print (f"Volume kubus {sisi} * {sisi} * {sisi} = {volume}")

def balok(panjang, lebar, tinggi):
    luas = (2 * panjang * lebar) + (2 * panjang * tinggi) + (2 * lebar * tinggi)
    volume = panjang * lebar * tinggi
    print(f"Luas balok ({2}*{panjang}*{lebar}) + ({2}*{panjang}*{tinggi} + (2{lebar}*{tinggi}) = {luas}")
    print (f"Volume balok {panjang} * {lebar} * {tinggi} = {volume}")

def tabung(jarijari, tinggi):
    luas = 2 * 3.14 * jarijari * (jarijari + tinggi)
    volume = 3.14 * jarijari * jarijari * tinggi
    print(f"Luas tabung {2} * {3.14} * {jarijari} * ({jarijari} + {tinggi}) = {luas}")
    print (f"Volume tabung {3.14} * {jarijari} * {jarijari} * {tinggi} = {volume}")

def prisma(luasalas, kelilingalas, tinggi):
    luas = (2 * luasalas) + (kelilingalas * tinggi)
    volume = luasalas * tinggi
    print(f"Luas prisma ({2}*{luasalas}) + ({kelilingalas}*{tinggi}) = {luas}")
    print (f"Volume prisma {luasalas} * {tinggi} = {volume}")

def bola(jarijari):
    luas = 4 * 3.14 * jarijari * jarijari 
    volume = 4/3 * 3.14 * jarijari * jarijari * jarijari
    print(f"Luas bola {4} * {3.14} * {jarijari} * {jarijari} = {luas}")
    print (f"Volume bola {4/3} * {3.14} * {jarijari} * {jarijari} * {jarijari} = {volume}")