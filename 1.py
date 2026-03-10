def todo_list_app():
    tasks = []
    
    while True:
        print("\n--- To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update/Mark Task Complete")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            if not tasks:
                print("Your to-do list is empty.")
            else:
                for idx, task in enumerate(tasks, start=1):
                    status = "[X]" if task['completed'] else "[ ]"
                    print(f"{idx}. {status} {task['name']}")
                    
        elif choice == '2':
            task_name = input("Enter the new task: ")
            tasks.append({'name': task_name, 'completed': False})
            print("Task added successfully.")
            
        elif choice == '3':
            try:
                task_num = int(input("Enter task number to mark complete/update: "))
                if 1 <= task_num <= len(tasks):
                    tasks[task_num - 1]['completed'] = True
                    print("Task updated.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == '4':
            print("Exiting To-Do List.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo_list_app()