# Functions refers to a set of
# the Add_Num returns the greatest number among three numbers
def Add_num(a, b, c):
    if (a > b and a > c):
        print(a, "is the largest")
    elif (b > a and b > c):
        print(b, "is the largest")
    else:
        print(c, "is the largest")


Add_num(a=10, b=100, c=103)

# a function that accepts inputs:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


def Greatest(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print(num1, "is the greatest")
    elif (num2 > num1 and num2 > num1):
        print(num2, "is the greatest")
    else:
        print(num3, "is the greatest")


Greatest(num1, num2, num3)

# the return statement in a python

num4 = int(input("Enter the first number: "))
num6 = int(input("Enter the second number: "))
num7 = int(input("Enter the third number: "))


def Multipy_Numbers(num4, num6, num7):
    return (num4 * num6 * num7)


print(Multipy_Numbers(num4, num6, num7))
