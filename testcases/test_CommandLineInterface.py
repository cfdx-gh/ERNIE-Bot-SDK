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

test_api_qianfan = "qianfan"
test_ak = get_config_elem_value(config_name, test_api_qianfan, "ak")
test_sk = get_config_elem_value(config_name, test_api_qianfan, "sk")

test_api_aistudio = "aistudio"
test_access_token = get_config_elem_value(config_name, test_api_aistudio, "access_token")

sleep_second_num = 0

def commandLineInterfacePrintModelListUseAistudio():
    """ Command Line Interface Print Model List Use Aistudio """
    # List supported models
    cmd = "export EB_API_TYPE=" + test_api_aistudio + " && "
    cmd += "export EB_ACCESS_TOKEN=" + test_access_token + " && "
    cmd += "erniebot api model.list"

    (status,value) = subprocess.getstatusoutput(cmd)

    return(value)


def commandLineInterfaceChatCompletionUseAistudio():
    """ Command Line Interface ChatCompletion Use Aistudio  """
    cmd = "export EB_API_TYPE=" + test_api_aistudio + " && "
    cmd += "export EB_ACCESS_TOKEN=" + test_access_token + " && "
    cmd += "erniebot api chat_completion.create --model ernie-bot-3.5 --message user \"请介绍下你自己\""
    #print(cmd)
    (status,value) = subprocess.getstatusoutput(cmd)

    return(value)


def commandLineInterfacePrintModelListUseQianfan():
    """ Command Line Interface Print Model List Use Qianfan """
    # List supported models
    cmd = "export EB_API_TYPE=" + test_api_qianfan + " && "
    cmd += "export EB_AK=" + test_ak + " && "
    cmd += "export EB_SK=" + test_sk + " && "
    cmd += "erniebot api model.list"

    (status,value) = subprocess.getstatusoutput(cmd)
    return(value)


def commandLineInterfaceChatCompletionUseQianfan():
    """ Command Line Interface ChatCompletion Use Qianfan  """
    cmd = "export EB_API_TYPE=" + test_api_qianfan + " && "
    cmd += "export EB_AK=" + test_ak + " && "
    cmd += "export EB_SK=" + test_sk + " && "
    cmd += "erniebot api chat_completion.create --model ernie-bot-3.5 --message user \"请介绍下你自己\""
    #print(cmd)
    (status,value) = subprocess.getstatusoutput(cmd)

    return(value)


class TestCommandLineInterface:
    """ Test Class for Command Line Interface """
    def test_aistudioPrintModelList(self):
        result = commandLineInterfacePrintModelListUseAistudio()
        print(result)
        assert "ernie-bot 文心一言旗舰版"              in result
        assert "ernie-bot-turbo 文心一言轻量版"        in result
        assert "ernie-text-embedding 文心百中语义模型" in result
        assert "ernie-vilg-v2 文心一格模型"            in result
        time.sleep(sleep_second_num)
    
    def test_aistudioCreateChatCompletion(self):
        result = commandLineInterfaceChatCompletionUseAistudio()
        print(result)
        assert "您好，我是文心一言，英文名是ERNIE Bot" in result
        time.sleep(sleep_second_num)

    def test_qianfanPrintModelList(self):
        result = commandLineInterfacePrintModelListUseQianfan()
        print(result)
        assert "ernie-bot 文心一言旗舰版"              in result
        assert "ernie-bot-turbo 文心一言轻量版"        in result
        assert "ernie-text-embedding 文心百中语义模型" in result
        assert "ernie-vilg-v2 文心一格模型"            in result
        time.sleep(sleep_second_num)
    
    def test_qianfanCreateChatCompletion(self):
        result = commandLineInterfaceChatCompletionUseQianfan()
        print(result)
        assert "您好，我是文心一言，英文名是ERNIE Bot" in result
        time.sleep(sleep_second_num)


if __name__ == '__main__':
    """ main function """
    pytest.main()

