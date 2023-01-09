#plimorphisem >> metod yang sama pada kelas yang berbeda
class Paus:
      def __init__(self,mangsa) -> None:
            self.mangsa = mangsa

      def makan(self):
            print(f"paus makan {self.mangsa}")

class Harimau:
      def __init__(self,mangsa) -> None:
            self.mangsa = mangsa
      def makan(self,):
           
            print(f"harimau makan {self.mangsa}")

paus = Paus("cumi cumi")
harimau = Harimau("Rusa")

paus.makan()
harimau.makan()



class Elang :
     def __init__(self,mencari_makan):
          self.cari_makan = mencari_makan

     def carimakan(self):
      print(f"elang mencari makan dengan cara {self.cari_makan}")

class Hiu :
     def __init__(self,mencari_makan):
          self.cari_makan = mencari_makan

     def carimakan(self):
      print(f"Hiu mencari makan dengan cara {self.cari_makan}")

elang = Elang("Terbang")
hiu = Hiu("berenang")

elang.carimakan()
hiu.carimakan()
