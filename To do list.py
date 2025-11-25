# ----------------------------------------
# Project 3: To-Do List Manager
# ----------------------------------------

import json
import os

FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    print("Task added!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\n--- Task List ---")
    for i, t in enumerate(tasks, 1):
        status = "✔ Done" if t["done"] else "❌ Pending"
        print(f"{i}. {t['task']} - {status}")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        print("Task deleted!")
    except:
        print("Invalid selection.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        tasks[index]["done"] = True
        print("Task marked as done!")
    except:
        print("Invalid selection.")

def main():
    tasks = load_tasks()

    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1": add_task(tasks)
        elif choice == "2": view_tasks(tasks)
        elif choice == "3": delete_task(tasks)
        elif choice == "4": mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Saved & Exiting...")
            break
        else:
            print("Invalid option!")

        save_tasks(tasks)

main()
