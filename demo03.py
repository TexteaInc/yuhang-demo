from typing import List, Literal

from funix import funix


@funix(
    title="03. 企业注册情况",
    input_layout=[
        [{"markdown": "**企业信息（如未注册请填写预注册信息）**"}],
        [{"argument": "business_name"}, {"argument": "legal_person_name"}],
        [{"argument": "legal_person_sex"}, {"argument": "legal_person_id_number"}],
        [{"argument": "business_address"}, {"argument": "business_registered_capital"}],
        [{"markdown": "**投资信息**"}],
    ],
    argument_labels={
        "business_name": "企业名称",
        "legal_person_name": "注册法人",
        "legal_person_sex": "法人性别",
        "legal_person_id_number": "法人身份证",
        "business_address": "注册地址",
        "business_registered_capital": "注册资本（单位：万元）",
        "investors": "投资人",
        "invest_amounts": "投资额（万元）",
        "capital_ratios": "资本比例（%）",
    },
    widgets={
        "legal_person_sex": "inputbox",
        ("investors", "invest_amounts", "capital_ratios"): "sheet",
    },
)
def business_registration(
    business_name: str,
    legal_person_name: str,
    legal_person_sex: Literal["男", "女"],
    legal_person_id_number: str,
    business_address: str,
    business_registered_capital: int,
    investors: List[str],
    invest_amounts: List[int],
    capital_ratios: List[float],
):
    pass
