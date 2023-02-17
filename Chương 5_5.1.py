def Input():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input(''))
        L=L+[a]
    x=int(input('x='))
    return L,x
def FirstAndLast(L):
    a=[L[0],L[len(L)-1]]
    print(a)
def Search(L,x):
    for i in range(0,len(L)):
        if L[i]==x:
            return True
    return False
L,x=Input()
FirstAndLast(L)
print(Search(L,x))