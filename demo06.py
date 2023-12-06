from funix import funix


@funix(
    title="06. 产品化程度",
    input_layout=[
        [{"markdown": "### 产品化程度"}],
        [{"markdown": "目前产业化程度（阶段性成果描述）"}],
        [{"argument": "industrialization"}],
        [{"markdown": "已具备的产业化条件（设备、技术、场地、人才、合作等）"}],
        [{"argument": "conditions"}],
        [{"markdown": "未来产业化过程（分年度目标及前景分析）"}],
        [{"argument": "future"}],
    ],
    widgets={("industrialization", "conditions", "future"): ("textarea", {"rows": 7})},
    argument_labels={
        "industrialization": "目前产业化程度",
        "conditions": "已具备的产业化条件",
        "future": "未来产业化过程",
    },
)
def project_production(
    industrialization: str,
    conditions: str,
    future: str,
) -> dict:
    return {
        "industrialization": industrialization,
        "conditions": conditions,
        "future": future,
    }
