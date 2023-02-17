m=[]
for i in range (0,10,1):
    n1=int(input("n="))
    m.append(n1)
print(m)
x=int(input("Nhap mot so nguyen:"))
i=0
while i<len(m):
    if m[i]==x:
         del(m[i])
         i=0
    else:
        i=i+1
print(m)