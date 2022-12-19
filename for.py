#for i in range(10):
    #kode yang ada di dalam for
   # print(f"perulangan ke - (i)")
    #kode di luar for

#for i in range (100):
    #print()


#break
makanan=['ote ote', "mendoan","cireng", "pisang gorang"]
pesan = "cireng"
for m in makanan:
    if m == pesan:
        print("cirengnya ada")
        break 
    else:
        print("cirengnya habis")
    
print()
print("menu makanan")
for m in makanan:
    print(m)
#mengurai string
#nama = budi
#for i in nama:
    #print (i)

#print()

#countinue
for i in range(10):
    if i == 7:
        continue
    print(f"(i)")

    print(10*'--')

#for using star paramneter
for i in range(2,10):
    print(f"(i)")

    print(10*'--')

for i in range(0,100,5):
    print(i)