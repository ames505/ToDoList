# ToDo.py

def display_tasks(tasks):
    """Display tasks  in the list."""
    if not tasks: 
        print("There are currently no tasks to complete!")
    else:
        print("Here are your current tasks.")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter new task: ")
    tasks.append(task)
    print(f'Task "{task}" added!\n')
          
def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        if 0 <= task_index < len(tasks):
            removed_task = tasks.pop(task_index)
            print(f'Task "{removed_task}" removed!\n')
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    tasks = []
    while True:
        print("To Do List:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit List")

        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose from options 1-4!\n")

if __name__ == "__main__":
    main()

