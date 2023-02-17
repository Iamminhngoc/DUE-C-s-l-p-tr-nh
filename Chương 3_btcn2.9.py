n=int(input())
i=2
# if 2<=n and n<=50:
#     i=2
#     while i<=n:
#         print(i,end=" ")
#         i=i+2
if 2<=n and n<=50:
    for i in range (2,n+1,2):
         print(i, end=" ")