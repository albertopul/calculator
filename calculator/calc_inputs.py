import sys
from calc import Calculator

class UserInput:


    i = int(input("Choose operation by digit: 1 - addition, 2 - subtraction,\
    3 - multiplication, 4 - division, 0 - exit the program:   "))
    if i == 1:
        x = int(input("Pass first number:   "))
        y = int(input("Pass second number:   "))
        Calculator.add(x, y)
    elif i == 2:
        x = int(input("Pass first number:   "))
        y = int(input("Pass second number:   "))
        Calculator.subtract(x, y)
    elif i == 3:
        x = int(input("Pass first number:   "))
        y = int(input("Pass second number:   "))
        Calculator.multiply(x, y)
    elif i == 4:
        x = int(input("Pass first number:   "))
        y = int(input("Pass second number:   "))
        Calculator.divide(x, y)
    elif i == 0:
        sys.exit()
    else:
        print("Try again or type 0 to exit the program.")