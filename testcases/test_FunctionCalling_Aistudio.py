import pytest
import erniebot
import os
import json
import time
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
test_access_token = get_config_elem_value(config_name, test_api_type, "access_token")

sleep_second_num = 5

functions = [
    {
        "name": "get_current_temperature",
        "description": "获取指定城市的气温",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "城市名称"
                },
                "unit": {
                    "type": "string",
                    "enum": [
                        "摄氏度",
                        "华氏度"
                    ]
                }
            },
            "required": [
                "location",
                "unit"
            ]
        },
        "responses": {
            "type": "object",
            "properties": {
                "temperature": {
                    "type": "integer",
                    "description": "城市气温"
                },
                "unit": {
                    "type": "string",
                    "enum": [
                        "摄氏度",
                        "华氏度"
                    ]
                }
            }
        }
    }
]


def get_current_temperature(location: str, unit: str) -> dict:
    """ return current temperature """
    return {"temperature": 25, "unit": "摄氏度"}


def functionCallingAiStudioGetWeatherInfo():
    """ Function Calling AIStudio Get Weather Info """
    messages = [
        {
            "role": "user",
            "content": "深圳市今天气温多少度？我想知道温度是多少摄氏度。"
        }
    ]

    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)
    res_function_callinfo = function_call

    name2function = {"get_current_temperature": get_current_temperature}
    func = name2function[function_call["name"]]
    args = json.loads(function_call["arguments"])
    res = func(location=args["location"], unit=args["unit"])

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
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot",
        messages=messages,
        functions=functions
    )
    return(response.result, res_function_callinfo)


class TestFunctionCalling:
    """ Test Class for Function Calling """
    def test_aistudioFunctionIsCalled(self):
        result, res_function_callinfo = functionCallingAiStudioGetWeatherInfo()
        print(res_function_callinfo)
        function_name = res_function_callinfo["name"]
        location = json.loads(res_function_callinfo["arguments"])["location"]
        unit = json.loads(res_function_callinfo["arguments"])["unit"]
        assert "get_current_temperature" == function_name
        assert "深圳市" == location
        assert "摄氏度" == unit
        time.sleep(sleep_second_num)

    def test_aistudioGetWeatherInfo(self):
        result, res_function_callinfo = functionCallingAiStudioGetWeatherInfo()
        print(result)
        assert "深圳市" in result
        time.sleep(sleep_second_num)

if __name__ == '__main__':
    """ main function """
    pytest.main()

