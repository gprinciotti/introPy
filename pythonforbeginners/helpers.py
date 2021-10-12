from datetime import datetime

def display(message, is_warning = False):
    if is_warning:
        print("Warning!")
    print(message)

def print_time2(task_name="DEFAULT MESSAGE"):
    print(task_name)
    print(datetime.now())