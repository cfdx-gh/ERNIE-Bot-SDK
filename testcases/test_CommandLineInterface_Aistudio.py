import pytest
import erniebot
import os
import sys
import io
import time
import subprocess
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
api_type = test_api_type
access_token = get_config_elem_value(config_name, test_api_type, "access_token")

sleep_second_num = 0

def commandLineInterfaceAiStudioPrintModelList():
    """ Command Line Interface AiStudio Print Model List  """
    # List supported models
    (status,value) = subprocess.getstatusoutput('erniebot api model.list')

    return(value)


def commandLineInterfaceAiStudioChatCompletion():
    """ Command Line Interface AiStudio ChatCompletion  """
    cmd = "export EB_API_TYPE=" + api_type + " && "
    cmd += "export EB_ACCESS_TOKEN=" + access_token + " && "
    cmd += "erniebot api chat_completion.create --model ernie-bot-3.5 --message user \"请介绍下你自己\""
    #print(cmd)
    (status,value) = subprocess.getstatusoutput(cmd)

    return(value)


class TestCommandLineInterface:
    """ Test Class for Command Line Interface """
    def test_aistudioPrintModelList(self):
        result = commandLineInterfaceAiStudioPrintModelList()
        print(result)
        assert "ernie-bot 文心一言旗舰版"              in result
        assert "ernie-bot-turbo 文心一言轻量版"        in result
        assert "ernie-text-embedding 文心百中语义模型" in result
        assert "ernie-vilg-v2 文心一格模型"            in result
        time.sleep(sleep_second_num)
    
    def test_aistudioCreateChatCompletion(self):
        result = commandLineInterfaceAiStudioChatCompletion()
        print(result)
        assert "您好，我是文心一言，英文名是ERNIE Bot" in result
        time.sleep(sleep_second_num)


if __name__ == '__main__':
    """ main function """
    pytest.main()

