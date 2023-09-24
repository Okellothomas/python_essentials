# try except enables us to catch an error and display it to the user
# It is also enables our code to run without breaking, with or without an error


'''
syntax
try:
code...
except:
code...
else:
code...
finally:
code...
'''

# Example of try except

try:
    num1 = int(input("Enter your favorite number: "))
    print(num1, "Is my favorite number")
except:
    print("Something went wrong! ")
else:
    print("Code excecuted successfully")
finally:
    print("Try, except has completed excecution")


def Try_Catch():

    try:
        # The body of the code to be executed
        age = int(input("Enter your age: "))
        return age
    except:
        # The error to be displayed to the user
        return "Something went wrong.... pleas try again"
    else:
        # The to be displayed to programmer to notify them of the success
        return "Code executed successfully!"
    finally:
        # code executed whether or not the it is a success.
        return "the try, except code has be excecuted"


print(Try_Catch())
