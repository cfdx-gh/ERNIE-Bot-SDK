import pytest
import erniebot
import os
import sys
import io
import subprocess
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
api_type = test_api_type
access_token = get_config_elem_value(config_name, test_api_type, "access_token")


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
        #assert 4 == len(result)
        #assert "ernie-bot-3.5"        == result[0][0]
        #assert "ernie-bot-turbo"      == result[1][0]
        #assert "ernie-text-embedding" == result[2][0]
        #assert "ernie-vilg-v2"        == result[3][0]
    
    def test_aistudioCreateChatCompletion(self):
        result = commandLineInterfaceAiStudioChatCompletion()
        print(result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

