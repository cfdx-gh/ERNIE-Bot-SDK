import pytest
import erniebot
import os
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_qianfan = "qianfan"
test_ak = get_config_elem_value(config_name, test_api_qianfan, "ak")
test_sk = get_config_elem_value(config_name, test_api_qianfan, "sk")

test_api_aistudio = "aistudio"
test_access_token = get_config_elem_value(config_name, test_api_aistudio, "access_token")

#test_model_name = "ernie-bot-3.5"
test_model_name = "ernie-bot"
#test_model_name = "ernie-bot-4"

def pythonAPIPrintModelListUseAistudio():
    """ python API Print Model List Use AiStudio """
    # List supported models
    erniebot.api_type = test_api_aistudio
    erniebot.access_token = test_access_token

    models = erniebot.Model.list()

    return(models)


def pythonAPICreateChatComletionUseAistudio():
    """ python API Create Chat Comletion Use AiStudio """
    # Create a chat completion
    erniebot.api_type = test_api_aistudio
    erniebot.access_token = test_access_token

    response = erniebot.ChatCompletion.create(model=test_model_name, messages=[{"role": "user", "content": "你好，请介绍下你自己"}])

    return(response.result)


def pythonAPIPrintModelListUseQianfan():
    """ python API Print Model List Use Qianfan """
    # List supported models
    erniebot.api_type = test_api_qianfan
    erniebot.ak = test_ak
    erniebot.sk = test_sk

    models = erniebot.Model.list()

    return(models)


def pythonAPICreateChatComletionUseQianfan():
    """ python API Create Chat Comletion Use Qianfan  """
    # Create a chat completion
    erniebot.api_type = test_api_qianfan
    erniebot.ak = test_ak
    erniebot.sk = test_sk

    response = erniebot.ChatCompletion.create(model=test_model_name, messages=[{"role": "user", "content": "你好，请介绍下你自己"}])

    return(response.result)


class TestPythonAPI:
    """ Test Class for Python API """
    @pytest.mark.skip
    def test_aistudioPrintModelList(self):
        result = pythonAPIPrintModelListUseAistudio()
        print(result)
        assert 5 == len(result)
        assert "ernie-bot"            == result[0][0]
        assert "ernie-bot-turbo"      == result[1][0]
        assert "ernie-bot-4"          == result[2][0]
        assert "ernie-text-embedding" == result[3][0]
        assert "ernie-vilg-v2"        == result[4][0]
    
    def test_aistudioCreateChatComletion(self):
        result = pythonAPICreateChatComletionUseAistudio()
        print(result)
        assert "您好，我是文心一言，英文名是ERNIE Bot" in result

    @pytest.mark.skip
    def test_qianfanPrintModelList(self):
        result = pythonAPIPrintModelListUseQianfan()
        print(result)
        assert 5 == len(result)
        assert "ernie-bot"            == result[0][0]
        assert "ernie-bot-turbo"      == result[1][0]
        assert "ernie-bot-4"          == result[2][0]
        assert "ernie-text-embedding" == result[3][0]
        assert "ernie-vilg-v2"        == result[4][0]
    
    def test_qianfanCreateChatComletion(self):
        result = pythonAPICreateChatComletionUseQianfan()
        print(result)
        assert "您好，我是文心一言，英文名是ERNIE Bot" in result


if __name__ == '__main__':
    """ main function """
    pytest.main()

