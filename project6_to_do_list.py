def show_tasks(tasks):

    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\nYour Tasks:\n")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    print()


def add_task(tasks):

    task = input("Enter Task: ")

    tasks.append(task)

    print("Task Added Successfully!")


def remove_task(tasks):

    if not tasks:
        print("\nNo tasks to remove.\n")
        return

    show_tasks(tasks)

    try:
        index = int(
            input("Enter Task Number to Remove: ")
        ) - 1

        if 0 <= index < len(tasks):

            removed_task = tasks.pop(index)

            print(f"Removed: {removed_task}")

        else:
            print("Invalid Task Number.")

    except ValueError:
        print("Please Enter a Valid Number.")


def save_tasks(tasks):

    with open("tasks.txt", "w") as file:

        for task in tasks:
            file.write(task + "\n")


def load_tasks():

    try:

        with open("tasks.txt", "r") as file:

            return [
                line.strip()
                for line in file.readlines()
            ]

    except FileNotFoundError:
        return []


tasks = load_tasks()

while True:

    print("\n===== TO-DO LIST MENU =====")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Save & Exit")

    choice = input("\nChoose an Option: ")

    if choice == "1":
        show_tasks(tasks)

    elif choice == "2":
        add_task(tasks)

    elif choice == "3":
        remove_task(tasks)

    elif choice == "4":

        save_tasks(tasks)

        print("\nTasks Saved Successfully.")
        print("Goodbye!")

        break

    else:
        print("Invalid Choice. Try Again.")