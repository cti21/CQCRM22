/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 回访记录
export function callbacks(data) {
  return request({
    url: '/api/callback/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      begindate: data.begindate,
      enddate: data.enddate,
      project: data.project,
      handleman: data.handleman,
      isfinish: data.isfinish,
      callbacktype: data.callbacktype,
      ishospital: data.ishospital,
      todaycallback: data.todaycallback,
      hrmdepartment_id: data.hrmdepartment_id,
      order_id: data.order_id
    }
  })
}

// 回访新增
export function createCallback(data) {
  return request({
    url: '/api/callback/',
    method: 'post',
    data: data
  })
}

// 回访修改
export function updateCallback(data) {
  return request({
    url: `/api/callback/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 回访删除
export function deleteCallback(data) {
  return request({
    url: `/api/callback/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}
