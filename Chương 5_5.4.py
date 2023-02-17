n=int(input('n='))
A=[]
B=[]
for i in range(1,n+1):
    a=int(input(''))
    A=A+[a]
    B=[a]+B
print(B)
C=[]
for i in range(0,len(B)):
    for j in range(i+1,len(B)):
        if B[i]>B[j]:
            t=B[i]
            B[i]=B[j]
            B[j]=t
    C=C+[B[i]]
print(C)
            

    
    
            
