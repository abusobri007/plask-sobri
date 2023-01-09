#inheritance --. penurunan sifat
#parent class
class Kucing():
      def __init__(self) -> None:
            self.kelenjar_susu = True
            self.daun_telinga = True
            self.warna = None
            self.berat = None
      def makan(self):
            print ("kucing makan")
      def minum(self):
            print("kucing minum")

class KucingAnggora(Kucing):
      __jenis_bulu = 'lebat'
      def makan(self):
            print("kucing anggora makan")
      def deskripsi(self):
            print(f"kucing anggora berbulu {self.__jenis_bulu} dengan berat{self.berat} memiliki warna {self.warna}")



Kucing_anggora = KucingAnggora()
Kucing_anggora.warna = 'hitam'
Kucing_anggora.berat = 3
Kucing_anggora.deskripsi()