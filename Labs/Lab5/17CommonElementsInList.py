# create a list of common elements from given two lists
li1 = [-1, -2, -3, 4, -5, 6, 7, 1, 2, 3, 4, 5, 4, 6, 7]
li2 = [6, 7, 1, 2, 3, 4, 5, 4, 6, 7]
li = []
for li1 in li2:
    li.append(li1)
li = list(set(li))
print(li)
