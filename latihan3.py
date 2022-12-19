print("----------selamat datang di toko kami----------\n")
total_belanja = int(input("masukkan total belanja: "))
if total_belanja >100000:
    diskon = total_belanja *5/100
    tagihan = total_belanja -diskon
    
    print(F"harga asli  {total_belanja} ")
    print(F"harga tagihan  {tagihan} ")
else:
    print("tagihan : (total_belanja)")
print("--------------------------------------------------")    

   