#### Requirements
- Implement a basic kanban board to be used from a command line interface with 3 statuses (Todo, In progress, and Done)
- Addition and removal of tasks to each, and moving them between statuses
- Assignees and Reporters
- Add more status fields to the Kanban Board
- Support for multiple boards for different projects
- Allow priorities and sorting by priority (High, Medium, Low)
#### Process:
1. I have created 3 lists named todo_list ,in_progress_list ,done_list so that when the task is given it will be added to the required specific list.
2. for the movement of the tasks between statuses i have created a loop so that it finds the task in the specific status and then removes it from that status and adds it to the new status given by the user.
3. coming to the part of assignees, i have created a dictionary and each key in the dictionary is the assigned person name and the value is a list containing all the tasks that specific person is assigned to.
