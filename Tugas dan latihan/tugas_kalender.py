print("---menentukan bulan hijriah berdasarkan kalender masehi 2022---")

tanggal = int(input("masukkan tanggal: "))
bulan = int(input("masukan bulan: "))
tahun = int(input ("masukan tahun:"))
if bulan == 1:
    if tanggal>= 1 and tanggal <= 4:
        print("jumadil ula 1443 H")
    if tanggal>= 4 and tanggal <= 30:
        print("jumadil akhir 1443 H")
elif bulan == 2:
    if tanggal== 1:
        print("jumadil akhir 1443 H")
    if tanggal>=2 and tanggal <= 29:
        print("rajab 1443 H")
elif bulan == 3:
    if tanggal>= 1 and tanggal <= 3:
        print("rajab 1443 H")
    if tanggal>= 3 and tanggal <= 28:
        print("sya'ban 1433 H")
elif bulan == 4:
    if tanggal >= 1 and tanggal <= 2:
        print("sya'ban 1443 H")
    if tanggal >= 3 and tanggal <= 30:
        print("ramadhan 1443 H")
elif bulan == 5:
    if tanggal == 1:
        print("ramadhan 1443 H")
    if tanggal >=2 and tanggal <= 30:
        print("syawal 1443 H")
elif bulan == 6:
    if tanggal >= 1 and tanggal <= 29:
        print("dzulqaidah 1443 H")
    if tanggal == 30:
        print("djulhijah 1443 H")
elif bulan == 7:
    if tanggal >=1 and tanggal <= 9:
        print("djulhijah 1443 H")
    if tanggal >= 10 and tanggal <= 30:
        print("muharam 1444 H")
elif bulan == 8:
    if tanggal >=1 and tanggal <= 28:
        print("muharam 1444 H")
    if tanggal == 29:
        print("syafar 1444 H")
elif bulan == 9:
    if tanggal >=1 and tanggal <= 26:
        print("syafar 1444 H")
    if tanggal >=27 and tanggal <= 29:
        print("Rabi'ul-awal 1444 H")
elif bulan == 10:
     if tanggal >=1 and tanggal <= 26:
        print("Rabi'ul-awal 1444 H")
     if tanggal >=27 and tanggal <= 29:
        print("Rabi'ul-akhir 1444 H")
elif bulan == 11:
    if tanggal >= 1 and tanggal <= 24:
        print("Rabi'ul-akhir 1444 H")
    if tanggal >= 25 and tanggal <= 29:
        print("jumadil-ula 1444 H")
elif bulan == 12:
    if tanggal >=1 and tanggal <= 24:
        print("jumadil-ula 1444 H")
    if tanggal >= 25 and tanggal <= 30:
        print("jumadil akhir 1443 H")
    