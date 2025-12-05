a = int(input("Enter a: "))
b = int(input("Enter b: "))

if (a>b):
    print(a,'>',b)
elif (b>a):
    print(a,'<',b)
else:
    print(a,'=',b)
 
print(a, ">", b) if(a > b) else print(a, "<", b)