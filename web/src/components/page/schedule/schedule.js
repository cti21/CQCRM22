/**
 * Created by david on 2018/7/31.
 */
import request from './request.js'

// 得到排班每天患者
export function getPatient(data) {
  return request({
    url: `api/patient/?page=` + data.page + `/`,
    method: 'get',
    params:  data
  })
}

// 得到单双周排班表
export function getschedule_odddual(data) {
  return request({
    url:'api/getOddDual/',
    method: 'get',
    params:  data
  })
}

// 设置某个患者的单双周排班计划
export function setschedule_patient(data) {
  return request({
    url: `api/getOddDual/` + data.odddualid + `/`,
    method: 'put',
    data: data
  })
}

// 设置某个患者的单日排班计划
export function setschedule_day(data) {
  return request({
    url: `api/schedulearrange/` + data.scheduleid + `/`,
    method: 'put',
    data: data
  })
}

// 得到具体日期的排班表
export function getschedule_day(data) {
  return request({
    url: 'api/schedulearrange/',
    method: 'get',
    params:  data
  })
}

// 创建排班基础数据1111111111111111111111
export function create_schedule() {
  return request({
    url: 'api/createschedule/',
    method: 'get',
    params:  ''
  })
}

export function create_dayschedule() {
  return request({
    url: 'api/createdayschedule/',
    method: 'get',
    params:  ''
  })
}

// 得到患者透析类型
export function getpatient_txtype(data) {
  return request({
    url: '/patient_txtype',
    method: 'get',
    params:  data
  })
}

export function getInfo(token) {
  return request({
    url: '/user/info',
    method: 'get',
    params: { token }
  })
}

create_dayschedule
