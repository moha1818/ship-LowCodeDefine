## 船东模型示例
# 模型1，最全模型订舱：
```
package org.dzg.ship.core.app.generator.booking

import com.dzg.lowcode.dsl.LowCodeRegistryBuilder
import com.dzg.ship.base.api.enums.BooleanEnum
import com.dzg.ship.base.api.enums.SpecialBooleanEnum
import com.dzg.ship.base.api.generate.enums.CargoTypeEnum
import com.dzg.ship.component.dict.api.enums.DictTypeEnum
import org.dzg.ship.core.api.enums.*
import org.dzg.ship.core.app.generator.basic.LowCodeDefineBuilder


/**
 * EDI通道配置定义
 */
object BookingInfoDefine {
    private const val MODEL_NAME = "BookingInfo"

    @JvmStatic
    fun main(args: Array<String>) {
        val registryBuilder = LowCodeDefineBuilder.builder("booking")

        models(registryBuilder)

        registryBuilder.build().generate()
    }

    @JvmStatic
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
                            dict("podCallId", "POD挂港港口", DictTypeEnum.VOYAGE_PORT_CALL.name) {
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
                            }
                            dictCode("hsCode", "HS CODE", DictTypeEnum.HS_CODE.name) {
                                valid {
                                    required()
                                }
                            }
                            long("count", "件数") {
                                extend {
                                    valid {
                                        required()
                                    }
                                }
                            }
                            dictCode("packageId", "包装类型", DictTypeEnum.PACKAGE.name) {
                                valid {
                                    required()
                                }
                            }
                            string("packageDesc", "包装类型描述", 11)
                            double("grossWeight", "毛重（KGS）") {
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
                            double("volume", "体积（CBM）") {
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
                            double("netWeight", "净重（KGS）") {
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
                            string("productName", "品名", 4000) {
                                extend {
                                    valid {
                                        required()
                                    }
                                }
                            }
                            string("content", "打单内容", 4000) {
                                extend {
                                    valid {
                                        required()
                                    }
                                }
                            }
                            string("mark", "唛头", 4000)
                            subModel(
                                "dangerousGoodsInfo",
                                "危险品货物信息",
                                "BookingDangerousGoodsInfo",
                                "bookingCargoId"
                            ) {
                                fields {
                                    string("dangerClass", "危险品类别", 50) {
                                        extend { valid { required() } }
                                    }
                                    string("secondaryDangerClass", "副危险品类别", 50)
                                    string("unNo", "联合国编号", 20) {
                                        extend { valid { required() } }
                                    }
                                    string("boilingPointValue", "沸点值", 50)
                                    string("boilingPointUnit", "沸点单位", 50)
                                    string("flashPointValue", "闪点值", 50)
                                    string("flashPointUnit", "闪点单位", 50)
                                    string("label", "标签", 50)
                                    dictEnum("marinePollutant", "海洋污染物", SpecialBooleanEnum.ENABLE)
                                    string("medicalEmergencyGuideline", "医疗急救指南号", 50)
                                    dictEnum("packagingCategory", "包装类", PackingGroupEnum.I) {
                                        valid { required() }
                                    }
                                    int("outerPackageCount", "外包装件数") {
                                        extend {
                                            valid {
                                                required()
                                                minValue = 0
                                            }
                                        }
                                    }
                                    dictCode("outerPackage", "外包装类型", DictTypeEnum.PACKAGE.name) {
                                        valid {
                                            required()
                                        }
                                    }
                                    int("innerPackageCount", "内包装件数") {
                                        extend {
                                            valid {
                                                minValue = 0
                                            }
                                        }
                                    }
                                    dictCode("innerPackage", "内包装类型", DictTypeEnum.PACKAGE.name)
                                    /**
                                     *  todo LQ，EQ 选中后，危险品文件必须要有包装证书
                                     */
                                    dictEnum("limitExemption", "是否限量/免除量", LimitExemptionEnum.NON)
                                    string("emergencyActionCode", "应急措施编号EMS", 50)
                                    string("correctTransportName", "正确运输品名", 4000) {
                                        extend { valid { required() } }
                                    }
                                    string("chemicalName", "化学品名", 4000)
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
                                    double("netWeight", "净重") {
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
                                    string("emergencyContact", "紧急联系人", 50)
                                    string("emergencyContactPhone", "应急联系电话", 50)
                                    string("communicationCode", "通讯方式代码", 50)
                                    string("mapGroup", "MAP组", 4000)
                                    string("offerorNameOrContractNumber", "报价人名称或合同", 500)
                                    string("cargoPackagingDescription", "货物包装描述", 500)
                                    string("netExplosiveContent", "净爆炸物含量", 500)
                                    string("dgRemark", "危险品备注", 500)
                                }
                            }
                        }
                    }
                    subModel("totalGoodsInfo", "订舱货物总信息", "BookingTotalGoodsInfo", "bookingId") {
                        fields {
                            string("goodsDesc", "货描描述", 4000)
                            dictCode("hsCode", "HS CODE", DictTypeEnum.HS_CODE.name) {
                                valid { required() }
                            }
                            long("count", "件数") {
                                extend {
                                    valid {
                                        required()
                                    }
                                }
                            }
                            dictCode("packageId", "包装类型", DictTypeEnum.PACKAGE.name) {
                                valid { required() }
                            }
                            string("packageDesc", "包装类型描述", 11)
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
                            double("volume", "体积") {
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
                            string("productName", "品名", 4000) {
                                extend { valid { required() } }
                            }
                            string("mark", "唛头", 4000)
                            double("netWeight", "净重（KGS）") {
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
                        }
                    }
                    subModels("containerInfos", "订舱箱信息", "BookingContainerInfo", "bookingId") {
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
                            dictCode("packageId", "包装类型", DictTypeEnum.PACKAGE.name)
                            dictCode("containerNo", "集装箱号", DictTypeEnum.CONTAINER.name)
                            dictEnum("containerStatus", "集装箱状态", ContainerStatusEnum.APPLY)
                            subModels(
                                "cargoTypes",
                                "货物类型信息",
                                "ContainerSubCargoTypeInfo",
                                "containerTypeInfoId"
                            ) {
                                fields {
                                    dictEnum("cargoType", "货物类型", CargoTypeEnum.GENERAL)
                                }
                            }
                            subModels(
                                "cargoInfos",
                                "订舱集装箱货物信息",
                                "BookingContainerCargoInfo",
                                "bookingContainerId"
                            ) {
                                fields {
                                    dictEnum("cargoType", "货物类型", CargoTypeEnum.DANGER) {
                                        valid { required() }
                                    }
                                    long("count", "件数") {
                                        extend {
                                            valid {
                                                required()
                                            }
                                        }
                                    }
                                    dictCode("packageId", "包装类型", DictTypeEnum.PACKAGE.name) {
                                        valid {
                                            required()
                                        }
                                    }
                                    string("packageDesc", "包装类型描述", 11)
                                    double("grossWeight", "毛重（KGS）") {
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
                                    double("volume", "体积（CBM）") {
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
                                    string("productName", "品名", 4000) {
                                        extend {
                                            valid {
                                                required()
                                            }
                                        }
                                    }
                                }
                            }
                            subModel(
                                "referContainerInfo",
                                "冷箱信息",
                                "BookingContainerReferInfo",
                                "bookingContainerId"
                            ) {
                                fields {
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
                            subModel(
                                "specialContainerInfo",
                                "特种箱信息",
                                "BookingContainerSpecialInfo",
                                "bookingContainerId"
                            ) {
                                fields {
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
                                                required()
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
                                                required()
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
                                                required()
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
                                                required()
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
                                                required()
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
                                                required()
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
                            string("containerOwner", "箱主", 50)
                            string("sealNo1", "封号1", 50)
                            string("sealNo2", "封号2", 50)
                            string("sealNo3", "封号3", 50)
                            string("vin1", "车架号1", 50)
                            string("vin2", "车架号2", 50)
                            string("vin3", "车架号3", 50)
                            string("contactName", "联系人", 100)
                            string("contactInfo", "联系方式", 100)
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
                            double("grossWeight", "毛重", 3) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 15
                                            fraction = 3
                                        }
                                    }
                                }
                            }
                            double("tareWeight", "箱皮重（KGS）", 3) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 15
                                            fraction = 3
                                        }
                                    }
                                }
                            }
                            double("netWeight", "净重（KGS）") {
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
                            long("count", "件数", 0)
                            dictCode("packageId", "包装类型", DictTypeEnum.PACKAGE.name)
                            string("packageDesc", "包装类型描述", 11)
                            double("volume", "体积（CBM）") {
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
                            dictEnum("isOwn", "是否自有箱", BooleanEnum.ENABLE)
                            date("pickupTime", "提箱时间")
                            date("entryTime", "进场时间")
                            dictCode("pickupLocationId", "提箱点", DictTypeEnum.WHARF.name)
                            dictCode("returnLocationId", "还箱点", DictTypeEnum.WHARF.name)
                        }
                    }
                    subModels("contacts", "订舱联系人", "BookingContact", "bookingId") {
                        fields {
                            dict("customerId", "客商ID", DictTypeEnum.CUSTOMER.name) {
                                valid {
                                    required()
                                }
                            }
                            dictEnum("contactType", "联系人类型", BookingContactTypeEnum.SHIPPER)
                            string("companyName", "公司名称", 100)
                            string("companyAddress", "公司地址", 100) {
                                extend {
                                    valid {
                                        required()
                                    }
                                }
                            }
                            dictCode("countryId", "国家", DictTypeEnum.COUNTRY.name)
                            dictCode("cityId", "城市", DictTypeEnum.REGION.name)
                            string("email", "邮箱", 100) {
                                extend { valid { email() } }
                            }
                            string("contactName", "联系人名称", 100)
                            string("contactTel", "联系人电话", 100)
                            string("zipCode", "邮编", 10)
                            string("content", "打单内容", 4000)
                            string("taxRegistrationNo", "税务登记号", 50) {
                                extend { valid { english() } }
                            }
                            dictEnum("sameAsConsignee", "SAME AS CONSIGNEE", BooleanEnum.ENABLE)
                        }
                        indexes {
                            uq("uq_booking_contact", "bookingId,contactType")
                        }
                    }
                    string("scacCode", "SCAC CODE", 20)
                    string("contractNo", "协议号", 50) {
                        extend { valid { required() } }
                    }
                    dictEnum("sendType", "出单方式", SendTypeEnum.MBL) {
                        valid { required() }
                    }
                    dictEnum("billType", "单证类型", BillTypeEnum.MBL) {
                        valid { required() }
                    }
                    dictEnum("transferTerms", "运输条款", TransferTermsEnum.CY_CY) {
                        valid { required() }
                    }
                    string("loadingRequirements", "装载要求", 200)
                    string("bookingRemark", "订舱备注", 200)
                    string("operateRemark", "操作备注", 4000)
                    string("shippingInformationRemark", "补料备注/SI备注", 4000)
                    /**
                     * todo 进港代码映射关系自动匹配得出
                     */
                    string("importCode", "进港代码", 50)
                    dictEnum("billCabinReturnStatus", "提单退舱状态", BillCabinReturnStatusEnum.SUCCESS) {
                        nullable()
                        maxLength = 10
                    }
                    dictEnum("bookingCabinReturnStatus", "订舱退舱状态", BookingCabinReturnStatusEnum.APPLY) {
                        nullable()
                        maxLength = 10
                    }
                    string("billOfLadingPendingReason", "提单pending原因", 200)
                    boolean("isBillOfLadingPendingWarning", "是否提单pending告警", 0)
                    dictEnum("bookingRejectReason", "订舱拒绝原因", BookingRejectReasonEnum.CONSIGNEE_INFO) {
                        nullable()
                        maxLength = 20
                    }
                    string("bookingRejectOtherReason", "订舱拒绝其他原因", 200)
                    string("bookingCabinRejectReason", "退舱拒绝原因", 0)
                    string("bookingCabinReason", "退舱原因", 0)
                    int("changeShipCount", "改船次数", 0)
                    dictEnum("changeShipReason", "改船原因", ChangeShipReasonEnum.OTHER) {
                        nullable()
                        maxLength = 10
                    }
                    string("freeTimeAgreement", "freetime协议", 100)
                    int("signedCount", "签单份数", 3)
                    date("bookingDate", "订舱日期") {
                        extend { valid { required() } }
                    }
                    date("yardReceivingClosingTime", "截港时间")
                    date("departureTime", "开航时间") {
                        extend { valid { required() } }
                    }
                    string("hblNo", "HBL NO", 4000)
                    date("loadingTime", "装船时间")
                    date("shippingInformationTime", "提单补料时间")
                    string("billCreator", "制单人", 50)
                    date("billCreateTime", "制单时间")
                    date("billConfirmTime", "提单确认时间")
                    date("bookingCabinConfirmTime", "订舱舱位确认时间")
                    string("bookingCabinConfirmBy", "订舱舱位确认人", 50)
                    string("operator", "操作人", 50)
                    string("billConfirmEmail", "提单确认邮箱", 500)
                    string("bookingConfirmEmail", "订舱确认邮箱", 500)
                    string("operator", "操作人", 500)
                    date("operatorTime", "操作时间")
                    dict("reviewerUserId", "审单人", DictTypeEnum.STAFF.name) {
                        valid { required() }
                    }
                    date("reviewerTime", "审单时间") {
                        extend { valid { required() } }
                    }
                    boolean("isDeleted", "删除标志", 0)
                }
                indexes {
                }
                selectors {
                    selector("BlNos") {
                        equals("rootOrgId", "#{rootOrgId}", null, Long::class.javaObjectType)
                        inEquals("blNo", "#{blNo}", null, String::class.javaObjectType)
                    }
                    selector("BookingNos") {
                        equals("rootOrgId", "#{rootOrgId}", null, Long::class.javaObjectType)
                        inEquals("bookingNo", "#{bookingNo}", null, String::class.javaObjectType)
                    }
                }
            }
        }
    }
}
```

## 模型2，船期模型:
```
package org.dzg.ship.core.app.generator

import com.dzg.lowcode.config.condition.Expression
import com.dzg.lowcode.dsl.LowCodeRegistryBuilder
import com.dzg.ship.component.dict.api.enums.DictTypeEnum
import org.dzg.ship.core.api.enums.ApprovalEnum
import org.dzg.ship.core.api.enums.ApprovalStatusEnum
import org.dzg.ship.core.app.generator.basic.LowCodeDefineBuilder


object VoyageDefine {
    private const val MODEL_NAME = "Voyage"

    @JvmStatic
    fun main(args: Array<String>) {
        val registryBuilder = LowCodeDefineBuilder.builder(MODEL_NAME)

        models(registryBuilder)

        registryBuilder.build().generate()
    }

    @JvmStatic
    fun models(registryBuilder: LowCodeRegistryBuilder) {
        registryBuilder.models {
            model(MODEL_NAME, "船期") {
                fields {
                    long("rootOrgId", "集团公司ID", 0)
                    dict("flightId", "航班代码id", DictTypeEnum.FLIGHT.name) {
                        valid {
                            required()
                        }
                    }
                    dict("vesselCode", "船舶代码Code", DictTypeEnum.VESSEL.name) {
                        valid {
                            required()
                        }
                    }
                    string("preVoyno", "上一次航次", 10) {
                        extend {
                            valid {
                                english()
                            }
                        }
                    }
                    string("voyno", "航次", 10) {
                        extend {
                            valid {
                                required()
                                english()
                            }
                        }
                    }
                    string("nextVoyno", "下一次航次", 10) {
                        extend {
                            valid {
                                english()
                            }
                        }
                    }
                    dict("carrierCode", "承运人Code", DictTypeEnum.CARRIER.name) {
                        valid {
                            maxLength=1
                            required()
                        }
                    }

                    string("belongMonth", "归属月") {
                        extend {
                            valid {
//                                required()
                            }
                        }
                    }
                    string("belongWeek", "归属周") {
                        extend {
                            valid {
//                                required()
                            }
                        }
                    }
                    date("belongMonthTime", "归属月-ETZ+8") {
                        extend {
                            valid {
//                                required()
                            }
                        }
                    }
                    date("belongWeekTime", "归属周-ETZ+8") {
                        extend {
                            valid {
//                                required()
                            }
                        }
                    }
                    boolean("isDeleted", "删除标志", 0)
                    boolean("isEnable", "状态", 1)

                    subModels("VoyageOrgRela", "船期运营方", "VoyageOrgRela", "voyageId") {
                        fields {
                            dict("relaOrgId", "运营方", DictTypeEnum.ORG.name) {
                                valid {
                                    required()
                                }
                            }
                        }
                    }

                    subModels("${MODEL_NAME}PortCall", "挂港", "${MODEL_NAME}PortCall", "voyageId") {
                        fields {
                            dict("importHeadingId", "进口航向", DictTypeEnum.HEADING.name) {
                                valid {
                                    required()
                                }
                            }
                            dict("exportHeadingId", "出口航向", DictTypeEnum.HEADING.name) {
                                valid {
                                    required()
                                }
                            }
                            string("voynoE", "出口航次", 10) {
                                extend {
                                    valid {
                                        english()
                                    }
                                }
                            }
                            string("voynoI", "进口航次",10) {
                                extend {
                                    valid {
                                        english()
                                    }
                                }
                            }
                            dict("portId", "港口代码", DictTypeEnum.PORT.name) {
                                valid {
                                    required()
                                }
                            }
                            dict("wharfId", "码头代码", DictTypeEnum.WHARF.name) {
                                valid {
                                    required()
                                }
                            }
                            dict("agencyId", "船代代码", DictTypeEnum.AGENCY.name) {
                                valid {
//                                    required()
                                }
                            }

                            date("etaTime", "ETA UTC+8")
                            string("eta", "ETA",50)
                            date("etbTime", "ETB UTC+8")
                            string("etb", "ETB",50)
                            date("etdTime", "ETD UTC+8")
                            string("etd", "ETD",50)


                            double("pilotage", "引水(h)", 1) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 4
                                            fraction = 1
                                        }
                                        minValue = 0
                                        maxValue =1000
                                    }
                                }
                            }
                            double("terminalOperation", "码头作业(h)", 1) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 4
                                            fraction = 1
                                        }
                                        minValue = 0
                                        maxValue =1000
                                    }
                                }
                            }
                            int("distanceAtSea", "距离(海里)") {
                                extend {
                                    valid {
                                        minValue = 0
                                        maxValue = 29999
                                    }
                                }
                            }
                            double("seaSpeed", "时速(节)", 4) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 3
                                            fraction = 4
                                        }
                                        minValue = 0
                                        maxValue =100
                                    }
                                }
                            }
                            double("seaVoyage", "航程(h)", 1) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 4
                                            fraction = 1
                                        }
                                        minValue = 0
                                        maxValue =1000
                                    }
                                }
                            }
                            double("buffer", "Buffer(h)", 1) {
                                extend {
                                    valid {
                                        digits {
                                            integer = 4
                                            fraction = 1
                                        }
                                        minValue = 0
                                        maxValue =1000
                                    }
                                }
                            }

                            date("ataTime", "ATA UTC+8")
                            string("ata", "ATA",50)
                            date("atbTime", "ATB UTC+8")
                            string("atb", "ATB",50)
                            date("atdTime", "ATD UTC+8")
                            string("atd", "ATD",50)

                            boolean("isDeleted", "删除标志", 0)
                            boolean("isEnable", "状态", 1)
                            string("createBy", "创建者", 50)
                            date("createTime", "创建时间")
                            string("modifyBy", "修改人", 50)
                            date("modifyTime", "修改时间")
                            int("seqNum","顺序", 1)
                            subModels("${MODEL_NAME}PortCallOrgRela", "船期挂港运营方1-N", "${MODEL_NAME}PortCallOrgRela", "voyagePortCallId") {
                                fields {
                                    dict("relaOrgId", "运营方", DictTypeEnum.ORG.name) {
                                        valid {
                                            required()
                                        }
                                    }
                                }
                            }
                        }
                    }
                    subModels("${MODEL_NAME}Transship", "转船", "${MODEL_NAME}Transship", "voyageId") {
                        fields {
                            dict("voyagePortCallId", "一程船挂港id", DictTypeEnum.VOYAGE.name) {
                                valid {
                                    required()
                                }
                            }
                            dict("transshipVoyageId", "转船船期ID", DictTypeEnum.VOYAGE.name) {
                                valid {
                                    required()
                                }
                            }
                            dict("transshipPortCallId", "二程船挂港ID", DictTypeEnum.VOYAGE_PORT_CALL.name) {
                                valid {
                                    required()
                                }
                            }
                            dict("transshipPortId", "转船港口ID", DictTypeEnum.PORT.name) {
                                valid {
                                    required()
                                }
                            }
                            boolean("isDeleted", "删除标志", 0)
                        }
                        indexes {
                            idx("idx_transshipPortCallId", "transshipPortCallId")
                            idx("idx_transshipVoyageId", "transshipVoyageId")
                        }
                    }
                }

                indexes {
                    idx("idx_voyage_carrier", "rootOrgId,carrierCode")
                    idx("idx_voyage_flightId", "rootOrgId,flightId")
                    uq("idx_voyage_vesselId_voyno", "rootOrgId,vesselCode,voyno")
                }

                selectors {
                    selector("getVoyageByVesselId") {
                        equals("rootOrgId", "#{rootOrgId}", null, Long::class.javaObjectType)
                        equals("vesselCode", "#{vesselCode}",  Expression.skipNullOn("vesselCode"), String::class.javaObjectType)
                        equals("voyno", "#{voyno}",  Expression.skipNullOn("voyno"), String::class.javaObjectType)
                        equals(
                            "isEnable",
                            "#{isEnable}",
                            Expression.skipNullOn("isEnable"),
                            Boolean::class.javaObjectType
                        )
                    }
                }
            }
        }
    }
}
```

