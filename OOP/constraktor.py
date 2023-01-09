class Paus():
      Nama = None
      jenis = None
      umur = None
      harga = None
      def __init__(self,nama,umur,harga,jenis):#spesial metod
            self.nama=nama
            self.umur=umur
            self.harga=harga
            self.jenis=jenis
            print("ini adalah hewan paus")
      def __repr__(self): #representation > dieksekusi ketika mengprint sebuah ojeck
          return self.nama
          
      def deskripsi(self):
            print(f"{self.nama} {self.jenis} {self.umur},{self.harga}")


class pinguin():

      def __init__(self):
            print("ini adalah pinguin")

      def __repr__(self): #representation > dieksekusi ketika mengprint sebuah ojeck
          return self.jenis


class kuda():


      def lari(self):#metod biasa
            print("kuda berlari")

paus1 =Paus('willy',9,1000000,'biru')#instance
paus2 =Paus('asep',9,1000000,'biru')#instance
paus3 =Paus('ucup',9,1000000,'biru')#instance
paus4 =Paus('udin',9,1000000,'biru')#instance
paus5 =Paus('jamilah',9,1000000,'biru')#instance
print(paus1.umur)
paus1.deskripsi()
paus2= Paus
print(paus1)
print(paus2)
print(paus3)
print(paus4)
print(paus5)