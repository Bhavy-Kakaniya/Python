# WAP in python to display the name of the day according to the number given by the user
days = int(input("Enter index of day: ")) - 1
days%=7
match days:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case _:
        print("Invalid")
