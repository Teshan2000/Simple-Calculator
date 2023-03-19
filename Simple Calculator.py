def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
def Power(x,y):
    return x ** y
def Remainder(x,y):
    return x % y

Num1 = int(input("Enter your first number: "))
Num2 = int(input("Enter your second number: "))

choice = str(input("Enter your choice: /n"))
print("+ - * / % ^")

if choice == '+':
    print(Num1 + " + " +  Num2 + " = ")

if choice == '-':
    print(Num1 + " - " + Num2 + " = ")
    
if choice == '*':
    print(Num1 + " * " +  Num2 + " = ")
    
if choice == '/':
    print(Num1 + " / " +  Num2 + " = ")

if choice == '^':
    print(Num1 + " ^ " +  Num2 + " = ")

if choice == '%':
    print(Num1 + " % " +  Num2 + " = ")

    