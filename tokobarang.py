banyak =[]
nama =[]
list_belanjaan=[]
Tbelanja =[]
Hbelanja =[]

jawab = "ya"
print('================== Menu ==============')
print('1. Daftar Menu')
print('2. Daftar minuman')
print('======================================')
menu = int(input("masukkan pilihan anda"))
if menu == 1:
 while jawab == "ya":
    print("------------------selamat datang di toko kami--------------")
    print("-----------------piliah barang--------------")
    print(" 1. tomat 1 bungkus : Rp. 5000")
    print(" 2. Ayam 1 kg : Rp.45000")
    print(" 3. kentang 1kg : Rp. 35000")
    print(" 4. cabai 1/4 kg : Rp. 55000")
    print(" 5. wortel 1 bungkus  : Rp. 7000")
    print()
    nama_pembeli = input("masukkan nama anda :")
    beli = int(input("mau beli apa ?"))
    jumlah_barang = int(input("masukkan jumlah : "))
    if beli == 1 :
       barang = "tomat 1 bungkus"
       harga =  5000
       Tbelanja.append(harga * jumlah_barang)
       Hbelanja.append(harga)
       banyak.append(jumlah_barang)
       list_belanjaan.append(barang)
       nama.append(nama_pembeli)
    
    elif beli == 2 :
         barang = "ayam 1kg "
         harga =  45000
         Tbelanja.append(harga * jumlah_barang)
         Hbelanja.append(harga)
         banyak.append(jumlah_barang)
         list_belanjaan.append(barang)
         nama.append(nama_pembeli)
    
    elif beli == 3 :
         barang = "kentang 1kg "
         harga =  35000
         Tbelanja.append(harga * jumlah_barang)
         Hbelanja.append(harga)
         banyak.append(jumlah_barang)
         list_belanjaan.append(barang)
         nama.append(nama_pembeli)
    
    
    elif beli == 4 :
          barang = "cabai 1/4kg "
          harga =  55000
          Tbelanja.append(harga * jumlah_barang)
          Hbelanja.append(harga)
          banyak.append(jumlah_barang)
          list_belanjaan.append(barang)
          nama.append(nama_pembeli)
    
    
    elif beli == 5 :
         barang = "wortel 1bungkus "
         harga =  7000
         Tbelanja.append(harga * jumlah_barang)
         Hbelanja.append(harga)
         banyak.append(jumlah_barang)
         list_belanjaan.append(barang)
         nama.append(nama_pembeli)
    jawab = input("adalagi ? ya/ tidak :")
    

while jawab == "ya":
   if menu == 2:
    print("------Menu Minuman--------")
   print("1. Es teh - Rp2000")
   print("2. Es jeruk - Rp3500")
   print("3. Es kopi - Rp4000\n")
   nomor=int(input("Masukan Pilihan: "))
   jumlah_barang= int(input("Berapa Gelas: "))
   if nomor==1:
      barang = "es teh" 
      harga = 2000        
      Tbelanja.append(harga * jumlah_barang)
      Hbelanja.append(harga)
      banyak.append(jumlah_barang)
      list_belanjaan.append(barang)
   elif nomor==2:
       barang = "es jeruk"
       harga = 3500
       Tbelanja.append(harga * jumlah_barang)
       Hbelanja.append(harga)
       banyak.append(jumlah_barang)
       list_belanjaan.append(barang)
   elif nomor==3:
       barang = "es kopi"
       harga = 4000
       Tbelanja.append(harga * jumlah_barang)
       Hbelanja.append(harga)
       banyak.append(jumlah_barang)
       list_belanjaan.append(barang)
   jawab = input("adalagi ? ya/ tidak :")
else:
     print()
     print("-----------------------------------------------")
     print(f"nama Pembeli :{nama}")
     print(f"harga barang : {Hbelanja}")
     print(f"list barang :{list_belanjaan}")
     print(f"jumlah barang : {banyak}")
     print(f"list harga :{Tbelanja}")
