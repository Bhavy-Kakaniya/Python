# split the List into two parts and append the first part to the end
li = [-1, 2, -3, 4, -5, 6, 7]
half = int(len(li) / 2)
print(li[half::] + li[0:half:])
