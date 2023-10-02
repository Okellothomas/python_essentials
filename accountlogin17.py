# initialize the username and password
username = str(input("Enter your username: "))
password = str(input("Enter your password: "))

# give more direction to the user
print("Your account has been created successfully!")
print("Login now!")

username2 = str(input("Enter your username: "))
password2 = str(input("Enter your password: "))

if username == username2 and password == password2:
    print("Your have logged in succesfully")
else:
    print("Wrong cridentials")
