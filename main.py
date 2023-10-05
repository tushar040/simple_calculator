def add(x , y):
    return x + y

def subtract(x , y):
    return  x - y

def multiply(x , y):
    return x * y

def divide(x , y):
    if y != 0:
        return x / y
    else:
        return "cannot divide by zero"

print("select operation")
print("1. for addition")
print("2. for subtraction")
print("3. for multiplication")
print("4. for division")

choice = int(input("Enter your choice(1/2/3/4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter your second number: "))

if choice == 1:
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input")
