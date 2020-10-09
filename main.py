import json

import logging
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

import json 
from botocore.vendored import requests
api_key = "feed281820238d79a28461f4fe757cfe"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


def lambda_handler(event, context):
    logger.debug(event)
    city_name =event["currentIntent"]["slots"]["location"]
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json() 
    if x["cod"] != "404": 
        y = x["main"] 

        current_temperature = y["temp"] -273.15
 
        current_pressure = y["pressure"] 
  
        current_humidiy = y["humidity"] 
  

        z = x["weather"] 
  
 
        weather_description = z[0]["description"]
        reply=" Temperature = " +str(current_temperature)+"degree Celsius" + "\n Atmospheric pressure (in hPa unit) = " +str(current_pressure) +"\n Humidity = " +str(current_humidiy)+"%" +"\n Description = " +str(weather_description)
    else:
        reply=" City Not Found "
        
    return {
        "sessionAttributes":event["sessionAttributes"],
        "dialogAction":{
            "type":"Close",
            "fulfillmentState":"Fulfilled",
            "message":{
                "contentType":"PlainText",
                "content":reply
            }
        }
    }
