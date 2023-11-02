import pytest
import openai
import os
import json
import requests
import time
from config_parse import get_config_elem_value
from function_calling_define import getCurrentWeather, getNDayWeatherForecast, getEarchQuakeInfo, getMarketNews, \
        getGasolineDieselPrices, searchAirport, searchFlights, searchHotels

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "openai"
openai.api_key = get_config_elem_value(config_name, test_api_type, "api_key")
xrapidapi_key = get_config_elem_value(config_name, "xrapidapi", "X-RapidAPI-Key")

json_config_dir = "function_message_json_config"

test_model_name = "gpt-3.5-turbo-0613"

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
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getCurrentWeather": getCurrentWeather,
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


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
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getNDayWeatherForecast": getNDayWeatherForecast,
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


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
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getEarchQuakeInfo": getEarchQuakeInfo,
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


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
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getMarketNews": getMarketNews,
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


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
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "getGasolineDieselPrices": getGasolineDieselPrices,
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def searchAirportCall():
    """ Function Calling Get Airport Info """
    messages = []
    filename = "search_airport_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_airport_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "searchAirport": searchAirport,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            location = function_args.get("location"),
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def searchFlightsCall():
    """ Function Calling Get Flights Info """
    messages = []
    filename = "search_flights_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_flights_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "searchFlights": searchFlights,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            sourceAirportCode = function_args.get("sourceAirportCode"),
            destinationAirportCode = function_args.get("destinationAirportCode"),
            date = function_args.get("date"),
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
            model=test_model_name,
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        response_result = first_response["choices"][0]["message"]
        print("response_result:", response_result)
        return(response_result)


def searchHotelsCall():
    """ Function Calling Get Hotels Info """
    messages = []
    filename = "search_hotels_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_hotels_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = openai.ChatCompletion.create(
        model=test_model_name,
        messages=messages,
        functions=functions,
        function_call="auto",  # auto is default, but we'll be explicit
    )
    response_message = response["choices"][0]["message"]
    print("function_call:", response_message)

    if response_message.get("function_call"):
        available_functions = {
            "searchHotels": searchHotels,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        fuction_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        function_response = fuction_to_call(
            query = function_args.get("query"),
            limit_num = function_args.get("limit_num"),
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
            model=test_model_name,
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

    def test_searchAirport(self):
        result = searchAirportCall()
        assert "" != result

    def test_searchFlights(self):
        result = searchFlightsCall()
        assert "" != result

    def test_searchHotels(self):
        result = searchHotelsCall()
        assert "" != result

if __name__ == '__main__':
    """ main function """
    pytest.main()

