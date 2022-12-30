# Import library pyhijri
import pyhijri

# Buat objek tanggal Hijrah
hijri_date = pyhijri.date(1443, 3, 1)

# Konversi ke tanggal Masehi
gregorian_date = hijri_date.to_gregorian()

# Cetak tanggal Masehi hasil konversi
print(gregorian_date)
