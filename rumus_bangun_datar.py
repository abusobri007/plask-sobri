def luas_persegi(sisi:int):
    return sisi*sisi

def keliling_persegi(sisi:int):
    return 4*sisi

def luas_persegi_panjang(panjang:float, lebar:float):
    return panjang*lebar

def keliling_persegi_panjang(panjang:float, lebar:float):
    return (panjang*lebar)*2


def luas_trapesium(sisi1:float, sisi2:float, tinggi:float):
    return ((sisi1+sisi2)*tinggi)/2


def keliling_trapesium(sisi1:float, sisi2:float, sisi3:float, sisi4:float):
    return sisi1+sisi2+sisi3+sisi4

def luas_jajar_genjang(alas:float, tinggi:float):
    return alas*tinggi

def keliling_jajar_genjang(sisi1:float, sisi2:float):
    return 2*(sisi1+sisi2)

def keliling_belah_ketupat(sisi:float):
    return 4*sisi

def luas_segitiga(alas:float, tinggi:float):
    return alas*tinggi/2

def keliling_segitiga(alas:float, tinggi:float, sisi_miring:float):
    return alas+tinggi+sisi_miring

def luas_segitiga(r:int):
    return 3.14*r**2

def keliling_segitiga(r:int):
    return 2*3.14*r


def luas_kubus(rusuk: int):
    return 6*rusuk**2

def volume_kubus(rusuk:int):
    return rusuk**3

def luas_balok():
                ...