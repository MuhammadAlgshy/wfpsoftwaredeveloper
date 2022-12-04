#Libraries
import requests
import json
#Settings
from settings import logging
from mysql.connector import Error

from settings import connectionDB

def selectData():

    try:
        connection = connectionDB("IConnection")
        cursor = connection.cursor()
        #List Coutries with Cffi_Calclation = 1
        cursor.execute("\
        SELECT B.iso3_code FROM cfii_list as A \
                        JOIN countries_iso3   as B \
                        on A.adm0_code=B.adm0_code \
                            where cfii_calcualtion=1 ")
        myresult = dict(zip(cursor.column_names, cursor.fetchone()))
        print(format(myresult))
        myresult = cursor.fetchall()
        for x in myresult:
            print(x)
    except Error as e:
         print("Error while connecting to MySQL", e)
    finally:
          if connection.is_connected():
              cursor.close()
              connection.close()
              print("MySQL connection is closed")

# Test API
def getData(status, iso3='AFG', start_date='2022-12-01', end_date='2022-12-02'):
   #Variables
    iso3= iso3.upper()
    api_URL= f'https://api.hungermapdata.org/v1/foodsecurity/country/{iso3}/region?date_start={start_date}&date_end={end_date}'
    print(api_URL)
    try:
        response_API= requests.get(api_URL)
        data = response_API.text
        if status == "production":
            parse_json = json.loads(data)  
            with open('data.json', 'w') as f:
                     json.dump(parse_json, f)
        logging.info(response_API.status_code)
    except:
        logging.error("ERROR: Failed to establish connection, please check your API URL!")
        # Uncomment raise to check full detailed errors!
        # raise
   

# active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
# print("Active cases in South Andaman:", parse_json)

