from Gempa import *

# membuat objek gempa dengan lokasi dan skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# info gempa 
print("## Gempa Bumi Info ##")
print()
gempa1.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi Info ##")
print()
gempa2.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi Info ##")
print()
gempa3.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi Info ##")
print()
gempa4.dampak() # memanggil method dampak()

print()
print("## Gempa Bumi Info ##")
print()
gempa5.dampak() # memanggil method dampak()