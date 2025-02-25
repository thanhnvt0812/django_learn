import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

try:
    dataBase = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASS')
    )
    cursorObject = dataBase.cursor()
    cursorObject.execute('CREATE DATABASE djangolearn')
    print("Done!")
except Error as e:
    print(f"Error: {e}")
finally:
    if dataBase.is_connected():
        cursorObject.close()
        dataBase.close()
        print("MySQL connection is closed")