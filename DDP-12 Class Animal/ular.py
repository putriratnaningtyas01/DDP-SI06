from animals import *

class ular(Animals):
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_ular, cara_menyerang):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna_ular
        self.cara = cara_menyerang

    def cetak_ular(self):
        super().cetak()
        print(f'warna ular ini berwarna {self.warna} dan hewan ini cara menyerangnya {self.cara}')

print('-----cetak ular-----')
print('-----objek pertama-----')
kobra = ular('ular kobra', 'daging', 'darat', 'bertelur', 'hitam', 'berbisa')
kobra.cetak_ular()

print('-----objek kedua-----')
sawah = ular('ular sawah', 'serangga/raptil', 'air', 'bertelur', 'berkamuflase', 'melilit')
sawah.cetak_ular()
