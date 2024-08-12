# -*- coding: utf-8 -*-
import json
import time
from common import CommonDatabase
import pytest
import requests

host = "192.168.111.232:17777"
# ANSI 转义序列
RED = "\033[31m"  # 红色
RESET = "\033[0m"  # 重置颜色


class TestRk:
    @pytest.fixture(scope="session")
    def share_rk_oder_no(self):
        return {"value": None}

    @pytest.fixture(scope="session")
    def get_in_order_data_list(self):
        return {}

    @pytest.mark.parametrize("description", ["入库订单查询接口"])
    def test_get_rk_oder(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/order/inOrder/pageInfo"
        data = {"orderByColumnList": [], "page": "1",
                "limit": 50}
        res = requests.post(url=url, json=data, headers=get_token)
        assert res.status_code == 200

    @pytest.mark.parametrize("description", ["出库订单查询接口"])
    def test_get_out_oder(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/order/outOrder/pageInfo"
        data = {"orderByColumnList": [], "page": "1",
                "limit": 50}
        res = requests.post(url=url, json=data, headers=get_token)
        assert res.status_code == 200

    @pytest.mark.parametrize("description", ["货主查询接口"])
    def test_get__owner(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/tm/owner/queryOwnerCbList"
        data = {"queryText": ""}
        res = requests.post(url=url, json=data, headers=get_token)
        assert res.json()['msg'] == "成功" and res.json()['total'] > 0

    @pytest.mark.parametrize("description", ["入库订单-手动新增接口"])
    def test_creat_hande_rk_oder(self, get_token, description, share_rk_oder_no):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/order/inOrder/add"
        data = {
            "origSys": "WMS",
            "orderStatus": "CJ",
            "jobType": "PTDD",
            "origNo": f"autotest{int(time.strftime('%Y%m%d%H%M%S'))}",
            "orderType": "CGDD",
            "partnerType": "SUPPLIER",
            "supplierId": "1838234556355072",
            "customerId": None,
            "storeId": None,
            "supplierName": "青岛医药科技集团有限公司--智汇奇策科技有限公司",
            "ownerId": "1770570116141568",
            "ownerName": "智汇奇策科技有限公司",
            "productFormType": "YP",
            "dtReqList": [
                {
                    "sourceProductionDateType": "0",
                    "sourceInvalidDateType": "0",
                    "skuId": "1825502431040000",
                    "key": "1825502431040000",
                    "companyCode": "ZHQC",
                    "whId": 1,
                    "id": "1825502431040000",
                    "remark": "",
                    "createTime": "2024-07-13 13:57:06",
                    "creator": "lihongbin",
                    "creatorName": "李鸿宾",
                    "updateTime": "2024-07-25 15:42:11",
                    "updater": "lhb001",
                    "updaterName": "李鸿宾",
                    "createTimeStr": "2024-07-13 13:57:06",
                    "updateTimeStr": "2024-07-25 15:42:11",
                    "ownerId": 1770570116141568,
                    "sysSkuCode": "SS24071300001",
                    "skuCode": "M123321",
                    "skuName": "维生素A",
                    "origSys": "WMS",
                    "spec": "50g",
                    "ephedrine": 1,
                    "tradeName": "维生素A",
                    "skuCategoryId": 1770467433878016,
                    "brandName": "",
                    "barcode": "01000101010000",
                    "mainUnit": "瓶",
                    "length": 15,
                    "width": 15,
                    "height": 15,
                    "vol": 3375,
                    "grossWeight": 2.5,
                    "netWeight": 2.5,
                    "abc": "A",
                    "zjAbc": "A",
                    "mfgId": 1825497449042432,
                    "mfg": "青岛医药科技生产有限公司",
                    "outFactoryCode": "",
                    "model": "",
                    "originCountry": "山东省青岛市市北区昆明路",
                    "logistics": "",
                    "isBatchManage": 1,
                    "isValidity": 0,
                    "validityType": "",
                    "validityDay": 0,
                    "warmValidityDay": 60,
                    "isValuables": 0,
                    "isCombination": 0,
                    "isGift": 0,
                    "isConsumables": 0,
                    "isChangeable": 0,
                    "isProneToMistakes": 0,
                    "isHeteromorphicProduct": 0,
                    "perQty": 100,
                    "midPackQty": 25,
                    "isEnable": 1,
                    "auditOpinion": None,
                    "auditStatus": None,
                    "auditTime": None,
                    "auditName": None,
                    "barcodeTwo": "",
                    "barcodeThree": "",
                    "taxCode": "",
                    "taxName": "",
                    "taxFee": None,
                    "tempControl": "CW",
                    "scatteredProperties": "",
                    "gmpCertNo": "",
                    "approvalNumber": "国药准字维生素A",
                    "categoryPrincipal": "",
                    "permitHolder": "",
                    "qtyStandard": "",
                    "mnemonicCode": "wssa",
                    "limitSaleDay": 30,
                    "routeOfAdministration": "",
                    "tempMax": None,
                    "tempMin": None,
                    "minInvoicingUnit": None,
                    "optimistic": 0,
                    "packFactoryId": 0,
                    "productFormType": "YP",
                    "isLimitMidPack": 0,
                    "hasAnaleptic": 0,
                    "tempCondition": None,
                    "diCode": None,
                    "erpUpdaterName": None,
                    "erpUpdateTime": None,
                    "erpCreatorName": None,
                    "erpCreateTime": None,
                    "creditType": None,
                    "medicalInsuranceCode": None,
                    "instrumentModel": None,
                    "entrustMfgId": None,
                    "hasAnalepticName": "否",
                    "ephedrineName": "是",
                    "isDoubleCheckName": "否",
                    "isDoubleCheck": 0,
                    "isFirstCamp": 0,
                    "isFirstCampName": "否",
                    "isLimitMidPackName": "否",
                    "prodLicenseCode": None,
                    "ownerCode": "ZHQCHZ",
                    "ownerName": "智汇奇策科技有限公司",
                    "skuCategoryName": "药品",
                    "skuCategoryCode": None,
                    "skuCategoryParentId": None,
                    "productFormTypeName": "药品",
                    "maintenanceType": "PT",
                    "maintenanceTypeName": "一般养护",
                    "skuCategorySecondId": None,
                    "drugForm": "_",
                    "drugFormSpec": "",
                    "grmpCertificateNo": None,
                    "grmpExpirationDate": "2033-07-31",
                    "pzwhExpirationDate": None,
                    "bomVOList": None,
                    "consumablesVOList": None,
                    "certificateVOList": None,
                    "approvalNumberList": None,
                    "gspData": None,
                    "imageVOList": None,
                    "packingVOList": None,
                    "tempControlName": "常温",
                    "isEnableName": "是",
                    "scatteredPropertiesName": None,
                    "packFactoryName": "",
                    "entrustMfgName": "",
                    "isValidityName": "否",
                    "sumUsableQty": None,
                    "auditStatusName": None,
                    "isDrugSuperCode": 0,
                    "isDrugSuperCodeName": "否",
                    "auditorTime": None,
                    "orgId": "1770560509055488",
                    "orgName": "零售事业部",
                    "orgFullName": "智汇奇策科技有限公司_零售事业部",
                    "supplierId": "1838234556355072",
                    "supplierName": "青岛医药科技集团有限公司--智汇奇策科技有限公司",
                    "inOrderQty": "100.000",
                    "amount": "111.100",
                    "unitPrice": "1.111",
                    "manageValidDay": "30",
                    "_X_ROW_KEY": "row_528"
                }
            ],
            "extendReq": {
                "refundReason": None,
                "isSqueezed": 1
            }
        }
        share_rk_oder_no['value'] = data['origNo']
        res = requests.post(url=url, json=data, headers=get_token)
        assert res.json()['code'] == 200 and res.json()['msg'] == "成功" and share_rk_oder_no['value'] is not None

    @pytest.mark.parametrize("description", ["入库订单-erp新增接口"])
    def test_creat_erp_oder(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/oms_232/api/erp/inOrder/add"
        data = {
            "origCompanyCode": "ZHQC",
            "origNo": f"autotest{int(time.strftime('%Y%m%d%H%M%S'))}",
            "orderType": "CGDD",
            "origSys": "CQ_ERP",
            "origWarehouseCode": "MRCK",
            "ownerCode": "ZHQCHZ",
            "orderPrice": 1234,
            "erpCreator": "李鸿宾",
            "shipAddr": "测试发货地区",
            "erpCreateTime": "2024-08-07 18:00:00",
            "erpUpdater": "李鸿宾",
            "erpUpdateTime": "2024-08-07 18:00:00",
            "productFormType": "YP",
            "jobType": "PTDD",
            "partnerType": "SUPPLIER",
            "partnerCode": "S00004729",
            "province": "山东省",
            "city": "青岛市",
            "area": "市北区",
            "refundReason": "测试退货原因",
            "contactName": "测试收件人",
            "contactAddr": "测试收货地址",
            "contactPhone": "测试1231241241",
            "contactTel": "52312412412",
            "origPurchaseOrderNo": "CGDD-1000-1000",
            "outWarehouseName": "测试",
            "dtList": [
                {
                    "origRowNo": 1,
                    "skuCode": "M123321",
                    "inOrderQty": 100.111,
                    "unitPrice": 12,
                    "amount": 48,
                    "orgCode": "110013687",
                    "supplierCode": "S00004729",
                    "productionBatch": "",
                    "productionDate": "",
                    "invalidDate": "",
                    "buyer": "李鸿宾"
                }
            ]
        }
        res = requests.post(url=url, data=json.dumps(data), headers=get_token)
        assert res.json()['code'] == 200 and res.json()['msg'] == "成功"

    @pytest.mark.parametrize("description", ["入库-提取数据接口"])
    def test_get_oder(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/ib/rec/queryUserNotFinishRecInOrder"
        res = requests.post(url=url, data="{}", headers=get_token)
        assert res.json()['msg'] == "成功" and res.json()['obj'] is not None

    @pytest.mark.parametrize("description", ["入库-ASNl列表查看接口"])
    def test_get_oder(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/ib/asn/pageInfo"
        data = {"page": 1, "limit": 50}
        res = requests.post(url=url, json=data, headers=get_token)
        assert res.json()['msg'] == "成功" and res.json()['total'] > 0

    @pytest.mark.parametrize("description", ["入库-ASN效期l列表查看接口"])
    def test_get_oder(self, get_token, description):
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/ib/asnRecRecord/pageInfoToAsnNearEffectivePeriod"
        data = {"orderByColumnList": None, "productFormType": "YP", "page": 1, "limit": 50}
        res = requests.post(url=url, json=data, headers=get_token)
        assert res.json()['msg'] == "成功" and res.json()['total'] > 0

    @pytest.mark.parametrize("description", ["入库-获取订单详情接口"])
    def test_get_oder(self, get_token, description, share_rk_oder_no, get_in_order_data_list):
        ys_data = CommonDatabase().select_data("*", "order_tt_in_order", f"orig_no ='{share_rk_oder_no['value']}'")
        print(f"用例名称: {description}")
        url = f"http://{host}/wms_232/ib/rec/queryUserNotFinishRecInOrderDt"
        data = {"inOrderId": ys_data['id']}
        res = requests.post(url=url, json=data, headers=get_token)
        if res.json()['obj'] is not None:
            for i in res.json()['obj']:
                get_in_order_data_list.update(i)
        else:
            print("入库订单详情为空")
        assert res.json()['msg'] == "成功" and res.json()['obj'] is not None
