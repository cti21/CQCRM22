/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 血管通路列表
export function xgtonglus(data) {
  return request({
    url: '/api/xgtonglu/',
    method: 'get',
    params: {
      patientid: data
    }
  })
}

// 血管通路不良事件列表
export function xgtonglu_adverse(data) {
  return request({
    url: '/api/xgtonglu_adverse/',
    method: 'get',
    params: { xgtonglu_id: data }
  })
}

// 血管通路新增
export function createxgtonglu(data) {
  return request({
    url: '/api/xgtonglu/',
    method: 'post',
    data: data
  })
}

// 血管通路修改
export function updatexgtonglu(data) {
  return request({
    url: `/api/xgtonglu/` + data.id + `/`,
    method: 'put',
    data:  data
  })
}

// 血管通路删除
export function deletexgtonglu(data) {
  return request({
    url: `/api/xgtonglu/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 血管通路不良事件新增
export function createxgtonglu_adverse(data) {
  return request({
    url: '/api/xgtonglu_adverse/',
    method: 'post',
    data: data
  })
}

// 血管通路不良事件修改
export function updatexgtonglu_adverse(data) {
  return request({
    url: `/api/xgtonglu_adverse/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 血管通路不良事件删除
export function deletexgtonglu_adverse(data) {
  return request({
    url: `/api/xgtonglu_adverse/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

