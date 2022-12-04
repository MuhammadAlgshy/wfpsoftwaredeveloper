from settings import  connectionDB
from mysql.connector import Error
import json

def createTable():

 try:
    #establishing the connectionection
    connection = connectionDB("DConnection")

    #Creating a cursor object using the cursor() method
    cursor = connection.cursor()

    #Dropping Countries_Cfii table if already exists.
    #cursor.execute("DROP TABLE IF EXISTS Countries_Cfii")

    #Creating table as per requirement
    sql ='''CREATE TABLE Countries_Cfii(
    Country CHAR(30) NOT NULL,
    Region CHAR(30) NOT NULL,
    Fcs float NOT NULL,
    Rcsi float NOT NULL,
    Cfii float NOT NULL,
    audit_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )'''
    cursor.execute(sql)
 except Error as e:
         print("Error while connecting to MySQL", e)
 finally:
          if connection.is_connected():
              cursor.close()
              connection.close()
            #   print("MySQL connection is closed")
    
def insertCountryData(selected_country):

    # read JSON file which is in the next parent folder
    file ='result_data/'+selected_country+'_country_data.json'
    json_data=open(file).read()
    json_obj = json.loads(json_data)
    
    try:
        #establishing the connectionection
        connection = connectionDB("DConnection")

        #Creating a cursor object using the cursor() method
        cursor = connection.cursor()
        for i, item in enumerate(json_obj):
            country =item.get("country", None)
            region =item.get("region", None)
            fcs =item.get("fcs", None)
            rcsi =item.get("rcsi", None)
            cfii =item.get("cfii", None)
            command =  f"INSERT INTO Countries_Cfii (Country, Region, Fcs, Rcsi, Cfii) \
                            VALUES ('{country}','{region}',{fcs},{rcsi}, {cfii} )"
            print(command)
            cursor.execute(command)
            connection.commit()

    except Error as e:
         print("Error while connecting to MySQL", e)
    finally:
          if connection.is_connected():
              cursor.close()
              connection.close()
              print("MySQL connection is closed")

createTable()