m=[]
for i in range (0,10,1):
    n1=int(input("n="))
    m.append(n1)
print(m)
x=int(input("Nhap mot so nguyen:"))
for i in range(0,len(m)):
    if m[i]==5:
        m[i]=x
print(m)
        

    