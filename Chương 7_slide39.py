TenMatHang=[]
SoLuong=[]
for i in range(4):
    ten=input("Mat hang: ")
    TenMatHang = TenMatHang+[ten]
    soluong=input("So luong: ")
    SoLuong=SoLuong+[soluong]
for i in range(0,4):
    print(TenMatHang[i].ljust(15,"."),end="")
    print(SoLuong[i].rjust(6))
    