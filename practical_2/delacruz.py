import random  


class Task:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority

    def display(self):
        """Display task details"""
        print(f"\nTask: {self.description}, Priority: {self.priority}")

tasks = {}


def add_task(description, priority):
    global tasks  
    task_id = random.randint(100, 999)
    tasks[task_id] = Task(description, priority)
    print(f"\nTask added with ID: {task_id}")

def update_priority(task_id, new_priority):
    if task_id in tasks:
        tasks[task_id].priority = new_priority
        print("\nTask priority updated.")
    else:
        print("\nTask not found!")

def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id] 
        print("\nTask deleted successfully.")
    else:
        print("\nTask ID not found!")


def list_tasks():
    if tasks:
        print("\nCurrent Tasks:")
        for task in tasks.values():
            task.display()
    else:
        print("\nNo tasks available.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id},{task.description},{task.priority}\n")
    print("\nTasks saved!")

def load_tasks():
    try:
        file = open("tasks.txt", "r")
        for line in file:
            task_id, description, priority = line.strip().split(",")
            tasks[int(task_id)] = Task(description, priority)
    except FileNotFoundError:
        print("\nNo saved tasks found.")
    finally:
        file.close()


def task_menu():
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
    save_tasks()  # Save tasks before exiting
