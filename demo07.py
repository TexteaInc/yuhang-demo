from funix import funix


@funix(
    title="07. 市场营销",
    input_layout=[
        [{"markdown": "## 融资说明"}],
        [{"markdown": "### 市场分析（行业历史与前景、现有市场规模及增长趋势）"}],
        [{"argument": "analysis"}],
        [{"markdown": "### 市场定位（地域、产业链、市场占有率分析）"}],
        [{"argument": "positioning"}],
        [{"markdown": "### 竞争力分析（分析竞争环境、行业竞争对手及本公司竞争优势与不足）"}],
        [{"argument": "competitive_analysis"}],
        [{"markdown": "### SWOT分析"}],
        [{"markdown": "**1. 优势（Strength）**"}],
        [{"argument": "swot_s"}],
        [{"markdown": "**2. 劣势（Weakness）**"}],
        [{"argument": "swot_w"}],
        [{"markdown": "**3. 机会（Opportunity）**"}],
        [{"argument": "swot_o"}],
        [{"markdown": "**4. 威胁（Threats）**"}],
        [{"argument": "swot_t"}],
        [{"markdown": "### 营销策略"}],
        [{"argument": "marketing_strategy"}],
        [{"markdown": "### 市场预测"}],
        [{"argument": "market_prediction"}],
    ],
    widgets={
        (
            "analysis",
            "positioning",
            "competitive_analysis",
            "swot_s",
            "swot_w",
            "swot_o",
            "swot_t",
            "marketing_strategy",
            "market_prediction",
        ): ("textarea", {"rows": 5})
    },
    argument_labels={
        "analysis": "市场分析",
        "positioning": "市场定位",
        "competitive_analysis": "竞争力分析",
        "swot_s": "优势",
        "swot_w": "劣势",
        "swot_o": "机会",
        "swot_t": "威胁",
        "marketing_strategy": "营销策略",
        "market_prediction": "市场预测",
    },
)
def project_marketing(
    analysis: str,
    positioning: str,
    competitive_analysis: str,
    swot_s: str,
    swot_w: str,
    swot_o: str,
    swot_t: str,
    marketing_strategy: str,
    market_prediction: str,
) -> dict:
    return {
        "project_total_investment": project_total_investment,
        "project_fund_usage": project_fund_usage,
        "project_fund_valuation": project_fund_valuation,
    }
