tasks=[]

while True:
    print("\n1.Add Task")
    print("2.View Tasks")
    print("3.Delete Tasks")
    print("4.Exit")


    choice=int(input("enter your choice :"))

    if choice==1:
        task=input("enter task:")
        tasks.append(task)

    elif choice==2:
        if len(tasks)==0:
            print("no task available")
        else:
            for i,task in enumerate(tasks):
                print(i+1,task)

    elif choice==3:
        num=int(input("enter task number to delete:"))
        if num <=len(tasks):
            tasks.pop(num-1)
        else:
            print("invalid task number")

    elif choice==4:
        break