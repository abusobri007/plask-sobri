import persegi
import persegi_panjang as pj
from trapesium import luas_trapesium, keliling_trapesium
from jajargenjang import* #memanggil selurh isis dalam module jajar genjang
s =12
p1= persegi.luas_persegi(s) #mangakses fungction luas_persegi dari module persegi
print(f"luas daei p1 adalah : {p1}")
pp1 = pj.keliling_persegi_panjang(10.0,5.0)
print(f"luas dari pp1 adalah : {pp1}")
ltp1 = {luas_trapesium(8.0, 10.0, 3.0)}
print(f"luas dari ltp1 adalah : {ltp1}")
print(persegi.test)# memanggial variabel module/file persegi
p_c = persegi.persegi()#memanggil class persegi
print(luas_jajar_genjang(10.0,5.0))