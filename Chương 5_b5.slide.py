def update(L,x,y):
    for i in range(0,len(L)):
        if L[i]==x:
            L[i]=y
    return L
L=[1,2,3,4,5]
x=2
y=3
print(update(L,x,y))