n=int(input('n='))
L=[]
for i in range(1,n+1):
    a=int(input(''))
    L=L+[a]
s=0
for i in range(0,len(L)):
    if i%2==1:
        s=s+L[i]
print('Tong=',s,sep='')