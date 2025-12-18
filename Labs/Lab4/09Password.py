# Check if the password and confirm password is same or not. In case of only case's mistake, show the error message.
password = input("Enter password: ")
confirm_password = input("Enter confirm password: ")
if (confirm_password == password):
    print("log in succesfully")
elif (password.lower() == confirm_password.lower()):
    print("check character")
elif (confirm_password != password):
    print("wrong password")
