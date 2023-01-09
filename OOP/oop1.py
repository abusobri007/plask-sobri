class Manusia():
    nama = ''
    umur = None
    __gender = None


    
    def makan(self):
        print("manusia makan nasi goreng")

    def minum(self):
        print("manusia minum kopi")
    def ulang_tahun(self):
        self.umur = self.umur+1
        print(f"sebelum ultah :{self.umur}")
        print(F"sesudah ultah :{self.umur +1}")
    def main_bola (self):
        print("sebagian manusia bisa bermain bola")
    def set_alamat(self,gender):#mengisi atribut 
       self.__gender= gender
    def get_gender(self): #method untuk mengakses atribut gender
       return self.__gender
#instance objeck
manusia1 = Manusia() #objeck 1
manusia2 = Manusia()#objec 2

print(manusia2)


print(f"mangakses objeck dari atribut manusia2 : {manusia2.nama}")

#memberi atribut pada objekck
manusia2.nama = "sobri"
manusia2.__gender = "laki laki"
manusia2.umur = 20
print(f"mengakses atribut nama dari objeck manusia 2 : {manusia2.nama}")
print(f"mengakses atribut gender dari objeck manusia 2 : {manusia2.__gender}")
print(f"mengakses atribut umur dari objeck manusia 2 : {manusia2.umur}")
#mangakses metod
manusia2.makan()
manusia2.minum()
manusia2.main_bola()
manusia2.ulang_tahun()
