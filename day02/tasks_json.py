import json

def save_tasks(tasks, filename):
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)
def load_tasks(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def add_task(filename, title):
    tasks = load_tasks(filename)
    new_task = {"title": title, "done": False}
    tasks.append(new_task)
    save_tasks(tasks, filename)


add_task("tasks.json", "Learn Python")
add_task("tasks.json", "Learn JSON")
print(load_tasks("tasks.json"))
add_task("tasks.json", "Learn files")
add_task("tasks.json", "Learn JSON")
print(load_tasks("tasks.json"))