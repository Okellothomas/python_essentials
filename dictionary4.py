# Dictionary is an equivalent of object in javascript

from multiprocessing import Value


dictionary = {
    "name": "Okello",
    "age": 27,
    "nationality": "Kenyan",
    "single": False,
    "friends": ["Sam", "Singa", "Gero"],
    "motoo": "Jaka Jinga, Jeuri"
}

x = dictionary['name']
p = dictionary['age']
y = dictionary['nationality']


def my_Dictionary(value):
    value = int(input("Enter the appropriate value: "))
    if value == x:
        return "Okello is the name"
    elif value == p:
        return "Okello is aged ", p
    elif value == y:
        return "Okello is a ", y
    else:
        return "Invalid input"


print(my_Dictionary(dictionary['age']))
