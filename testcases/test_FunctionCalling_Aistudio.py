import pytest
import erniebot
import os
import json
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
erniebot.api_type = test_api_type
erniebot.access_token = get_config_elem_value(config_name, test_api_type, "access_token")


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
        model="ernie-bot-3.5",
        messages=messages,
        functions=functions
    )
    assert hasattr(response, "function_call")
    function_call = response.function_call
    print("function_call:",function_call)

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
        model="ernie-bot-3.5",
        messages=messages,
        functions=functions
    )
    return(response.result)


class TestFunctionCalling:
    """ Test Class for Function Calling """
    def test_aistudioGetWeatherInfo(self):
        result = functionCallingAiStudioGetWeatherInfo()
        print(result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

