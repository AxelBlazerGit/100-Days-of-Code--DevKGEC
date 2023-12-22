a=int(input("Enter a number to be reversed: "))
a2=0
while(a>0):
    a2=a2*10+(a%10)
    a//=10
print(a2)