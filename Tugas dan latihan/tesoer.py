print("--------------Selamat datang di ATM itec----------------")
jawab = "y"
ulang = 0

while jawab == "y":
    password = int(input("masukkan password anda :"))
    if password == 123456:
        print("silahkan ke menu selanjutnya")
        
        break
    else:
        ulang +=1
        print("pasword  yang anda masukkan  salah")
        jawab = input(F"anda ingin mengulang ? ya/ tidak  :")
    if ulang == 2 :
        print("maaf kartu anda terlelan hehehe")
        break
    