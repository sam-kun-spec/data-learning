# while loop = run the code til a certain condition is true , and 
#                recheck the condition at the end of the loop

# while 2 == 2:
#     print("This is true.")

# while 2 == 2:
#     print("This is true.")
#     break  # to prevent infinite loop

# name  = input("Enter your name: ")

# while name == "" or not name.isalpha():
#     print("Invalid input. Please enter a valid name.")
#     name = input("Enter your name: ")

# print("Hello " + name + "!")


age = input("Enter your age: ")

while not age.isdigit():
    print("please enter a valid age.")
    age = input("enter your age:")

age = int(age)

while age < 0 or age > 150:
    print("please enter a valid age.")
    age = int(input("Enter your age: "))

print("you are " , age , " years old.")