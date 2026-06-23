def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Нельзя делить на 0"
    return a / b

a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
operation = input("Введите операцию ")
if operation == "+":
    print(add(a, b))
elif operation == "-":
    print(subtract(a, b))
elif operation == "*":
    print(multiply(a, b))
elif operation == "/":
    print(divide(a, b))
