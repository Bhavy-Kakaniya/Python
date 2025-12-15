# string is palindrome or not
string = input("Enter string: ")
if(string == string[::-1]): #this is how string is reversed
    print("Palindrome")
else:
    print("Not Palindrome")
