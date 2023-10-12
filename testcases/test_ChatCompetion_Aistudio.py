import pytest
import erniebot
import os
import time
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
test_access_token = get_config_elem_value(config_name, test_api_type, "access_token")

sleep_second_num = 15

def chatCompetionAiStudioStreamFalse():
    """ Chat Competion AIStudio Stream False """
    stream = False
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot-3.5",
        messages=[{
            "role": "user",
            "content": "请介绍下你自己？"
        }],
        top_p=0.95,
        stream=stream)

    result = ""
    if stream:
        for res in response:
            result += res.result 
    else:
        result = response.result

    return(result)


def chatCompetionAiStudioCommunicate():
    """ Chat Competion AIStudio Communicate """
    stream = False
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot-3.5",
        messages=[{
            "role": "user",
            "content": "帮我推荐中国四大名著"
        }],
        top_p=0.95,
        stream=stream)

    result = ""
    if stream:
        for res in response:
            result += res.result 
    else:
        result = response.result

    return(result)


def chatCompetionAiStudioContentCreation():
    """ Chat Competion AIStudio content creation """
    stream = False
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot-3.5",
        messages=[{
            "role": "user",
            "content": "用'百度文心'创作一首藏头诗"
        }],
        top_p=0.95,
        stream=stream)

    result = ""
    if stream:
        for res in response:
            result += res.result 
    else:
        result = response.result

    return(result)


def chatCompetionAiStudioCodeGeneration():
    """ Chat Competion AIStudio code generation """
    stream = False
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot-3.5",
        messages=[{
            "role": "user",
            "content": "用python怎么写出'hello world'?"
        }],
        top_p=0.95,
        stream=stream)

    result = ""
    if stream:
        for res in response:
            result += res.result 
    else:
        result = response.result

    return(result)


def chatCompetionAiStudioConfigParam():
    """ Chat Competion AIStudio use _config_ param """
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot",
        messages=[{"role": "user", "content": "你好，请介绍下你自己",
        }],
    )
    return(response.result)


class TestChatCompetion:
    """ Test Class for Chat Competion """
    def test_aistudioStreamFalse(self):
        time.sleep(sleep_second_num)
        result = chatCompetionAiStudioStreamFalse()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_aistudioCommunicate(self):
        result = chatCompetionAiStudioCommunicate()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_aistudioContentCreation(self):
        result = chatCompetionAiStudioContentCreation()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_aistudioCodeGeneration(self):
        result = chatCompetionAiStudioCodeGeneration()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)


if __name__ == '__main__':
    """ main function """
    pytest.main()

