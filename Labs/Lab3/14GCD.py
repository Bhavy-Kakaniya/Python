# print GCD of given two numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
while(b != 0):
    a,b = b,a % b
print("Hcf is ", a)
