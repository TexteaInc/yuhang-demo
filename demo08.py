from funix import funix


@funix(
    title="8. 发展战略",
    widgets={"development_strategy": ("textarea", {"rows": 15})},
    argument_labels={
        "development_strategy": "发展战略",
    },
)
def project_development_strategy(
    development_strategy: str,
) -> dict:
    return {
        "development_strategy": development_strategy,
    }
