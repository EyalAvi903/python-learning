class Task:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.completed = False  # By default, a task is not completed

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} ({self.priority.capitalize()} Priority) - {status}"
    
class TodoList:
    def __init__(self):
        self.tasks = []  # List to store Task objects

    def add_task(self, name, priority):
        task = Task(name, priority)
        self.tasks.append(task)

    def remove_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            return self.tasks.pop(task_number - 1)
        else:
            return None

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1].mark_completed()
            return True
        return False

    def print_tasks_by_priority(self):
        priorities = {"high": [], "medium": [], "low": []}
        for task in self.tasks:
            priorities[task.priority].append(task)

        for priority, tasks in priorities.items():
            print(f"\n{priority.capitalize()} Priority:")
            for task in tasks:
                print(f" - {task}")

    def __str__(self):
        if not self.tasks:
            return "No tasks available."
        return "\n".join([f"{i+1}. {task}" for i, task in enumerate(self.tasks)])

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. View Tasks by Priority")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            print("\nYour To-Do List:")
            print(todo_list)
        elif choice == "2":
            name = input("Enter the task name: ").strip()
            priority = input("Enter the task priority (high, medium, low): ").strip().lower()
            if priority in {"high", "medium", "low"}:
                todo_list.add_task(name, priority)
                print(f"Task '{name}' added.")
            else:
                print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to remove: "))
                removed_task = todo_list.remove_task(task_number)
                if removed_task:
                    print(f"Task '{removed_task.name}' removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == "4":
            try:
                task_number = int(input("Enter the task number to mark as completed: "))
                if todo_list.mark_task_completed(task_number):
                    print("Task marked as completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        elif choice == "5":
            todo_list.print_tasks_by_priority()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
