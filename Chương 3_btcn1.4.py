toan=int(input())
ly=int(input())
hoa=int(input())
tb=int((toan*2+ly*3+hoa)/6)
if tb<3:
    print("Kem")
if 3<=tb and tb<5:
    print("Yeu")
if 5<=tb and tb<6:
    print("Trung binh")
if 6<=tb and tb<7:
    print("Trung binh Kha")
if 7<=tb and tb<8:
    print("Kha")
if 8<=tb and tb<9:
    print("Gioi")
if 9<=tb and tb<10:
    print("Xuat sac")


