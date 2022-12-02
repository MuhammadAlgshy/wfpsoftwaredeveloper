#Libraries
import logging
import requests
import json

#Settings
from settings import *


api_URL= 'https://api.hungermapsdata.org/v1/foodsecurity/country/AFG/region?date_start=2022-01-01&date_end=2022-02-01'

try:
    response_API= requests.get(api_URL)
    print(response_API.status_code)
    data = response_API.text
    parse_json = json.loads(data)   
except:
    logging.error("ERROR: Failed to establish connection, please check your API URL!")

    # Uncomment raise to check full detailed errors!
    # raise

