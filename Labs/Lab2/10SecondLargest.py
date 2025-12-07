# second largest number among three user input numbers
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if(a>b):
    if(a > c):
        if (b > c):
            print(b, "is second largest")
        else:
            print(c, "is second largest")
    else:
        print(a, "is second largest")

else:
    if (b > c):
        if (a > c):
            print(a, "is second largest")
        else:
            print(c, "is second largest")
    else:
        print(b, "is second largest")
