/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 设备字典
export function deviceDict(data) {
  return request({
    url: '/api/deviceDict/',
    method: 'get',
    params: data
  })
}

// 设备列表
export function devices(data) {
  return request({
    url: '/api/device/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      type: data.type
    }
  })
}

// 设备新增
export function createdevice(data) {
  return request({
    url: '/api/device/',
    method: 'post',
    data: data
  })
}
// 设备修改
export function updatedevice(data) {
  return request({
    url: `/api/device/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 设备删除
export function deletedevice(data) {
  return request({
    url: `/api/device/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 设备维修列表
export function device_repairs(data) {
  return request({
    url: '/api/devicerepair/',
    method: 'get',
    params: {
      page: data.page,
      state: data.state,
      name: data.name
    }
  })
}

// 设备维修新增
export function createdevice_repair(data) {
  return request({
    url: '/api/devicerepair/',
    method: 'post',
    data: data
  })
}
// 设备维修修改
export function updatedevice_repair(data) {
  return request({
    url: `/api/devicerepair/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 设备维修删除
export function deletedevice_repair(data) {
  return request({
    url: `/api/devicerepair/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 保养字典列表
export function maintainences(data) {
  return request({
    url: '/api/maintainence/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      leixing: data.leixing
    }
  })
}

// 保养字典新增
export function createMaintainence(data) {
  return request({
    url: '/api/maintainence/',
    method: 'post',
    data: data
  })
}
// 保养字典修改
export function updateMaintainence(data) {
  return request({
    url: `/api/maintainence/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 保养字典删除
export function deleteMaintainence(data) {
  return request({
    url: `/api/maintainence/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 设备保养列表
export function device_maintainences(data) {
  return request({
    url: '/api/devicemaintainence/',
    method: 'get',
    params: {
      page: data.page,
      fromdate: data.fromdate,
      todate: data.todate,
      name: data.name
    }
  })
}

// 设备保养新增
export function createdevice_maintainence(data) {
  return request({
    url: '/api/devicemaintainence/',
    method: 'post',
    data: data
  })
}
// 设备保养修改
export function updatedevice_maintainence(data) {
  return request({
    url: `/api/devicemaintainence/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 设备保养删除
export function deletedevice_maintainence(data) {
  return request({
    url: `/api/devicemaintainence/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 设备保养明细列表
export function device_maintainence_details(data) {
  return request({
    url: '/api/dmd/',
    method: 'get',
    params: {
      dm_id: data
    }
  })
}

// 设备保养明细新增
export function createdevice_maintainence_detail(data) {
  return request({
    url: '/api/dmd/',
    method: 'post',
    data: data
  })
}
// 设备保养明细修改
export function updatedevice_maintainence_detail(data) {
  return request({
    url: `/api/dmd/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 设备保养明细删除
export function deletedevice_maintainence_detail(data) {
  return request({
    url: `/api/dmd/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 水质监测列表
export function water_exams(data) {
  return request({
    url: '/api/waterExam/',
    method: 'get',
    params: {
      page: data.page,
      fromdate: data.fromdate,
      todate: data.todate
    }
  })
}

// 水质监测新增
export function createwater_exam(data) {
  return request({
    url: '/api/waterExam/',
    method: 'post',
    data: data
  })
}
// 水质监测修改
export function updatewater_exam(data) {
  return request({
    url: `/api/waterExam/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 水质监测删除
export function deletewater_exam(data) {
  return request({
    url: `/api/waterExam/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 细菌监测列表
export function monitor_records(data) {
  return request({
    url: '/api/monitorRecord/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      fromdate: data.fromdate,
      todate: data.todate
    }
  })
}

// 细菌监测新增
export function createmonitor_record(data) {
  return request({
    url: '/api/monitorRecord/',
    method: 'post',
    data: data
  })
}
// 细菌监测修改
export function updatemonitor_record(data) {
  return request({
    url: `/api/monitorRecord/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 细菌监测删除
export function deletemonitor_record(data) {
  return request({
    url: `/api/monitorRecord/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 细菌监测点列表
export function mpds(data) {
  return request({
    url: '/api/mpd/',
    method: 'get',
    params: {
      id: data.id,
      type: data.type
    }
  })
}

// 细菌监测点新增
export function creatempds(data) {
  return request({
    url: '/api/mpd/',
    method: 'post',
    data: data
  })
}

// 细菌监测点修改
export function updatempds(data) {
  return request({
    url: `/api/mpd/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 细菌监测点删除
export function deletempds(data) {
  return request({
    url: `/api/mpd/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 水质监测记录列表
export function water_process_recs(data) {
  return request({
    url: '/api/waterProcessRec/',
    method: 'get',
    params: {
      page: data.page,
      name: data.name,
      fromdate: data.fromdate,
      todate: data.todate
    }
  })
}

// 水质监测记录新增
export function createwater_process_rec(data) {
  return request({
    url: '/api/waterProcessRec/',
    method: 'post',
    data: data
  })
}
// 水质监测记录修改
export function updatewater_process_rec(data) {
  return request({
    url: `/api/waterProcessRec/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 水质监测记录删除
export function deletewater_process_rec(data) {
  return request({
    url: `/api/waterProcessRec/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 细菌监测位置
export function mps(data) {
  return request({
    url: '/api/mp/',
    method: 'get',
    params: {
      type: data.type
    }
  })
}

// 细菌监测位置新增
export function createmps(data) {
  return request({
    url: '/api/mp/',
    method: 'post',
    data: data
  })
}

// 细菌监测位置修改
export function updatemps(data) {
  return request({
    url: `/api/mp/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 细菌监测位置删除
export function deletemps(data) {
  return request({
    url: `/api/mp/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}
