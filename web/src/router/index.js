
import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const constantRouterMap = [
  {
    path: '/',
    redirect: '/login',
    hidden: true
  },
  {
    path: '/login',
    name: '登录页面',
    hidden: true,
    component: resolve => require(['../views/login/Login.vue'], resolve)
  },
  {
    path: '/homepage',
    name: 'homepage',
    index: 'homepage',
    meta: {
      title: '主页',
      icon: 'dashboard'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'mainpage',
        path: '/mainpage',
        meta: {
          title: '首页',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/Readme.vue'], resolve)
      }
    ]
  },
  // //////////////////////////////////////////////
  {
    path: '/selectPatient',
    hidden: true,
    index: 'selectPatient',
    meta: {
      title: '排班',
      icon: 'el-icon-menu'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'selectPatient',
        path: '/',
        meta: {
          title: '选择患者',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/selectPatient.vue'], resolve)
      }
    ]
  },
  {
    path: '/client_index',
    hidden: true,
    index: 'client_index',
    meta: {
      title: '宣教开单',
      icon: 'el-icon-menu'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'client_index',
        path: '/',
        meta: {
          title: '宣教开单',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/orders/client_index.vue'], resolve)
      }
    ]
  },
  {
    path: '/patientinfo',
    hidden: true,
    index: 'doctor',
    meta: {
      title: '医疗管理',
      icon: 'el-icon-menu'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'patientinfo',
        path: '/',
        meta: {
          title: '电子病历',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/patient.vue'], resolve)
      }
    ]
  },
  {
    path: '/nurse_detail',
    hidden: true,
    index: 'nurse_detail',
    meta: {
      title: '医疗管理',
      icon: 'el-icon-menu'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'nurse_detail',
        path: '/',
        meta: {
          title: '护士工作平台',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/nurse_detail.vue'], resolve)
      }
    ]
  }
]

export default new Router({
  mode: 'history',
  routes: constantRouterMap
})
// 异步挂载的路由
// 动态需要根据权限加载的路由表
export const asyncRouterMap = [
  {
    path: '/per_manage',
    name: 'xper_manage',
    index: 'Readme',
    meta: {
      title: '人事管理',
      icon: 'lock'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'userProfile',
        path: '/userProfile',
        meta: {
          title: '员工档案',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/per_manage/userProfile.vue'], resolve)
      },
      {
        name: 'xUser',
        path: '/user',
        meta: {
          title: '员工管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/user.vue'], resolve)
      },
      {
        name: 'xRole',
        path: '/role',
        meta: {
          title: '角色管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/role.vue'], resolve)
      }
    ]
  },
  {
    path: '/client_manage',
    name: 'client_manage',
    index: 'client_manage',
    meta: {
      title: '客户管理',
      icon: 'table'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'client',
        path: '/client',
        meta: {
          title: '客户档案',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/client/client.vue'], resolve)
      }
    ]
  },
  {
    path: '/chankang_manage',
    name: 'chankang_manage',
    index: 'chankang_manage',
    meta: {
      title: '产康服务',
      icon: 'table'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'order',
        path: '/order',
        meta: {
          title: '宣教开单',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/orders/order.vue'], resolve)
      },
      {
        name: 'treat',
        path: '/treat',
        meta: {
          title: '检查治疗',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/orders/treat.vue'], resolve)
      }
    ]
  },
  {
    path: '/service',
    name: 'service',
    index: 'service',
    meta: {
      title: '客户服务',
      icon: 'table'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'callback',
        path: '/callback',
        meta: {
          title: '客户回访',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/service/callback.vue'], resolve)
      }
    ]
  },
  {
    path: '/permission',
    meta: {
      title: '医疗管理',
      icon: 'international'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'xpermission',
        path: '/xpermission',
        meta: {
          title: '医生工作平台',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/permission.vue'], resolve)
      },
      {
        path: '/jiaobanPatient',
        name: 'xjiaobanPatient',
        meta: {
          title: '医生交班记录',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/doctor/jiaobanPatient.vue'], resolve)
      },
      {
        path: '/patient',
        name: 'xpatient',
        meta: {
          title: '患者管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/doctor/patient.vue'], resolve)
      },
      {
        path: '/txpgSpkt',
        name: 'xtxpgSpkt',
        meta: {
          title: '透析评估',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/doctor/tx_evaluate.vue'], resolve)
      },
      {
        name: 'txnurse',
        path: '/nurse',
        meta: {
          title: '护士工作平台',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/nurse.vue'], resolve)
      },
      {
        path: '/jiaoban_nurse',
        name: 'xjiaoban_nurse',
        meta: {
          title: '护士交班记录',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/nurse/jiaobanPatient.vue'], resolve)
      },
      {
        path: '/jiaobanDevice',
        name: 'xjiaobanDevice',
        meta: {
          title: '设备交班记录',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/nurse/jiaobanDevice.vue'], resolve)
      },
      {
        name: 'txdrug',
        path: '/drug',
        meta: {
          title: '药品管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/drug.vue'], resolve)
      },
      {
        path: '/drug_person',
        name: 'xdrug_person',
        meta: {
          title: '自备药管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/drug_person/drug_person.vue'], resolve)
      },
      {
        name: 'txmaterial',
        path: '/material',
        meta: {
          title: '耗材管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/material.vue'], resolve)
      },
      {
        name: 'txdevice',
        path: '/device',
        meta: {
          title: '设备管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/device.vue'], resolve)
      },
      {
        path: '/expense_today',
        name: 'xexpense_today',
        meta: {
          title: '今天费用',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/expense/expense_today.vue'], resolve)
      },
      {
        name: 'txexpense',
        path: '/expense',
        meta: {
          title: '费用查询',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/expense/expense_search.vue'], resolve)
        // component: resolve => require(['../components/page/expense.vue'], resolve)
      },
      {
        name: 'prepayment',
        path: '/prepayment',
        meta: {
          title: '预交金管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/prepayment.vue'], resolve)
      }
    ]
  },
  {
    path: '/analysis',
    name: 'analysis',
    meta: {
      title: '统计分析',
      icon: 'chart'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        path: '/countTxTypeByYear',
        name: 'xcountTxTypeByYear',
        meta: {
          title: '透析方式按年分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/txTypeByYear.vue'], resolve)
      },
      {
        path: '/countTxTypeBymonth',
        name: 'xcountTxTypeBymonth',
        meta: {
          title: '透析方式按月分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/txTypeBymonth.vue'], resolve)
      },
      {
        path: '/deviceByYear',
        name: 'xdeviceByYear',
        meta: {
          title: '透析器按年分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/deviceByYear.vue'], resolve)
      },
      {
        path: '/deviceBymonth',
        name: 'xdeviceBymonth',
        meta: {
          title: '透析器按月分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/deviceBymonth.vue'], resolve)
      },
      {
        path: '/operateByYear',
        name: 'xoperateByYear',
        meta: {
          title: '手术分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/operateByYear.vue'], resolve)
      },
      {
        path: '/analyseBykind',
        name: 'xanalyseBykind',
        meta: {
          title: '分类分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseBykind.vue'], resolve)
      },
      {
        path: '/analyseFirstTx',
        name: 'xanalyseFirstTx',
        meta: {
          title: '首次透析分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseFirstTx.vue'], resolve)
      },
      {
        path: '/analysePTH',
        name: 'xanalysePTH',
        meta: {
          title: '甲状旁腺分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analysePTH.vue'], resolve)
      },
      {
        path: '/analyseCaP',
        name: 'xanalyseCaP',
        meta: {
          title: '钙磷乘积分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseCaP.vue'], resolve)
      },
      {
        path: '/AlarmLab',
        name: 'xAlarmLab',
        meta: {
          title: '检验预警分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/AlarmLab.vue'], resolve)
      },
      {
        path: '/analyseBfzBymonth',
        name: 'xanalyseBfzBymonth',
        meta: {
          title: '并发症分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseBfzBymonth.vue'], resolve)
      },
      {
        path: '/analyseBloodPressure',
        name: 'xanalyseBloodPressure',
        meta: {
          title: '血压异常分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseBloodPressure.vue'], resolve)
      },
      {
        path: '/analyseByYuanfa',
        name: 'xanalyseByYuanfa',
        meta: {
          title: '原发病分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseByYuanfa.vue'], resolve)
      },
      {
        path: '/analyseZhuangui',
        name: 'xanalyseZhuangui',
        meta: {
          title: '转归分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseZhuangui.vue'], resolve)
      },
      {
        path: '/analyseZhengzhuang',
        name: 'xanalyseZhengzhuang',
        meta: {
          title: '症状分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseZhengzhuang.vue'], resolve)
      },
      {
        path: '/analyseDrugByyear',
        name: 'xanalyseDrugByyear',
        meta: {
          title: '药品分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseDrugByyear.vue'], resolve)
      },
      {
        path: '/analyseMaterialByyear',
        name: 'xanalyseMaterialByyear',
        meta: {
          title: '耗材分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseMaterialByyear.vue'], resolve)
      },
      {
        path: '/analysedrug',
        name: 'xanalysedrug',
        meta: {
          title: '药品明细汇总',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analysedrugDetail.vue'], resolve)
      },
      {
        path: '/analysematerial',
        name: 'xanalysematerial',
        meta: {
          title: '耗材明细汇总',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseMaterialDetail.vue'], resolve)
      },
      {
        path: '/analyseDrugstock',
        name: 'xanalyseDrugstock',
        meta: {
          title: '药品出入库分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseDrugstock.vue'], resolve)
      },
      {
        path: '/analyseMaterialstock',
        name: 'xanalyseMaterialstock',
        meta: {
          title: '耗材出入库分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseMaterialstock.vue'], resolve)
      },
      {
        path: '/analyseDeptCharge',
        name: 'xanalyseDeptCharge',
        meta: {
          title: '科室收费分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseDeptCharge.vue'], resolve)
      },
      {
        path: '/deptChargeBymonth',
        name: 'xdeptChargeBymonth',
        meta: {
          title: '科室收费按月分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/deptChargeBymonth.vue'], resolve)
      }
    ]
  },
  {
    path: '/system',
    name: 'system',
    meta: {
      title: '系统管理',
      icon: 'list'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'diseaseArea',
        path: '/diseaseArea',
        meta: {
          title: '病区管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/diseaseArea_tabs.vue'], resolve)
      },
      {
        name: 'coo_hospital',
        path: '/coo_hospital',
        meta: {
          title: '合作医院',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/coo_hospital.vue'], resolve)
      },
      {
        name: 'dept_dict',
        path: '/dept_dict',
        meta: {
          title: '科室字典',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/dept_dict.vue'], resolve)
      },
      {
        name: 'dept',
        path: '/dept',
        meta: {
          title: '中心科室',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/dept.vue'], resolve)
      },
      {
        name: 'project_dict',
        path: '/project_dict',
        meta: {
          title: '项目字典',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/project_dict.vue'], resolve)
      },
      {
        name: 'project',
        path: '/project',
        meta: {
          title: '中心项目',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/project.vue'], resolve)
      },
      {
        name: 'post_dict',
        path: '/post_dict',
        meta: {
          title: '岗位字典',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/post_dict.vue'], resolve)
      },
      {
        name: 'finance_month',
        path: '/finance_month',
        meta: {
          title: '财务月',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/finance_month.vue'], resolve)
      },
      {
        path: '/performance_dict',
        name: 'performance_dict',
        meta: {
          title: '绩效字典',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/performance_dict.vue'], resolve)
      },
      {
        path: '/performance',
        name: 'performance',
        meta: {
          title: '中心绩效',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/performance.vue'], resolve)
      },
      {
        path: '/benefit_dict',
        name: 'benefit_dict',
        meta: {
          title: '工资福利字典',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/benefit_dict.vue'], resolve)
      },
      {
        path: '/benefit',
        name: 'benefit',
        meta: {
          title: '中心工资福利',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/benefit.vue'], resolve)
      },
      {
        path: '/tuition_fee',
        name: 'tuition_fee',
        meta: {
          title: '带教费',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/tuitionFee.vue'], resolve)
      },
      {
        name: 'organization',
        path: '/organization',
        meta: {
          title: '组织机构设置',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/organization.vue'], resolve)
      },
      {
        path: '/huiyuan_set',
        name: 'huiyuan_set',
        meta: {
          title: '回院设置',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/huiyuan_set.vue'], resolve)
      },
      {
        name: 'xlog',
        path: '/xlog',
        meta: {
          title: '操作日志',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/operate_log/operatelog.vue'], resolve)
      }
    ]
  },
  {
    path: '*',
    redirect: '/404',
    hidden: true
  }
]
