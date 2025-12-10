# sum of series 1 + 4 + 9 + 16 + 25 + 36 + ...n
n = int(input("Enter n: "))
sum = 0
for i in range(1, n+1):
    sum += i**2
print(sum)
