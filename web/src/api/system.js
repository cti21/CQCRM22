/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 班次字典
export function banci(data) {
  return request({
    url: '/api/banci/',
    method: 'get',
    params: data
  })
}

// 病区字典
export function diseaseArea(data) {
  return request({
    url: '/api/diseaseArea/',
    method: 'get',
    params: data
  })
}

// 病区新增
export function createDiseaseArea(data) {
  return request({
    url: '/api/diseaseArea/',
    method: 'post',
    data: data
  })
}
// 病区修改
export function updateDiseaseArea(data) {
  return request({
    url: `/api/diseaseArea/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 病区删除
export function deleteDiseaseArea(data) {
  return request({
    url: `/api/diseaseArea/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 病床字典
export function beds(data) {
  return request({
    url: '/api/bed/',
    method: 'get',
    params: data
  })
}

// 病床新增
export function createBed(data) {
  return request({
    url: '/api/bed/',
    method: 'post',
    data: data
  })
}
// 病床修改
export function updateBed(data) {
  return request({
    url: `/api/bed/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 病床删除
export function deleteBed(data) {
  return request({
    url: `/api/bed/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 套餐字典
export function xyjh_search(data) {
  return request({
    url: '/api/xyjh_search/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      type: data.type
    }
  })
}

// 套餐字典
export function xyjhdict(data) {
  return request({
    url: '/api/xyjhdict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      type: data.type
    }
  })
}

// 套餐字典新增
export function createxyjhdict(data) {
  return request({
    url: '/api/xyjhdict/',
    method: 'post',
    data: data
  })
}
// 套餐字典修改
export function updatexyjhdict(data) {
  return request({
    url: `/api/xyjhdict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 套餐字典删除
export function deletexyjhdict(data) {
  return request({
    url: `/api/xyjhdict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 套餐列表
export function xyjhs(data) {
  return request({
    url: '/api/xyjh/',
    method: 'get',
    params: {
      page: data.page,
      id: data.id,
      name: data.name
    }
  })
}

// 套餐新增
export function createxyjh(data) {
  return request({
    url: '/api/xyjh/',
    method: 'post',
    data: data
  })
}
// 套餐修改
export function updatexyjh(data) {
  return request({
    url: `/api/xyjh/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 套餐删除
export function deletexyjh(data) {
  return request({
    url: `/api/xyjh/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 利润分成类型字典
export function profit_distri_dicts(data) {
  return request({
    url: '/api/profit_distri_dict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 利润分成类型新增
export function createProfit_distri_dict(data) {
  return request({
    url: '/api/profit_distri_dict/',
    method: 'post',
    data: data
  })
}
// 利润分成类型修改
export function updateProfit_distri_dict(data) {
  return request({
    url: `/api/profit_distri_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 利润分成类型删除
export function deleteProfit_distri_dict(data) {
  return request({
    url: `/api/profit_distri_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 发票字典
export function invoice_dicts(data) {
  return request({
    url: '/api/invoice_dict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      patientid: data.patientid
    }
  })
}

// 发票新增
export function createInvoice_dict(data) {
  return request({
    url: '/api/invoice_dict/',
    method: 'post',
    data: data
  })
}
// 发票修改
export function updateInvoice_dict(data) {
  return request({
    url: `/api/invoice_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 发票删除
export function deleteInvoice_dict(data) {
  return request({
    url: `/api/invoice_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 开票字典
export function invoice_sets(data) {
  return request({
    url: '/api/invoice_set/',
    method: 'get',
    params: {
      page: data.page,
      hospital_id: data.hospital_id
    }
  })
}
// 开票新增
export function createInvoice_set(data) {
  return request({
    url: '/api/invoice_set/',
    method: 'post',
    data: data
  })
}
// 开票修改
export function updateInvoice_set(data) {
  return request({
    url: `/api/invoice_set/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 开票删除
export function deleteInvoice_set(data) {
  return request({
    url: `/api/invoice_set/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 合作医院
export function coohospitals(data) {
  return request({
    url: '/api/coo_hospital/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 合作医院新增
export function createCoohospital(data) {
  return request({
    url: '/api/coo_hospital/',
    method: 'post',
    data: data
  })
}
// 合作医院修改
export function updateCoohospital(data) {
  return request({
    url: `/api/coo_hospital/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 合作医院删除
export function deleteCoohospital(data) {
  return request({
    url: `/api/coo_hospital/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 科室字典
export function dept_dicts(data) {
  return request({
    url: '/api/dept_dict/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 科室字典新增
export function createDept_dict(data) {
  return request({
    url: '/api/dept_dict/',
    method: 'post',
    data: data
  })
}
// 科室字典修改
export function updateDept_dict(data) {
  return request({
    url: `/api/dept_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 科室字典删除
export function deleteDept_dict(data) {
  return request({
    url: `/api/dept_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 岗位字典
export function post_dicts(data) {
  return request({
    url: '/api/post_dict/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 岗位字典新增
export function createPost_dict(data) {
  return request({
    url: '/api/post_dict/',
    method: 'post',
    data: data
  })
}
// 岗位字典修改
export function updatePost_dict(data) {
  return request({
    url: `/api/post_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 岗位字典删除
export function deletePost_dict(data) {
  return request({
    url: `/api/post_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 中心科室
export function depts(data) {
  return request({
    url: '/api/dept/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 中心科室新增
export function createDept(data) {
  return request({
    url: '/api/dept/',
    method: 'post',
    data: data
  })
}

// 中心科室删除
export function deleteDept(data) {
  return request({
    url: `/api/dept/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 科室岗位
export function dept_posts(data) {
  return request({
    url: '/api/dept_post/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 科室岗位新增
export function createDept_post(data) {
  return request({
    url: '/api/dept_post/',
    method: 'post',
    data: data
  })
}

// 科室岗位删除
export function deleteDept_post(data) {
  return request({
    url: `/api/dept_post/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 财务月
export function finance_months(data) {
  return request({
    url: '/api/finance_month/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 财务月新增
export function createFinance_month(data) {
  return request({
    url: '/api/finance_month/',
    method: 'post',
    data: data
  })
}
// 财务月修改
export function updateFinance_month(data) {
  return request({
    url: `/api/finance_month/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 财务月删除
export function deleteFinance_month(data) {
  return request({
    url: `/api/finance_month/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 绩效字典
export function performance_dicts(data) {
  return request({
    url: '/api/performance_dict/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 绩效字典新增
export function createPerformance_dict(data) {
  return request({
    url: '/api/performance_dict/',
    method: 'post',
    data: data
  })
}
// 绩效字典修改
export function updatePerformance_dict(data) {
  return request({
    url: `/api/performance_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 绩效字典删除
export function deletePerformance_dict(data) {
  return request({
    url: `/api/performance_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 中心绩效字典
export function performances(data) {
  return request({
    url: '/api/performance/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 中心绩效字典新增
export function createPerformance(data) {
  return request({
    url: '/api/performance/',
    method: 'post',
    data: data
  })
}

// 中心绩效字典删除
export function deletePerformance(data) {
  return request({
    url: `/api/performance/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 工资福利字典
export function benefit_dicts(data) {
  return request({
    url: '/api/benefit_dict/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 工资福利字典新增
export function createBenefit_dict(data) {
  return request({
    url: '/api/benefit_dict/',
    method: 'post',
    data: data
  })
}
// 工资福利字典修改
export function updateBenefit_dict(data) {
  return request({
    url: `/api/benefit_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 工资福利字典删除
export function deleteBenefit_dict(data) {
  return request({
    url: `/api/benefit_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 中心工资福利字典
export function benefits(data) {
  return request({
    url: '/api/benefit/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 中心工资福利字典新增
export function createBenefit(data) {
  return request({
    url: '/api/benefit/',
    method: 'post',
    data: data
  })
}

// 中心工资福利字典删除
export function deleteBenefit(data) {
  return request({
    url: `/api/benefit/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 项目字典
export function project_dicts(data) {
  return request({
    url: '/api/project_dict/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      isindependent: data.isindependent
    }
  })
}

// 套餐子项目
export function project_dict_childs(data) {
  return request({
    url: '/api/project_dict_child/',
    method: 'get',
    params: {
      parentid: data.parentid
    }
  })
}

// 项目之所有单项
export function project_dict_individuals(data) {
  return request({
    url: '/api/project_dict_individual/',
    method: 'get',
    params: {
      parentid: data.parentid
    }
  })
}

// 项目字典新增
export function createProject_dict(data) {
  return request({
    url: '/api/project_dict/',
    method: 'post',
    data: data
  })
}
// 项目字典修改
export function updateProject_dict(data) {
  return request({
    url: `/api/project_dict/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 项目字典删除
export function deleteProject_dict(data) {
  return request({
    url: `/api/project_dict/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 中心项目
export function projects(data) {
  return request({
    url: '/api/project/',
    method: 'get',
    params: {
      name: data.name,
      register_id: data.register_id
    }
  })
}


// 中心套餐子项目
export function project_childs(data) {
  return request({
    url: '/api/project_child/',
    method: 'get',
    params: {
      name: data.name,
      hrmdepartment_id: data.hrmdepartment_id,
      parentid: data.parentid
    }
  })
}

// 中心项目之所有项目(不含中心自定义套餐)
export function project_individuals(data) {
  return request({
    url: '/api/project_individual/',
    method: 'get',
    params: {
      name: data.name,
      parentid: data.parentid
    }
  })
}


// 中心项目新增
export function createProject(data) {
  return request({
    url: '/api/project/',
    method: 'post',
    data: data
  })
}

// 中心项目修改
export function updateProject(data) {
  return request({
    url: `/api/project/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 中心项目删除
export function deleteProject(data) {
  return request({
    url: `/api/project/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 回院设置字典
export function huiyuan_sets(data) {
  return request({
    url: '/api/huiyuan_set/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 回院设置字典新增
export function createHuiyuan_set(data) {
  return request({
    url: '/api/huiyuan_set/',
    method: 'post',
    data: data
  })
}

// 回院设置字典删除
export function deleteHuiyuan_set(data) {
  return request({
    url: `/api/huiyuan_set/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 带教费
export function tuition_fees(data) {
  return request({
    url: '/api/tuition_fee/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 带教费新增
export function createTuition_fee(data) {
  return request({
    url: '/api/tuition_fee/',
    method: 'post',
    data: data
  })
}
// 带教费修改
export function updateTuition_fee(data) {
  return request({
    url: `/api/tuition_fee/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 带教费删除
export function deleteTuition_fee(data) {
  return request({
    url: `/api/tuition_fee/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 带教费明细
export function tuitionfee_details(data) {
  return request({
    url: '/api/tuitionfee_detail/',
    method: 'get',
    params: {
      name: data.name
    }
  })
}

// 带教费明细新增
export function createTuitionfee_detail(data) {
  return request({
    url: '/api/tuitionfee_detail/',
    method: 'post',
    data: data
  })
}
// 带教费明细修改
export function updateTuitionfee_detail(data) {
  return request({
    url: `/api/tuitionfee_detail/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 带教费明细删除
export function deleteTuitionfee_detail(data) {
  return request({
    url: `/api/tuitionfee_detail/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}


