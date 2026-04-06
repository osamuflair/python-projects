# A simple todo list
import csv
tasks = []

def add_task(task):
    global tasks
    tasks.append(task)

def delete_task(task):
    global tasks
    tasks.remove(task)

def clear_task():
    global tasks
    tasks = []

def view_task():
    global tasks
    print("To_do List:")
    for task in tasks:
        print(f"{task[0]} : {task[1]}")

def close_program():
    global tasks
    with open("to_do.csv", "w", newline="") as new_csv:
        csv_writer = csv.writer(new_csv)
        for line in tasks:
            csv_writer.writerow(line)

def load_tasks():
    global tasks
    try:
        with open("to_do.csv", "r") as new_csv:
            csv_reader = csv.reader(new_csv)
                
            for line in csv_reader:
                tasks.append(line)
    except FileNotFoundError:
         pass #first time running, no files yet

def main():
    while True:
        print("Welcome to your Task Manager")
        print("Press 1 to view your tasks  Press 2 to add a new task")
        print("Press 3 to remove a task    Press 4 to clear all tasks")
        print("Press 0 to close program")

        
        try:
            k = int(input(" "))
        except ValueError:
            print("Enter number 0 to 4")
            continue

        if k == 1:
            view_task()
            print("\n")
        elif k == 2:
            a = input("Enter the name of the task: ")
            b = input("Enter the time for the task: ")

            task = [a,b]
            add_task(task)
            print("\n")
        elif k == 3:
            a = input("Enter the name of the task to be removed: ")
            b = input("Enter the time for the task to be removed: ")

            task = [a,b]
            delete_task(task)
            print("\n")
        elif k == 4:
            clear_task()
            print("\n")
        elif k == 0:
            close_program()
            break
        else:
            print("Enter numbers from 0 to 4")
            print("\n")
load_tasks()
main()