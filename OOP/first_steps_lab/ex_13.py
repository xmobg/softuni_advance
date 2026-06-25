class TodoList:
    def __init__(self,owner):
        self.list = list()
        self.owner = owner

    def add_task(self,task):
        self.list.append(task)
        return f"Task '{task}' added"

    def complete_task(self,task):
        if task not in self.list:
            return 'Task not found'
        self.list.remove(task)
        return f"Task '{task}' completed"

    def show_tasks(self):
        if len(self.list) == 0:
            return 'No tasks'
        return f"{self.owner}'s tasks: {self.list}"


todo = TodoList("Pesho")
print(todo.add_task("Buy milk"))     # Task 'Buy milk' added
print(todo.add_task("Study OOP"))    # Task 'Study OOP' added
print(todo.show_tasks())             # Pesho's tasks: ['Buy milk', 'Study OOP']
print(todo.complete_task("Buy milk"))# Task 'Buy milk' completed
print(todo.show_tasks())             # Pesho's tasks: ['Study OOP']
