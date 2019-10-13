/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 用药字典
export function drugs(data) {
  return request({
    url: '/api/drug/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 透析用药列表
export function Tx_drugs(data) {
  return request({
    // url: '/api/product/filterProducts/',
    url: '/api/tx_drug/',
    method: 'get',
    params: { patientid: data }
  })
}

// 透析用药新增
export function createtx_drug(data) {
  return request({
    url: '/api/tx_drug/',
    method: 'post',
    data: data
  })
}
// 透析用药修改
export function updatetx_drug(data) {
  return request({
    url: `/api/tx_drug/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 透析用药删除
export function deletetx_drug(data) {
  return request({
    url: `/api/tx_drug/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}
