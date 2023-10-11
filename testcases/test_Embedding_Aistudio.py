import pytest
import erniebot
import os
import time
import numpy as np
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_type = "aistudio"
erniebot.api_type = test_api_type
erniebot.access_token = get_config_elem_value(config_name, test_api_type, "access_token")

sleep_second_num = 10

def embeddingAiStudioSingleInput():
    """ Test Class for Embedding AIStudio """
    response = erniebot.Embedding.create(
    model="ernie-text-embedding",
    input=[
        "2023年北京市GDP总量"
    ])
    for emb_res in response.data:
        embedding = np.array(emb_res["embedding"])
    return(embedding)


def embeddingAiStudioTwoInput():
    """ Test Class for Embedding AIStudio """
    response = erniebot.Embedding.create(
    model="ernie-text-embedding",
    input=[
        "2023年北京市GDP总量",
        "2023年北京市GDP增量",
    ])
    #print(response)

    embedding_index0 = response.data[0]["embedding"]
    embedding_index1 = response.data[1]["embedding"]
    return embedding_index0, embedding_index1


class TestEmbedding:
    """ Test Class for Embedding """
    def test_aistudioSingleInput(self):
        result = embeddingAiStudioSingleInput()
        assert 384 == len(result)
        time.sleep(sleep_second_num)

    def test_aistudioTwoInput(self):
        res1, res2 = embeddingAiStudioTwoInput()
        assert 384 == len(res1)
        assert 384 == len(res2)
        time.sleep(sleep_second_num)


if __name__ == '__main__':
    """ main function """
    pytest.main()

