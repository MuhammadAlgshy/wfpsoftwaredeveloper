#Libraries
import requests
import json
#Settings
from settings import logging

#Variables
api_URL= 'https://api.hungermapdata.org/v1/foodsecurity/country/AFG/region?date_start=2022-01-01&date_end=2022-02-01'

def getData(status):
   
    try:
        response_API= requests.get(api_URL)
        data = response_API.text
        if status == "production":
            parse_json = json.loads(data)   
        logging.info(response_API.status_code)
    except:
        logging.error("ERROR: Failed to establish connection, please check your API URL!")
        # Uncomment raise to check full detailed errors!
        # raise
   

# active_case = parse_json['Andaman and Nicobar Islands']['districtData']['South Andaman']['active']
# print("Active cases in South Andaman:", parse_json)

