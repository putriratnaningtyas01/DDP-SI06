from animals import *

class ikan(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ikan, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ikan
        self.jenis = jenis_ikan

    def cetak_ikan(self):
        super().cetak()
        print(f'warna ikan ini adalah warna {self.warna} dan hewan ini jenisnya ikan {self.jenis}')

print('-----cetak ikan-----')
print('-----objek pertama-----')
nemo = ikan('ikan nemo', 'plankton', 'air', 'bertelur', 'orange', 'air laut')
nemo.cetak_ikan()

print('-----objek kedua-----')
arwana = ikan('ikan arwana', 'jangkrik', 'air', 'bertelur', 'merah', 'air tawar')
arwana.cetak_ikan()
