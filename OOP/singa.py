class Singa():
    nama = ''
    umur = None
    gender = None
    attack = None
    def __init__(self,nama,umur,gender,attack):
        self.nama=nama
        self.umur=umur
        self.gender=gender
        self.attack=attack

        print("ini adalah singa")
    def deskripsi(self):
            print(f"{self.nama} {self.umur} {self.gender},{self.attack}")



    def makan(self):
        print("singa makan daging rusa")

    def minum(self):
        print("manusia minum air sungai")

    def minum(self):
        print("manusia minum air sungai")


    def berburu(self):
       print("berburu mangsa")
    
    def __repr__(self): #representation > dieksekusi ketika mengprint sebuah ojeck
          return self.nama

singa1 =Singa('udin',5,'laki laki','99%')
singa2 =Singa('ucup',5,'laki laki','99%')
singa3 =Singa('konah',5,'laki laki','99%')
singa4 =Singa('jamilah',5,'prempuan','99%')
print(singa1.nama)
singa1.deskripsi()
print(singa1)
print(singa2)
print(singa3)
print(singa4)



print(f"mangakses objeck dari atribut singa2 : {singa1.nama}")


singa1.nama = "minter x"
singa1.gender = "perempuan"
singa1.umur = 5
singa1.attack = 1000
print(f"jenis kelamin singa singa1 : {singa1.gender}")
print(f"umur singa adalah singa1: {singa1.umur}")
print(f"besar attack pada singa adalah : {singa1.attack}")
singa1.makan()
singa1.minum()
singa1.berburu()



