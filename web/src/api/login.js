import request from '@/utils/request'

export function login(username, password) {
  return request({
    url: '/api-token-auth/',
    method: 'post',
    data: {
      username: username,
      password: password
    }
  })
}

export function getInfo(token) {
  return request({
    url: '/api/info',
    method: 'get',
    params: { token }
  })
}

export function logout() {
  return request({
    url: '/api/logout',
    method: 'post'
  })
}

export function products(data) {
  return request({
    // url: '/api/product/filterProducts/',
    url: '/api/product/',
    method: 'get',
    params: data
  })
}

// 护理字典
export function huliDict(data) {
  return request({
    url: '/api/huli/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 并发症字典
export function bingfazheng(data) {
  return request({
    url: '/api/bingfazheng/',
    method: 'get',
    params: {
      page: data.page,
      kind: data.kind
    }
  })
}

// 处置字典
export function chuzhiDict(data) {
  return request({
    url: '/api/chuzhi/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 透析类型字典
export function txtypedict(data) {
  return request({
    url: '/api/txType/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 用药字典
export function drug_dict(data) {
  return request({
    url: '/api/drug_dict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 用药新增
export function createdrug_dict(data) {
  return request({
    url: '/api/drug_dict/',
    method: 'post',
    data: data
  })
}

// 医嘱用药字典
export function mydrugDict(data) {
  return request({
    url: '/api/mydrugdict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      type: data.type,
      patientid: data.patientid
    }
  })
}

// 用药字典
export function drugDict(data) {
  return request({
    url: '/api/drugdict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 用药新增
export function createdrugDict(data) {
  return request({
    url: '/api/drugdict/',
    method: 'post',
    data: data
  })
}

// 耗材字典
export function mymaterialDict(data) {
  return request({
    url: '/api/mymaterialdict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 耗材字典
export function materialDict(data) {
  return request({
    url: '/api/materialdict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

export function users(data) {
  return request({
    url: '/api/user/',
    method: 'get',
    params: data
  })
}

// 医嘱字典
export function yz(data) {
  return request({
    url: '/api/yz/',
    method: 'get',
    params: data
  })
}

export function createProduct(data) {
  return request({
    url: '/api/product/',
    method: 'post',
    data: data
  })
}

export function updateProduct(data) {
  return request({
    url: `/api/product/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

export function schedules(data) {
  return request({
    url: '/api/schedule/',
    method: 'get',
    params: data
  })
}

export function patients(data) {
  return request({
    url: '/api/patient/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      patientid: data.patientid
    }
  })
}

export function createPatient(data) {
  return request({
    url: '/api/patient/',
    method: 'post',
    data: data
  })
}

export function updatePatient(data) {
  return request({
    url: `/api/patient/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 临时医嘱透析参数列表
export function yz_touxi(data) {
  return request({
    url: '/api/yz_touxi/',
    method: 'get',
    params: { register_id: data }
  })
}

// 临时医嘱透析参数新增
export function createyz_touxi(data) {
  return request({
    url: '/api/yz_touxi/',
    method: 'post',
    data: data
  })
}

// 临时医嘱透析参数修改
export function updateyz_touxi(data) {
  return request({
    url: `/api/yz_touxi/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 取一条临时医嘱透析参数
export function get_touxi(data) {
  return request({
    url: '/api/yz_touxi/',
    method: 'get',
    params: {
      register_id: data,
      doctor_state:　0
    }
  })
}

// 处置医嘱参数列表
export function yz_chuzhi(data) {
  return request({
    url: '/api/yz_chuzhi/',
    method: 'get',
    params: { register: data }
  })
}

// 处置医嘱新增
export function createyz_chuzhi(data) {
  return request({
    url: '/api/yz_chuzhi/',
    method: 'post',
    data: data
  })
}

// 处置医嘱修改
export function updateyz_chuzhi(data) {
  return request({
    url: `/api/yz_chuzhi/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 处置医嘱修改
export function deleteyz_chuzhi(data) {
  return request({
    url: `/api/yz_chuzhi/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 医嘱、耗材列表
export function Patient_yz(data) {
  return request({
    url: '/user/getPatient_yz/',
    method: 'get',
    params: {
      patientid: data.patientid,
      checked: data.checked,
      Startyear: data.Startyear,
      Endyear: data.Endyear
    }
  })
}

// 临时医嘱给药列表
export function yz_drug(data) {
  return request({
    url: '/api/yz_drug/',
    method: 'get',
    params: {
      register_id: data.registerid,
      Startyear: data.Startyear,
      Endyear: data.Endyear
    }
  })
}
// 临时医嘱给药新增
export function createyz_drug(data) {
  return request({
    url: '/api/yz_drug/',
    method: 'post',
    data: data
  })
}

// 临时医嘱给药修改
export function updateyz_drug(data) {
  return request({
    url: `/api/yz_drug/` + data[0].id + `/`,
    method: 'put',
    data: data
  })
}

// 临时医嘱删除
export function deleteyz_drug(data) {
  return request({
    url: `/api/yz_drug/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 临时医嘱给药修改
export function updateyz_material(data) {
  return request({
    url: `/api/yzmaterial/` + data[0].id + `/`,
    method: 'put',
    data: data
  })
}

// 临时医嘱护理列表
export function yz_huli(data) {
  return request({
    url: '/api/yz_huli/',
    method: 'get',
    params: { register_id: data }
  })
}

// 临时医嘱护理新增
export function createyz_huli(data) {
  return request({
    url: '/api/yz_huli/',
    method: 'post',
    data: data
  })
}

// 临时医嘱护理修改
export function updateyz_huli(data) {
  return request({
    url: `/api/yz_huli/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 自备药患者列表
export function patient_Drug(data) {
  return request({
    url: '/api/patientDrug/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid,
      rq: data.rq
    }
  })
}

// 透前评估之登记信息
export function register_pres(data) {
  return request({
    url: '/api/register_pre/',
    method: 'get',
    params: {
      register_id: data.register_id
    }
  })
}

// 透前评估之修改
export function updateRegister_pre(data) {
  return request({
    url: `/api/register_pre/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析记录之透前信息patientDrug
export function Registers(data) {
  return request({
    url: '/api/register/',
    method: 'get',
    params: { register_id: data }
  })
}

// 医生工作平台患者登记列表
export function Register_Nur(data) {
  return request({
    url: '/api/register_nur/',
    method: 'get',
    params: {
      page: data.page,
      diseaseArea: data.diseaseArea,
      banci: data.banci,
      name: data.name,
      checked: data.checked
    }
  })
}

// 透析记录之治疗记录
export function Tx_treatRecs(data) {
  return request({
    url: '/api/tx_treatRecord/',
    method: 'get',
    params: { txrecord_id: data }
  })
}

// 透析记录之治疗记录新增
export function createtx_treatRec(data) {
  return request({
    url: '/api/tx_treatRecord/',
    method: 'post',
    data: data
  })
}

// 透析记录之治疗记录修改
export function updatetx_treatRec(data) {
  return request({
    url: `/api/tx_treatRecord/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析记录之透后情况
export function Tx_records(data) {
  return request({
    url: '/api/tx_record/',
    method: 'get',
    params: {
      register_id: data
    }
  })
}

// 透析记录之小结修改
export function updatetx_record(data) {
  return request({
    url: `/api/tx_record/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析记录之病情评估修改
export function updatetRegister(data) {
  return request({
    url: `/api/register/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析评估之列表
export function Tx_pinggu(data) {
  return request({
    url: '/api/tx_pinggu/',
    method: 'get',
    params: { register_id: data }
  })
}

// 透析评估新增
export function createtx_pinggu(data) {
  return request({
    url: '/api/tx_pinggu/',
    method: 'post',
    data: data
  })
}

// 透析评估之修改
export function updatetx_pinggu(data) {
  return request({
    url: `/api/tx_pinggu/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析评估删除
export function deletetx_pinggu(data) {
  return request({
    url: `/api/tx_pinggu/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 检验主记录之列表
export function lab_test_master(data) {
  return request({
    url: '/api/lab_test_master/',
    method: 'get',
    params: {
      patient_id: data.patientid,
      register_id: data.registerid
    }
  })
}

// 检验主记录update
export function updatelab_test_master(data) {
  return request({
    url: `/api/lab_test_master/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 检验主记录明细之列表
export function lab_test_result(data) {
  return request({
    url: '/api/lab_test_result/',
    method: 'get',
    params: { register_id: data }
  })
}

// 检验明细
export function lab_test_item(data) {
  return request({
    url: '/api/lab_test_item/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      fromdate: data.fromdate,
      todate: data.todate,
      patient_id: data.patientid,
      registerid: data.registerid,
      itemcode: data.itemcode
    }
  })
}

// 检验结果
export function lab_result(data) {
  return request({
    url: '/api/lab_result/',
    method: 'get',
    params: {
      masterid: data
    }
  })
}

// 检查主记录
export function exam_master(data) {
  return request({
    url: '/api/exam_master/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      fromdate: data.fromdate,
      todate: data.todate,
      patient_id: data.patientid
    }
  })
}

// 检查结果
export function exam_report(data) {
  return request({
    url: '/api/exam_report/',
    method: 'get',
    params: {
      masterid: data
    }
  })
}

// 药品申请列表
export function Apply_drugs(data) {
  return request({
    url: '/api/apply_drug/',
    method: 'get',
    data: data
  })
}

// 药品申请新增
export function createApply_drug(data) {
  return request({
    url: '/api/apply_drug/',
    method: 'post',
    data: data
  })
}

// 药品申请update
export function updateApply_drug(data) {
  return request({
    url: `/api/apply_drug/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// Apply_drug_total列表
export function Apply_drug_total(data) {
  return request({
    url: '/api/apply_drug_total/',
    method: 'get',
    params: {
      id: data
    }
  })
}

// Apply_drug_detail列表
export function Apply_drug_detail(data) {
  return request({
    url: '/api/apply_drug_detail/',
    method: 'get',
    params: {
      id: data.id,
      drugid: data.drugid
    }
  })
}

// 耗材申请列表
export function Apply_materials(data) {
  return request({
    url: '/api/apply_material/',
    method: 'get',
    data: data
  })
}

// 耗材申请新增
export function createApply_material(data) {
  return request({
    url: '/api/apply_material/',
    method: 'post',
    data: data
  })
}

// 耗材申请update
export function updateApply_material(data) {
  return request({
    url: `/api/apply_material/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// Apply_material_total列表
export function Apply_material_total(data) {
  return request({
    url: '/api/apply_material_total/',
    method: 'get',
    params: {
      id: data
    }
  })
}

// Apply_material_detail列表
export function Apply_material_detail(data) {
  return request({
    url: '/api/apply_material_detail/',
    method: 'get',
    params: {
      id: data.id,
      materialid: data.materialid
    }
  })
}


// 耗材列表
export function materials(data) {
  return request({
    url: '/api/material/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      type: data.type
    }
  })
}

// 耗材新增
export function createMaterial(data) {
  return request({
    url: '/api/material/',
    method: 'post',
    data: data
  })
}

// 耗材update
export function updateMaterial(data) {
  return request({
    url: `/api/material/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 耗材删除
export function deleteMaterial(data) {
  return request({
    url: `/api/material/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 药品新增
export function createDrug(data) {
  return request({
    url: '/api/drug/',
    method: 'post',
    data: data
  })
}

// 药品update
export function updateDrug(data) {
  return request({
    url: `/api/drug/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 药品删除
export function deleteDrug(data) {
  return request({
    url: `/api/drug/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 耗材库存列表
export function dep_materialStore(data) {
  return request({
    url: '/api/dep_materialStore/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      code: data.code
    }
  })
}

// 耗材出入列表
export function materialStocks(data) {
  return request({
    url: '/api/materialStock/',
    method: 'get',
    params: {
      status: data.status,
      page: data.page,
      fromdate: data.begindate,
      todate: data.enddate,
      name: data.name,
      type: data.type
    }
  })
}

// 耗材库存新增
export function createMaterialStock(data) {
  return request({
    url: '/api/materialStock/',
    method: 'post',
    data: data
  })
}

// 耗材库存update
export function updateMaterialStock(data) {
  return request({
    url: `/api/materialStock/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 科室药品库存列表
export function drugStore(data) {
  return request({
    url: '/api/drugStore/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 自备药品库存列表
export function dep_drugStore(data) {
  return request({
    url: '/api/dep_drugStore/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      patientid: data.patientid
    }
  })
}

// 药品出入库列表
export function drugStocks(data) {
  return request({
    url: '/api/drugStock/',
    method: 'get',
    params: {
      page: data.page,
      status: data.status,
      name: data.name,
      fromdate: data.fromdate,
      todate: data.todate
    }
  })
}

// 药品库存新增
export function createDrugStock(data) {
  return request({
    url: '/api/drugStock/',
    method: 'post',
    data: data
  })
}

// 药品库存update
export function updateDrugStock(data) {
  return request({
    url: `/api/drugStock/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 自备药出入库列表
export function drugStocks_Person(data) {
  return request({
    url: '/api/drugStock_Person/',
    method: 'get',
    params: {
      page: data.page,
      status: data.status,
      name: data.name,
      code: data.code,
      fromdate: data.fromdate,
      todate: data.todate,
      patientid: data.patientid
    }
  })
}

// 病例首页
export function front_page(data) {
  return request({
    url: '/api/front_page/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 病例首页update
export function updatefront_page(data) {
  return request({
    url: `/api/front_page/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 手术记录
export function operations(data) {
  return request({
    url: '/api/operation/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 首次病程
export function firstDiseaseDurations(data) {
  return request({
    url: '/api/fdd/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 首次病程新增
export function createFirstDiseaseDuration(data) {
  return request({
    url: '/api/fdd/',
    method: 'post',
    data: data
  })
}

// 首次病程update
export function updateFirstDiseaseDuration(data) {
  return request({
    url: `/api/fdd/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 原发病字典
export function yfdisease(data) {
  return request({
    url: '/api/yfdisease/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 原发病新增
export function createYfdisease(data) {
  return request({
    url: '/api/yfdisease/',
    method: 'post',
    data: data
  })
}

// 原发病update
export function updateYfdisease(data) {
  return request({
    url: `/api/yfdisease/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 原发病删除
export function deleteYfdisease(data) {
  return request({
    url: `/api/yfdisease/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 病理字典
export function bingli(data) {
  return request({
    url: '/api/bingli/',
    method: 'get',
    params: {
      page: data.page,
      id: data.id,
      name: data.name
    }
  })
}
// 病理新增
export function createBingli(data) {
  return request({
    url: '/api/bingli/',
    method: 'post',
    data: data
  })
}

// 病理update
export function updateBingli(data) {
  return request({
    url: `/api/bingli/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 病理删除
export function deleteBingli(data) {
  return request({
    url: `/api/bingli/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}


// 转归类型字典
export function zgtype(data) {
  return request({
    url: '/api/zgtype/',
    method: 'get',
    params: {
      page: data.page
    }
  })
}

// 转归原因字典
export function zgreason(data) {
  return request({
    url: '/api/zgreason/',
    method: 'get',
    params: {
      page: data.page
    }
  })
}

// 患者转归
export function pat_zhuangui(data) {
  return request({
    url: '/api/pat_zhuangui/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid
    }
  })
}

// 患者转归新增
export function createPat_zhuangui(data) {
  return request({
    url: '/api/pat_zhuangui/',
    method: 'post',
    data: data
  })
}

// 患者转归update
export function updatePat_zhuangui(data) {
  return request({
    url: `/api/pat_zhuangui/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 患者转归删除
export function deletePat_zhuangui(data) {
  return request({
    url: `/api/pat_zhuangui/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 内瘘症状字典
export function neilou(data) {
  return request({
    url: '/api/neilou/',
    method: 'get',
    params: {
      page: data.page
    }
  })
}

// 导管症状字典
export function daoguan(data) {
  return request({
    url: '/api/daoguan/',
    method: 'get',
    params: {
      page: data.page
    }
  })
}

// 身体症状字典
export function shenti(data) {
  return request({
    url: '/api/shenti/',
    method: 'get',
    params: {
      page: data.page
    }
  })
}

// 预交金余额
export function prepaybalance(data) {
  return request({
    url: '/api/prepaybalance/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 结算
export function createOutp_master_jiesuan(data) {
  return request({
    url: '/api/outp_master_jiesuan/',
    method: 'post',
    data: data
  })
}

// 判断结算日期是否交叉
export function getTimeIntersect(data) {
  return request({
    url: '/user/getTimeIntersect/',
    method: 'get',
    params: {
      startdate: data.startdate,
      enddate: data.enddate,
      patientid: data.patientid
    }
  })
}

// 获取患者费用信息
export function patientfee(data) {
  return request({
    url: '/api/patientfee/',
    method: 'get',
    params: {
      registerid: data.registerid,
      patientid: data.patientid
    }
  })
}

// 耗材库存状况
export function getMaterialStock(data) {
  return request({
    url: '/api/getMaterialStock/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      start: data.begindate,
      end: data.enddate
    }
  })
}

// 收费药库存状况
export function getDrugStock(data) {
  return request({
    url: '/api/getDrugStock/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      code: data.code,
      start: data.begindate,
      end: data.enddate
    }
  })
}

// 将患者加入到register
export function PatientsToRegister(data) {
  return request({
    url: '/user/PatientsToRegister/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 将透析处方应用到yz_touxi和yz_drug
export function copyTotouxi_drug(data) {
  return request({
    url: '/user/copyTotouxi_drug/',
    method: 'get',
    params: {
      txtype: data.txtype,
      registerid: data.registerid
    }
  })
}

// 获取所有护士
export function getNurses(data) {
  return request({
    url: '/user/getNurses/',
    method: 'get',
    params: {}
  })
}

// 获取前一次或后一次收费记录
export function getProPostRecord(data) {
  return request({
    url: '/user/getProPostRecord/',
    method: 'get',
    params: {
      patientid: data.patientid,
      fromdate: data.fromdate,
      type: data.type
    }
  })
}

// 获取当前日期附近10条收费记录
export function getExpenseRecord(data) {
  return request({
    url: '/user/getExpenseRecord/',
    method: 'get',
    params: {
      patientid: data.patientid,
      fromdate: data.fromdate
    }
  })
}

// 收费药库存状况
export function getDrugAlert(data) {
  return request({
    url: '/user/getDrugAlert/',
    method: 'get',
    params: {}
  })
}

// 获取个人检验菜单
export function getLab_Test_Items(data) {
  return request({
    url: '/user/getLab_Test_Items/',
    method: 'get',
    params: {
      patientid: data.patientid
    }
  })
}

// 获取个人检查菜单
export function getExam_Items(data) {
  return request({
    url: '/user/getExam_Items/',
    method: 'get',
    params: {
      patientid: data.patientid
    }
  })
}

// 护士负责病床
export function bedNurses(data) {
  return request({
    url: '/api/bedNurse/',
    method: 'get',
    params: {
      page: 1
    }
  })
}

// 护士负责病床之create
export function createBedNurse(data) {
  return request({
    url: '/api/bedNurse/',
    method: 'post',
    data: data
  })
}

// 公司
export function Companys(data) {
  return request({
    url: '/api/Company/',
    method: 'get',
    params: {}
  })
}

// 公司修改
export function updateCompany(data) {
  return request({
    url: `/api/Company/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 公司分部自定义
export function subCompanyFields(data) {
  return request({
    url: '/api/subCompanyField/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 公司分部select
export function subComSelect(data) {
  return request({
    url: '/api/subComSelect/',
    method: 'get',
    params: {
      companyid: data.comid,
      subcomid: data.subcomid
    }
  })
}

// 公司分部
export function SubCompanys(data) {
  return request({
    url: '/api/SubCompany/',
    method: 'get',
    params: {
      name: data.name,
      code: data.code,
      kind: data.kind
    }
  })
}

// 公司分部新增
export function createSubCompany(data) {
  return request({
    url: '/api/SubCompany/',
    method: 'post',
    data: data
  })
}

// 公司分部修改
export function updateSubCompany(data) {
  return request({
    url: `/api/SubCompany/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 公司分部删除
export function deleteSubCompany(data) {
  return request({
    url: `/api/SubCompany/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 公司部门
export function departments(data) {
  return request({
    url: '/api/department/',
    method: 'get',
    params: {
      name: data.name,
      code: data.code,
      kind: data.kind
    }
  })
}

// 公司部门新增
export function createDepartment(data) {
  return request({
    url: '/api/department/',
    method: 'post',
    data: data
  })
}

// 公司部门修改
export function updateDepartment(data) {
  return request({
    url: `/api/department/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 公司部门删除
export function deleteDepartment(data) {
  return request({
    url: `/api/department/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 组织机构树
export function Organization(data) {
  return request({
    url: '/user/getOrganization',
    method: 'get',
    params: {
      code: data.code
    }
  })
}

// excel上传
export function uploadFile(data) {
  return request({
    url: '/upload/',
    method: 'post',
    data: data
  })
}

// excel下载
export function downloadFile(data) {
  return request({
    url: '/user/down_file/',
    method: 'post',
    responseType: 'blob',
    headers: {
      'Content-Type': 'application/json'
    },
    data: data
  })
}

// 操作日志
export function operateLog(data) {
  return request({
    url: '/api/operateLog/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

