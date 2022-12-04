import logging
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

dotenv_path = ('.env')
load_dotenv(dotenv_path)

#Logger Settings
logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s',
 level=logging.INFO)


def connectionDB(status):
    if status =="DConnection":
        return mysql.connector.connect(host=os.environ.get("DDB_SERVER"),
                                            database=os.environ.get("DDB_NAME"),
                                            user=os.environ.get("DDB_USERNAME"),
                                            password=os.environ.get("DDB_PASSWORD"))

    elif status=="IConnection":
        return mysql.connector.connect(host=os.environ.get("IDB_SERVER"),
                                            database=os.environ.get("IDB_NAME"),
                                            user=os.environ.get("IDB_USERNAME"),
                                            password=os.environ.get("IDB_PASSWORD"))

    elif status=="Test":
        #DB Settings and Testing
        DBs =["Info","Dedicated"]
        for db in DBs:
                try:
                    connection = mysql.connector.connect(host=os.environ.get(db[0]+"DB_SERVER"),
                                                database=os.environ.get(db[0]+"DB_NAME"),
                                                user=os.environ.get(db[0]+"DB_USERNAME"),
                                                password=os.environ.get(db[0]+"DB_PASSWORD"))
                    if connection.is_connected():
                        db_Info = connection.get_server_info()
                        print("Test DB Connection to "+ db +" Database")
                        print("Connected to MySQL Server version ", db_Info)
                        cursor = connection.cursor()
                        cursor.execute("select database();")
                        record = cursor.fetchone()
                        print("You're connected to database: ", record)

                except Error as e:
                    print("Error while connecting to MySQL", e)
                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")
