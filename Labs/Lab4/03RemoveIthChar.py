s1 = input("Enter string: ")
idx = int(input("Enter index: "))
s1 = s1[:idx:] + s1[idx + 1]
print(s1)
