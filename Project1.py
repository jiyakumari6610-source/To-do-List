my_tasks=[]
print("====Welcome to your Task Builder App====")
while True:
    print("===Menu===")
    print(" 1. Add tasks\n 2. View tasks\n 3. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        task=input("Enter your task 📑:")
        my_tasks.append(task)
        print("Task added successfully!💯👍")
    elif choice==2:
        if len(my_tasks)==0:
            print("No task to display")
        else:
            for index,task in enumerate(my_tasks,start=1):
                print(f"{index}.{task}")
    elif choice==3:
        print("Let's exit the program")
        break
    else:
        print("Invalid Choice ! Enter a valid choice.")



    

