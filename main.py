def changer():
    task_finder = input("Enter the task you need to change: ")
    final_place = input("Where do you want to change it to?: ").lower()

    for lst in [todo_list, in_progress_list, done_list]:
        if task_finder in lst:
            lst.remove(task_finder)
            if final_place == "todo":
                todo_list.append(task_finder)
            elif final_place == "inprogress":
                in_progress_list.append(task_finder)
            elif final_place == "done":
                done_list.append(task_finder)
            break
    print("TODO:", todo_list)
    print("In Progress:", in_progress_list)
    print("Done:", done_list)

print("Hello and welcome to Kanban board")

todo_list = []
in_progress_list = []
done_list = []
def assign_tasks():
    assignees_dict = {}
    while True:
        assignee = input("Whom do you want to assign the task to? (If none, enter 'done'): ")
        if assignee.lower() == "done":
            break
        else:
            assign_task = input("What task would you like to assign?: ")
            assignees_dict.setdefault(assignee, []).append(assign_task)

    print("Assignees and Tasks:", assignees_dict)
number_of_tasks = int(input("Enter the number of tasks you need to add:"))
def reporter():
    report = []
    for key, value in assignees_dict.items():
        counter = 0
        for item in value:
            if item in todo_list:
                counter += 1
        if counter >= (len(value)//2)+1:
            report.append(key)
    print(report)
def sorting_wrt_priority():
    high_priority = []
    mid_priority = []
    low_priority = []
    while True:
        task_for_prior = input("what is the task that you would like to prioritize(if done enter done): ")
        if task_for_prior == "done":
            break
        type_of_prior = input("what is the level of priority(high/mid/low): ")
        if type_of_prior == "high":
            high_priority.append(task_for_prior)
        elif type_of_prior == "mid":
            mid_priority.append(task_for_prior)
        elif type_of_prior == "low":
            low_priority.append(task_for_prior)
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
