# add taks to a list 
# mark task as complete
# view tasks 
# quit

massege = """ 1-add task to the list 
 2-mark task as complete
 3-view tasks 
 4-quit"""
tasks = []
# ===============================================================
def add_task():
    
    # take the task
    task = input("what is the task:\n")

    # defin task info 
    task_info = {"task": task,'status':False}

    # add task to the list 
    tasks.append(task_info)
    
    # tell it done :
    print('task added.\nit is now in list of tasks ')
# ===============================================================
def mark_task_complete():
    # get list of tasks didnt complete
    incompleted_tasks = [task for task in tasks if task['status'] == False]
    if len(incompleted_tasks) ==0 :
         print('no tasks to mark as complete')
         return
    # show them to the user 
    for i,task  in enumerate(incompleted_tasks):
           print(f"{i+1}- {task['task']}")
           print('='*50)
    
    # get the task from the user
    task_num = int( input('\nput the number of tasks you did it, (press 0 to skip)\n'))
    if task_num != 0 and task_num-1 <= len(tasks):
       incompleted_tasks[task_num - 1]['status']=True
    elif task_num-1 > len(tasks):
         print('Error please write correct num')
    return
# ===============================================================
def view_tasks():
    # see if there is a tasks,not : print no tasks to view
     if not tasks:
         print('no tasks to view')
         return
     for i, task in enumerate(tasks):
        if task["status"]:
            completed = '✔'
        else:
             completed = '❌'
        print(f'{i+1}. {task["task"]} {completed}')
# ===============================================================
def body_pro():
   while True:
      print(massege)
      choice = input('Enter your choice:\n')
      if choice == "1":
        add_task()
      elif choice == '2':
        mark_task_complete()
      elif choice == '3':
        view_tasks()
      elif choice == '4':
        break
      else :
          print('sorry but you write wrong => (you must chose the number of the choice)')
# ===============================================================
body_pro()
