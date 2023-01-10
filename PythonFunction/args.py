def coba(*args):
    print(args)
    print(args[0]+7)
    print(args[1])
coba(1,2, "woe")  

def penjumlahan(*args):
    total = args[0]+args[1]
    return total
print (penjumlahan(1,2))