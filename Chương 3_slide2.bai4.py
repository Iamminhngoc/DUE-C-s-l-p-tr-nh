d=1
while d!="T" and d!="t":
    a=float(input("a="))
    b=float(input("b="))
    c=input("Toan tu:")
    
    if c=="+":
        print(a,c,b,"=",a+b,sep="")
    if c=="-":
        print(a,c,b,"=",a-b,sep="")
    if c=="*":
        print(a,c,b,"=",a*b,sep="")
    if c=="/":
        print(a,c,b,"=",a/b,sep="")
    d=input("Tiep tuc: ")
    
    

