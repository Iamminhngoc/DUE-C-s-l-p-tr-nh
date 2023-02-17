n=int(input("n="))
t=1
i=1
if 0<=n and n<=100:
    for i in range (1,n+1):
        t=t*i
    print(n,"!=",t,sep="")