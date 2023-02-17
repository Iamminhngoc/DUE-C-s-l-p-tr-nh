n=int(input("Nhap so nguyen:"))
for i in range (1,n+1,1):
    n=int(input("n="))
    if n==2:
        print(n,"la so nguyen to")
    else:
        if n%i==0:
            print(n,"khong la so nguyen to")
        else:
            print(n,"la so nguyen to")