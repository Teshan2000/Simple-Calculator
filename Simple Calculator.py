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

print("| + | - | * | / | % | ^ |")
choice = str(input("Enter your choice: \n"))

if choice == '+':
    print(Num1, " + ", Num2, " = ", add(Num1,Num2))

elif choice == '-':
    print(Num1, " - ", Num2, " = ", subtract(Num1,Num2))
    
elif choice == '*':
    print(Num1 + " * " +  Num2 + " = ", multiply(Num1,Num2))
    
elif choice == '/':
    print(Num1 + " / " +  Num2 + " = ", divide(Num1,Num2))

elif choice == '^':
    print(Num1 + " ^ " +  Num2 + " = ", Power(Num1,Num2))

elif choice == '%':
    print(Num1 + " % " +  Num2 + " = ", Remainder(Num1,Num2))

else:
    print("Something went wrong")

    