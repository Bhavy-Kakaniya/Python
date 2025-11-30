# basic function with no return and parameters
def greet():
    print("Hello")

# function with parameters
def calculateSum(a, b):
    print(a + b)

# default parameters
def power(base, exp=2):
    return base ** exp

# return multiple values
def calculate(a, b):
    return a+b, a-b, a*b

s, d, m = calculate(10, 3)

# keywords arguments
def info(name, age):
    print(name, age)

info(age=20, name="Bhavy")

# variable number of arguments
def total(*nums):
    return sum(nums)

total(1, 2, 3, 4)

# keyword variable number of arguments
def otherInfo(**data):
    for key, value in data.items():
        print(key, value)
otherInfo(name="Bhavy", age=20, city="Rajkot")

# lambda or anonymous function
square = lambda n: n*n
print(square(5))

#nested function
def outer():
    def inner():
        print("inside")
    inner()

# passing function into another function
def fun(x):
    return x*3
def apply(f, value):
    return f(value)
apply(fun, 10)
