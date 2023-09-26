import os
import json
import requests
import time
from config_parse import get_config_elem_value

cur_path = os.getcwd()
rapid_api_result_dir = "rapid_api_result"
config_name = os.path.join(cur_path, "config/authentication.ini")
xrapidapi_key = get_config_elem_value(config_name, "xrapidapi", "X-RapidAPI-Key")


def getCurrentWeather(location, format="摄氏度"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "78",
        "format": format,
        "forecast": ["晴朗的", "有风"],
    }
    return json.dumps(weather_info)


def getNDayWeatherForecast(location, num_days, format="华氏度"):
    """Get forecast weather in a given location for n days in the future"""
    if num_days == 1:
        weather_info = {
            "location": location,
            "temperature": "71",
            "format": format,
            "forecast": ["大雨", "大风"],
        }
    elif num_days == 2:
        weather_info = {
            "location": location,
            "temperature": "72",
            "format": format,
            "forecast": ["小雨", "微风"],
        }
    elif num_days == 3:
        weather_info = {
            "location": location,
            "temperature": "73",
            "format": format,
            "forecast": ["多云", "比较舒服"],
        }
    else:
        weather_info = {
            "location": location,
            "temperature": "80",
            "format": format,
            "forecast": ["晴天", "有风", "舒适"],
        }

    return json.dumps(weather_info)


def getEarchQuakeInfo(latitude, longitude, radius, magnitude, count):
    """Get every earthquake and any other event that registers on the richter scale"""
    url = "https://everyearthquake.p.rapidapi.com/earthquakes"
    #querystring = {"start":"1","count":"10","type":"earthquake","latitude":"39.4","longitude":"115.7","radius":"1000","units":"miles","magnitude":"7","intensity":"1"}
    querystring = {"start":"1","count":str(count), \
            "type":"earthquake","latitude":str(latitude), \
            "longitude":str(longitude), \
            "radius":str(radius),"units":"miles", \
            "magnitude":str(magnitude),"intensity":"1"}
    headers = {
        "X-RapidAPI-Key": xrapidapi_key,
        "X-RapidAPI-Host": "everyearthquake.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    earchquake_list = []
    filename = "earthquake.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    earchquake_num = response["count"]
    for elem in response["data"]:
        tmp_dict = {}
        tmp_dict["magnitude"] = elem["magnitude"]
        tmp_dict["title"] = elem["title"]
        tmp_dict["date"] = elem["date"]
        tmp_dict["detail_info"] = elem["detailUrl"]
        tmp_dict["country"] = elem["country"]
        tmp_dict["city"] = elem["city"]
        tmp_dict["latitude"] = elem["latitude"]
        tmp_dict["longitude"] = elem["longitude"]
        earchquake_list.append(tmp_dict)
    #print(earchquake_list)
    return json.dumps(earchquake_list)


def getMarketNews(symbol, num):
    """Get Market news of some Stock"""
    url = "https://mboum-finance.p.rapidapi.com/ne/news/"
    #querystring = {"symbol":"BIDU"}
    querystring = {"symbol":symbol}
    headers = {
        "X-RapidAPI-Key": xrapidapi_key,
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    news_list = []
    filename = "marketnews.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    i = 0
    for elem in response["item"]:
        tmp_dict = {}
        tmp_dict["title"] = elem["title"]
        tmp_dict["description"] = elem["description"]
        tmp_dict["link"] = elem["link"]
        tmp_dict["pubDate"] = elem["pubDate"]
        i += 1
        news_list.append(tmp_dict)
        if i > num:
            break
    #print(news_list)
    return json.dumps(news_list)

def getGasolineDieselPrices(state):
    """Get gasoline and diesel prices in different fuel stations in different cities."""
    url = "https://gas-price.p.rapidapi.com/stateUsaPrice"
    #querystring = {"state":"NY"}
    querystring = {"state": state}
    headers = {
        "X-RapidAPI-Key": xrapidapi_key,
        "X-RapidAPI-Host": "gas-price.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "gasoline_diesel_prices.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    for elem in response["result"]["cities"]:
        tmp_dict = {}
        tmp_dict["name"] = elem["name"]
        tmp_dict["gasoline"] = elem["gasoline"]
        tmp_dict["diesel"] = elem["diesel"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def searchAirport(location):
    """Get gasoline and diesel prices in different fuel stations in different cities."""
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchAirport"
    #querystring = {"query":"london"}
    querystring = {"query":"location"}
    headers = {
	"X-RapidAPI-Key": xrapidapi_key,
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "search_airport.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    for elem in response["data"][0]["children"]:
        tmp_dict = {}
        tmp_dict["name"] = elem["name"]
        tmp_dict["parent_name"] = elem["details"]["parent_name"]
        tmp_dict["airportCode"] = elem["airportCode"]
        tmp_dict["coords"] = elem["coords"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def searchFlights(sourceAirportCode, destinationAirportCode, date):
    """Get flights info between two cities """
    url = "https://tripadvisor16.p.rapidapi.com/api/v1/flights/searchFlights"
    #querystring = {"sourceAirportCode":"BOM","destinationAirportCode":"DEL","date":"2023-09-28","itineraryType":"ONE_WAY","sortOrder":"ML_BEST_VALUE","numAdults":"1","numSeniors":"0","classOfService":"ECONOMY","returnDate":"2023-09-28","nearby":"yes","nonstop":"yes","currencyCode":"USD"}
    querystring = {"sourceAirportCode": sourceAirportCode, "destinationAirportCode": destinationAirportCode, \
            "date": date, "itineraryType": "ONE_WAY", "sortOrder": "ML_BEST_VALUE", "numAdults": "1", \
            "numSeniors": "0", "classOfService": "ECONOMY", "returnDate": date, \
            "nearby": "yes", "nonstop": "yes", "currencyCode": "USD"}
    headers = {
	"X-RapidAPI-Key": xrapidapi_key,
	"X-RapidAPI-Host": "tripadvisor16.p.rapidapi.com"
    }
    #response = requests.get(url, headers=headers, params=querystring)
    #print(response.json())

    res_list = []
    filename = "search_flights.json"
    with open(cur_path + "/" + rapid_api_result_dir + "/" + filename, 'r') as f:
        response = json.load(f)
    i = 0
    for flight in response["data"]["flights"]:
        for segment in flight["segments"]:
            for leg in segment["legs"]:
                tmp_dict = {}
                tmp_dict["originStationCode"] = leg["originStationCode"]
                tmp_dict["destinationStationCode"] = leg["destinationStationCode"]
                tmp_dict["equipmentId"] = leg["equipmentId"]
                tmp_dict["flightNumber"] = leg["flightNumber"]
                tmp_dict["distanceInKM"] = leg["distanceInKM"]
                tmp_dict["departureDateTime"] = leg["departureDateTime"]
                tmp_dict["arrivalDateTime"] = leg["arrivalDateTime"]
                i += 1
                if i < 10:
                    res_list.append(tmp_dict)
                else:
                    break
    #print(res_list)
    return json.dumps(res_list)

