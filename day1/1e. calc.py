while(True):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("9. Exit")
    ch=int(input("Enter Your Choice: "))
    if(ch==1):
        a=int(input("Enter First Number"))
        b=int(input("Enter Second Number"))
        print("Sum=",a+b)
    elif(ch==2):
        a=int(input("Enter First Number"))
        b=int(input("Enter Second Number"))
        print("Difference=",a-b)
    elif(ch==3):
        a=int(input("Enter First Number"))
        b=int(input("Enter Second Number"))
        print("Multiplication=",a*b)
    elif(ch==4):
        a=int(input("Enter First Number"))
        b=int(input("Enter Second Number"))
        print("Division=",a/b)
    elif(ch==9):
        break
    else:
        print("Faulty Input")
