import pytest
import erniebot
import os
import time
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "qianfan"
test_ak = get_config_elem_value(config_name, test_api_type, "ak")
test_sk = get_config_elem_value(config_name, test_api_type, "sk")
test_access_token = get_config_elem_value(config_name, test_api_type, "access_token")

sleep_second_num = 2

def chatCompetionAiStudioStreamFalse():
    """ Chat Competion AIStudio Stream False """
    stream = False
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            ak = test_ak,
            sk = test_sk,
        ),
        model="ernie-bot",
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


def chatCompetionAiStudioStreamTrue():
    """ Chat Competion AIStudio Stream True """
    stream = True
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            ak = test_ak,
            sk = test_sk,
        ),
        model="ernie-bot",
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


def chatCompetionAiStudioMultiple():
    """ Chat Competion AIStudio Multiple """
    stream = True
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            ak = test_ak,
            sk = test_sk,
        ),
        model="ernie-bot",
        messages=[{
        "role": "user",
        "content": "请问你是谁？"
    }, {
        "role": "assistant",
        "content":
        "我是百度公司开发的人工智能语言模型，我的中文名是文心一言，英文名是ERNIE-Bot，可以协助您完成范围广泛的任务并提供有关各种主题的信息，比如回答问题，提供定义和解释及建议。如果您有任何问题，请随时向我提问。"
    }, {
        "role": "user",
        "content": "我在深圳，周末可以去哪里玩？"
    }])

    return(response)


def chatCompetionAiStudioCommunicate():
    """ Chat Competion AIStudio Communicate """
    stream = False
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            ak = test_ak,
            sk = test_sk,
        ),
        model="ernie-bot",
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
            ak = test_ak,
            sk = test_sk,
        ),
        model="ernie-bot",
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
            ak = test_ak,
            sk = test_sk,
        ),
        model="ernie-bot",
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


def chatCompetionAiStudioUseAccessToken():
    """ Chat Competion AIStudio Use Access Token """
    stream = True
    response = erniebot.ChatCompletion.create(
        _config_ = dict(
            api_type = test_api_type,
            access_token = test_access_token,
        ),
        model="ernie-bot",
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


class TestChatCompetion:
    """ Test Class for Chat Competion """
    def test_qianfanStreamFalse(self):
        time.sleep(sleep_second_num)
        result = chatCompetionAiStudioStreamFalse()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_qianfanStreamTrue(self):
        result = chatCompetionAiStudioStreamTrue()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_qianfanChatCompetionMultiple(self):
        result = chatCompetionAiStudioMultiple()
        print("res:", result["result"])
        assert "" != result
        time.sleep(sleep_second_num)

    def test_qianfanCommunicate(self):
        result = chatCompetionAiStudioCommunicate()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_qianfanContentCreation(self):
        result = chatCompetionAiStudioContentCreation()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_qianfanCodeGeneration(self):
        result = chatCompetionAiStudioCodeGeneration()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)

    def test_qianfanUseAccessToken(self):
        result = chatCompetionAiStudioUseAccessToken()
        print("res:", result)
        assert "" != result
        time.sleep(sleep_second_num)


if __name__ == '__main__':
    """ main function """
    pytest.main()

