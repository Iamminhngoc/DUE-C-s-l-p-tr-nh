n=int(input('n='))
L=[]
for i in range(1,n+1):
    a=int(input(''))
    L=L+[a]

i=0
j=0
while i<len(L):
    j=i+1
    while j<len(L):
        if L[i]==L[j]:
            del(L[j])
        else:
            j=j+1
    M=L.copy()
    i=i+1
print(M)