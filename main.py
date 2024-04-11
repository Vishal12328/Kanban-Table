print("Hello and welcome to Kanban board")

todo_list = []
in_progress_list = []
done_list = []

number_of_tasks = int(input("Enter the number of tasks you need to add:"))

def task_input():
    task = input("Enter the task: ")
    task_type = input("Enter the type of the task (todo/inProgress/done): ").lower()
    if task_type == "todo":
        todo_list.append(task)
    elif task_type == "inprogress":
        in_progress_list.append(task)
    elif task_type == "done":
        done_list.append(task)

for u in range(number_of_tasks):
    task_input()
print("TODO:", todo_list)
print("In Progress:", in_progress_list)
print("Done:", done_list)
