a='''---Người---đâu-gặp---gỡ-làm-chi---
trăm---năm-biết-có-duyên---gì---hay--không?'''
b=a.split("\n")

c=b[0].split("-")
while "" in c:
    c.remove("")
print(" ".join(c))

d=b[1].split("-")
while "" in d:
    d.remove("")
print(" ".join(d))




        
        
    

    
    
