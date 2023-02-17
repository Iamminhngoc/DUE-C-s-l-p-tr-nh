def Nhap():
    n=int(input("Nhap mot so nguyen:"))
    return n
def Xuly(n):
    for i in range (2,n,1):
            if n%i==0:
                return 1
            return 0
def InKQ(n,kq):
    if kq==1:
        print(n,"khong la so nguyen to")
    else:
        print(n,"la so nguyen to")
n=Nhap()
kq=Xuly(n)
InKQ(n,kq)
        