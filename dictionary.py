orang = {"nama": "sobri"}
umur = {"umur" : 20}
print(orang)
print(umur)
biodata = {
    "nama" : "sobri",
    "umur" : 19,
    "alamat": "sayang-sayang",
    "kawin"  : False,
    "tinggi": 166.6 
}
print(biodata)
#mangakses data
print(biodata['alamat'])
#mwnambah data
biodata['semester'] = 3
print(biodata)
warna_buah = dict(jeruk="oren", aple="merah",pisang = "kuning")
print(warna_buah)
#mengubah data
#menghapus data dict
#menggunakan methiod pop() manghapus data besarkan key
biodata.pop("semester")
print(f"data di hapus menggunkan metod pop(): {biodata}")
#menghapus data terakhir
biodata.popitem()
print(biodata)
#looping
for b in biodata.values():
    print(b)
for m,n in biodata.items():
    print(m,n)