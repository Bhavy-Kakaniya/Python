import math
n = int(input("Enter n: "))
ans = True
for i in range(2, int(math.sqrt(n) + 1)):
    if(n % i == 0):
        ans = False
        break
if(ans):
    print(n, "is a prime number")
else:
    print(n, "is not prime number")
