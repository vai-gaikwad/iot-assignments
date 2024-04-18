# import module of mysql connector
import mysql.connector

# create a connection with mysql database server
def get_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        port = 3306,
        user = "sunbeam",
        password = "sunbeam",
        database = "iotdb"
        )
    return connection
