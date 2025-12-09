a = int(input("enter age: "))
print("your age is: ", a)

if(a>18):
    print("you can drive")
else:
    print("you cannot drive you are under 18")

print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
print()
applePrice = 10
budget = 200
if(budget - applePrice > 50) :
    print("Add 1kg apples")
elif(budget - applePrice > 70) :
    print("Its okay you can buy")
else :
    print("Dont buy")
