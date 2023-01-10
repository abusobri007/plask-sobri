print("--------------Selamat datang di ATM itec----------------")
jawab = "y"
ulang = 0
saldo = 500000
while jawab == "y":
    password = int(input("masukkan password anda :"))
    if password == 123456:
        print("1.cek saldo")
        
    
    else:
        ulang +=1
        print("pasword  yang anda masukkan  salah")
        jawab = input(F"anda ingin mengulang ? ya/ tidak  :")
    if  ulang == 3 :
        print("maaf kartu anda tertelan hehehe")
        break
    
    elif saldo == 500000:
        int(input("masukkan pilihan :"))
        print(f"sisa saldo anda adalah {saldo}")
