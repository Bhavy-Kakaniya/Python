# interchange first and last element in list
li = [1, 2, 3, 4, 6, 9, 10]
print("Before: ", li)
li[0], li[-1] = li[-1], li[0]
print("After: ", li)
