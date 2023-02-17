# Ham Insert
L=[1,2,3,4,5]
def add(L,x,k):
    if k>=len(L):
        L=L+[x]
    else:
        L=L[:k]+[x]+L[k:]
    return L

x=10
k=3
L=add(L,x,k)
print(L)