
def addition():
    result = num1 + num2
    print(f"The answer is {result}")
    return result

def subtraction():
    result = num1 - num2
    print(f"The answer is {result}")
    return num1 - num2

def multiplication():
    result = num1 * num2
    print(f"The answer is {result}")
    return num1 * num2

def division():
    result = num1 / num2
    print(f"The answer is {result}")
    return num1 / num2

print("Welcome to our python calculator app. Select two numbers and an operation to be performed on it.")
print("What would you like to do?")
print("\n")
print("select 1 perform addition")
print("select 2 perform subtraction")
print("select 3 perform multiplication")
print("select 4 perform division")
print("select 5 to exit the app")
print("-------------------------------")

if __name__ == "__main__":
    while True:
        try:
            num1 = int(input("Enter the first number: "))
            num2 = int(input("Enter the second number: "))
            option = int(input("Enter the number coresponding to the operation: "))
        except:
            print("Invalid Input. Try again")
        
        if option ==1:
            addition()

        elif option == 2:
            subtraction()

        elif option == 3:
            multiplication()

        elif option == 4:
            division()

        elif option == 5:
            break

        else:
            print("Invalid Input!!")

print("Thank you for using our App. See you again!!")