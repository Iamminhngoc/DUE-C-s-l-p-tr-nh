n=int(input("n="))
for n in range(1,n+1,1):
    print(n,end=" ")
    if n%10==0:
        print("\n")