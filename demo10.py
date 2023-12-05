from funix import funix


@funix(
    title="10. 融资说明",
    input_layout=[
        [{"markdown": "### 融资说明"}],
        [{"markdown": "项目总投入（目前项目已有的总投资、已有融资情况，项目未来一年的融资计划及进展预测）"}],
        [{"argument": "project_total_investment"}],
        [{"markdown": "资金用途（资金分阶段使用计划及用途）"}],
        [{"argument": "project_fund_usage"}],
        [{"markdown": "资金估值（有形资产估值、无形资产估值及估值计算方法）"}],
        [{"argument": "project_fund_valuation"}],
    ],
    widgets={
        ("project_total_investment", "project_fund_usage", "project_fund_valuation"): ("textarea", {"rows": 7})
    },
    argument_labels={
        "project_total_investment": "项目总投入",
        "project_fund_usage": "资金用途",
        "project_fund_valuation": "资金估值",
    }
)
def project_fund_information(
    project_total_investment: str,
    project_fund_usage: str,
    project_fund_valuation: str,
) -> dict:
    return {
        "project_total_investment": project_total_investment,
        "project_fund_usage": project_fund_usage,
        "project_fund_valuation": project_fund_valuation,
    }
