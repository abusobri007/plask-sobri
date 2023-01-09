class Warteg():
      def __init__(self) -> None:
            self.total = 0
            self.item = []

      def nasi(self):
            self.item.append("nasi 1 porsi")
            self.total = self.total+1000
            return self

      def bakwan(self):
            self.item.append("bakwan 1 biji")
            self.total = self.total+2500
            return self
      
      def kangkung(self):
            self.item.append("sayur kangkung")
            self.total = self.total+2500
            return self
      
      def ayam_krispi(self):
            self.item.append("ayam krispi")
            self.total = self.total+10000
            return self

      def kerupuk_udang(self):
            self.item.append("kerupuk udang")
            self.total = self.total+1000
            return self

      def bayar(self):
            print(f"item : {self.item}")
            print(f"tagihan : {self.total}")
            return

sobri = Warteg().nasi().ayam_krispi().bakwan().kangkung().bayar()


      