def delete(L,x):
    M=L.copy()
    L.clear()
    for i in M:
        if x!=i:
            L.append(i)
L=[1,2,3,4,5]
delete(L,2)
print(L)