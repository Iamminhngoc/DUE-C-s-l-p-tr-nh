def nhap():
    print("Nhap 3 so nguyen:")
    a=int(input("a="))
    b=int(input("b="))
    c=int(input("c="))
    return a,b,c
def max(a,b,c):
    if a>c and a>b:
        kq=a
    if b>a and b>c:
        kq=b
    if c>a and c>b:
        kq=c
    return kq
def inkq(kq):
    print("So lon nhat la:",kq)
a,b,c=nhap()
kq=max(a,b,c)
inkq(kq)