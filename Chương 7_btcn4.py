s=input('')
s=s.split(',')
i=0
j=0
while i<len(s):
    j=i+1
    while j<len(s):
        if s[i]==s[j]:
            del(s[j])
        else:
            j=j+1
    i=i+1
s.sort()
s=','.join(s)
print(s)