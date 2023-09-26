import pytest
import openai
import os
import json
import requests
import time
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "openai"
openai.api_key = get_config_elem_value(config_name, test_api_type, "api_key")
xrapidapi_key = get_config_elem_value(config_name, "xrapidapi", "X-RapidAPI-Key")

rapid_api_result_dir = "rapid_api_result"
json_config_dir = "function_message_json_config"

def getCurrentWeatherDef(location, format="摄氏度"):
    """Get the current weather in a given location"""
    weather_info = {
        "location": location,
        "temperature": "78",
        "format": format,
        "forecast": ["晴朗的", "有风"],
    }
    return json.dumps(weather_info)


def getCurrentWeatherCall():
    """ Function Calling Get Current Weather Info """
    messages = []
    filename = "current_weather_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "current_weather_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getCurrentWeatherDef": getCurrentWeatherDef,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            location = function_args.get("location"),
            format = function_args.get("format"),
        )
        print("function_response:", function_response)

        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
        )  # extend conversation with function response
        print("messages:", messages)
        first_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def getNDayWeatherForecastDef(location, num_days, format="华氏度"):
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


def getNDayWeatherForecastCall():
    """ Function Calling Get Current Weather Info """
    messages = []
    filename = "n_day_weather_forecast_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "n_day_weather_forecast_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getNDayWeatherForecastDef": getNDayWeatherForecastDef,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            location = function_args.get("location"),
            num_days = function_args.get("num_days"),
            format = function_args.get("format"),
        )
        print("function_response:", function_response)

        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
        )  # extend conversation with function response
        print("messages:", messages)
        first_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def getEarchQuakeInfoDef(latitude, longitude, radius, magnitude, count):
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
    with open(cur_path + "/rapid_api_result/" + filename, 'r') as f:
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


def getEarchQuakeInfoCall():
    """ Function Calling Get EarchQuake Info """
    messages = []
    filename = "earch_quake_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "earch_quake_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getEarchQuakeInfoDef": getEarchQuakeInfoDef,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            latitude = function_args.get("latitude"),
            longitude = function_args.get("longitude"),
            radius = function_args.get("radius"),
            magnitude = function_args.get("magnitude"),
            count = function_args.get("count"),
        )
        print("function_response:", function_response)

        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
        )  # extend conversation with function response
        print("messages:", messages)
        first_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def getMarketNewsDef(symbol, num):
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
    with open(cur_path + "/rapid_api_result/" + filename, 'r') as f:
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


def getMarketNewsCall():
    """ Function Calling Get Market News of some stock """
    messages = []
    filename = "market_news_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "market_news_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getMarketNewsDef": getMarketNewsDef,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            symbol = function_args.get("symbol"),
            num = function_args.get("num"),
        )
        print("function_response:", function_response)

        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
        )  # extend conversation with function response
        print("messages:", messages)
        first_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def getGasolineDieselPricesDef(state):
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
    with open(cur_path + "/rapid_api_result/" + filename, 'r') as f:
        response = json.load(f)
    for elem in response["result"]["cities"]:
        tmp_dict = {}
        tmp_dict["name"] = elem["name"]
        tmp_dict["gasoline"] = elem["gasoline"]
        tmp_dict["diesel"] = elem["diesel"]
        res_list.append(tmp_dict)
    #print(res_list)
    return json.dumps(res_list)


def getGasolineDieselPricesCall():
    """ Function Calling Get Gasoline and Diesel Prices """
    messages = []
    filename = "gasoline_diesel_prices_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "gasoline_diesel_prices_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getGasolineDieselPricesDef": getGasolineDieselPricesDef,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            state = function_args.get("state"),
        )
        print("function_response:", function_response)

        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
        )  # extend conversation with function response
        print("messages:", messages)
        first_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


class TestFunctionCalling:
    """ Test Class for Function Calling """
    def test_GetCurrentWeather(self):
        result = getCurrentWeatherCall()
        assert "" != result

    def test_get_N_DayWeatherForecast(self):
        result = getNDayWeatherForecastCall()
        assert "" != result

    def test_get_earchquakeInfo(self):
        result = getEarchQuakeInfoCall()
        assert "" != result

    def test_get_marketNews(self):
        result = getMarketNewsCall()
        assert "" != result

    def test_get_gasolineDieselPrices(self):
        result = getGasolineDieselPricesCall()
        assert "" != result

if __name__ == '__main__':
    """ main function """
    pytest.main()

