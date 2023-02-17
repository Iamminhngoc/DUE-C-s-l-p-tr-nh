s=input('')
dem1=0
dem2=0
dem3=0
dem4=0
for i in s:
    if i.islower():
        dem1=dem1+1
    elif i.isupper():
        dem2=dem2+1
    elif i.isdecimal():
        dem3=dem3+1
    else:
        dem4=dem4+1
print('In hoa:',dem2)
print('In thuong:',dem1)
print('Chu so:',dem3)
print('Khac:',dem4)