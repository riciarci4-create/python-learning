def greet(name):
    return "привет, " + name + "!"


def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


names = greet(input("Имя: "))
print(names)

result = add(7, 10)
print(result)

numbers = is_even(int(input("Введите число: ")))
print(numbers)
