def Input():
    n=int(input('n='))
    L=[]
    for i in range(1,n+1):
        a=int(input(''))
        L=L+[a]
    return L
def Search(L):
    max=L[0]
    for i in range(0,len(L)):
        if L[i]>max:
            max=L[i]
    min=L[0]
    for i in range(0,len(L)):
        if L[i]<min:
            min=L[i]
    return max,min
def Output(max,min):
    print(max,min)               
L=Input()
max,min=Search(L)
Output(max,min)