# WAP to count numbers of vowels in given string
s = input("Enter string: ")
count = 0
for i in s:
    if 'aeiouAEIOU'.find(i) != -1:
        count+=1
print(count)
