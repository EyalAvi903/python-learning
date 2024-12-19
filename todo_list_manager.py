import os

# Function to load tasks from the file
def load_tasks(file_name):
    tasks = []
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

# Function to save tasks to the file
def save_tasks(file_name, tasks):
    with open(file_name, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Main program
def todo_list_manager():
    file_name = "todo_list.txt"
    tasks = load_tasks(file_name)

    while True:
        print("\nTo-Do List Manager")
        print("1: View Tasks")
        print("2: Add Task")
        print("3: Remove Task")
        print("4: Mark Task as Complete")
        print("5: Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
        elif choice == "2":
            task = input("Enter a new task: ").strip()
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "3":
            try:
                task_num = int(input("Enter the task number to remove: "))
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' removed.")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "4":
            try:
                task_num = int(input("Enter the task number to mark as complete: "))
                tasks[task_num - 1] += " (Completed)"
                print(f"Task {task_num} marked as complete.")
            except (ValueError, IndexError):
                print("Invalid task number.")
        elif choice == "5":
            save_tasks(file_name, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
todo_list_manager()
