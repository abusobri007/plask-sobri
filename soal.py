passwod =int(input("masukkan pin atm anda bro: "))
if passwod == 123456:
    print("silahkan ke menu selanjutnya")

    while passwod == "y":
          passwod = int(input("apakah anda ingin mengulang pasword anda ? ya / tidak : "))
else:
    print("pasword yang anda masukkan salah")