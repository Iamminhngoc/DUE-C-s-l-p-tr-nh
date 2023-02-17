n=int(input())
i=0
str = ""
if 0<=n and n<=9999:
    while n>0:
        x = n%10
        n=n/10
        n=int(n)
        i=i+1
        if x == 0:
            str = "A"+str
        elif x == 1:
            str="B"+str
        elif x == 2:
            str="C"+str
        elif x == 3:
            str="D"+str
        elif x == 4:
            str="E"+str
        elif x == 5:
            str="F"+str
        elif x == 6:
            str="G"+str
        elif x == 7:
            str="H"+str 
        elif x == 8:
            str="K"+str 
        elif x == 9:
            str="L"+str  
    print(str)
   
