leap=int(input("Enter a year to check for leap year: "))

if leap % 400==0:
    print("Leap Year!")
elif leap % 100==0:
    print("Not a Leap Year...")
elif leap % 4==0:
    print("Leap Year!")
else:
    print("Not a Leap Year...")
