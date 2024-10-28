import getpass
import mysql.connector
from mysql.connector import Error
def Create_Database():
    try:
        username = input("Enter the username:")
        password = getpass.getpass("Enter your password: ")
        connection = mysql.connector.connect(
            host = "localhost",
            password = password,
            username = username
        )
        if  connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print (f"Database 'alx_book_store' created successfully!")
    except mysql.connector.Error:
        print(f"I cannot connect to my SQL")