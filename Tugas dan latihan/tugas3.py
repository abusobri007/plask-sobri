text = input("masukkan text : ")
out = []
for t in text:
    txt = t
    if t.isupper():
     txt = t.lower()
    if t.islower():
     txt = t.upper()
     out.append(txt)
print(out)
print("".join(out))