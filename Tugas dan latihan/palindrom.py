kalimat = input("masuukan kalimat :")
i=[]
for k in kalimat:
    i.append(k)
i.reverse()
B= "".join(i)
if kalimat == B:
  print("palindrom")
else :
  print("bukan palindroam")  