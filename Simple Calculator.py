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