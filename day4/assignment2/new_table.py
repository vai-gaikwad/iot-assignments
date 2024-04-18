import connector as con

connection=con.get_connection()

#table creation query

query="create table employee(empid INT, name VARCHAR(40), dept VARCHAR(40), email VARCHAR(20),sal INT, djoin INT);"

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
