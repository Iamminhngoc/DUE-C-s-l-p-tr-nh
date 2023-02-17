a=input()
demchu=0
demso=0
for i in a:
    if i.isalpha():
        demchu=demchu+1
    if i.isnumeric():
        demso=demso+1
print("Chu cai:",demchu)
print("Chu so:",demso )
        