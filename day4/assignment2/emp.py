import connector as con

#connection=con.get_connection()

def get_query_result(query):
    connection=con.get_connection()
    # create a cursor to execute the query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # get result of query execution
    records = cursor.fetchall() 

    # close the cursor
    cursor.close()

    #close the connection with mysql server 
    connection.close()
    return records

def print_r(result):
    for rec in result:
        print(f"eid ={rec[0]},  name ={rec[1]}, dept ={rec[2]}, email ={rec[3]},    salary ={rec[4]},   date of join ={rec[5]}")
        print("")


def execute_c(query):
    connection=con.get_connection()
    # create a cursor to execute the query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # after execution of query commit your changes
    connection.commit()

    # close the cursor
    cursor.close()

    #close the connection with mysql server 
    connection.close()


def add_emp():
    # creat the employee record query
    empid=int(input("Enter employee id =  "))
    name=input("Enter employee name =  ")
    dept=input("Enter employee departmet =  ")
    email=input("Enter employee emial =  ")
    sal=int(input("enter employee salary = "))
    djoin=int(input("Enter employee joining date =  "))


    query = f"insert into employee values({empid}, '{name}', '{dept}', '{email}', {sal}, {djoin});"
    
    execute_c(query)
   
def delete_emp():
    eid=int(input("Enter eid to delete record"))
    query = f"delete from employee where empid = {eid};"

    execute_c(query)

def update_emp():
    eid=int(input("Enter Employee id to update record"))
    dept=input("Enter employee departmet =  ")
    email=input("Enter employee emial =  ")
    sal=int(input("enter employee salary = "))

    query = f"update employee SET dept='{dept}',email = '{email}',sal={sal} where empid = {eid};"
    
    execute_c(query)

def show_table():
    query= f"select * from employee;"

    result=get_query_result(query)
   
    print_r(result)

def from_dept():
    dept=(input("Enter Department name to get records : "))
    query= f"select * from employee where dept ='{dept}';"

    result=get_query_result(query)
  
    print_r(result)

def max_sal():

    query= f"select * from employee order by sal DESC LIMIT 1;"

    result=get_query_result(query)
  
    print_r(result)

def min_sal():

    query= f"select * from employee order by sal ASC LIMIT 1;"

    result=get_query_result(query)
  
    print_r(result)

#add_emp()

#delete_emp()

#update_emp()

#show_table()

#from_dept()

#max_sal()

#min_sal()







