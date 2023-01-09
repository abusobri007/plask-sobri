class dosen():
   nama = ''
   tinggi = None
   umur = None
   __alamat = None

   def makan(self):
        print("manusia makan nasi goreng")
   

   def minum(self):
        pass
   def ulang_tahun(self):
        self.umur = self.umur+1
        print(f"sebelum ultah :{self.umur}")
        print(F"sesudah ultah :{self.umur +1}")
   def mengajar(self):
        print("dosen mengajar banyak mahasiswa")
   def set_alamat(self,alamat):#mengisi atribut 
       self.__alamat=alamat
   def get_gender(self): #method untuk mengakses atribut gender
       return self.__alamat	

dosen1 = dosen() #objeck 1
dosen2 = dosen()#objec 2

dosen1.nama = "sobri"
dosen1.tinggi = "laki laki"
dosen1.__alamat = ""
dosen1.umur = 40
print(f"mengakses nama : {dosen1.nama}")
print(f"mengakses alamat: {dosen1.__alamat}")
print(f"mengakses tinggi: {dosen1.tinggi}")
print(f"mengakses umur: {dosen1.umur}")

#mangakses metod
dosen1.makan()
dosen1.mengajar()
dosen1.ulang_tahun()
dosen1.ulang_tahun()
dosen1.ulang_tahun()
dosen1.ulang_tahun()
dosen1.ulang_tahun()
dosen1.ulang_tahun()
dosen1.ulang_tahun()
