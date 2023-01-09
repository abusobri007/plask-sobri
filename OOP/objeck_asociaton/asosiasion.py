class Serigala():
    def __init__(self,id,hp,jenis,umur,kekuatan) -> None:
       
       self.id= id
       self.jenis = jenis
       self.Umur = umur
       self.kekuatan  = kekuatan
       self.hit_point = hp

    def menyerang(self,mangsa):
       mangsa.hit_point -= self.kekuatan
       print(f"serigala {self.id} menyerang kelenci {mangsa.id}")
 
    def berlari(self):
       print(f"serigala {self.id} berlari :" )


    def deskripsi(self):
       print(f"serigala {self.id} memiliki hp : {self.hit_point}")
    
class kelinci():
    def __init__(self, id , hp ,warna) -> None:
       self.id=id
       self.hit_point = hp
       self.warna = warna

    def makan(self):
       print(f"kelinci {self.id} makan")

    def berlari(self):
       print(f"kelinci {self.id} berlari")
    
    def bersembunyi(self):
       print(f"kelinci {self.id} bersembunyi")
    

    def deskripsi(self):
       print(f"kelinci {self.id} memiliki hp : {self.hit_point}")
    
    def __repr__(self) -> str:
       return f"kelinci {self.id}"


s1 = Serigala('1',100,'kutub',3,35)
k1 = kelinci('1',100,'biru')

k1.deskripsi()
k1.berlari()

s1.menyerang(k1)
k1.deskripsi()
k1.bersembunyi()
s1.menyerang(k1)
k1.deskripsi()

s2 = Serigala('2',100,"Gurun", 2,45)
s2.menyerang(s1)
s1.deskripsi
s2.menyerang(s1)
s1.deskripsi
s1.menyerang(s2)
s2.deskripsi()

