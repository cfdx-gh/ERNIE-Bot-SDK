import pytest
import erniebot
import os
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
erniebot.api_type = test_api_type
erniebot.access_token = get_config_elem_value(config_name, test_api_type, "access_token")


def pythonAPIAiStudioPrintModelList():
    """ python API AiStudio Print Model List  """
    # List supported models
    models = erniebot.Model.list()

    return(models)
    # ernie-bot             文心一言旗舰版
    # ernie-bot-turbo       文心一言轻量版
    # ernie-text-embedding  文心百中语义模型
    # ernie-vilg-v2         文心一格模型


def pythonAPIAiStudioCreateChatComletion():
    """ python API AiStudio Create Chat Comletion  """
    # Create a chat completion
    response = erniebot.ChatCompletion.create(model="ernie-bot-3.5", messages=[{"role": "user", "content": "你好，请介绍下你自己"}])

    return(response.result)


class TestPythonAPI:
    """ Test Class for Python API """
    def test_aistudioPrintModelList(self):
        result = pythonAPIAiStudioPrintModelList()
        print(result)
        assert 4 == len(result)
        assert "ernie-bot-3.5"        == result[0][0]
        assert "ernie-bot-turbo"      == result[1][0]
        assert "ernie-text-embedding" == result[2][0]
        assert "ernie-vilg-v2"        == result[3][0]
    
    def test_aistudioCreateChatComletion(self):
        result = pythonAPIAiStudioCreateChatComletion()
        print(result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

