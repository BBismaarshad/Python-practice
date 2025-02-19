def task():
    # List to store tasks
    tasks = []
    print("Welcome To The Task Management App")

    # Asking user how many tasks they want to add initially
    total_task = int(input("Enter how many tasks you want to add: "))
    
    # Loop to take task inputs
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)  # Adding task to the list

    print(f"Today's tasks: {tasks}")

    # Infinite loop for task management operations
    while True:
        # Displaying menu options
        print("\nOperations:")
        print("1 - Add Task")
        print("2 - Update Task")
        print("3 - Delete Task")
        print("4 - View Tasks")
        print("5 - Exit")

        # Taking user input for operation selection
        operation = int(input("Enter your choice: "))

        if operation == 1:  
            # Adding a new task
            add = input("Enter the task you want to add: ")
            tasks.append(add)  # Adding new task to the list
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            # Updating an existing task
            updated_val = input("Enter the task name you want to update: ")
            if updated_val in tasks:
                new_task = input("Enter the new task: ")
                ind = tasks.index(updated_val)  # Finding index of old task
                tasks[ind] = new_task  # Replacing old task with new task
                print(f"Task updated: '{updated_val}' → '{new_task}'")
            else:
                print("Task not found.")  # Error message if task doesn't exist

        elif operation == 3:
            # Deleting a task
            del_val = input("Which task do you want to delete: ")
            if del_val in tasks:
                tasks.remove(del_val)  # Removing task from the list
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found.")  # Error message if task doesn't exist

        elif operation == 4:
            # Viewing all tasks
            print(f"Total tasks: {tasks}")

        elif operation == 5:
            # Exiting the program
            print("Closing the program...")
            break  # Breaking the loop

        else:
            print("Invalid input. Please enter a valid option.")  # Handling invalid inputs

# Run the function
task()
