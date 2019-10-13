/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 员工档案
export function users(data) {
  return request({
    url: '/api/userProfile/',
    method: 'get',
    params: {
      hrmdepartment_id: data.hrmdepartment_id,
      name: data.name
    }
  })
}

// 员工档案新增
export function createUser(data) {
  return request({
    url: '/api/userProfile/',
    method: 'post',
    data: data
  })
}

// 员工档案修改
export function updateUser(data) {
  return request({
    url: `/api/userProfile/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 员工档案删除
export function deleteUser(data) {
  return request({
    url: `/api/userProfile/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}
