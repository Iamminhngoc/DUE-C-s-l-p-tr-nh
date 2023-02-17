# Nhap mọt so nguyen n
def Nhap():
    n=int(input("n="))
    return n 
#Nhap va dem
def NhapVaDem(n):
  print("Nhap",n,"so nguyen:")
  kq=0
  for i in range (1,n+1,1):
     n=int(input())
     if n%2==0:
         kq=kq+1
  return kq
def InKQ(kq):      
    print("So chu so chan la:",kq)
n=Nhap()
x=NhapVaDem(n)
InKQ(x)