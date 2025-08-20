list = []
print("---welcome to Todo app---")
total_task = int(input("Enter number of tasks you want to add : "))

for i in range(1,total_task+1):
    task = input(f"Enter task {i} = ")
    list.append(task)
print(f"Today's tasks is {list}")

while True:
    operation = int(input("1. Add Task \n2. Update Task \n3. Delete Task \n4. View Task \n5. Exit \n\n Enter Your Choice - "))

    if operation == 1:
        task = input("Enter task you want to Add = ")
        list.append(task)
        print(f"Task {task} added successfully")

    elif operation == 2:
        update = input("Enter task you want to update = ")
        if update in list:
            new = input("Enter a new task = ")
            ind = list.index(update)
            list[ind] = new
            print(f"Updated value is {new}.")

    elif operation == 3:
        delete = input("Enter task you want to delete = ")
        if delete in list:
            ind = list.index(delete)
            del list[ind]
            print(f"{delete} is Deleted.")

    elif operation == 4:
        print(" ",list)

    elif operation == 5:
        break

    else:
        print("Invalid Choice.")