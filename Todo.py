print("To do List Menu\n"
      "1. View Task\n"
      "2. Add a Task\n"
      "3. Remove a Task\n"
      "4. Exit\n")
choice =0
iterator=1
todolist ={}
keys = list(todolist.keys())
while True:
    try:
        choice = int(input("What is your choice? "))
        if choice==4:
            break

        elif choice ==1:
            if not todolist:
                print("No tasks available.")
            for i in todolist:
                print(i,todolist[i])
        elif choice ==2:
            new_task =input("input new task: ")
            todolist[iterator]=new_task
            iterator =iterator+1
            keys = list(todolist.keys())
        elif choice == 3:
            if not todolist:
                print("No tasks to remove.")
                continue
            del_task =int(input("Number of the task you wanna delete?: "))
            if del_task in todolist:
                del todolist[del_task]
            new_todolist = {}
            new_index = 1  # Restart numbering from 1
            for key in sorted(todolist.keys()):  
                    new_todolist[new_index] = todolist[key]
                    new_index += 1

            todolist = new_todolist  # Replace old dictionary
            iterator = len(todolist) + 1 

        else:
            print("invalid input")
            continue
    except ValueError:
        print("invalid input")
        continue

        



