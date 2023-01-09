class Motor():
    jenis=None
    merek = ''
    harga = None
    warna = None
    def __init__(self,jenis,merek,harga,warna):
        self.jenis=jenis
        self.merek=merek
        self.harga=harga
        self.warna=warna
    def balap_liar(self):
       print("balap di udayana")
    
    def bepergian(self):
      print ("ke lotim")
    def deskripsi(self):
      print(f"{self.jenis} {self.merek} {self.harga} {self.warna}")
    def __repr__(self): #representation > dieksekusi ketika mengprint sebuah ojeck
          return self.jenis

motor1 =Motor('supra','honda',24000,'coklat')
motor2 =Motor('vario','honda',250000,'biru')
motor3 =Motor('beat','yamaha',24000,'pink')
motor4 =Motor('klx','yamaha',24000,'merah')

print(motor1.jenis)
motor1.deskripsi()
print(motor1)
print(motor2)
print(motor3)
print(motor4)



print(f"mangakses objeck dari atribut motor : {motor1.merek}")


motor1.jenis = "minter x"
motor1.merek = "supra"
motor1.harga= 240000
motor1.warna = "merah"
print(f"jenis motor adalah supra {motor1.jenis}")
print(f"merek motor ini adalah {motor1.merek}")
print(f"harga motor itu adalalh {motor1.harga}")
print(f"warna motor itu adalah {motor1.warna}")
motor1.balap_liar()
motor1.bepergian