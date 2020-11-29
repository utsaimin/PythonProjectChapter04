

#Program Hitung Tarif Rental
import math
jamMulai = int(input("jam pinjaman(jam) = "))
menitMulai = int(input("jam pinjam(menit) = "))
jamSelesai = int(input("jam kembali(jam) = "))
menitSelesai = int(input("jam kembali(menit) = "))

tarif1 = 200000
tarif2 = 10000

lamaSewa = (jamSelesai - jamMulai) + (menitSelesai-menitMulai) / 60
totalTarif = (tarif1+lamaSewa * tarif2)
print ("Tarif yang dibayar = ")
print(math.floor(totalTarif))




    
