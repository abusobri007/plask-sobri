kalimat=(input("masuukan kalimat :"))
palindrom = True
kata = len(kalimat)
for i in range(kata//2):
   if (kalimat[i] != kalimat[kata-i-1] ):
     palindrom = False
     break
if palindrom:
   print(kalimat,"adalah palindrom")
else :
   print(kalimat,"bukan palindroam")