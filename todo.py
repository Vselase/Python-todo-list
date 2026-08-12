tasks = []

while True:
    print("/nTO-DO LIST")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        print("task added!")

    elif choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else: 
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            number = int(input("Enter task number to delete: "))
            tasks.pop(number - 1)

            print("Task deleted!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")