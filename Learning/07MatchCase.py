age = 2
match age:
    case 0:
        print("you are newborn")
    case 2:
        print("You are 2 years old")
    case 18:
        print("You are adult")
    case _ if(x != 0):
        print("Your age is not 0")
