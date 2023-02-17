# Ham Index
def search(L,x):
    for i in range(0,len(L)):
        if L[i]==x:
            return i
    return None
L=[1,2,3,4,5]
x=5
print(search(L,x))