from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        return f"Task is already in the section {self.name}"

    def complete_task(self, task_name: str):
        for current_task in self.tasks:
            if task_name == current_task.name:
                current_task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        amount_of_removed_tasks = 0
        for current_task in self.tasks:
            if current_task.completed:
                self.tasks.remove(current_task)
                amount_of_removed_tasks += 1
        return f"Cleared {amount_of_removed_tasks} tasks."

    def view_section(self):
        tasks_details = "\n".join([current_task.details() for current_task in self.tasks])
        result = f"Section {self.name}:" + "\n" + tasks_details
        return result


