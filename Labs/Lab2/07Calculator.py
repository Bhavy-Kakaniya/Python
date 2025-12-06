#  WAP to implement simple calculator which performs (add,sub,mul,div) of two no. based on user input
a = int(input("Enter A: "))
operation = input("Enter operation to perform")
b = int(input("Enter B: "))

match operation:
    case '+':
        print(a, " + ", b, " = ", (a + b))
    case '-':
        print(a, " - ", b, " = ", (a - b))
    case '*':
        print(a, " * ", b, " = ", (a * b))
    case '/':
        print(a, " / ", b, " = ", (a / b))
    case _:
        print("Invalid")
