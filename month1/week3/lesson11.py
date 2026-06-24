try:
    number = int(input("Введите число "))
    result = 10 / number
    print(result)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На 0 делить нельзя")

