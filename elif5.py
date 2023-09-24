# The elif and function
# elif function to return divisibility table

value = int(input("Enter a number: "))


def Divisibility(value):
    if value % 2 == 0:
        return value, "is divisible by two"
    elif value % 3 == 0:
        return value, "is divisible by three"
    elif value % 5 == 0:
        return value, "is divisible by five"
    elif value % 2 == 0 and value % 3 == 0:
        return value, "is divisible by six"
    elif value % 7 == 0:
        return value, "is divisible by 7"
    elif value % 11 == 0:
        return value, "is divisible by eleven"
    else:
        return "We have not captured the divisiblity of", value


print(Divisibility(value))
