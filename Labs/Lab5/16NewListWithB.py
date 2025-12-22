# create a new list (fruit whose name starts with 'b') from the list of fruits given by user
li = ["apple", "banana", "papaya", "cherry", "Banana"]
b = []
for i in li:
    if i[0] == "b" or i[0] == "B":
        b.append(i)
print(b)
