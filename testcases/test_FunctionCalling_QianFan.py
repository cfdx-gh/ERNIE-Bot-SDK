import pytest
import erniebot
import os
import json
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


class TestFunctionCalling:
    """ Test Class for Function Calling """
    def test_GetCurrentWeather(self):
        result = getCurrentWeatherCall()
        print(result)
        assert "" != result

    def test_get_N_DayWeatherForecast(self):
        result = getNDayWeatherForecastCall()
        print(result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

