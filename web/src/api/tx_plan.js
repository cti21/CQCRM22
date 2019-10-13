/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 透析处方列表
export function Tx_plans(data) {
  return request({
    url: '/api/tx_plan/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 透析处方新增
export function createtx_plan(data) {
  return request({
    url: '/api/tx_plan/',
    method: 'post',
    data: data
  })
}

// 透析处方修改
export function updatetx_plan(data) {
  return request({
    url: `/api/tx_plan/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 透析处方删除
export function deletetx_plan(data) {
  return request({
    url: `/api/tx_plan/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 个人血液净化套餐列表
export function xyjh_pat(data) {
  return request({
    url: '/api/xyjh_pat/',
    method: 'get',
    params: data
  })
}

// 个人血液净化套餐新增
export function createtc(data) {
  return request({
    url: '/api/xyjh_pat/',
    method: 'post',
    data: data
  })
}

// 个人血液净化套餐修改
export function updatetc(data) {
  return request({
    url: `/api/xyjh_pat/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 个人血液净化套餐删除
export function deletetc(data) {
  return request({
    url: `/api/xyjh_pat/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 血管通路
export function getXgtonglu(data) {
  return request({
    url: '/user/getXgtonglu/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid
    }
  })
}

// 血管通路类型
export function getXgtongluType(data) {
  return request({
    url: '/user/getXgtongluType/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid
    }
  })
}

// 血管通路类型
export function getMaterialType(data) {
  return request({
    url: '/user/getMaterialType/',
    method: 'get',
    params: {
      page: data.page,
      kind: data.kind
    }
  })
}
