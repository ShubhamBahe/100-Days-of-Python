print("============= TO-Do List ==============")


task = []

print("""
1. Add Task
2. View Tasks
3. Mark Task Completed
4. Delete Task
5. Exit
""")

while True:
  try :
    user_choice = int(input("Enter Your Choice to Perform Task 1/2/3/4/5:"))
  except ValueError :
    print("Invalid Input")
    continue

  if user_choice == 1:
    task_name = input("Enter task :")
    task.append(task_name)
    print("✅ Task Added")

  elif user_choice == 2:
    if task == []:
      print("No task added")
      print("Add Some Task")
    for index, t in enumerate(task, start=1):
      print(f"{index}.{t}")

  elif user_choice == 3:
     task_name2 = int(input("Enter No. which task is completed :"))
     if task_name2 > len(task):
       print("Enter valid Numbering")

     else :
      indexupdate = task_name2 - 1

      if task[indexupdate].endswith("✅"):
        print("Task Already Marked")
      else :
        task[indexupdate] = task[indexupdate] + "✅"
        print("mark as complete")


  elif user_choice == 4:
    indexno = int(input("Enter task no. to remove :"))
    task.pop(indexno-1)
    print("removed task")

  elif user_choice == 5 :
    print("thank you")
    break

  else :
    print("invalid choice")
