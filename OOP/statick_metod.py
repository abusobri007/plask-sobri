#static metod --> merupakan fungsi atau metod yang bersifat statis dalam sebuah class
#cara membuat static metod 
#dengan cara mendefinikan decorator @staticmedo pads fungsi yang ingin di buat menjadi static
class Konversi:
    @staticmethod
    def satuan_ke_lusin(n):#static metod ga pakai self
        return n/12
    @staticmethod
    def satuan_ke_gross(n):
        return n/144
print(Konversi().satuan_ke_lusin(12))
print(Konversi().satuan_ke_gross(32))

class Mahasiswa():
    def __init__(self,nama) -> None:
        self.nama = nama

    def getNama(self):
        return self.nama

    @staticmethod
    def hurufBesar(nama):
        return nama.upper()

s = Mahasiswa("sobri")
print(Mahasiswa.hurufBesar(s.getNama()))


class Konversi:
      @staticmethod
      def celcius_ke_pahrenheit(c):
            return c*180000+32.00
      @staticmethod
      def ringgit_ke_rupiah(r):
        return r*3412

print(Konversi().celcius_ke_pahrenheit(12))
print(Konversi().ringgit_ke_rupiah(10))


    