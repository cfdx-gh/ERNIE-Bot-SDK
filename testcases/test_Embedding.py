import pytest
import erniebot
import os
import time
import numpy as np
from config_parse import get_config_elem_value

cur_path = os.getcwd()
config_name = os.path.join(cur_path, "config/authentication.ini")

test_api_qianfan = "qianfan"
test_ak = get_config_elem_value(config_name, test_api_qianfan, "ak")
test_sk = get_config_elem_value(config_name, test_api_qianfan, "sk")

test_api_aistudio = "aistudio"
test_access_token = get_config_elem_value(config_name, test_api_aistudio, "access_token")

sleep_second_num = 10

def embeddingSingleInputUseAistudio():
    """ Test Class for Embedding Single Input Use AIStudio """
    erniebot.api_type = test_api_aistudio
    erniebot.access_token = test_access_token

    response = erniebot.Embedding.create(
    model="ernie-text-embedding",
    input=[
        "2023年北京市GDP总量"
    ])
    for emb_res in response.data:
        embedding = np.array(emb_res["embedding"])
    return(embedding)


def embeddingTwoInputUseAistudio():
    """ Test Class for Embedding Two Input Use AIStudio """
    erniebot.api_type = test_api_aistudio
    erniebot.access_token = test_access_token

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


def embeddingSingleInputUseQianfan():
    """ Test Class for Embedding Single Input Use Qianfan """
    erniebot.api_type = test_api_qianfan
    erniebot.ak = test_ak
    erniebot.sk = test_sk

    response = erniebot.Embedding.create(
    model="ernie-text-embedding",
    input=[
        "2023年北京市GDP总量"
    ])
    for emb_res in response.data:
        embedding = np.array(emb_res["embedding"])
    return(embedding)


def embeddingTwoInputUseQianfan():
    """ Test Class for Embedding Two Input Use Qianfan """
    erniebot.api_type = test_api_qianfan
    erniebot.ak = test_ak
    erniebot.sk = test_sk

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


def embeddingOutputCheckForTwoRequestUseAistudio():
    """ Test Class for Embedding Output Check For Two Request Use AIStudio """
    erniebot.api_type = test_api_aistudio
    erniebot.access_token = test_access_token

    response = erniebot.Embedding.create(
    model="ernie-text-embedding",
    input=[
        "2023年北京市GDP总量"
    ])
    for emb_res in response.data:
        embedding = np.array(emb_res["embedding"])
    return(embedding)


class TestEmbedding:
    """ Test Class for Embedding """
    def test_aistudioSingleInput(self):
        result = embeddingSingleInputUseAistudio()
        assert 384 == len(result)
        time.sleep(sleep_second_num)

    def test_aistudioTwoInput(self):
        res1, res2 = embeddingTwoInputUseAistudio()
        assert 384 == len(res1)
        assert 384 == len(res2)
        time.sleep(sleep_second_num)

    def test_qianfanSingleInput(self):
        result = embeddingSingleInputUseQianfan()
        assert 384 == len(result)
        time.sleep(sleep_second_num)

    def test_qianfanTwoInput(self):
        res1, res2 = embeddingTwoInputUseQianfan()
        assert 384 == len(res1)
        assert 384 == len(res2)
        time.sleep(sleep_second_num)

    def test_aistudioOutputCheckForTwoRequest(self):
        result_1 = embeddingOutputCheckForTwoRequestUseAistudio()
        time.sleep(sleep_second_num)
        result_2 = embeddingOutputCheckForTwoRequestUseAistudio()
        assert True == np.array_equal(result_1, result_2)
        time.sleep(sleep_second_num)

if __name__ == '__main__':
    """ main function """
    pytest.main()

