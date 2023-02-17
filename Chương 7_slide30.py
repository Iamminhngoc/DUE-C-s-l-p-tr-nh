while True:
    a=input("Nhap mat khau: ")
    if a.isupper() or a.islower() or a.isnumeric () or a.isalpha() or len(a)<8: 
        print(" Khong hop le!!!")
    else:
        print("Hop le!!!")
        break
        
  