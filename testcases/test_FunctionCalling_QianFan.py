import pytest
import erniebot
import os
import json
import requests
from config_parse import get_config_elem_value
from function_calling_define import getCurrentWeather, getNDayWeatherForecast, getEarchQuakeInfo, getMarketNews, \
        getGasolineDieselPrices, searchAirport, searchFlights, searchHotels, searchQQBindInfo, searchIdentityInfo, \
        getWebsiteSpeed, getTimeKeeper, getEncryMd5, getTelAddress, getHistoryTodayInfo, getHotList, getDeliveryInfo, \
        getFoodHeatInfo, getOlyMedalsList, isOrNotHarassPhone, searchTradeMarkInfo, searchDomainWhoisInfo, jianhuangPicture, \
        queryGasolinePrice, garbageClassification, queryMovieRank, queryIpAddressInfo, queryQQInfo, queryQQWechatWhetherWaylay, \
        queryCityWeather, queryLongitudeAndLatitudeInfo, queryDictWordMean, translateText, queryTaobaoSuggestList, \
        queryConstellationHoroscope, queryDomainEmploy

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "qianfan"
erniebot.api_type = test_api_type
erniebot.ak = get_config_elem_value(config_name, test_api_type, "ak")
erniebot.sk = get_config_elem_value(config_name, test_api_type, "sk")

json_config_dir = "function_message_json_config"

test_model_name = "ernie-bot"
#test_model_name = "ernie-bot-3.5"
#test_model_name = "ernie-bot-4"

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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getCurrentWeather": getCurrentWeather}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    #res = func(location=args["location"], format=args["format"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


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

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchHotels": searchHotels}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def searchPizzaStoreCall():
    """ Function Calling Get Pizza Store Info """
    messages = []
    filename = "search_pizzastore_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_pizzastore_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchPizzaStore": searchPizzaStore}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def searchQQBindInfoCall():
    """ Function Calling Get QQ Bind Info """
    messages = []
    filename = "search_qq_bind_info_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_qq_bind_info_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchQQBindInfo": searchQQBindInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def searchIdentityInfoCall():
    """ Function Calling Get Identity Info """
    messages = []
    filename = "search_identity_info_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_identity_info_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchIdentityInfo": searchIdentityInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getWebsiteSpeedCall():
    """ Function Calling Get Website Speed """
    messages = []
    filename = "get_website_speed_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_website_speed_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getWebsiteSpeed": getWebsiteSpeed}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getTimeKeeperCall():
    """ Function Calling Get Time Keeper """
    messages = []
    filename = "get_timekeeper_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_timekeeper_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getTimeKeeper": getTimeKeeper}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getEncryMd5Call():
    """ Function Calling Get Encry Md5 """
    messages = []
    filename = "get_encry_md5_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_encry_md5_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getEncryMd5": getEncryMd5}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getTelAddressCall():
    """ Function Calling Get Tel Address """
    messages = []
    filename = "get_tel_address_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_tel_address_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getTelAddress": getTelAddress}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getHistoryTodayInfoCall():
    """ Function Calling Get What happened in History Today """
    messages = []
    filename = "get_history_today_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_history_today_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getHistoryTodayInfo": getHistoryTodayInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getHotListCall():
    """ Function Calling Get Host List """
    messages = []
    filename = "get_hot_list_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_hot_list_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getHotList": getHotList}
    func = name2function[function_call["name"]]
    #print("func:", func.__code__)
    args = json.loads(function_call["arguments"])
    res = func(**args)
    #print("args:", args)
    #breakpoint()
    #res = func(platform_name1=args['platform_name1'], platform_name2=args['platform_name2'], count=args['count'])
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getDeliveryInfoCall():
    """ Function Calling Get Delivery Info """
    messages = []
    filename = "get_delivery_info_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_delivery_info_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getDeliveryInfo": getDeliveryInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getFoodHeatInfoCall():
    """ Function Calling Get Food Heat Info """
    messages = []
    filename = "get_food_heat_info_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_food_heat_info_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getFoodHeatInfo": getFoodHeatInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def getOlyMedalsListCall():
    """ Function Calling Get Oly Medals List """
    messages = []
    filename = "get_oly_medal_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_oly_medal_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getOlyMedalsList": getOlyMedalsList}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def isOrNotHarassPhoneCall():
    """ Function Calling Is or Not Harass Phone """
    messages = []
    filename = "get_whether_harass_phone_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "get_whether_harass_phone_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"isOrNotHarassPhone": isOrNotHarassPhone}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def searchTradeMarkInfoCall():
    """ Function Calling Search TradeMark Info """
    messages = []
    filename = "search_trademark_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_trademark_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchTradeMarkInfo": searchTradeMarkInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def searchDomainWhoisInfoCall():
    """ Function Calling Search Domain Whois Info """
    messages = []
    filename = "search_domain_whois_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "search_domain_whois_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"searchDomainWhoisInfo": searchDomainWhoisInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def jianhuangPictureCall():
    """ Function Calling jianhuang Picture """
    messages = []
    filename = "jianhuang_picture_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "jianhuang_picture_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"jianhuangPicture": jianhuangPicture}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryGasolinePriceCall():
    """ Function Calling Query Gasoline Price """
    messages = []
    filename = "query_gasoline_price_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_gasoline_price_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryGasolinePrice": queryGasolinePrice}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def garbageClassificationCall():
    """ Function Calling Garbage Classification """
    messages = []
    filename = "garbage_classification_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "garbage_classification_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"garbageClassification": garbageClassification}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryMovieRankCall():
    """ Function Calling Query Movie Rank """
    messages = []
    filename = "query_movie_rank_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_movie_rank_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryMovieRank": queryMovieRank}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryIpAddressInfoCall():
    """ Function Calling Query IP Address Info """
    messages = []
    filename = "query_ip_address_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_ip_address_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryIpAddressInfo": queryIpAddressInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryQQInfoCall():
    """ Function Calling Query QQ Info """
    messages = []
    filename = "query_qq_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_qq_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryQQInfo": queryQQInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryQQWechatWhetherWaylayCall():
    """ Function Calling Query QQ and Wechat Whether Waylay """
    messages = []
    filename = "query_qq_wechat_waylay_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_qq_wechat_waylay_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryQQWechatWhetherWaylay": queryQQWechatWhetherWaylay}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryCityWeatherCall():
    """ Function Calling Query City Weather """
    messages = []
    filename = "query_city_weather_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_city_weather_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryCityWeather": queryCityWeather}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryLongitudeAndLatitudeInfoCall():
    """ Function Calling Query Longitude And Latitude Info """
    messages = []
    filename = "query_longitude_latitude_info_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_longitude_latitude_info_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryLongitudeAndLatitudeInfo": queryLongitudeAndLatitudeInfo}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryDictWordMeanCall():
    """ Function Calling Query Dict Word Mean """
    messages = []
    filename = "query_dict_word_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_dict_word_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryDictWordMean": queryDictWordMean}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryTaobaoSuggestListCall():
    """ Function Calling Query Taobao Suggest List """
    messages = []
    filename = "query_taobao_suggest_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_taobao_suggest_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryTaobaoSuggestList": queryTaobaoSuggestList}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryConstellationHoroscopeCall():
    """ Function Calling Query Constellation Horoscope """
    messages = []
    filename = "query_constellation_horoscope_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_constellation_horoscope_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryConstellationHoroscope": queryConstellationHoroscope}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def queryDomainEmployCall():
    """ Function Calling Query Domain Employ Info """
    messages = []
    filename = "query_domain_employ_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "query_domain_employ_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"queryDomainEmploy": queryDomainEmploy}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


def translateTextCall():
    """ Function Calling Translate Text """
    messages = []
    filename = "translate_text_message.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        message_dict = json.load(f)
    messages.append(message_dict)

    functions = []
    filename = "translate_text_functions.json"
    with open(cur_path + "/" + json_config_dir + "/" + filename, 'r') as f:
        function_dict = json.load(f)
    functions.append(function_dict)

    response = erniebot.ChatCompletion.create(
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"translateText": translateText}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(**args)
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
        model = test_model_name,
        messages = messages,
        functions = functions
    )
    print("response_result:", response.result)
    return(response.result)


class TestFunctionCalling:
    """ Test Class for Function Calling """
    #@pytest.mark.skip
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

    def test_searchQQBindInfo(self):
        result = searchQQBindInfoCall()
        assert "" != result

    def test_searchIdentityInfo(self):
        result = searchIdentityInfoCall()
        assert "" != result

    def test_getWebsiteSpeed(self):
        result = getWebsiteSpeedCall()
        assert "" != result

    def test_getTimeKeeper(self):
        result = getTimeKeeperCall()
        assert "" != result

    def test_getEncrypMd5(self):
        result = getEncryMd5Call()
        assert "" != result

    def test_getTelAddress(self):
        result = getTelAddressCall()
        assert "" != result

    def test_getHistoryTodayInfo(self):
        result = getHistoryTodayInfoCall()
        assert "" != result

    def test_getHotList(self):
        result = getHotListCall()
        assert "" != result

    def test_getDeliveryInfo(self):
        result = getDeliveryInfoCall()
        assert "" != result

    def test_getFoodHeatInfo(self):
        result = getFoodHeatInfoCall()
        assert "" != result

    def test_getOlyMedalsList(self):
        result = getOlyMedalsListCall()
        assert "" != result

    def test_isOrNotHarassPhone(self):
        result = isOrNotHarassPhoneCall()
        assert "" != result

    def test_searchTradeMarkInfo(self):
        result = searchTradeMarkInfoCall()
        assert "" != result

    def test_searchDomainWhoisInfo(self):
        result = searchDomainWhoisInfoCall()
        assert "" != result

    def test_jianhuangPicture(self):
        result = jianhuangPictureCall()
        assert "" != result

    def test_queryGasolinePrice(self):
        result = queryGasolinePriceCall()
        assert "" != result

    def test_garbageClassification(self):
        result = garbageClassificationCall()
        assert "" != result

    def test_queryMovieRank(self):
        result = queryMovieRankCall()
        assert "" != result

    def test_queryIpAddressInfo(self):
        result = queryIpAddressInfoCall()
        assert "" != result

    def test_queryQQInfo(self):
        result = queryQQInfoCall()
        assert "" != result

    def test_queryQQWechatWhetherWaylay(self):
        result = queryQQWechatWhetherWaylayCall()
        assert "" != result

    def test_queryCityWeather(self):
        result = queryCityWeatherCall()
        assert "" != result

    def test_queryLongitudeAndLatitudeInfo(self):
        result = queryLongitudeAndLatitudeInfoCall()
        assert "" != result

    def test_queryDictWordMean(self):
        result = queryDictWordMeanCall()
        assert "" != result

    def test_queryTaobaoSuggestList(self):
        result = queryTaobaoSuggestListCall()
        assert "" != result

    def test_translateText(self):
        result = translateTextCall()
        assert "" != result

    def test_queryConstellationHoroscope(self):
        result = queryConstellationHoroscopeCall()
        assert "" != result

    def test_queryDomainEmploy(self):
        result = queryDomainEmployCall()
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

