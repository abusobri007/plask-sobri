print("--------formulir pendaftaramn kos kosan pak erte---------")
namaL = []
namaP = []
jawab = "ya"
while jawab == "ya":
    nama = [input("masukkan nama :")]
    jenis_kelamin = input(" masuukan jenis kelamin L/P :")
    if jenis_kelamin == 'L' :
        namaL.append(nama)
    if jenis_kelamin == 'P' :
        namaP.append(nama)
        jawab = input ("isi pormulir lagi ? ya / tidak  :")
    if jawab == "tidak":
            print(f"List kos Putra {namaL}")
            print(f"List kos Putri {namaP}")

print("-------------------------Terimakasi------------------------")
