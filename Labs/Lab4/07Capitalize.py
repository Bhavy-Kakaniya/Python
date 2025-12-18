# WAP to capitalize the first and last character of each word in a string
s = input("Enter string: ")
s = s.replace(s[0],s[0].upper())
s = s.replace(s[-1], s[-1].upper())
print(s)
