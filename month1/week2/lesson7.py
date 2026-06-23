car = {
    "marka": "Niva",
    "age": 2000,
    "color": "red"
}

car["mileage"] = 150000
car["color"] = "blue"
del car["age"]
print(car)

person = {
    "name": "Artem",
    "age": 27,
    "city": "Kazan"
}

for key in person:
    print(person[key])

for value in person.values():
    print(value)

for key, value in person.items():
    print(key, value)
