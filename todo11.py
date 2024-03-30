import os
import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip().split(",")
                    self.tasks.append(task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(",".join(task) + "\n")

    def add_task(self, name, priority, due_date):
        self.tasks.append([name, priority, due_date, "Incomplete"])
        self.save_tasks()

    def remove_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def mark_task_complete(self, index):
        self.tasks[index][-1] = "Complete"
        self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. Name: {task[0]}, Priority: {task[1]}, Due Date: {task[2]}, Status: {task[3]}")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()
    
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(name, priority, due_date)
        elif choice == "2":
            index = int(input("Enter index of task to remove: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.remove_task(index)
            else:
                print("Invalid index.")
        elif choice == "3":
            index = int(input("Enter index of task to mark as complete: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.mark_task_complete(index)
            else:
                print("Invalid index.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
import os
import datetime

class ToDoList:
    def _init_(self):
        self.tasks = []

    def load_tasks(self):
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                for line in file:
                    task = line.strip().split(",")
                    self.tasks.append(task)

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(",".join(task) + "\n")

    def add_task(self, name, priority, due_date):
        self.tasks.append([name, priority, due_date, "Incomplete"])
        self.save_tasks()

    def remove_task(self, index):
        del self.tasks[index]
        self.save_tasks()

    def mark_task_complete(self, index):
        self.tasks[index][-1] = "Complete"
        self.save_tasks()

    def display_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        print("Tasks:")
        for i, task in enumerate(self.tasks):
            print(f"{i+1}. Name: {task[0]}, Priority: {task[1]}, Due Date: {task[2]}, Status: {task[3]}")

def main():
    todo_list = ToDoList()
    todo_list.load_tasks()
    
    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. Display Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            priority = input("Enter priority (High/Medium/Low): ").capitalize()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            todo_list.add_task(name, priority, due_date)
        elif choice == "2":
            index = int(input("Enter index of task to remove: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.remove_task(index)
            else:
                print("Invalid index.")
        elif choice == "3":
            index = int(input("Enter index of task to mark as complete: ")) - 1
            if 0 <= index < len(todo_list.tasks):
                todo_list.mark_task_complete(index)
            else:
                print("Invalid index.")
        elif choice == "4":
            todo_list.display_tasks()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
