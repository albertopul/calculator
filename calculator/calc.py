import sys
import calc_inputs

hello = "Hello, this is a simple calculator created in Python"
print(hello)

class Calculator:


    def add(x,y):
        print(f"Adding", x, "and", y)
        result = x + y
        print(f"Result is {result}")
        return result

    def subtract(x,y):
        print(f"Subtracking", y, "from", x)
        result = x - y
        print(f"Result is {result}")
        return result

    def multiply(x,y):
        print(f"Multiplying", x, "by", y)
        result = x * y
        print(f"Result is {result}")
        return result

    def divide(x,y):
        if y == 0:
            print("Dividing by 0 is forbidden!")
            raise ZeroDivisionError("Division by zero is not allowed")
        elif y != 0:
            print(f"dividing", x, "by", y)
            result = x / y
            print(f"Result is {result}")
            return result
    

if __name__ == "__main__":
    Calculator()