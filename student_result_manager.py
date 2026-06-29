student ={}

while True:
    print("\nStudent Result Manager------")
    print("1. Add Student")
    print("2. View Student")
    print("3. check Result")
    print("4. Exit")
    
    choice=int(input("Enter your cHoice:"))
    
    if choice==1:
        name = input("Enter Student name:")
        marks = int(input("Enter marks:"))
        student[name]=marks
        print(f"{name} successfully Added!")
        
    elif choice==2:
        if not student:
            print("No Student Found!")
        else:
            for name,marks in student.items():
                print(name,":",marks)
    
    elif choice==3:
        name=input("Enter name first:")
        if name in student:
            marks = student[name]
            
            if marks>=40:
                print("Pass")
            else:
                print("fail")
        else:
            print("student Not Found!")
    elif choice==4:
        print("Exiting......")
        break
    else:
        print("In-valid Input")