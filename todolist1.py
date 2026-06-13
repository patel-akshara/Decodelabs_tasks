import json
import os

FILE_NAME = "tasks.json"


# -----------------------------
# Data Persistence Functions
# -----------------------------

def load_tasks():
    """
    Load tasks from JSON file.
    If file doesn't exist, return empty list.
    """
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


def save_tasks(tasks):
    """
    Save task list to JSON file.
    """
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Core Logic Functions
# -----------------------------

def add_task(tasks):
    """
    Add a new task into the list.
    """
    task_name = input("Enter task: ").strip()

    if task_name == "":
        print("Task cannot be empty.")
        return

    task = {
        "id": len(tasks) + 1,
        "task": task_name
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Task added successfully.")


def view_tasks(tasks):
    """
    Display all tasks using enumerate().
    """
    if not tasks:
        print("\nNo tasks available.\n")
        return

    print("\n----- TO-DO LIST -----")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['task']}")

    print("----------------------\n")


def delete_task(tasks):
    """
    Delete a task by number.
    """
    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)

            # Reassign IDs
            for i, task in enumerate(tasks, start=1):
                task["id"] = i

            save_tasks(tasks)

            print(f"Deleted: {removed_task['task']}")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# -----------------------------
# User Interface
# -----------------------------

def display_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")


def main():

    tasks = load_tasks()

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            delete_task(tasks)

        elif choice == "4":
            print("Thank you for using To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")


# -----------------------------
# Program Entry Point
# -----------------------------

if __name__ == "__main__":
    main()