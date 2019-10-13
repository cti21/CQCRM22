/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 交班记录
export function jiaobanpatient(data) {
  return request({
    url: '/api/jiaobanPatient/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 交班记录修改
export function updatejiaobanpatient(data) {
  return request({
    url: `/api/jiaobanPatient/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析评估患者列表
export function txpgPatient(data) {
  return request({
    url: '/api/patientTxpg/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      patientid: data.patientid,
      checked: data.checked
    }
  })
}

// 透析评估记录
export function txpgspkt(data) {
  return request({
    url: '/api/txpgSpkt/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 检验目的
export function getLabreason(data) {
  return request({
    url: '/user/getLabreason/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid
    }
  })
}

// 检验子项目
export function getLabItems(data) {
  return request({
    url: '/user/getLabItems/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid,
      reason: data.reason
    }
  })
}

// 检验结果分析
export function analyseLabResultData(data) {
  return request({
    url: '/user/analyseLabResultData/',
    method: 'get',
    params: {
      id: data.id,
      num: data.num,
      itemname: data.itemname,
      patientid: data.patientid
    }
  })
}
