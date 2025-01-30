import mysql.connector

try:
    mydb = mysql.connector.connect(
    host = "localhost"
    user = "root"
    password = "nextvisiontech2022@gmail.comU"
    )
except mysql.connector.Error as e:
    print(f"Error: {e}")
else:
    print("Database connection successful")

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

print("Database 'alx_book_store' created successfully!")

mycursor.close()
mydb.close()
