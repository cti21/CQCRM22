/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 门诊收费主记录
export function outp_rcpt_masters(data) {
  return request({
    url: '/api/outp_rcpt_master/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      patientid: data.patientid,
      rcptno: data.rcptno
    }
  })
}

// 门诊收费主记录新增
export function createOutp_rcpt_master(data) {
  return request({
    url: '/api/outp_rcpt_master/',
    method: 'post',
    data: data
  })
}

// 门诊收费主记录修改
export function updateOutp_rcpt_master(data) {
  return request({
    url: `/api/outp_rcpt_master/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 门诊收费主记录删除
export function deleteOutp_rcpt_master(data) {
  return request({
    url: `/api/outp_rcpt_master/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 门诊收费明细
export function outp_bill_items(data) {
  return request({
    url: '/api/outp_bill_items/',
    method: 'get',
    params: {
      masterid: data.masterid,
      fromdate: data.Startyear,
      patientid: data.patientid
    }
  })
}

// 门诊收费明细新增
export function createOutp_bill_items(data) {
  return request({
    url: '/api/outp_bill_items/',
    method: 'post',
    data: data
  })
}

// 门诊收费明细修改
export function updateOutp_bill_items(data) {
  return request({
    url: `/api/outp_bill_items/` + data[0].id + `/`,
    method: 'put',
    data: data
  })
}

// 门诊收费明细删除
export function deleteOutp_bill_items(data) {
  return request({
    url: `/api/outp_bill_items/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 收费明细查询
export function myOutp_bill_items(data) {
  return request({
    url: '/api/myOutp_bill_items/',
    method: 'get',
    params: {
      page: data.page,
      patientid: data.patientid,
      name: data.name,
      fromdate: data.fromdate,
      todate: data.todate
    }
  })
}

// 预交金记录
export function prepayment(data) {
  return request({
    url: '/api/prepayment/',
    method: 'get',
    params: {
      page: data.page,
      name: data.patientid,
      rcptno: data.rcptno,
      operatedate: data.operatedate
    }
  })
}

// 门诊收费明细新增
export function createPrepayment(data) {
  return request({
    url: '/api/prepayment/',
    method: 'post',
    data: data
  })
}

