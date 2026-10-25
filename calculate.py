import math
print("Hello , WELCOME TO CALCULATOR APP")

def inputs_from_user():
    try:
        a=int(input("enter 'a' number:"))
        b=int(input("enter 'b' number:"))
        return a,b
    except:
        print("Invalid input,Please enter numbers only.")
        a=int(input("enter 'a' number:"))
        b=int(input("enter 'b' number:"))
        return a,b

def Add():
    a,b=inputs_from_user()
    print("sum =",a+b)

def Subtract():
    a, b = inputs_from_user()
    print("Subtraction=",a-b)

def Multiply():
    a, b = inputs_from_user()
    print("Multiplication=",a*b)
def Divide():
    try:
        a, b = inputs_from_user()
        print("Divided by =",a/b)
    except ZeroDivisionError:
        print("Cannot divide by zero! Please enter a non-zero number.")

def Modulous():
    a, b = inputs_from_user()
    print("Modulous =",a%b)

def power():
    a,b = inputs_from_user()
    print("Power =",a**b)

def square():
    s=int(input("Enter a number to square:"))
    if s<0:
        print("Square Error, Negative numbers are not allowed")
    else:
        print("square=",math.sqrt(s))

def percentage():
    a,b=inputs_from_user()
    print("percentage=",(a/b)*100)

def exit():
    print("Exiting")

while True:
#print("Hello , Choose the Operator \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Modulous\n")
 try:
    n=int(input("Choose the Operator\n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Modulous\n 6.power\n 7.square\n 8.percentage\n 9.Exit\n"))
    if(n>0):
        if(n==1):
            Add()
        elif(n==2):
            Subtract()
        elif(n==3):
            Multiply()
        elif(n==4):
            Divide()
        elif(n==5):
            Modulous()
        elif(n==6):
            power()
        elif(n==7):
            square()
        elif(n==8):
            percentage()
        elif(n==9):
            exit()
            break
        else:
            print("choose numbers from above otherwise,Exit")
    else:
        print("Invalid Operator")
 except ValueError:
     print("Invalid Operator,Please enter numbers only from the menu")
