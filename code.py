from datetime import datetime
class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.completed = False
        self.due_date = due_date

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        due_date_str = f", Due: {self.due_date}" if self.due_date else ""
        return f"{self.description} - {status}{due_date_str}"


class TaskBuilder:
    def __init__(self, description):
        self.task = Task(description)

    def set_due_date(self, due_date):
        self.task.set_due_date(due_date)
        return self

    def build(self):
        return self.task


# Memento pattern to manage state history for undo/redo functionality
class TaskHistory:
    def __init__(self):
        self.history = []

    def add_state(self, state):
        self.history.append(state)

    def undo(self):
        if len(self.history) > 1:
            self.history.pop()
            return self.history[-1]
        else:
            return self.history[0]


class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None):
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        return new_task

    def mark_completed(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                task.mark_completed()
                return True
        return False

    def delete_task(self, task_description):
        self.tasks = [task for task in self.tasks if task.description != task_description]

    def view_tasks(self, filter_type=None):
        if filter_type == 'completed':
            return [task for task in self.tasks if task.completed]
        elif filter_type == 'pending':
            return [task for task in self.tasks if not task.completed]
        else:
            return self.tasks


def manage_todo_list():
    manager = ToDoListManager()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            due_date_input = input("Enter due date (YYYY-MM-DD), leave empty if none: ")
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d") if due_date_input else None
            manager.add_task(description, due_date)
            print("Task added successfully!")

        elif choice == '2':
            description = input("Enter task description to mark as completed: ")
            if manager.mark_completed(description):
                print(f"Task '{description}' marked as completed.")
            else:
                print(f"No task found with description '{description}'.")

        elif choice == '3':
            description = input("Enter task description to delete: ")
            manager.delete_task(description)
            print(f"Task '{description}' deleted.")

        elif choice == '4':
            filter_type = input("Enter filter type (all/completed/pending): ")
            tasks = manager.view_tasks(filter_type)
            if tasks:
                print("Tasks:")
                for task in tasks:
                    print(task)
            else:
                print("No tasks found with the given filter.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    manage_todo_list()
