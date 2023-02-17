n=int(input('n='))
L=[]
for i in range(1,n+1):
    a=int(input(''))
    L=L+[a]
dem1=0
S=0
dem2=0
for i in range(0,len(L)):
    if L[i]>0:
        dem1=dem1+1
    if L[i]%2==0:
        S=S+L[i]
        dem2=dem2+1
print('SND=',dem1,sep='')
if dem2!=0:
    P=S/dem2
    print('TBC=',P,sep='')
else:
    print('TBC=0')