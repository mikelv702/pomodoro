import os
import json



class TaskConfig:
    def __init__(self):
        self.config_path = os.path.join(os.path.expanduser('~'), '.local/tasks/')
        self.task_file = os.path.join(self.config_path, 'task.json')
        self.tasks = self.get_tasks()

    def get_tasks(self):

        if os.path.exists(self.task_file):
            try:
                task_json = json.load(open(self.task_file))
                self.tasks = task_json
                return self.tasks
            except FileNotFoundError:
                print('Tasks not found. Maybe you forgot to init?')
            except Exception as e: 
                print("Unhanlded exception...")
                print(e)
        else:
            try:
                if not os.path.exists(self.config_path):
                    os.mkdir(self.config_path)
                with open(self.task_file, 'w') as f:
                    json.dump("[]", f)
            except Exception as e:
                print("Whoops")
                print(e)

    def add_task(self, task_name):
        if task_name in self.tasks:
            print("tasks exists")
        else:
            print(type(self.tasks))
            self.tasks.append(task_name)
            with open(self.task_file, 'w') as f:
                json.dump(self.tasks, f )
            