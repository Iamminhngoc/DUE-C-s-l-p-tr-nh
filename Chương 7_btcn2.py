nhap = input()
nhap = nhap.lower()
tach = nhap.split(" ")

while "" in tach:
  tach.remove("")
nhap = " ".join(tach)

nhap = nhap.replace(" ,", ",")
nhap = nhap.replace(" .", ".")
nhap = nhap.replace(nhap[0], nhap[0].upper(), 1)

print(nhap)
