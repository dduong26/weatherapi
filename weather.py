"""

This script is used to grab the weather for the specific city

Author: David Duong
Email: dduong26@gmail.com
Date: Sept 27th 2015

"""

# Import Requests module
import requests


def Main():
    # Your API Key from openweathermap.org
    apikey = <your key>
    # Your cityid you can obtain from openweathermap
    cityid = <your cityid>
    # Connect to the API and grab the data you supplied above
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?id=%s&APPID=%s&units=metric' % (cityid,apikey))
    # Grabbed the data as a json format and put it in the result variable
    result = r.json()

    # Specifically grabbed the "main" and "name" json objects and put them in their
    # respective variable
    main = result['main']
    city = result['name']

#Print the name of the city and grab the key and value of the "main" object items
#and format it like the following:
#
#<object> = <value>

    print city
    for key,val in main.items():
        print "{} = {}".format(key,val)


# Runs the program
if __name__ == "__main__":
    Main()
