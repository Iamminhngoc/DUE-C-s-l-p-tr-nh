s=input('')
s=s.split()
a='@gmail.com'
b=''
for i in s:
    if a in i:
        print(i)
if a not in s[len(s)-1]:
    print(b) 

