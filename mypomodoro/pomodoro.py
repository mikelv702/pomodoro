import time
from rich.console import Console
from rich.progress_bar import ProgressBar
from rich.progress import Progress
from rich.prompt import Confirm


console = Console()

class PomodoroTask:
    def __init__(self, task_name, task_time, break_time, task_iterations):
        self.task_name = task_name
        self.task_time = task_time
        self.break_time = break_time
        self.task_iterations = task_iterations
        self.tasks = []

    def start_task(self):
        self.progressbar = Progress()
        for iteration in range(self.task_iterations):
            task_description = f"[TASK] {self.task_name} - {iteration}"
            self.tasks.append(task_description)
            break_description = f"[BREAK] {self.task_name} - {iteration}"
            self.tasks.append(break_description)
        self.progressbar.start()
        for task in self.tasks:
            if "[TASK]" in task:
                task_id = self.progressbar.add_task(description=task, total=self.task_time)

            if "[BREAK]" in task: 
                task_id = self.progressbar.add_task(description=task, total=self.break_time)
            completed_time_update = 0
            while not self.progressbar.finished:
                time.sleep(60)
                completed_time_update = completed_time_update + 1
                self.progressbar.update(task_id=task_id, completed=completed_time_update)
                if self.progressbar.finished:
                    for notify in range(6):
                        console.bell()
                        time.sleep(2)
                    
                    self.progressbar.remove_task(task_id=task_id)

        
