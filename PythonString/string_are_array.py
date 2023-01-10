#memahami string sebagai array"
nama = "Abu Sobri Al Jamali"
print(f"Akses Huruf B : {nama[0]}")
#melakukkan lopping
for n in nama:
    print(n)
#mengecek panjang dari string
print(f"panjang string pada variabel nama : {len(nama)}")
#chek string
print("Abu Sobri Al Jamali" in nama)
#check is not
print("budi" not in nama)
#mengiris String
print(f"{nama[:2]}")
#slice to the and
print(f"{nama [5:]}")
#pengecekan String
text_biasa = 'text biasa'
text_angka = 'text angka'
text_judul = 'Python For Trainer'
text_kecil = 'huruf kecil'
text_besar = 'HURUF BESAR'
print(' apakah txt_angka itu digit ?', text_angka.isdigit())
print('Apakah txt_kecil itu lowercase ?', text_kecil.islower())
print('Apakah txt_besar itu uppercase ?', text_besar.isupper())
