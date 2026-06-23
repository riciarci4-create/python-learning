def greet(name):
    return "привет, " + name + "!"
names = greet(input("Имя"))
print(names)
def add(a, b):
    return a + b
result = add(7, 10)
print(result)
def is_even(number):
    return number % 2 == 0
numbers = is_even(int(input("Введите число ")))
print(numbers)