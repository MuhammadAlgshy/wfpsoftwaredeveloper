#Libraries
import requests
import json

#Settings
from settings import *

#Variables
api_URL= 'https://api.hungermapdata.org/v1/foodsecurity/country/AFG/region?date_start=2022-01-01&date_end=2022-02-01'

def getData():
    try:
        response_API= requests.get(api_URL)
        data = response_API.text
        parse_json = json.loads(data)   
        logging.info(response_API.status_code)
    except:
        logging.error("ERROR: Failed to establish connection, please check your API URL!")

    # Uncomment raise to check full detailed errors!
    # raise


getData()