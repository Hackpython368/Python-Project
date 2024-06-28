TODOLIST = []
def TodoList():
    while True:
        print("Welcome to a simple ToDo List .")

        print()
        print("1. Add Task in List")
        print("2. Remove Task in List")
        print("3. View Task in List")
        print("4. Exit")
        option = int(input("Enter your Choice :"))

        if option == 1:
            task = input("Enter the task :")
            TODOLIST.append(task)
        
        
        if option == 2:
            task = input("Enter the task :")
            try:
                TODOLIST.remove(task)
                print("Task Removed")
            except:
                print("\'",task,"\' is not in List")
        
        if option == 3:
            a = 1
            for i in TODOLIST:
                print(a,'---',i)
                a+=1
        
        if option == 4:
            print('Thank You ')
            break        
        
if __name__=='__main__':
    TodoList()
