import pytest
import erniebot
import os
import json
import requests
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "qianfan"
erniebot.api_type = test_api_type
erniebot.ak = get_config_elem_value(config_name, test_api_type, "ak")
erniebot.sk = get_config_elem_value(config_name, test_api_type, "sk")


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
    messages = [{"role": "user", "content": "波士顿的天气怎么样？多少度？"}]
    #messages = [{"role": "user", "content": "波士顿的天气怎么样？多少度？调用function call功能"}]
    functions = [
        {
        "name": "getCurrentWeatherDef",
        "description": "获取给定位置的当前天气",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "城市和州，例如加利福尼亚州旧金山",
                },
                "format": {
                    "type": "string",
                    "enum": ["摄氏度", "华氏度"],
                    "description": "要使用的温度单位，从用户位置推断。",
                },
            },
            "required": ["location", "format"],
        },
        }
    ]
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getCurrentWeatherDef": getCurrentWeatherDef}
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
    messages = [{"role": "user", "content": "波士顿未来两天的天气怎么样？我想知道是多少摄氏度。"}]
    functions = [
        {
        "name": "getNDayWeatherForecastDef",
        "description": "获取N天天气预报",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "城市和州，例如加利福尼亚州旧金山",
                },
                "format": {
                    "type": "string",
                    "enum": ["摄氏度", "华氏度"],
                    "description": "要使用的温度单位，从用户位置推断。",
                },
                "num_days": {
                    "type": "integer",
                    "description": "要预测的天数",
                }
            },
            "required": ["location", "format", "num_days"]
        },
        }
    ]
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getNDayWeatherForecastDef": getNDayWeatherForecastDef}
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
	"X-RapidAPI-Key": "392bcfea46msh84593dd258b2545p10ec1ejsn3a20adeb1874",
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
    messages = [{"role": "user", "content": "广州周边1000英里范围内发生过的7级以上的地震有哪些？请帮我列出所有符合要求的地震详细信息"}]
    functions = [
        {
        "name": "getEarchQuakeInfoDef",
        "description": "获取指定经纬度周边范围内发生过的地震信息",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "float",
                    "description": "纬度，例如北京是北纬39.4",
                },
                "longitude": {
                    "type": "float",
                    "description": "经度，例如北京是东经115.6",
                },
                "radius": {
                    "type": "integer",
                    "description": "以指定经纬度为中心的圆半径，例如1000 miles",
                },
                "magnitude": {
                    "type": "integer",
                    "description": "地震的震级，例如里氏7级",
                },
                "count": {
                    "type": "integer",
                    "description": "符合参数要求的地震数量，例如10",
                }
            },
            "required": ["latitude", "longitude", "radius", "magnitude", "count"]
        },
        "response": {
            "type": "object",
            "properties": {
                "magnitude": {
                    "type": "integer",
                    "description": "地震的震级，例如里氏7级",
                },
                "title": {
                    "type": "string",
                    "description": "地震标题，概要信息",
                },
                "date": {
                    "type": "string",
                    "description": "地震发生的日期",
                },
                "detail_info": {
                    "type": "string",
                    "description": "地震的详细信息链接地址",
                },
                "country": {
                    "type": "string",
                    "description": "地震发生地所属国家名称",
                },
                "city": {
                    "type": "string",
                    "description": "地震发生地所属城市名称",
                },
                "latitude": {
                    "type": "float",
                    "description": "地震发生地纬度",
                },
                "longitude": {
                    "type": "float",
                    "description": "地震发生地经度",
                }
            },
            "required": ["magnitude", "title", "date", "country", "city", "latitude", "longitude", "detail_info"]
        },
        }
    ]
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getEarchQuakeInfoDef": getEarchQuakeInfoDef}
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


def getMarketNewsDef(symbol, num):
    """Get Market news of some Stock"""
    url = "https://mboum-finance.p.rapidapi.com/ne/news/"
    #querystring = {"symbol":"BIDU"}
    querystring = {"symbol":symbol}
    headers = {
	"X-RapidAPI-Key": "392bcfea46msh84593dd258b2545p10ec1ejsn3a20adeb1874",
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
    messages = [{"role": "user", "content": "最近有关百度股票的新闻有哪些？请帮忙列出前10条"}]
    functions = [
        {
        "name": "getMarketNewsDef",
        "description": "获取近期有关某只股票的新闻",
        "parameters": {
            "type": "object",
            "properties": {
                "symbol": {
                    "type": "string",
                    "description": "股票代码",
                },
                "num": {
                    "type": "integer",
                    "description": "新闻数量",
                },
            },
            "required": ["symbol", "num"]
        },
        "response": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "新闻标题",
                },
                "description": {
                    "type": "string",
                    "description": "新闻摘要",
                },
                "link": {
                    "type": "string",
                    "description": "新闻网址，链接地址",
                },
                "pubDate": {
                    "type": "string",
                    "description": "新闻发布日期",
                },
            },
            "required": ["title", "description", "link", "pubDate"]
        },
        }
    ]
    response = erniebot.ChatCompletion.create(
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

    name2function = {"getMarketNewsDef": getMarketNewsDef}
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


if __name__ == '__main__':
    """ main function """
    pytest.main()

