mahasiswa1 = {
    'nim' : 202145,
    'nama' : 'fauzi',
    'alamat' :'sumbawa' ,

}
mahasiswa2 = {
    'nim' :[ 202146, 335, 442 ],
    'nama':['Digo','Sobri', 'devan'],
    'almat':['sumbawa','lombok','sumbawa']

}
#ubah isi data 
barang =[mahasiswa1, mahasiswa2]
print(barang)
barang [0] ['harga']=17500
barang[1] ['harga']=17500
print (barang)
#tambah kode  4
mahasiswa2['nim'].append(333)
mahasiswa2['nama'].append('budi')
mahasiswa2['alamat'].append('kediri')
print(mahasiswa2)


