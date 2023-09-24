# we are going to write a basic calculator
# We will use
'''
1. input
2. function
3. elif statement
'''

# varible initiliaztions
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
operator = str(input("Enter the operator: "))

# function defination


def My_Calculator():
    if operator == '+':
        return "Sum is", num1 + num2 + num3
    elif operator == '-':
        return "Difference is", abs(num1 - num2 - num3)
    elif operator == '%':
        return "remender is", (num1 + num2) % num3
    elif operator == "*":
        return "Product is", num1 * num2 * num3
    elif operator == '/':
        return "Quotient is", (num1 * num2) / num3
    else:
        return "Invalid Operator"


# Call the function to return the appropriate answer
print(My_Calculator())
