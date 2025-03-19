import random
import os


class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def display(self):
        """Display task details"""
        print(f"\nTask: {self.description}, Priority: {self.priority}")


tasks = {}


def add_task(description, priority):
    """Add a new task"""
    global tasks
    task_id = random.randint(100, 999)
    tasks[task_id] = Task(description, priority)
    print(f"\nTask added with ID: {task_id}")
    save_tasks()  # Save after adding a task


def update_priority(task_id, new_priority):
    """Update the priority of an existing task"""
    if task_id in tasks:
        tasks[task_id].priority = new_priority
        print("\nTask priority updated.")
        save_tasks()  # Save after updating priority
    else:
        print("\nTask not found!")


def delete_task(task_id):
    """Delete a task by its ID"""
    if task_id in tasks:
        del tasks[task_id]
        print("\nTask deleted successfully.")
        save_tasks()  # Save after deleting
    else:
        print("\nTask ID not found!")


def list_tasks():
    """Display all tasks"""
    if tasks:
        print("\nCurrent Tasks:")
        for task_id, task in tasks.items():
            print(f"\nID: {task_id} | Task: {task.description} | Priority: {task.priority}")
    else:
        print("\nNo tasks available.")


def save_tasks():
    """Save all tasks to a file"""
    with open("tasks.txt", "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id},{task.description},{task.priority}\n")


def load_tasks():
    """Load tasks from a file"""
    global tasks
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_id, description, priority = line.strip().split(",")
                tasks[int(task_id)] = Task(description, priority)
    else:
        print("\nNo saved tasks found.")


def task_menu():
    """Task management menu"""
    while True:
        print("\n1. Add Task\n2. Update Priority\n3. Delete Task\n4. List Tasks\n5. Exit")
        try:
            choice = int(input("\nEnter choice: "))

            if choice == 1:
                description = input("\nEnter task description: ")
                priority = input("Enter priority (High/Medium/Low): ")
                add_task(description, priority)

            elif choice == 2:
                task_id = int(input("\nEnter Task ID: "))
                new_priority = input("Enter new priority: ")
                update_priority(task_id, new_priority)

            elif choice == 3:
                task_id = int(input("\nEnter Task ID: "))
                delete_task(task_id)

            elif choice == 4:
                list_tasks()

            elif choice == 5:
                print("\nExiting task manager...")
                break  # Using break keyword

            else:
                print("\nInvalid choice, try again.")

        except ValueError:
            print("\nInvalid input! Please enter valid numbers.")


# Run the task manager
if __name__ == "__main__":
    load_tasks()  # Load existing tasks
    task_menu()
