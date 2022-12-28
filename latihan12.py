banyak =[]

list_belanjaan=[]
Tbelanja =[]
Hbelanja =[]

jawab = "ya"
while jawab == "ya":
    
    print("-----------------piliah barang--------------")
    print(" 1. tomat 1 bungkus : Rp. 5000")
    print(" 2. Ayam 1 kg : Rp.45000")
    print(" 3. kentang 1kg : Rp. 35000")
    print(" 4. cabai 1/4 kg : Rp. 55000")
    print(" 5. wortel 1 bungkus  : Rp. 7000")
    print()

    beli = int(input("mau beli apa ?"))
    jumlah_barang = int(input("masukkan jumlah : "))
    if beli == 1 :
       barang = "tomat 1 bungkus"
       harga =  5000
       Tbelanja.append(harga * jumlah_barang)
       Hbelanja.append(harga)
       banyak.append(jumlah_barang)
       list_belanjaan.append(barang)
    
    
    elif beli == 2 :
         barang = "ayam 1kg "
         harga =  45000
         Tbelanja.append(harga * jumlah_barang)
         Hbelanja.append(harga)
         banyak.append(jumlah_barang)
         list_belanjaan.append(barang)
    
    
    elif beli == 3 :
         barang = "kentang 1kg "
         harga =  35000
         Tbelanja.append(harga * jumlah_barang)
         Hbelanja.append(harga)
         banyak.append(jumlah_barang)
         list_belanjaan.append(barang)
    
    
    
    elif beli == 4 :
          barang = "cabai 1/4kg "
          harga =  55000
          Tbelanja.append(harga * jumlah_barang)
          Hbelanja.append(harga)
          banyak.append(jumlah_barang)
          list_belanjaan.append(barang)
    
    
    
    elif beli == 5 :
         barang = "wortel 1bungkus "
         harga =  7000
         Tbelanja.append(harga * jumlah_barang)
         Hbelanja.append(harga)
         banyak.append(jumlah_barang)
         list_belanjaan.append(barang)
    
    jawab = input("adalagi ? ya/ tidak :")
    
else :


         
    print()
    print("-----------------------------------------------")
    print(f"harga barang : {Hbelanja}")
    print(f"list barang :{list_belanjaan}")
    print(f"jumlah barang : {banyak}")
    print(f"list harga :{Tbelanja}")
    