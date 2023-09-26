import pytest
import erniebot
import os
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "qianfan"
erniebot.api_type = test_api_type
erniebot.ak = get_config_elem_value(config_name, test_api_type, "ak")
erniebot.sk = get_config_elem_value(config_name, test_api_type, "sk")
erniebot.access_token = get_config_elem_value(config_name, test_api_type, "access_token")


def chatCompetionAiStudioStreamFalse():
    """ Chat Competion AIStudio Stream False """
    stream = False
    response = erniebot.ChatCompletion.create(
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


class TestChatCompetion:
    """ Test Class for Chat Competion """
    def test_qianfanStreamFalse(self):
        erniebot.access_token = ""
        result = chatCompetionAiStudioStreamFalse()
        print("res:", result)
        assert "" != result

    def test_qianfanStreamTrue(self):
        erniebot.access_token = ""
        result = chatCompetionAiStudioStreamTrue()
        print("res:", result)
        assert "" != result

    def test_qianfanChatCompetionMultiple(self):
        erniebot.access_token = ""
        result = chatCompetionAiStudioMultiple()
        print("res:", result)
        assert "" != result

    def test_qianfanCommunicate(self):
        erniebot.access_token = ""
        result = chatCompetionAiStudioCommunicate()
        print("res:", result)
        assert "" != result

    def test_qianfanContentCreation(self):
        erniebot.access_token = ""
        result = chatCompetionAiStudioContentCreation()
        print("res:", result)
        assert "" != result

    def test_qianfanCodeGeneration(self):
        erniebot.access_token = ""
        result = chatCompetionAiStudioCodeGeneration()
        print("res:", result)
        assert "" != result

    def test_qianfanUseAccessToken(self):
        erniebot.ak = ""
        erniebot.sk = ""
        result = chatCompetionAiStudioStreamTrue()
        print("res:", result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

