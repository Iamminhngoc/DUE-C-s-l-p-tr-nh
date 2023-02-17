a=int(input("Tien thu="))
if a>=1   and a<=100 :
 print("Phai tra=",(550*a)*1.1,sep="")

if a>=101 and a<=150 :
 print("Phai tra=",round((550*100+750*(a-100))*1.1,1),sep="")
if a>=151 and a<=200 :
 print("Phai tra=",round((550*100+750*50+950*(a-150))*1.1,1),sep="")
if a>=201: 
 print("Phai tra=",round((550*100+750*50+950*50+(a-200))*1.1,1),sep="")


    

    