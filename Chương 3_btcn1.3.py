x=float(input("x="))
y=float(input("y="))
ch=input("Phep toan:")
if ch=="+" :
    print(str(x)+"+"+str(y)+"=",x+y,sep="")
if ch=="-" :
    print(str(x)+"-"+str(y)+"=",x-y,sep="")
if ch=="*" :
    print(str(x)+"*"+str(y)+"=",x*y,sep="")
if ch=="/" :
    #print(str(x)+"?"+str(y)+"=",x/y,sep="")
    if y==0:
        print("Khong hop le")
    if y!=0:
        print(str(x)+"/"+str(y)+"=",x/y,sep="")
if ch!="+" and ch!="-" and ch!="*" and ch!="/" : 
    print("Khong hop le")
    