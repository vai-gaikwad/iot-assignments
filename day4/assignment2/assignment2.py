import emp


# employee table has been created on iotdb by using new_table.py

#connector is making conection with mysql server and  this python program

# emp.py has all the definations for add_emp(), delete_emp(), update_emp(), show_table(), from_dept(), max_sal(), min_sal()

choice=0
choice=int(input("enter 1 to enter into employee db : "))
print("")
while choice==1:
    print("1. display all records from db")
    print("")
    print("2. add employee record")
    print("")
    print("3. delete employee record")
    print("")
    print("4. update employee record")
    print("")
    print("5. display records from deparrtment")
    print("")
    print("6. max salary employee")
    print("")
    print("7. least salary employee")
    print("")
    choice=int(input(" 1 to proceed 0 to exit : "))
    if choice==0:
        print("")
        print("     ~~good bye")
        continue
    else:
        print("")
        option=int(input("Enter db option to perform :")) 
    if option==1:
        emp.show_table()
    elif option==2:
        emp.add_emp()
    elif option==3:
        emp.delete_emp()
    elif option==4:
        emp.update_emp()
    elif option==5:
        emp.from_dept()
    elif option==6:
        emp.max_sal()
    elif option==7:
        emp.min_sal()

     
            

