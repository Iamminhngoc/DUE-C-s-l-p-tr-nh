s=input('')
x=int(input(''))
s=s.split()
dem=0
for i in range(0,len(s)):
    if int(s[i])==x:
        a=i+1
        dem=dem+1
        print(a)
if dem==0:
    print('0')