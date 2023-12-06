from funix import funix


@funix(
    title="05. 产品与研发",
    input_layout=[
        [{"markdown": "## 融资说明"}],
        [{"markdown": "### 产品服务介绍（产品的用途、功能、行业领域、市场定位及客户价值观）"}],
        [{"argument": "service"}],
        [{"markdown": "### 产品特色优势（产品的新颖性、先进性、独特性、市场的竞争优势）"}],
        [{"argument": "feature"}],
        [{"markdown": "### 技术研发水平"}],
        [{"markdown": "**1. 项目研究内容，已有技术成果及指标**"}],
        [{"argument": "develop_content"}],
        [{"markdown": "**2. 项目实施的技术方案（包括技术路线、工艺的合理性及成熟性）**"}],
        [{"argument": "develop_technical"}],
        [{"markdown": "**3. 项目的关键技术、创新点**"}],
        [{"argument": "develop_keypoint"}],
        [{"markdown": "### 知识产权情况"}],
        [{"argument": "property_right"}],
    ],
    widgets={
        (
            "service",
            "feature",
            "develop_content",
            "develop_technical",
            "develop_keypoint",
            "property_right",
        ): ("textarea", {"rows": 5})
    },
    argument_labels={
        "service": "产品服务介绍",
        "feature": "产品特色优势",
        "develop_content": "项目研究内容",
        "develop_technical": "项目实施的技术方案",
        "develop_keypoint": "项目的关键技术、创新点",
        "property_right": "知识产权情况",
    },
)
def project_rna(
    service: str,
    feature: str,
    develop_content: str,
    develop_technical: str,
    develop_keypoint: str,
    property_right: str,
) -> dict:
    return {
        "service": service,
        "feature": feature,
        "develop_content": develop_content,
        "develop_technical": develop_technical,
        "develop_keypoint": develop_keypoint,
        "property_right": property_right,
    }
