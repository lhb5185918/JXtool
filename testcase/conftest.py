import pytest
import requests

host = "192.168.111.232:17777"


@pytest.fixture(scope='function')
def get_token():
    url = f"http://{host}/oauth/password/unencrypted"
    data = {"userNo": "lhb001",
            "pwd": "lhx7758521", "platForm": "app",
            "companyCode": "ZHQC", "whId": 1,
            "warehouseId": "", "haveWarehouse": 1,
            "clientId": "iowtb-new", "userLanguage": "zh-CN"}
    res = requests.post(url=url, json=data).json()
    return {"Authorization": res['obj']['token'], "Content-Type": "application/json;charset"}
