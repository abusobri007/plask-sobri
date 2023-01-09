class Hanabi():
    def __init__(self,id,jenis,umur,hp,kekuatan) -> None:
       
       self.id= id
       self.jenis = jenis
       self.Umur = umur
       self.kekuatan  = kekuatan
       self.hit_point = hp

    def menyerang(self,musuh):
       musuh.hit_point -= self.kekuatan
       print(f"hanabi {self.id} menyerang lesley {musuh.id}")
 
    def berlari(self):
       print(f"hanabi {self.id} berlari :" ) 

    def Bertahan(self):
      print(f"hanabi {self.id} mundur")


    def deskripsi(self):
       print(f"hanabi {self.id} memiliki darah : {self.hit_point}")
    
    
class Lesley():
    def __init__(self, id , damage,hp) -> None:
       self.id=id
       self.damage = damage
       self.hit_point = hp

    def bertahan(self):
       print(f"lesley {self.id} bertahan")

    def berlari(self):
       print(f"lesley {self.id} berlari")
    
    def bersembunyi(self):
       print(f"lesley {self.id} bersembunyi di rumput")
    

    def deskripsi(self):
       print(f"lesley {self.id} memiliki darah : {self.hit_point}")
    
    def __repr__(self) -> str:
       return f"kelinci {self.id}"


hn = Hanabi('1','hero_ml',3,100,50)
ls = Lesley('1',100,100)

ls.deskripsi()
hn.menyerang(ls)
ls.deskripsi()
hn.menyerang(ls)
ls.bersembunyi()
ls.deskripsi()