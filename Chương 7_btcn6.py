s=input('')
s=s.split(',')
a=s.copy()
b=[]
for i in range(0,len(s)):
    s[i]=int(s[i],2)
    if s[i]%3==0:
        b=b+[a[i]]
b=','.join(b)
print(b)