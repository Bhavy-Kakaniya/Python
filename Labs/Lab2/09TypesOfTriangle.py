# Three sides of a triangle are entered through the keyboard, WAP to check whether the triangle is isosceles, equilateral 
# scalene or rightangled triangle
a = int(input("Enter Side 1: "))
b = int(input("Enter Side 2: "))
c = int(input("Enter Side 3: "))

if(a == b == c):
    print("Equilateral Triangle")
elif((a==b) or (b==c) or (a==c)):
    print("Isosceles Triangle")
elif((a**2==b**2+c**2) or (b**2==a**2+c**2) or (c**2==b**2+a**2)):
    print("Right Angled Triangle")
else:
    print("Scalene Triangle")
