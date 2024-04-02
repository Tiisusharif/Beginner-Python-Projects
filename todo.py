tasks = []


#Adding tasks to the list
def addTask():
        task = input("Please enter your task: ")
        tasks.append(task)
        print(f"Your task, '{task}' has been added successfully") 

#Displays the tasks in the list
def viewTask():
    if not tasks:
        print("Your task list is empty.")
    else:
        for index, task in enumerate(tasks):
            index =+1
            print(f"Task #{index}. {task}")

#Removes tasks from the list
def renoveTask():
    viewTask()
    try:
        removedTask = int(input("Enter the index of the task to delete it: "))
        if removedTask >= 0 and removedTask < len(tasks):
            del tasks[removedTask]
            print(f"Your task at the '{removedTask}' index has been removed")
        else:
            print(f"#{removedTask} was not found.")
    except:
        print("Invalid Input. Try again.")

if __name__ == "__main__":
    print("Welcome to our Todo App. ")

    while True:
        print("\n")
        print("What would you like to do. ")
        print("----------------------------")
        print("1. Add a task.")
        print("2. Remove a task.")
        print("3. View your tasks.")
        print("4. Quit.")

        option = input("Select one of the options above: ")

        if option == "1":
            addTask()

        elif option == "2":
            renoveTask()

        elif option == "3":
            viewTask()

        elif option == "4":
            break

        else:
            print("Invalid Input. Try again!!!")

print("Thanks for using our app see you soon!!")



