import typer
import time
from rich.console import Console
import pomodoro
from pomodoro import PomodoroTask
from task_handler import TaskConfig
import json



app = typer.Typer()

tasks = TaskConfig()

@app.command()
def start_task(name: str, task_time: int = 25):
    #pomodoro.start_pomodoro_task(name=name, task_time=task_time)
    task = PomodoroTask(task_name=name, task_time=task_time, break_time=5, task_iterations=4)
    task.start_task()



@app.command()
def create_task(name: str):
    tasks.add_task(task_name= name)

@app.command()
def read_tasks():
    return print(tasks.get_tasks())

@app.command()
def delete_task(name: str):
    pass

@app.command()
def update_task(name: str):
    pass


if __name__ == "__main__":
    app()


