class kuda():
      def __init__(self):
            self.jenis_makanan = True
            self.warna    = True
      def berjalan(self):
            print ("kuda berjalan")
      def makan(self):
            print("kuda menyusui")
class Kuda_Arab(kuda):
      __jenis_bulu = 'lebat'
      def makan(self):
            print("kucing anggora makan")
      def deskripsi(self):
            print(f"kucing anggora berbulu {self.__jenis_bulu} dengan berat{self.berat} memiliki warna {self.warna}")

