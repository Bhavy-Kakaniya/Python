# WAP to read marks of five subjects. Calculate percentage and print class accordingly.
s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
s4 = int(input("Enter marks of subject 4: "))
s5 = int(input("Enter marks of subject 5: "))

p = (s1+s2+s3+s4+s5) / 5

print('Percentage:', p)


if(p < 35):
    print("Fail")
elif(p >= 35 and p < 45):
    print("Pass")
elif(p >= 45 and p < 60):
    print("Second Class")
elif(p >= 60 and p < 70):
    print("First Class")
elif(p >= 70):
    print("Distinction")
else:
    print("Invalid")
