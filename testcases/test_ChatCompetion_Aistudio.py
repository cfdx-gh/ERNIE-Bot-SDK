import pytest
import erniebot
import os
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
erniebot.api_type = test_api_type
erniebot.access_token = get_config_elem_value(config_name, test_api_type, "access_token")


def chatCompetionAiStudioStreamFalse():
    """ Chat Competion AIStudio Stream False """
    stream = False
    response = erniebot.ChatCompletion.create(
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


class TestChatCompetion:
    """ Test Class for Chat Competion """
    def test_aistudioStreamFalse(self):
        result = chatCompetionAiStudioStreamFalse()
        print("res:", result)
        assert "" != result

    def test_aistudioCommunicate(self):
        result = chatCompetionAiStudioCommunicate()
        print("res:", result)
        assert "" != result

    def test_aistudioContentCreation(self):
        result = chatCompetionAiStudioContentCreation()
        print("res:", result)
        assert "" != result

    def test_aistudioCodeGeneration(self):
        result = chatCompetionAiStudioCodeGeneration()
        print("res:", result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

