
cumicumi=[]
Makanan_hari=[]
list_makanan=[]
class Pausbalin():
    makanan=None
    umur = ''
    berat = None
    def __init__(self,makanan,umur,berat):
       
        self.umur=umur
        self.berat=berat
        self.makanan = makanan
    
          
    def berenang(self):
        print("berenng di dasar laut")
    def Makan(self,makanan):
        self.makanan = makanan
        
    
        
    def makan_hari_ini(self):
        Makanan_hari.append(cumi_cumi)
        
    
    def deskrisip(self):
         print(f"{self.umur} {self.berat} {self.makanan}")

    def __repr__(self):
          
          return self.makanan
         



class cumi_cumi():
    jumlah='cumi cumi 1'
    jumlah2 = 'cumi cumi 2'
    Makanan_hari.append(jumlah)
    Makanan_hari.append(jumlah2)
    list_makanan.append(jumlah)
    list_makanan.append(jumlah2)
    
    def __init__(self,jumlah):
        self.jumlah=jumlah
    def __repr__(self):
        return self.jumlah
    def tidur(self):
        pass
class planton():
    makanan=None
    umur = ''
    ukuran = None
    def __init__(self,makanan,umur,ukuran):
        self.makanan=makanan
        self.umur=umur
        self.ukuran=ukuran
    def renang(self):
        pass

class krill():
    makanan=None
    umur = ''
    ukuran = None
    def __init__(self,umur,ukuran):
        self.umur=umur
        self.ukuran=ukuran
    def renang(self):
        pass
print(f"Paus berhasil memangsa {cumi_cumi.jumlah}")
print(f"Paus berhasil memangsa {cumi_cumi.jumlah2}")
print(f"hari ini paus makan{Makanan_hari}")


paus = Pausbalin(12,200,'cumi cumi')
cumi1 = cumi_cumi('1')
cumi2 = cumi_cumi('2')
#paus makan cumi 1
paus.Makan(cumi1)
#paus makan cumi 2
paus.Makan(cumi2)
paus.makan_hari_ini()

#list makanan paus 
print(f"list makanan {list_makanan}")







