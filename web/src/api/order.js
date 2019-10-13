/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 开单档案
export function orders(data) {
  return request({
    url: '/api/order/',
    method: 'get',
    params: {
      page: data.page,
      hrmdepartment_id: data.hrmdepartment_id,
      clientid: data.clientid,
      begindate: data.begindate,
      enddate: data.enddate,
      clientname:data.name,
      issuccess: data.issuccess,
      isacquire: data.isacquire,
      isproorder: data.isproorder,
      project: data.project,
      orderuser: data.orderuser,
      marketuser: data.marketuser
    }
  })
}

// 开单新增
export function createOrder(data) {
  return request({
    url: '/api/order/',
    method: 'post',
    data: data
  })
}

// 开单修改
export function updateOrder(data) {
  return request({
    url: `/api/order/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 开单删除
export function deleteOrder(data) {
  return request({
    url: `/api/order/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 治疗档案
export function treats(data) {
  return request({
    url: '/api/treat/',
    method: 'get',
    params: {
      page: data.page,
      hrmdepartment_id: data.hrmdepartment_id,
      clientid: data.clientid,
      clientname: data.clientname,
      phone: data.phone,
      begindate: data.begindate,
      enddate: data.enddate,
      project: data.project,
      isacquire: data.isacquire,
      residue: data.residue,
      todaytreated: data.todaytreated,
    }
  })
}

// 治疗新增
export function createTreat(data) {
  return request({
    url: '/api/treat/',
    method: 'post',
    data: data
  })
}

// 治疗修改
export function updateTreat(data) {
  return request({
    url: `/api/treat/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 治疗删除
export function deleteTreat(data) {
  return request({
    url: `/api/treat/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 治疗历史记录
export function treat_historys(data) {
  return request({
    url: '/api/treat_histrorys/',
    method: 'get',
    params: {
      page: data.page,
      project_id: data.project_id,
      treat_id: data.treat_id,
      type: data.type
    }
  })
}

// 套餐子项的治疗历史记录
export function treat_subhistorys(data) {
  return request({
    url: '/api/treat_subhistorys/',
    method: 'get',
    params: {
      treat_id: data.treat_id,
      operatedate: data.operatedate
    }
  })
}

// 治疗历史记录
export function getTcTreatHistroryData(data) {
  return request({
    url: '/api/getTcTreatHistroryData/',
    method: 'get',
    params: {
      treat_id: data.treat_id
    }
  })
}

// 单条治疗记录
export function treat_details(data) {
  return request({
    url: '/api/treat_detail/',
    method: 'get',
    params: {
      page: data.page,
      treat_id: data.treat_id
    }
  })
}

// 开单页面下拉框数据
export function getOrderSelectData(data) {
  return request({
    url: '/api/getOrderSelectData/',
    method: 'get',
    params: {
      hrmdepartment_id: data.hrmdepartment_id
    }
  })
}

// 下拉框数据
export function getAllSelectData(data) {
  return request({
    url: '/user/getAllSelectData/',
    method: 'get',
    params: {
    }
  })
}

// 问卷字典
export function surveys(data) {
  return request({
    url: '/api/survey/',
    method: 'get',
    params: {
      page: data.page
    }
  })
}

// 治疗问卷
export function treat_surveys(data) {
  return request({
    url: '/api/treat_survey/',
    method: 'get',
    params: {
      page: data.page,
      treat_id: data.treat_id
    }
  })
}

// 治疗问卷新增
export function createTreat_survey(data) {
  return request({
    url: '/api/treat_survey/',
    method: 'post',
    data: data
  })
}

// 治疗问卷删除
export function deleteTreat_survey(data) {
  return request({
    url: `/api/treat_survey/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 问卷题目及选项
export function survey_titles(data) {
  return request({
    url: '/api/survey_title/',
    method: 'get',
    params: {
      page: data.page,
      survey_id: data.survey_id,
      treat_id: data.treat_id
    }
  })
}

// 问卷题目及选项新增
export function createSurvey_title(data) {
  return request({
    url: '/api/survey_title/',
    method: 'post',
    data: data
  })
}




