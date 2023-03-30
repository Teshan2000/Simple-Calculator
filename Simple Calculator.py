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
    if (choice=='#'):
        print("~Terminated~")
        exit()

    elif (choice=='$'):
        exit()

    elif (choice in '+','-','*','/','^','%'):
        while (True):
            
            Num1 = int(input("Enter your first number: "))
            print(Num1)

            Num2 = int(input("Enter your second number: "))
            print(Num2)

            
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

while(True):

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
    


print("----------------------------------------------")


   