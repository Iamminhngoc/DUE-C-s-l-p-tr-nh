def nhap():
    n=int(input("n="))
    return n
def inkq(n):
    for i in range(1,n+1,1):
        if i%2==0:
            print(i,end=" ")
n=nhap()
inkq(n)
a=str(input("Tiep tuc khong?"))
while a!="k" or a!="K":
    n=nhap()
    inkq(n)
    a=str(input("Tiep tuc khong?"))
    
    
        
        
        
    