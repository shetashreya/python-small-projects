class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, priority):
        task = Task(title, description, priority)
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_completed(self, index):
        if 0 < index <= len(self.tasks):
            task = self.tasks[index - 1]
            task.completed = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def view_tasks(self, filter_priority=None, filter_completed=None):
        filtered_tasks = self.tasks.copy()

        if filter_priority is not None:
            filtered_tasks = [task for task in filtered_tasks if task.priority == filter_priority]

        if filter_completed is not None:
            filtered_tasks = [task for task in filtered_tasks if task.completed == filter_completed]

        if filtered_tasks:
            print("Tasks:")
            for index, task in enumerate(filtered_tasks, start=1):
                status = "Completed" if task.completed else "Pending"
                print(f"{index}. {task.title} - Priority: {task.priority}, Status: {status}")
        else:
            print("No tasks matching the filter criteria.")

def main():
    task_manager = TaskManager()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. View Completed Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = input("Enter task priority (High, Medium, Low): ").capitalize()
            task_manager.add_task(title, description, priority)

        elif choice == "2":
            index = int(input("Enter task index to mark as completed: "))
            task_manager.mark_task_completed(index)

        elif choice == "3":
            filter_priority = input("Filter by priority (High, Medium, Low) or press Enter for all tasks: ").capitalize()
            filter_completed = input("Filter by completion status (Completed, Pending) or press Enter for all tasks: ").capitalize()
            task_manager.view_tasks(filter_priority, filter_completed)

        elif choice == "4":
            task_manager.view_tasks(filter_completed=True)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

