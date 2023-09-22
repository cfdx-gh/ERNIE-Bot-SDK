import pytest
import openai
import os
import json
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "openai"
openai.api_key = get_config_elem_value(config_name, test_api_type, "api_key")


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

