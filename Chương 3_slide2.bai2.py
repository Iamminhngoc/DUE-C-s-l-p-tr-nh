n=int(input("n="))
i=1
if 2<=n and n<=100:
    for i in range(2,n,1):
        if n%i==0:
            print(n,"khong la SNT")
            break
        if n%i!=0:
            print(n,"la SNT")
            break
         
           
    
        
    