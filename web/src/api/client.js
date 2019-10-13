/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 客户档案
export function clients(data) {
  return request({
    url: '/api/client/',
    method: 'get',
    params: {
      name: data.name,
      clientid: data.clientid
    }
  })
}

// 客户档案新增
export function createClient(data) {
  return request({
    url: '/api/client/',
    method: 'post',
    data: data
  })
}

// 客户档案修改
export function updateClient(data) {
  return request({
    url: `/api/client/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 客户档案删除
export function deleteClient(data) {
  return request({
    url: `/api/client/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 客户登记
export function client_registers(data) {
  return request({
    url: '/api/client_register/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      clientid: data.clientid,
      clienttype: data.clienttype,
      indate: data.indate
    }
  })
}

// 客户登记新增
export function createClient_register(data) {
  return request({
    url: '/api/client_register/',
    method: 'post',
    data: data
  })
}

// 客户登记修改
export function updateClient_register(data) {
  return request({
    url: `/api/client_register/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 客户登记删除
export function deleteClient_register(data) {
  return request({
    url: `/api/client_register/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 科室对应的客户来源
export function dept_client_types(data) {
  return request({
    url: '/api/dept_client_type/',
    method: 'get',
    params: {
      dept_id: data.dept_id
    }
  })
}

// 禁忌症字典
export function jinjizhengs(data) {
  return request({
    url: '/api/jinjizheng/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name
    }
  })
}

// 禁忌症新增
export function createJinjizheng(data) {
  return request({
    url: '/api/jinjizheng/',
    method: 'post',
    data: data
  })
}

// 禁忌症修改
export function updateJinjizheng(data) {
  return request({
    url: `/api/jinjizheng/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 禁忌症删除
export function deleteJinjizheng(data) {
  return request({
    url: `/api/jinjizheng/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 项目禁忌症
export function project_jinjizhengs(data) {
  return request({
    url: '/api/project_jinjizheng/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      projectdict_id: data.project_id
    }
  })
}

// 项目禁忌症新增
export function createProject_jinjizheng(data) {
  return request({
    url: '/api/project_jinjizheng/',
    method: 'post',
    data: data
  })
}

// 项目禁忌症删除
export function deleteProject_jinjizheng(data) {
  return request({
    url: `/api/project_jinjizheng/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}
