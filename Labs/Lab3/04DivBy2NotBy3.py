# print numbers between two given numbers which is divisible by 2 but not divisible by 3
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))

for i in range(n1, n2+1):
    if((i % 2 == 0) and (i % 3 != 0)):
        print(i)
