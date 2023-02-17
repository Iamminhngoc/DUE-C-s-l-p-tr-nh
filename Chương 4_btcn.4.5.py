def LaSoNguyenTo(x):
    dem=0
    for i in range(1,x+1):
        if x%i==0 :
            dem=dem+1
    if (x<2) or (dem!=2) :
        return 0
    else:
        return 1
def SoHopLe(x):
    if x>1:
        return 1
    else:
        return 0
def NhapVaDem():
    print('Nhap day so:')
    x=int(input(''))
    kq=0
    while SoHopLe(x)==1:
        if LaSoNguyenTo(x)==1:
            kq=kq+1
            x=int(input(''))
        else:
            x=int(input(''))
    return kq  
def InKQ(kq):
   print('Co',kq,'so nguyen to')
kq=NhapVaDem()
InKQ(kq)