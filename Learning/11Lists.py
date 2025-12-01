# Creating list
arr = [1, 2, 3]
mixed = [10, "Bhavy", 3.14, True]
empty = []

# accessing elements
x = arr[0]
y = arr[-1]  # last element

# slicing
arr[1:4]
arr[:3]
arr[2:]
arr[::-1] # reverse

# adding elements
arr.append(10)
arr.insert(1, 50)
arr.extend([7, 8, 9])

# removing elements 
arr.remove(3)      # removes first occurrence of 3
arr.pop()          # removes last
arr.pop(2)         # remove by index
del arr[1]         # delete element at index
arr.clear()        # empty list

# searching
if 5 in arr:
    print("found")

# List Comprehension
arr.index(5)    # returns index
arr.count(5)    # count occurrences
squares = [x*x for x in range(1, 11)]
evens = [x for x in range(50) if x % 2 == 0]

# Copy lists
new = arr.copy()

# Sorting
arr.sort()
arr.sort(reverse=True)
sorted_arr = sorted(arr)    # returns new list

# Unpacking
a, b, c = [10, 20, 30]
x, *mid, y = [1, 2, 3, 4, 5]

# Join lists
c = a + b

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][2]  # is 6
