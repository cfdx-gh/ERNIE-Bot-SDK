import pytest
import erniebot
import os
import json
import requests
from config_parse import get_config_elem_value
from function_calling_define import getCurrentWeather, getNDayWeatherForecast, getEarchQuakeInfo, getMarketNews, \
        getGasolineDieselPrices, searchAirport, searchFlights

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "qianfan"
erniebot.api_type = test_api_type
erniebot.ak = get_config_elem_value(config_name, test_api_type, "ak")
erniebot.sk = get_config_elem_value(config_name, test_api_type, "sk")

json_config_dir = "function_message_json_config"


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getCurrentWeather": getCurrentWeather}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(location=args["location"], format=args["format"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getNDayWeatherForecast": getNDayWeatherForecast}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(location=args["location"], num_days=args["num_days"], format=args["format"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getEarchQuakeInfo": getEarchQuakeInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(latitude = args["latitude"], \
               longitude = args["longitude"], \
               radius = args["radius"], \
               magnitude = args["magnitude"], \
               count = args["count"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getMarketNews": getMarketNews}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(symbol = args["symbol"], num = args["num"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getGasolineDieselPrices": getGasolineDieselPrices}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(state = args["state"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchAirport": searchAirport}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(location = args["location"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchFlights": searchFlights}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(sourceAirportCode = args["sourceAirportCode"], \
            destinationAirportCode = args["destinationAirportCode"], \
            date = args["date"])
    print("function_response:", res)

    messages.append(
        {
            "role": "assistant",
            "content": None,
            "function_call": function_call
        }
    )
    messages.append(
        {
            "role": "function",
            "name": function_call["name"],
            "content": json.dumps(res, ensure_ascii=False)
        }
    )
    print("messages:",messages)
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    print("response_result:", response.result)
    return(response.result)


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


if __name__ == '__main__':
    """ main function """
    pytest.main()

