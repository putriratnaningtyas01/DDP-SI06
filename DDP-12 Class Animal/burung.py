from animals import *

class burung(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis_bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis_bulu = jenis_bulu
        self.bunyi = bunyi

    def cetak_burung(self):
        super().cetak()
        print(f'hewan ini berbulu {self.jenis_bulu} dan hewan ini berbunyi {self.bunyi}')

print('-----cetak burung-----')
print('-----objek pertama-----')
beo = burung('Burung beo', 'biji-bijian', 'udara', 'bertelur', 'blue and orange', 'kamu jelek')
beo.cetak_burung()

print('-----objek kedua-----')
merpati = burung('Burung merpati', 'biji-bijian', 'udara', 'bertelur', 'putih', 'kuk-kuk')
merpati.cetak_burung()

