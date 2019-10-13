/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 交班记录
export function jiaobanNurse(data) {
  return request({
    url: '/api/jiaoban_nurse/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 交班记录修改
export function updatejiaobanNurse(data) {
  return request({
    url: `/api/jiaoban_nurse/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 设备交班记录
export function jiaobanDevice(data) {
  return request({
    url: '/api/jiaobanDevice/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      banci: data.banci,
      type: data.type
    }
  })
}

// 设备交班记录修改
export function updatejiaobanDevice(data) {
  return request({
    url: `/api/jiaobanDevice/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 医嘱之耗材、处置
export function yz_material(data) {
  return request({
    url: '/api/yz_material/',
    method: 'get',
    params: {
      page: data.page,
      yzdrug_id: data.yzdrug_id
    }
  })
}

// 医嘱之耗材、处置增加
export function createyz_material(data) {
  return request({
    url: '/api/yz_material/',
    method: 'post',
    data: data
  })
}

// 医嘱之耗材、处置修改
export function updateyz_material(data) {
  return request({
    url: `/api/yz_material/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 医嘱之耗材、处置删除
export function deleteyz_material(data) {
  return request({
    url: `/api/yz_material/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}
