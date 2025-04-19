class TodoApp:
    def __init__(self):
        self.todo_items = {}  # {id: {'name': ..., 'priority': ...}}
        self.next_id = 1

    def show_menu(self):
        print("-- ToDo CLI App --")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Delete Task")
        print("4. View Missing Priorities")
        print("5. Exit")

    def add_task(self):
        try:
            name = input("Enter task name: ").strip()
            priority = int(input("Enter task priority (positive integer): "))

            if priority <= 0:
                print("Priority must be a positive integer.")
                return

            self.todo_items[self.next_id] = {'name': name, 'priority': priority}
            self.next_id += 1
            print("Task added.")

        except ValueError:
            print("Priority must be a valid integer.")

    def get_priority(self, task_tuple):
        # task_tuple = (id, {'name': ..., 'priority': ...})
        return task_tuple[1]['priority']

    def list_tasks(self):
        if not self.todo_items:
            print("Your ToDo list is empty.")
            return

        print("--- TODO List ---")
        sorted_tasks = sorted(self.todo_items.items(), key=self.get_priority)
        for task_id, item in sorted_tasks:
            print(f"(ID: {task_id}) (task: {item['name']}) (priority:[{item['priority']}])")

    def delete_task(self):
        try:
            task_id = int(input("Enter the task ID to delete: "))
            if task_id in self.todo_items:
                del self.todo_items[task_id]
                print("Task deleted.")
            else:
                print("Task with that ID not found.")
        except ValueError:
            print("Task ID must be a valid integer.")

    def view_missing_priorities(self):
        if not self.todo_items:
            print("No tasks in the list.")
            return

        priorities = [item['priority'] for item in self.todo_items.values()]
        max_priority = max(priorities)
        existing_set = set(priorities)

        missing = [p for p in range(1, max_priority + 1) if p not in existing_set]
        if missing:
            print("Missing priorities:", missing)
        else:
            print("No missing priorities.")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Choose an option (1-5): ").strip()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.list_tasks()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.view_missing_priorities()
            elif choice == '5':
                print("Thank you for using the ToDo App!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == '__main__':
    app = TodoApp()
    app.run()
