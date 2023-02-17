a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
#def find_max(a, b, c):
max = a
min=b
if a<b:
     max=b
     min=a
if a<c:
     max=c
if c<b:
    min=c
print("SLN=",max,sep="")
print("SBN=",min,sep="")



 
