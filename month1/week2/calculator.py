def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


try:
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
except ValueError:
    print("Не является числом")
else:
    operation = input("Введите операцию ")
    if operation == "+":
        print(add(a, b))
    elif operation == "-":
        print(subtract(a, b))
    elif operation == "*":
        print(multiply(a, b))
    elif operation == "/":
        division_result = divide(a, b)
        if division_result is None:
            print("На ноль делить нельзя")
        else:
            print(division_result)
    else:
        print("Неподдерживаемая операция")
