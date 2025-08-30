#def to_do_list():
task = []
try:
    while True:
        print("1. Add")
        print("2. Remove")
        print("3. See")
        user = int(input("Enter What Do You Want to select = "))
        
        if user == 1:
            add = input("Enter = ")
            task.append(add)
        elif user == 2:
            remove = input("remove = ")
            if remove in task:
                task.remove(remove)
            else:
                print("Not Found")
        elif user == 3:
            print(task)
        
        x = input("wanna again Yes/No = ").lower()
        if x == "yes":
            continue
        elif x == "no":
            print("THANK YOU 🤖")
            break
except ValueError:
    print("Please Enter The Valid Value")        
            
                                 

                

    