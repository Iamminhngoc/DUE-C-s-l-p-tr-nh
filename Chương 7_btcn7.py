import re
nhap = input()
nhap = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', nhap)
if nhap:
  print(nhap[0])
else:
  print()
