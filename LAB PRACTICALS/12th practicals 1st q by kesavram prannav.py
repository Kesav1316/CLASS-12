#Create a menu driven program to perform arithmetic operations (+ - * /)
def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplcation(x,y):
    return x*y

def division(x,y):
    return x/y

while True:
    x = input("Enter the symbol of arithmetic operation: ")
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    if x == "+":
        print(addition(a,b))
    if x == "-":
        print(subtraction(a,b))
    if x == "*":
        print(multiplication(a,b))
    if x == "/":
        print(division(a,b))
    y = input("Do you want to continue:(Y for yes, N for no): ")
    if y == "Y":
        continue
    else:
        print("Thank you for using our program")
        break
