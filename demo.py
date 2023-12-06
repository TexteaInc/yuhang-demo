from typing import Literal

from funix import funix
from funix.hint import BytesFile


@funix(
    title="01. 项目基本情况",
    input_layout=[
        [{"markdown": "### 基本信息"}],
        [{"argument": "project_attribute"}],
        [{"argument": "project_name"}, {"argument": "project_location"}],
        [{"argument": "is_company_already_registered"}, {"argument": "project_realm"}],
        [{"markdown": "**答辩 PPT 上传**"}],
        [{"argument": "project_ppt"}],
        [{"markdown": "### 项目简介"}],
        [{"argument": "project_description"}],
        [{"markdown": "### 项目现状"}],
        [{"argument": "project_status"}],
    ],
    widgets={
        (
            "project_location",
            "project_realm",
            "is_company_already_registered",
        ): "inputbox",
        ("project_description", "project_status"): ("textarea", {"rows": 10}),
    },
    argument_labels={
        "project_attribute": "项目属性",
        "project_name": "项目名称",
        "project_location": "拟落地平台（街道）",
        "is_company_already_registered": "是否已注册公司",
        "project_realm": "所属领域",
        "project_description": "项目简介（1000 字以内）",
        "project_status": "项目现状（1000 字以内）",
    },
)
def project_basic_information(
    project_attribute: Literal["领军人才项目", "青年人才项目"],
    project_name: str,
    project_location: Literal["未来科技城（海创园）", "钱江经济开发区", "良渚新城", "区招才局"],
    is_company_already_registered: Literal["是", "否"],
    project_realm: Literal["电子信息", "生物医药", "新能源新材料", "装备制造", "文化与创意", "节能环保"],
    project_ppt: BytesFile,
    project_description: str,
    project_status: str,
) -> dict:
    return {
        "project_attribute": project_attribute,
        "project_name": project_name,
        "project_location": project_location,
        "is_company_already_registered": is_company_already_registered,
        "project_realm": project_realm,
        "project_ppt_size": len(project_ppt),
        "project_description": project_description,
        "project_status": project_status,
    }
