#inheritance --. penurunan sifat
#parent class
#child class
class Kucing():#parent class
      def __init__(self):
            self.kelenjar_susu = True
            self.daun_telinga = True
      def makan (self):
            print("kucing makan")
      def minum (self):
            print("kucing minum")
class KucingAnggora(Kucing): #overidding
      __jenis_bulu = 'Lebat'
      print("kucing anggora makan")


kucing_anggora=KucingAnggora()
print(kucing_anggora.kelenjar_susu)#mengakses atribut kelenjar susudari parent classs
kucing_anggora.makan()
