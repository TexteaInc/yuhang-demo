from funix import funix


@funix(
    title="4. 申报项目投资简介",
    input_layout=[
        [{"markdown": "## 申报项目投资简介"}],
        [{"markdown": "注册资金"}],
        [{"argument": "registered_capital"}, {"argument": "actual_capital"}],
        [{"markdown": "申请项目总投资"}],
        [{"argument": "request_equipment_purchase_fee"}, {"argument": "request_energy_material_fee"}],
        [{"argument": "request_trial_outsourcing_fee"}, {"argument": "request_material_printing_fee"}],
        [{"argument": "request_conference_research_fee"}, {"argument": "request_rental_fee"}],
        [{"argument": "request_appraisal_inspection_fee"}, {"argument": "request_personnel_costs"}],
        [{"argument": "request_management_fee"}, {"argument": "request_other_fee"}],
        [{"markdown": "已完成项目投资额"}],
        [{"argument": "completed_equipment_purchase_fee"}, {"argument": "completed_energy_material_fee"}],
        [{"argument": "completed_trial_outsourcing_fee"}, {"argument": "completed_material_printing_fee"}],
        [{"argument": "completed_conference_research_fee"}, {"argument": "completed_rental_fee"}],
        [{"argument": "completed_appraisal_inspection_fee"}, {"argument": "completed_personnel_costs"}],
        [{"argument": "completed_management_fee"}, {"argument": "completed_other_fee"}],
    ],
    widgets={
        (
            "registered_capital",
            "actual_capital",
            "request_equipment_purchase_fee",
            "request_energy_material_fee",
            "request_trial_outsourcing_fee",
            "request_material_printing_fee",
            "request_conference_research_fee",
            "request_rental_fee",
            "request_appraisal_inspection_fee",
            "request_personnel_costs",
            "request_management_fee",
            "request_other_fee",
            "completed_equipment_purchase_fee",
            "completed_energy_material_fee",
            "completed_trial_outsourcing_fee",
            "completed_material_printing_fee",
            "completed_conference_research_fee",
            "completed_rental_fee",
            "completed_appraisal_inspection_fee",
            "completed_personnel_costs",
            "completed_management_fee",
            "completed_other_fee",
        ): "inputbox",
    },
    argument_labels={
        "registered_capital": "实到注册资金（万元）",
        "actual_capital": "申请人实到资金（万元）",
        ("request_equipment_purchase_fee", "completed_equipment_purchase_fee"): "设备购置费（万元）",
        ("request_energy_material_fee", "completed_energy_material_fee"): "能源材料费（万元）",
        ("request_trial_outsourcing_fee", "completed_trial_outsourcing_fee"): "试验外协费（万元）",
        ("request_material_printing_fee", "completed_material_printing_fee"): "资料印刷费（万元）",
        ("request_conference_research_fee", "completed_conference_research_fee"): "会议研讨费（万元）",
        ("request_rental_fee", "completed_rental_fee"): "租赁费（万元）",
        ("request_appraisal_inspection_fee", "completed_appraisal_inspection_fee"): "鉴定验收费（万元）",
        ("request_personnel_costs", "completed_personnel_costs"): "人员经费（万元）",
        ("request_management_fee", "completed_management_fee"): "管理经费（万元）",
        ("request_other_fee", "completed_other_fee"): "其他经费（万元）",
    }
)
def project_industry(
    registered_capital: int = 0,
    actual_capital: int = 0,
    request_equipment_purchase_fee: int = 0,
    request_energy_material_fee: int = 0,
    request_trial_outsourcing_fee: int = 0,
    request_material_printing_fee: int = 0,
    request_conference_research_fee: int = 0,
    request_rental_fee: int = 0,
    request_appraisal_inspection_fee: int = 0,
    request_personnel_costs: int = 0,
    request_management_fee: int = 0,
    request_other_fee: int = 0,
    completed_equipment_purchase_fee: int = 0,
    completed_energy_material_fee: int = 0,
    completed_trial_outsourcing_fee: int = 0,
    completed_material_printing_fee: int = 0,
    completed_conference_research_fee: int = 0,
    completed_rental_fee: int = 0,
    completed_appraisal_inspection_fee: int = 0,
    completed_personnel_costs: int = 0,
    completed_management_fee: int = 0,
    completed_other_fee: int = 0,
) -> dict:
    return {
        "申请人所占份额": actual_capital / registered_capital if registered_capital > 0 else 0,
        "申请项目总投资":
            request_equipment_purchase_fee +
            request_energy_material_fee +
            request_trial_outsourcing_fee +
            request_material_printing_fee +
            request_conference_research_fee +
            request_rental_fee +
            request_appraisal_inspection_fee +
            request_personnel_costs +
            request_management_fee +
            request_other_fee,
        "已完成项目投资额":
            completed_equipment_purchase_fee +
            completed_energy_material_fee +
            completed_trial_outsourcing_fee +
            completed_material_printing_fee +
            completed_conference_research_fee +
            completed_rental_fee +
            completed_appraisal_inspection_fee +
            completed_personnel_costs +
            completed_management_fee +
            completed_other_fee,
    }
