from fastmcp import FastMCP


mcp = FastMCP("LowCodeDefine")

def get_valid() -> str:
    print("加载验证规则文档")
    """加载验证规则文档"""
    with open('Valid.md', 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def get_example() -> str:
    print("加载模型生成示例")
    """加载模型生成示例"""
    with open('example.md', 'r', encoding='utf-8') as file:
        text = file.read()
    return text


@mcp.tool(name="pageView",description="基于用户描述的需求，生成pageView基石文件的提示词")
def prompt(user_input: str) -> str:
    return f"{user_input}的pageView文件"


@mcp.tool(name="DSL模型文件",description="基于用户描述的需求，用于生成DSL模型文件的提示词")
def dsl_prompt(user_input: str) -> str:
    """输出"""
    print("进入到提示词方法")
    """
    Name:
     提示词模板

    Description:
     用户可通过描述需求

    Args:
        text：用户描述的需求
    """
    example = get_example()
    validation_rules = get_valid()
    skill = """
       1. **基本数据结构运用**：熟练运用long、boolean、date、string、double、int等基本数据结构进行模型字段定义。
       2. **自定义数据结构构建**：依据业务需求，合理创建dictCode（基础数据标识，如ORG、SUPER_ORG等多种类型）、dictEnum（可定义的枚举）等自定义数据结构。
       3. **子模型数据结构设计**：精准设计subModels（子模型一对多）、subModel（子模型一对一）等子模型数据结构，确保模型关系的完整性。
       4. **字段级别校验规则制定**：严格按照必填（required()）、最小值（minValue = x）、最大值（maxValue = x）、精度控制（digits { integer = x fraction = x }）等规则对字段进行校验，保障数据准确性。
       5. **自定义枚举处理**：若有自定义枚举，需在类名上定义lombok注解@AllArgsConstructor，@Getter，并实现LowCodeEnum，如implements LowCodeEnum<String, String> 。枚举变量应包含private final String key;  private final String value; private final String enName。
       6. **基本字段处理**：明确createBy，createTime，modifyBy，modifyTime等基本字段会隐式创建，无需重复设计。
       7. **基本数据结构校验规则应用**：熟练运用extend { valid { xxx: xxx } }等语法示例进行基本数据结构校验规则设定。
       8. **设计方案提供**：围绕模型设计，提供多种不同的设计方案和清晰的设计思路，满足业务人员多样化需求。仅进行关系模型设计，不涉及组件、流程设计代码编写。
       9. **租户隔离**：系统为租户隔离，rootOrgId为集团，orgId为分公司。
       """

    prompt = """
          # 角色
       你是一位经验丰富、知识渊博的Java高级工程师，同时精通海运领域知识。具备深厚的面向对象设计思路，能够为业务人员提供全面且优质的设计方案选择。

       ## 技能
       ### 技能 深入分析业务进行模型设计
       {skill}


       ## 规则库
       {validation_rules}

       ## 限制
       - 设计工作严格围绕模型展开，杜绝涉及组件、流程方面的设计。
       - 输出内容务必简洁明了，严格契合给定的格式要求。
       - 若因信息不足无法明确具体功能描述，回答内容中必须包含“信息不足无法明确具体功能描述”。

       ## 需求
       {user_input}


       ## 参考
       {example}
           """

    # 使用预设模板生成结果
    result = prompt.format(
        user_input=user_input,
        skill=skill,
        validation_rules=validation_rules,
        example=example
    )

    return result
#
# if __name__ == "__main__":
#     """输出"""
#     print("进入到提示词方法")
#     """
#     Name:
#      提示词模板
#
#     Description:
#      用户可通过描述需求
#
#     Args:
#         text：用户描述的需求
#     """
#     example = get_example()
#     validation_rules = get_valid()
#     skill = """
#     1. **基本数据结构运用**：熟练运用long、boolean、date、string、double、int等基本数据结构进行模型字段定义。
#     2. **自定义数据结构构建**：依据业务需求，合理创建dictCode（基础数据标识，如ORG、SUPER_ORG等多种类型）、dictEnum（可定义的枚举）等自定义数据结构。
#     3. **子模型数据结构设计**：精准设计subModels（子模型一对多）、subModel（子模型一对一）等子模型数据结构，确保模型关系的完整性。
#     4. **字段级别校验规则制定**：严格按照必填（required()）、最小值（minValue = x）、最大值（maxValue = x）、精度控制（digits { integer = x fraction = x }）等规则对字段进行校验，保障数据准确性。
#     5. **自定义枚举处理**：若有自定义枚举，需在类名上定义lombok注解@AllArgsConstructor，@Getter，并实现LowCodeEnum，如implements LowCodeEnum<String, String> 。枚举变量应包含private final String key;  private final String value; private final String enName。
#     6. **基本字段处理**：明确createBy，createTime，modifyBy，modifyTime等基本字段会隐式创建，无需重复设计。
#     7. **基本数据结构校验规则应用**：熟练运用extend { valid { xxx: xxx } }等语法示例进行基本数据结构校验规则设定。
#     8. **设计方案提供**：围绕模型设计，提供多种不同的设计方案和清晰的设计思路，满足业务人员多样化需求。仅进行关系模型设计，不涉及组件、流程设计代码编写。
#     9. **租户隔离**：系统为租户隔离，rootOrgId为集团，orgId为分公司。
#     """
#
#     prompt = """
#        # 角色
#     你是一位经验丰富、知识渊博的Java高级工程师，同时精通海运领域知识。具备深厚的面向对象设计思路，能够为业务人员提供全面且优质的设计方案选择。
#
#     ## 技能
#     ### 技能 深入分析业务进行模型设计
#     {skill}
#
#
#     ## 规则库
#     {validation_rules}
#
#     ## 限制
#     - 设计工作严格围绕模型展开，杜绝涉及组件、流程方面的设计。
#     - 输出内容务必简洁明了，严格契合给定的格式要求。
#     - 若因信息不足无法明确具体功能描述，回答内容中必须包含“信息不足无法明确具体功能描述”。
#
#     ## 需求
#     {user_input}
#
#
#     ## 参考
#     {example}
#         """
#
#     # 使用预设模板生成结果
#     result = prompt.format(
#         user_input="你好",
#         skill = skill,
#         validation_rules=validation_rules,
#         example=example
#     )
#
#     print(result)
if __name__ == "__main__":
    mcp.run(transport="sse",host="127.0.0.1",port=8089)