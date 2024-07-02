import time
from rich.console import Console
from rich.progress_bar import ProgressBar
from rich.progress import Progress


console = Console()


def start_pomodoro_break(name: str, break_time: int = 5):
    notification_timmer = 6
    break_time_converted = break_time * 60
    sleep_interval = 60
    console.clear()
    console.print(f"Break Remaining: {break_time_converted/60}")
    with console.status(
        f"Solving global problems... But first a break...", spinner="earth"
    ) as status:
        while break_time_converted > 0:
            time.sleep(sleep_interval)
            console.clear()
            break_time_converted = break_time_converted - sleep_interval
            console.print(f"Break Remaining: {break_time_converted/60}")
        while notification_timmer < 0:
            console.bell()
            time.sleep(5)
            notification_timmer = notification_timmer - 1
    

def start_pomodoro_task(name: str, task_time: int = 25):
    notification_timmer = 6
    progressbar = Progress()
    progressbar.start()
    task_id = progressbar.add_task(f"[blue] {name}",total=task_time)
    break_id = progressbar.add_task(f"[red]Break Time")
    if task_time > 25:
        console.log("You are using a time that is over 25 minutes")
    task_time_converted = task_time * 60
    sleep_interval = 60
    console.clear()
    console.print(f"Time Remaining: {task_time_converted/60}")
    completed_minutes = 0
    while task_time_converted > 0:
        time.sleep(sleep_interval)
        task_time_converted = task_time_converted - sleep_interval
        completed_minutes = task_time - (task_time_converted / 60)
        print(completed_minutes)
        progressbar.update(task_id=task_id, completed=completed_minutes)
    progressbar.update(task_id=task_id, completed=completed_minutes)
    while notification_timmer < 0:
        console.bell()
        time.sleep(5)
        notification_timmer = notification_timmer - 1



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
            task_description = f"{self.task_name} - {iteration}"
            self.tasks.append(self.progressbar.add_task(description=task_description, total=self.task_time))
            self.tasks.append(self.progressbar.add_task(description=f"break - {iteration}", total=self.break_time))
        self.progressbar.start()
        for task in self.tasks:
            making_progress = True
            completed_time_update = 0
            while making_progress:
                time.sleep(10)
                completed_time_update = completed_time_update + 1
                self.progressbar.update(task_id=task, completed=completed_time_update)
                if completed_time_update >= self.task_time:
                    making_progress = False

        
