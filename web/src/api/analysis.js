/**
 * Created by david on 2018/7/31.
 */

import request from '@/utils/request'

// 透析类型按年统计记录
export function txtypeByYear(data) {
  return request({
    url: '/user/countTxTypeByYear/',
    method: 'get',
    params: {
      nian: data.searchyear
    }
  })
}

// 透析类型按月统计记录
export function TxtypeBymonth(data) {
  return request({
    url: '/user/countTxTypeBymonth/',
    method: 'get',
    params: {
      yue: data.searchyear
    }
  })
}

// 透析类型按月统计图标数据
export function txtypeBymonthData(data) {
  return request({
    url: '/user/txTypeBymonthData/',
    method: 'get',
    params: {
      nian: data.searchyear
    }
  })
}

// 透析器按年统计记录
export function txDeviceByYear(data) {
  return request({
    url: '/user/txDeviceByYear/',
    method: 'get',
    params: {
      nian: data.searchyear
    }
  })
}

// 透析器按月统计记录
export function txDeviceBymonth(data) {
  return request({
    url: '/user/txDeviceBymonth/',
    method: 'get',
    params: {
      nian: data.searchyear
    }
  })
}

// 手术按年统计记录
export function operateByYear(data) {
  return request({
    url: '/user/operateByYear/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 分类统计记录
export function analyseBykind(data) {
  return request({
    url: '/user/analyseBykind/',
    method: 'get',
    params: {
      start: data.startyear,
      end: data.endyear,
      multisel: data.multisel
    }
  })
}

// 首次透析统计
export function analyseFirstTx(data) {
  return request({
    url: '/user/analyseFirstTx/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 甲状旁腺激素统计
export function analysePTH(data) {
  return request({
    url: '/user/analysePTH/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 钙磷乘积统计
export function analyseCaP(data) {
  return request({
    url: '/user/analyseCaP/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 检验预警统计
export function AlarmLab(data) {
  return request({
    url: '/user/AlarmLab/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear,
      nanme: data.name
    }
  })
}

// 急性并发症统计
export function analyseBfzBymonth(data) {
  return request({
    url: '/user/analyseBfzBymonth/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear,
      name: data.name
    }
  })
}

// 透析血压异常统计
export function analyseBloodPressure(data) {
  return request({
    url: '/user/analyseBloodPressure/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 原发病统计
export function analyseByYuanfa(data) {
  return request({
    url: '/user/analyseByYuanfa/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 转归统计
export function analyseZhuangui(data) {
  return request({
    url: '/user/analyseZhuangui/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 症状统计
export function analyseZhengzhuang(data) {
  return request({
    url: '/user/analyseZhengzhuang/',
    method: 'get',
    params: {
      start: data.startyear,
      end: data.endyear,
      multisel: data.multisel
    }
  })
}

// 药品按年统计
export function analyseDrugByyear(data) {
  return request({
    url: '/user/analyseDrugByyear/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 耗材按年统计
export function analyseMaterialByyear(data) {
  return request({
    url: '/user/analyseMaterialByyear/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 药品明细汇总
export function analysedrug(data) {
  return request({
    url: '/user/analysedrug/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 耗材明细汇总
export function analysematerial(data) {
  return request({
    url: '/user/analysematerial/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 药品明细
export function analysedrugDetail(data) {
  return request({
    url: '/user/analysedrugDetail/',
    method: 'get',
    params: {
      id: data.id,
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 耗材明细
export function analysematerialDetail(data) {
  return request({
    url: '/user/analysematerialDetail/',
    method: 'get',
    params: {
      id: data.id,
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 药品出入库统计
export function analyseDrugstock(data) {
  return request({
    url: '/user/analyseDrugstock/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 耗材出入库统计
export function analyseMaterialstock(data) {
  return request({
    url: '/user/analyseMaterialstock/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 科室收费统计
export function analyseDeptCharge(data) {
  return request({
    url: '/user/analyseDeptCharge/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}

// 科室收费按月统计
export function deptChargeBymonth(data) {
  return request({
    url: '/user/deptChargeBymonth/',
    method: 'get',
    params: {
      start: data.Startyear,
      end: data.Endyear
    }
  })
}
