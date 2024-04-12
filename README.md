#### Requirements
- Implement a basic kanban board to be used from a command line interface with 3 statuses (Todo, In progress, and Done)
- Addition and removal of tasks to each, and moving them between statuses
- Assignees and Reporters
- Add more status fields to the Kanban Board
- Support for multiple boards for different projects
- Allow priorities and sorting by priority (High, Medium, Low)
- Please make use of an appropriate storage solution to persist tasks, boards, and statuses across runs.
#### Process:
1. I have created 3 lists named todo_list ,in_progress_list ,done_list so that when the task is given it will be added to the required specific list.
2. for the movement of the tasks between statuses i have created a loop so that it finds the task in the specific status and then removes it from that status and adds it to the new status given by the user.
3. coming to the part of assignees, i have created a dictionary and each key in the dictionary is then assigned person name and the value is a list containing all the tasks that specific person is assigned to.
4. when it comes to reports, the condition for reports is when an assignee has more than half of his/her tasks in todo status, then that particular asignee will be added to the report list.
5. Idea of the 4th feature is something like this. use the existing code in a base class and when ever a new board is required, create a class which inherits from the base class. with this we can create different boards for different projects.
6. sorting with priority is completely done by user, when the user enters a task, at the same time it is asked what kind of priority is the task and then that task is added to that specific priority task list.
7. An extra status field that I added is the "Redo" Field where the user can change the task which is "done" to "todo" so that he can redo the task.
8. For the 6th feature i used the "File Handling" where at the end of the programme, it create a file named "man.txt" which contains all the lists and the items, so that the data entered by the user is stored in between runs.
