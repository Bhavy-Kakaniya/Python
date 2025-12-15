s1 = input("Enter string: ")
li = s1.split()
li = [i for i in li if len(i) % 2 == 0]
str = " ".join(li)
print(str)
