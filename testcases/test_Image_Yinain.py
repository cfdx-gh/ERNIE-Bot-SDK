import pytest
import erniebot
import os
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "yinian"
erniebot.api_type = test_api_type
erniebot.ak = get_config_elem_value(config_name, test_api_type, "ak")
erniebot.sk = get_config_elem_value(config_name, test_api_type, "sk")
erniebot.access_token = get_config_elem_value(config_name, test_api_type, "access_token")

def imageGenerate():
    """ Image generate use yinain """
    response = erniebot.Image.create(
        model="ernie-vilg-v2",
        prompt="雨后的桃花",
        width=512,
        height=512
    )

    return(response.data["sub_task_result_list"][0]["final_image_list"][0]["img_url"])


class TestImage:
    """ Test Class for Image """
    def test_yinianImageGenerate(self):
        #erniebot.access_token = ""
        result = imageGenerate()
        print("res:", result)
        assert "" != result

    def test_yinianImageGenerateUseAccessToken(self):
        erniebot.ak = ""
        erniebot.sk = ""
        result = imageGenerate()
        print("res:", result)
        assert "" != result


if __name__ == '__main__':
    """ main function """
    pytest.main()

