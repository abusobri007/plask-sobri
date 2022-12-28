film = ['naruto', "one pice", "avanger","fast and forius", "pengabdi setan" ]

print  (film)
#mengambil data pada variabel tertentu
print(f" ambil data pada index ke 0 : {film[0]}")
print(f" ambil data pada index ke 3 : {film[3]}")
#mangambil data pada index ke 1dan 3
print(F"mengambil data pada index 3 sampai dengan terakhir : {film[1:4]}")
#mengambil data dari index 3 sampai terakhir
print(F"mengambil data pada index 3 sampai dengan terakhir : {film[3:]}")
#mengitung data film
print(f"jumlah film {len(film)}")
#mengcek data 
print("avanger" in film)
#mena,bahkan data menggunakan metod append
film_baru = "avatar 2"
film.append(film_baru)
print(f"film berhasil di update : {film}")
#menggunakan metod insert
film_baru2 = "korin"
film.insert(2,film_baru2)
#mengubah data
film_baru3 ="kupu-kupu malam"
film[5] = film_baru3
print(f"film berhasil di update : {film}")
#mengapus data pada aray
film.pop()
print(f"film berhasil di hapus : {film}")
#remove
#mengurutkan data dengan menggunakan method sort
angka = [2,5,3,4,6,4,7,1]
angka.sort(reverse=True)
film.sort()
print(f"mengurutkan berdasarkan nama : {film}")
print(f"mengurutkan angka dengan secara descending:{angka}")
#mwmbalikkan data menggunakan reverse
buah = [ 'ceri', 'namanas','jeruk','anggur','salak']
buah.reverse()
print(f"dari kecil hingga terbesar  : {angka}")
#menghitung jumlah item yang sama menggunakan metod count
print(f"jumlah jeruk : {buah.count('jeruk')}")
#copy
buah_buahan = buah.copy()
print(f"buah-buahan : {buah_buahan} ")
#multlpe aray
matrix = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
print(matrix[1][3])
matrix[1][4]=21
print("matrix baru",matrix)