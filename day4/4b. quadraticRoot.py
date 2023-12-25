import math
def roots(a,b,c):
    discriminant=b**2-4*a*c
    if discriminant>0:
        root1=(-b + math.sqrt(discriminant))/(2*a)
        root2=(-b - math.sqrt(discriminant))/(2*a)
        print(f"Roots are real and different: {root1}, {root2}")
    elif discriminant==0:
        root=-b/(2*a)
        print(f"Roots are real and the same: {root}")
    else:
        real=-b/(2*a)
        img=math.sqrt(abs(discriminant))/(2*a)
        print(f"Roots are complex: {real} + {img}i and {real} - {img}i")
print("Assume Quadratic Equation as Ax²+Bx+C=0")
a=float(input("Enter A: "))
b=float(input("Enter B: "))
c=float(input("Enter C: "))
roots(a,b,c)