# factorial of given number
n = int(input("Enter n: "))
ans = 1
for i in range (n, 0, -1):
    ans *= i
print(ans)
