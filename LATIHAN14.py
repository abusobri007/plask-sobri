biodata = {
      'nama' : "randi",
      'Alamat': {
         'alamat' : "jln belibis no 7", 
         'Kecamatan' : "pejanggik", 
         'kota' : "mataram",
         'provinsi'  : "NTB",
         

      },
      'nilai_rapot': [87, 85, 75, 90]
}
print(f"1. {biodata['nama']}")
print(f"2. {biodata['nama']['Kecamatan']}")
#ubahlah ke pada value pada varibale biodata
biodata['nama']= "susanto"
print(f"4. {biodata}")
# 5 hapus data dengan key provinsi
biodata['alamat'].pop('provinsi')
print(f"5. {biodata}")