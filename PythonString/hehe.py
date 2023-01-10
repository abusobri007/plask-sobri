# Daftar harga barang
harga_barang = {
    "apel": 10000,
    "jeruk": 15000,
    "anggur": 20000,
    "mangga": 12000
}

# Daftar barang yang ingin dibeli
daftar_belanja = ["apel", "jeruk", "anggur"]

# Hitung total harga
total_harga = 0
for barang in daftar_belanja:
    if barang in harga_barang:
        total_harga += harga_barang[barang]

# Cetak total harga
print("Total harga:", total_harga)
