li = [-1, 2, -3, 4, -5, 6, 7]
print("Before:", li)
p1 = int(input("Enter one position: "))
p2 = int(input("Enter second position: "))
if p1 >= len(li) or p2 >= len(li):
    print("Invalid position")
else:
    li[p1], li[p2] = li[p2], li[p1]
print("After:", li)
