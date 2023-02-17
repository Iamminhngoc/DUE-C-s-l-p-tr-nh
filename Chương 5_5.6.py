A=[]
for i in range(10):
    n=int(input(''))
    A=A+[n]
B=A.copy()
for i in range(0,10,2):
    B[i]=A[i+1]
    B[i+1]=A[i]
print(B)