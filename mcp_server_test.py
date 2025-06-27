from fastmcp import FastMCP


mcp = FastMCP("LowCodeDefine-test")
#
# example_path = Path("./example.md").resolve()
# if example_path.exists():
#     # Use a file:// URI scheme
#     readme_resource = FileResource(
#         uri=f"file://{example_path.as_posix()}",
#         path=example_path, # Path to the actual file
#         name="example",
#         description="这个是一个模型示例文件",
#         mime_type="text/markdown",
#         tags={"documentation"}
#     )
#     mcp.add_resource(readme_resource)
#
# valid_path = Path("./Valid.md").resolve()
# if valid_path.exists():
#     # Use a file:// URI scheme
#     valid_resource = FileResource(
#         uri=f"file://{valid_path.as_posix()}",
#         path=valid_path,  # Path to the actual file
#         name="valid",
#         description="这是一个所有验证规则文件",
#         mime_type="text/markdown",
#         tags={"documentation"}
#     )
#     mcp.add_resource(valid_resource)


@mcp.tool()
def add(a: int, b: int) -> str:
    """Add two numbers"""
    return a + b


@mcp.resource("config://valid")
def get_valid() -> str:
    print("加载验证规则文档")
    """加载验证规则文档"""
    with open('Valid.md', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

@mcp.resource("config://example")
def get_example() -> str:
    print("加载模型生成示例")
    """加载模型生成示例"""
    with open('example.md', 'r', encoding='utf-8') as file:
        text = file.read()
    return text

@mcp.prompt()
def prompt(text: str) -> str:
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
    prompt = """
   # 角色
你是一位经验丰富、知识渊博的Java高级工程师，同时精通海运领域知识。具备深厚的面向对象设计思路，能够为业务人员提供全面且优质的设计方案选择。

## 技能
### 技能 深入分析业务进行模型设计
1. **基本数据结构运用**：熟练运用long、boolean、date、string、double、int等基本数据结构进行模型字段定义。
2. **自定义数据结构构建**：依据业务需求，合理创建dictCode（基础数据标识，如ORG、SUPER_ORG等多种类型）、dictEnum（可定义的枚举）等自定义数据结构。
3. **子模型数据结构设计**：精准设计subModels（子模型一对多）、subModel（子模型一对一）等子模型数据结构，确保模型关系的完整性。
4. **字段级别校验规则制定**：严格按照必填（required()）、最小值（minValue = x）、最大值（maxValue = x）、精度控制（digits { integer = x fraction = x }）等规则对字段进行校验，保障数据准确性。
5. **自定义枚举处理**：若有自定义枚举，需在类名上定义lombok注解@AllArgsConstructor，@Getter，并实现LowCodeEnum，如implements LowCodeEnum<String, String> 。枚举变量应包含private final String key;  private final String value; private final String enName。
6. **基本字段处理**：明确createBy，createTime，modifyBy，modifyTime等基本字段会隐式创建，无需重复设计。
7. **基本数据结构校验规则应用**：熟练运用extend { valid { xxx: xxx } }等语法示例进行基本数据结构校验规则设定。
8. **设计方案提供**：围绕模型设计，提供多种不同的设计方案和清晰的设计思路，满足业务人员多样化需求。仅进行关系模型设计，不涉及组件、流程设计代码编写。
9. **租户隔离**：系统为租户隔离，rootOrgId为集团，orgId为分公司。

## 限制
- 设计工作严格围绕模型展开，杜绝涉及组件、流程方面的设计。
- 输出内容务必简洁明了，严格契合给定的格式要求。
- 若因信息不足无法明确具体功能描述，回答内容中必须包含“信息不足无法明确具体功能描述”。

## 参考
```
## 参考
package org.dzg.ship.core.app.generator.booking

import com.dzg.lowcode.dsl.LowCodeRegistryBuilder
import com.dzg.ship.base.api.enums.BooleanEnum
import com.dzg.ship.base.api.enums.SpecialBooleanEnum
import com.dzg.ship.base.api.generate.enums.CargoTypeEnum
import com.dzg.ship.component.dict.api.enums.DictTypeEnum
import org.dzg.ship.core.api.enums.*
import org.dzg.ship.core.app.generator.basic.LowCodeDefineBuilder

object BookingInfoDefine {
 private const val MODEL_NAME = "BookingInfo" @JvmStatic
 fun main(args: Array) {  val registryBuilder = LowCodeDefineBuilder.builder("booking")  models(registryBuilder)  registryBuilder.build().generate()  } @JvmStatic
 fun models(registryBuilder: LowCodeRegistryBuilder) {
 registryBuilder.models {
     model(MODEL_NAME, "订舱信息") {
         fields {
             long("rootOrgId", "集团公司ID", 0)
             dictCode("orgId", "公司ID", DictTypeEnum.ORG.name)
             dictEnum("source", "单据来源", BookingSourceEnum.CREATED) {
                 valid {
                     required()
                     maxLength = 10
                 }
             }
             dictEnum("bookingType", "订舱类型", BookingTypeEnum.FCL) {
                 valid { required() }
             }
             dictEnum("prevBillOfLadingStatus", "上一个提单状态", BillOfLadingStatusEnum.COMMIT) {
                 nullable()
                 maxLength = 20
             }
             dictEnum("billOfLadingStatus", "提单状态", BillOfLadingStatusEnum.COMMIT) {
                 nullable()
                 maxLength = 20
             }
             dictEnum("billOfLadingImportStatus", "进口提单状态", BillOfLadingImportStatusEnum.REPLACED_BILL) {
                 valid { required() }
                 maxLength = 15
             }
             dictEnum("bookingStatus", "订舱状态", BookingStatusEnum.WAIT) {
                 valid { required() }
                 maxLength = 15
             }
             dictEnum("prevBookingStatus", "上一个订舱状态", BookingStatusEnum.WAIT) {
                 valid { required() }
                 maxLength = 15
             }
             dictEnum("cabinStatus", "舱位状态", CabinStatusEnum.PENDING) {
                 nullable()
                 maxLength = 15
             }
             dictEnum("isLock", "是否锁单", BooleanEnum.DISABLE)
             string("bookingNo", "订舱号", 50) {
                 extend { valid { required() } }
             }
             string("blNo", "提单号", 50) {
                 extend { valid { required() } }
             }
             string("totalBookingNo", "总单号", 50) {
                 extend { valid { required() } }
             }
             dictEnum("mergeBillSign", "并单标记", MergeBillSignEnum.SUB) {
                 nullable()
             }
             dictEnum("splitBillSign", "拆单标记", SplitBillSignEnum.SUB) {
                 nullable()
                 maxLength = 10
             }
             dictEnum("mergeSplitBillSign", "并拆单标记", MergeSplitBillSignEnum.MERGE) {
                 nullable()
                 maxLength = 10
             }
             dict("voyageId", "船期ID", DictTypeEnum.VOYAGE.name) {
                 valid { required() }
             }
             string("vessel", "船名", 50) {
                 extend { valid { required() } }
             }
             string("voyno", "航次", 30) {
                 extend { valid { required() } }
             }
             dict("routeId", "航线代码", DictTypeEnum.ROUTE.name) {
                 valid {
                     required()
                 }
             }
             string("ctnDesc", "箱型箱量描述", 1000) {
                 extend { valid { required() } }
             }
             long("teu", "TEU", 0)
             string("voyageDesc", "中转船期描述", 50) {
                 extend { valid { required() } }
             }
             string("transitVoyageDesc", "中转船期描述", 500) {
                 extend { valid { required() } }
             }
             dictEnum("isTransitPort", "是否中转港", BooleanEnum.DISABLE)
             subModels("vesselSchedulePorts", "船期挂港港口信息", "BookingVesselSchedulePortInfo", "bookingId") {
                 fields {
                     int("seqNum", "程次", 1)
                     dict("portId", "港口id", DictTypeEnum.PORT.name) {
                         valid { required() }
                     }
                     dict("portCallId", "挂港港口", DictTypeEnum.VOYAGE_PORT_CALL.name) {
                         valid { required() }
                     }
                     dict("voyageId", "船期ID", DictTypeEnum.VOYAGE.name) {
                         valid { required() }
                     }
                     string("vessel", "船名", 50) {
                         extend { valid { required() } }
                     }
                     string("voyno", "航次", 30) {
                         extend { valid { required() } }
                     }
                     dict("routeId", "航线代码", DictTypeEnum.ROUTE.name) {
                         valid {
                             required()
                         }
                     }
                 }
             }
             subModel("portInfo", "港口信息", "BookingPortInfo", "bookingId") {
                 fields {
                     dict("porId", "收货地", DictTypeEnum.PORT.name) {
                         valid { required() }
                     }
                     dict("polId", "装货港", DictTypeEnum.PORT.name) {
                         valid { required() }
                     }
                     dict("polCallId", "POL挂港港口", DictTypeEnum.VOYAGE_PORT_CALL.name) {
                         valid { required() }
                     }
                     dict("podId", "卸货港", DictTypeEnum.PORT.name) {
                         valid { required() }
                     }
                     dict("delId", "目的港", DictTypeEnum.PORT.name) {
                         valid { required() }
                     }
                     dict("signLocationId", "签单地点", DictTypeEnum.PORT.name) {
                         valid { required() }
                     }
                     string("porDesc", "收货地描述", 50) {
                         extend { valid { required() } }
                     }
                     string("polDesc", "装货港描述", 50) {
                         extend { valid { required() } }
                     }
                     string("podDesc", "卸货港描述", 50) {
                         extend { valid { required() } }
                     }
                     string("delDesc", "目的港描述", 50) {
                         extend { valid { required() } }
                     }
                 }
             }
             subModel("paymentInfo", "付费信息", "BookingPaymentInfo", "bookingId") {
                 fields {
                     dict("paymentLocationId", "付费地点", DictTypeEnum.PORT.name)
                     dict("payingCustomerId", "付费方", DictTypeEnum.CUSTOMER.name) {
                         valid { required() }
                     }
                     dict("thirdPaymentLocationId", "第三付费地", DictTypeEnum.PORT.name)
                     string("thirdPayerAddress", "第三付费方地址", 500)
                     dict("thirdPayerId", "第三付费方", DictTypeEnum.CUSTOMER.name)
                     string("thirdPayerEmail", "第三付费方邮箱", 100)
                     string("thirdPayerDescription", "第三付费方描述", 500)
                     dict("paymentMethodConfigId", "付费方式", DictTypeEnum.PAYMENT_METHOD.name)
                 }
             }
             subModels("bookingNodes", "订舱链路", "bookingNodeInfo", "bookingId") {
                 fields {
                     dictEnum("node", "节点类型", BookingNodeTypeEnum.BOOKING_SUBMIT) {
                         valid { required() }
                     }
                     string("createBy", "创建者", 50)
                     date("createTime", "创建时间")
                 }
             }
             subModels("bookingSplitRelations", "拆单关系", "BookingSplitRelation", "bookingId") {
                 fields {
                     long("subSplitBookingId", "拆单关联ID", 0)
                 }
             }
             subModel("bookingMergeInfo", "并单信息", "BookingMergeInfo", "bookingId") {
                 fields {
                     long("mainMergeBookingId", "并单主单", 0)
                     subModels(
                         "bookingMergeRelations",
                         "并单关系",
                         "BookingMergeRelation",
                         "bookingMergeRelationId"
                     ) {
                         fields {
                             long("subMergeBookingId", "并单关联ID", 0)
                             long("bookingId", "主单关联ID", 0)
                         }
                     }
                 }
             }
             subModels("containerTypeInfos", "订舱箱型箱量", "BookingContainerTypeInfo", "bookingId") {
                 fields {
                     dictEnum("ctnSize", "尺寸", ContainerSizeEnum.S_20) {
                         maxLength = 2
                         valid { required() }
                     }
                     dictCode("ctnType", "箱型", DictTypeEnum.SIZE_CTN_TYPE.name) {
                         valid {
                             maxLength = 4
                             required()
                         }
                     }
                     long("ctnQty", "数量") {
                         extend {
                             valid {
                                 required()
                                 minValue = 1
                             }
                         }
                     }
                     double("grossWeight", "毛重") {
                         extend {
                             valid {
                                 required()
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("weight", "总重量）") {
                         extend {
                             valid {
                                 required()
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     subModels(
                         "cargoTypes",
                         "货物类型信息",
                         "ContainerTypeSubCargoTypInfo",
                         "containerTypeInfoId"
                     ) {
                         fields {
                             dictEnum("cargoType", "货物类型", CargoTypeEnum.GENERAL)
                         }
                     }
                 }
             }
             subModels("referContainerInfos", "箱型描述-冷箱信息", "ContainerTypeSubReferInfo", "bookingId") {
                 fields {
                     dictEnum("ctnSize", "尺寸", ContainerSizeEnum.S_20) {
                         maxLength = 2
                         valid { required() }
                     }
                     dictCode("ctnType", "箱型", DictTypeEnum.SIZE_CTN_TYPE.name) {
                         valid {
                             maxLength = 4
                             required()
                         }
                     }
                     long("ctnQty", "数量") {
                         extend {
                             valid {
                                 required()
                                 minValue = 1
                             }
                         }
                     }
                     double("temperature", "温度") {
                         extend { valid { required() } }
                     }
                     double("humidity", "湿度") {
                         extend {
                             valid {
                                 minValue = 0
                                 maxValue = 100
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("ventilationQuantity", "通风量")
                 }
             }
             subModels(
                 "specialContainerInfos",
                 "箱型描述-特种箱信息",
                 "ContainerTypeSubSpecialInfo",
                 "bookingId"
             ) {
                 fields {
                     dictEnum("ctnSize", "尺寸", ContainerSizeEnum.S_20) {
                         maxLength = 2
                         valid { required() }
                     }
                     dictCode("ctnType", "箱型", DictTypeEnum.SIZE_CTN_TYPE.name) {
                         valid {
                             maxLength = 4
                             required()
                         }
                     }
                     long("ctnQty", "数量") {
                         extend {
                             valid {
                                 required()
                                 minValue = 1
                             }
                         }
                     }
                     double("length", "长（cm）") {
                         extend {
                             valid {
                                 required()
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("width", "宽（cm）") {
                         extend {
                             valid {
                                 required()
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("height", "高（cm）") {
                         extend {
                             valid {
                                 required()
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("weight", "货物重量（KGS）") {
                         extend {
                             valid {
                                 required()
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("frontOverhang", "前超（cm）") {
                         extend {
                             valid {
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("rearOverhang", "后超（cm）") {
                         extend {
                             valid {
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("topOverhang", "上超（cm）") {
                         extend {
                             valid {
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("leftOverhang", "左超（cm）") {
                         extend {
                             valid {
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("rightOverhang", "右超（cm）") {
                         extend {
                             valid {
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                     double("overWeight", "超重") {
                         extend {
                             valid {
                                 minValue = 0
                                 digits {
                                     integer = 15
                                     fraction = 3
                                 }
                             }
                         }
                     }
                 }
             }
             subModels("cargoInfos", "货物信息", "BookingCargoInfo", "bookingId") {
                 fields {
                     subModels("cargoTypes", "货物类型信息", "CargoInfoSubCargoTypInfo", "bookingCargoId") {
                         fields {
                             dictEnum("cargoType", "货物类型", CargoTypeEnum.GENERAL)
                         }

```
    """

    return prompt+f"\n\n{text}"

if __name__ == "__main__":
    mcp.run(transport="sse",host="127.0.0.1",port=8088)