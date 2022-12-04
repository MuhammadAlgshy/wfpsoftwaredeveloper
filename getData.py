#Libraries
import requests
import json
from mysql.connector import Error
#Settings
from settings import logging, connectionDB

from dedicatedDB import insertCountryData
   
def calc_cfii(fsc,rcsi):
    if fsc < 0.5:
        return (fsc + rcsi)/2
    elif fsc >= 0.5:
        return(0.5*fsc+1.5*rcsi)/2


def selectCfii_calcualtion():
    try:
        connection = connectionDB("IConnection")
        cursor = connection.cursor()
        #List Coutries with Cffi_Calclation = 1
        cursor.execute("\
        SELECT B.iso3_code FROM cfii_list as A \
                        JOIN countries_iso3   as B \
                        on A.adm0_code=B.adm0_code \
                            where cfii_calcualtion=1 ")
        
        records = cursor.fetchall()
        list_of_countries =[]
        print("\nPrinting each row")
        for row in records:
            print("iso3_code = ", row[0], )
            list_of_countries.append(row[0])
        return list_of_countries

    except Error as e:
         print("Error while connecting to MySQL", e)
    finally:
          if connection.is_connected():
              cursor.close()
              connection.close()

def getData(status, iso3='AFG', start_date='2022-10-01', end_date='2022-10-02'):
   #Variables
    iso3= iso3.upper()
    api_URL= f'https://api.hungermapdata.org/v1/foodsecurity/country/{iso3}/region?date_start={start_date}&date_end={end_date}'
    country_data=[]
    print(api_URL)
    try:
        response_API= requests.get(api_URL)
        data = response_API.text
        parse_json = json.loads(data) 
        
        if status == "production":
                for region in parse_json:
                        single_region_data = {
                                'country': region['country']['name'],
                                'region': region['region']['name'],
                                'fcs':region['metrics']['fcs']['prevalence'],
                                'rcsi':region['metrics']['rcsi']['prevalence'],
                                'cfii': calc_cfii(region['metrics']['fcs']['prevalence'], region['metrics']['rcsi']['prevalence'])
                                }
                        country_data.append(single_region_data)

                #Create File for each country 
                file_path='result_data/'+iso3+ "_country_data.json"
                with open(file_path, 'w') as f: json.dump(country_data, f)
                insertCountryData(iso3)
        logging.info(response_API.status_code)
        
    except:
         logging.error("ERROR: Failed to establish connection, please check your API URL! \n \
            # or the RCSI does not exist!")
         # Uncomment raise to check full detailed errors!
         #raise
   
def generateCfiiData(start_date='2022-10-01', end_date='2022-10-02'):
    countries = selectCfii_calcualtion()
    #Generate Files
    for country in countries:
        getData('production',country ,start_date, end_date)
    print (countries)


