def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    try:
        return x / y
    except Exception as e:
        print(e)

def Power(x,y):
    return x ** y

def Remainder(x,y):
    return x % y

def select_option(choice):
    if choice == '#':
        print("~Terminated~")
        exit()
    
    if choice == '$':
        return -1


Num1 = int(input("Enter your first number: "))
Num2 = int(input("Enter your second number: "))

        
print("Select operation:")
print("1.Add      : + ")
print("2.Subtract : - ")
print("3.Multiply : * ")
print("4.Divide   : / ")
print("5.Power    : ^ ")
print("6.Remainder: % ")
print("7.Terminate: # ")
print("8.Reset    : $ ")

choice = str(input("Enter your choice: \n"))

#ans = "Your answer is {}"
#print(ans.format())
     
while (Num1 or Num2 != 0):

    if choice == '+':
        print(Num1, " + ", Num2, " = ", add(Num1,Num2))

    elif choice == '-':
        print(Num1, " - ", Num2, " = ", subtract(Num1,Num2))
            
    elif choice == '*':
        print(Num1, " * ", Num2, " = ", multiply(Num1,Num2))
            
    elif choice == '/':
        print(Num1, " / ", Num2, " = ", divide(Num1,Num2))

    elif choice == '^':
        print(Num1, " ^ ", Num2, " = ", Power(Num1,Num2))

    elif choice == '%':
        print(Num1, " % ", Num2, " = ", Remainder(Num1,Num2))

    else:
        print("Something went wrong")

   