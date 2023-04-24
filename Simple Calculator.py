past_calculations = []

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


def history():
    if past_calculations:
        for index, calc in enumerate(past_calculations):
            print(calc)
    else:
        print("No past calculations to show")
        return 0

def select_option(choice):
    if (choice=='#'):
        return 1
        
    elif (choice=='$'):
        print("~Reset~")
        return 0

    elif (choice in ('+','-','*','/','^','%')):
        while (True):
            
            Num1s = str(input("Enter your first number: "))
            print(Num1s)

            if (Num1s=='#'):
                return 1
        
            if (Num1s=='$'):
                print("~Reset~")
                return 0
            
            try:
                Num1 = float(Num1s)
                break
            except:
                print("~Not a valid number, Please enter again~")
                continue

        while (True):
            Num2s = str(input("Enter your second number: "))
            print(Num2s)

            if (Num2s=='#'):
                return 1
        
            if (Num2s=='$'):
                print("~Reset~")
                return 0

            try:
                Num2 = float(Num2s)
                break
            except:
                print("~Not a valid number, Please enter again~")
                continue          
           
        Result = 0.0
        last_calculation = ""

        if choice == '+':
            print(Num1, "+", Num2, "=", add(Num1,Num2))

        elif choice == '-':
            print(Num1, "-", Num2, "=", subtract(Num1,Num2))
                        
        elif choice == '*':
            print(Num1, "*", Num2, "=", multiply(Num1,Num2))
                        
        elif choice == '/':
            print(Num1, "/", Num2, "=", divide(Num1,Num2))

        elif choice == '^':
            print(Num1, "^", Num2, "=", Power(Num1,Num2))

        elif choice == '%':
            print(Num1, "%", Num2, "=", Remainder(Num1,Num2))

        else:
            print("~Something went wrong~")

        last_calculation = "{0} {1} {2} = {3}".format(Num1, choice, Num2, Result)
        #print("Previous Calculations are,")
        print(last_calculation)
        past_calculations.append(last_calculation)

    else: 
        print("~Unrecognized operation~")

while (True):

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
    
    if(select_option(choice) == 1):
        print("~Terminated~")
        exit()
    
    print("----------------------------------------------\n")


   