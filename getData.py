#Libraries
import requests
import json
#Settings
from settings import logging


def getData(status, iso3='AFG', start_date='2022-12-01', end_date='2022-12-02'):
   #Variables
    api_URL= f'https://api.hungermapdata.org/v1/foodsecurity/country/{iso3.isupper()}/region?date_start={start_date}&date_end={end_date}'
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

