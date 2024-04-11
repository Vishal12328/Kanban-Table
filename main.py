def display_board():
    print("TODO:", todo_list)
    print("In Progress:", in_progress_list)
    print("Done:", done_list)

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
def redo_task():
    print(done_list)
    task_redo = input("which task from this would you like to redo?:")
    for l in done_list:
        if l == task_redo:
            done_list.remove(task_redo)
            todo_list.append(task_redo)
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

while True:
    print("\nMenu:")
    print("1. Display Board")
    print("2. Change Task Status")
    print("3. Assign Tasks")
    print("4. Generate Report")
    print("5. Sort by Priority")
    print("6. Redo Task")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        display_board()
    elif choice == "2":
        changer()
    elif choice == "3":
        assign_tasks()
    elif choice == "4":
        reporter()
    elif choice == "5":
        sorting_wrt_priority()
    elif choice == "6":
        redo_task()
    elif choice == "7":
        print("See you again..")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")
