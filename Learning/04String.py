# name = "bhavy"
# friend = "neel"
# anotherFriend = "another"

# print("Hello, " + name)

# names = "hello, hi, how, are, you"
# print(names[0:5]) #prints hello
# print(names[:5]) #prints hello
# print(names[:]) #prints whole string
# print(names[0:-3]) #prints [0:len(names)-3]
# print(len(names)) #returns length of string

# String are immutable
a = "!!bhavy!!!!!!!"
spl = "ab cd ef gh"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # will remove ! behind string but before will be as it is !!bhavy
print(a.replace("bhavy", "new name")) # will change all occurence bhavy to new name in the string
print(spl.split(" ")) # this will print 'ab', 'cd', 'ef', 'gh'
heading = "this is heading"
print(heading.capitalize())
str1 = "Welcome to Python"
print(len(str1)) # 25
print(len(str1.center(50))) # will add 25 space on both side (50 length)
print(a.count("bhavy"))
print(a.endswith("!"))
