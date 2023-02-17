n=int(input("n="))
L= [item for item in range (1,n+1,1)]
print(L)
for i in L :
    if L[i]%2==0:
        L[i]=0
print(L)
    
    