
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
  ////////////////////////////////////////////////
  //  {
  //   path: '/selectPatient',
  //   hidden: true,
  //   index: 'Tx_plan',
  //   meta: {
  //     title: '透析处方',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'Tx_plan',
  //       path: '/',
  //       meta: {
  //         title: 'Tx_plan',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../components/page/schedule/selectPatient.vue'], resolve)
  //     }
  //   ]
  // },
  // //////////////////////////////////////////////////////
  // {
  //   path: '/Tx_plan',
  //   hidden: true,
  //   index: 'Tx_plan',
  //   meta: {
  //     title: '透析处方',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'Tx_plan',
  //       path: '/',
  //       meta: {
  //         title: 'Tx_plan',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../views/Medical/tx_plan.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/Tx_drug',
  //   hidden: true,
  //   index: 'Tx_drug',
  //   meta: {
  //     title: '透析用药',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'Tx_drug',
  //       path: '/',
  //       meta: {
  //         title: 'Tx_drug',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../views/Medical/tx_drug.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/xgtonglu',
  //   hidden: true,
  //   index: 'xgtonglu',
  //   meta: {
  //     title: '血管通路',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'xgtonglu',
  //       path: '/',
  //       meta: {
  //         title: 'xgtonglu',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../views/Medical/xgtonglu.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/Tx_pinggu',
  //   hidden: true,
  //   index: 'Tx_pinggu',
  //   meta: {
  //     title: '透析评估',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'Tx_pinggu',
  //       path: '/',
  //       meta: {
  //         title: 'Tx_pinggu',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../views/Medical/tx_pinggu.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/Tx_rec',
  //   hidden: true,
  //   index: 'Tx_rec',
  //   meta: {
  //     title: '透析记录单',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'Tx_rec',
  //       path: '/',
  //       meta: {
  //         title: 'Tx_rec',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../views/Medical/tx_record.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/yz_linshi',
  //   hidden: true,
  //   index: 'yz_linshi',
  //   meta: {
  //     title: '临时医嘱',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'yz_linshi',
  //       path: '/',
  //       meta: {
  //         title: 'yz_linshi',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../views/Medical/tem_order.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/doctor',
  //   hidden: true,
  //   index: 'doctor',
  //   meta: {
  //     title: '医生工作平台',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'doctor',
  //       path: '/',
  //       meta: {
  //         title: 'doctor',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../components/page/doctor.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/patientinfo',
  //   hidden: true,
  //   index: 'doctor',
  //   meta: {
  //     title: '患者管理',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'patientinfo',
  //       path: '/',
  //       meta: {
  //         title: 'patientinfo',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../components/page/patient.vue'], resolve)
  //     }
  //   ]
  // },
  // {
  //   path: '/nurse_detail',
  //   hidden: true,
  //   index: 'nurse_detail',
  //   meta: {
  //     title: '护士工作平台',
  //     icon: 'el-icon-menu'
  //   },
  //   component: resolve => require(['../components/common/Home.vue'], resolve),
  //   children: [
  //     {
  //       name: 'nurse_detail',
  //       path: '/',
  //       meta: {
  //         title: 'nurse_detail',
  //         icon: 'el-icon-menu'
  //       },
  //       component: resolve => require(['../components/page/nurse_detail.vue'], resolve)
  //     }
  //   ]
  // },
  {
    path: '/Readme',
    index: 'Readme',
    meta: {
      title: '预约登记签到',
      icon: 'el-icon-phone'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'txReadme',
        path: '/Readme',
        meta: {
          title: '预约登记签到子菜单',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/Readme.vue'], resolve)
      }
    ]
  },

  {
    path: '/schedule',
    index: 'Readme',
    meta: {
      title: '权限',
      icon: 'el-icon-menu'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'Readme',
        path: '/depart',
        meta: {
          title: '部门管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/department.vue'], resolve)
      },
      {
        name: 'Readme',
        path: '/user',
        meta: {
          title: '员工管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/user.vue'], resolve)
        // component: resolve => require(['../components/page/schedule/selectPatient.vue'], resolve)
      },
      {
        name: 'Readme',
        path: '/role',
        meta: {
          title: '角色管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/role.vue'], resolve)
      }
    ]
  }
]

export default new Router({
  routes: constantRouterMap
})
// 异步挂载的路由
// 动态需要根据权限加载的路由表
export const asyncRouterMap = [
 {
    path: '/schedule',
    index: 'Readme',
    meta: {
      title: '排班',
      icon: 'el-icon-menu'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'Readme',
        path: '/odddual',
        meta: {
          title: '单双周排班',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/odddual.vue'], resolve)
      },
      {
        name: 'Readme',
        path: '/day',
        meta: {
          title: '按日期排班',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/schedule/day.vue'], resolve)
      }
    ]
  },
  {
    path: '/permission',
    meta: {
      title: '医疗管理',
      icon: 'el-icon-share'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'txpermission',
        path: '/permission',
        meta: {
          title: '医生工作平台',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/permission.vue'], resolve)
      },
      {
        path: '/jiaobanPatient',
        meta: {
          title: '医生交班记录',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/doctor/jiaobanPatient.vue'], resolve)
      },
      {
        path: '/patient',
        meta: {
          title: '患者管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/doctor/patient.vue'], resolve)
      },
      {
        path: '/txpgSpkt',
        meta: {
          title: '透析评估',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/doctor/txpgSpkt.vue'], resolve)
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
        meta: {
          title: '护士交班记录',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/nurse/jiaobanPatient.vue'], resolve)
      },
      {
        path: '/jiaobanDevice',
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
        name: 'txmedical_report',
        path: '/medical_report',
        meta: {
          title: '电子病历',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/medical_report.vue'], resolve)
      },
      {
        name: 'txexpense',
        path: '/expense',
        meta: {
          title: '费用管理',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/expense.vue'], resolve)
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
      icon: 'el-icon-search'
    },
    component: resolve => require(['../components/common/myHome.vue'], resolve),
    children: [
      {
        path: '/countTxTypeByYear',
        meta: {
          title: '透析方式按年分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/txTypeByYear.vue'], resolve)
      },
      {
        path: '/countTxTypeBymonth',
        meta: {
          title: '透析方式按月分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/txTypeBymonth.vue'], resolve)
      },
      {
        path: '/deviceByYear',
        meta: {
          title: '透析器按年分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/deviceByYear.vue'], resolve)
      },
      {
        path: '/deviceBymonth',
        meta: {
          title: '透析器按月分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/deviceBymonth.vue'], resolve)
      },
      {
        path: '/operateByYear',
        meta: {
          title: '手术分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/operateByYear.vue'], resolve)
      },
      {
        path: '/analyseBykind',
        meta: {
          title: '分类分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseBykind.vue'], resolve)
      },
      {
        path: '/analyseFirstTx',
        meta: {
          title: '首次透析分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseFirstTx.vue'], resolve)
      },
      {
        path: '/analysePTH',
        meta: {
          title: '甲状旁腺分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analysePTH.vue'], resolve)
      },
      {
        path: '/analyseCaP',
        meta: {
          title: '钙磷乘积分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseCaP.vue'], resolve)
      },
      {
        path: '/AlarmLab',
        meta: {
          title: '检验预警分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/AlarmLab.vue'], resolve)
      },
      {
        path: '/analyseBfzBymonth',
        meta: {
          title: '并发症分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseBfzBymonth.vue'], resolve)
      },
      {
        path: '/analyseBloodPressure',
        meta: {
          title: '血压异常分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseBloodPressure.vue'], resolve)
      },
      {
        path: '/analyseByYuanfa',
        meta: {
          title: '原发病分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseByYuanfa.vue'], resolve)
      },
      {
        path: '/analyseZhuangui',
        meta: {
          title: '转归分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseZhuangui.vue'], resolve)
      },
      {
        path: '/analyseZhengzhuang',
        meta: {
          title: '症状分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseZhengzhuang.vue'], resolve)
      },
      {
        path: '/analyseDrugByyear',
        meta: {
          title: '药品分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseDrugByyear.vue'], resolve)
      },
      {
        path: '/analyseMaterialByyear',
        meta: {
          title: '耗材分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseMaterialByyear.vue'], resolve)
      },
      {
        path: '/analysedrug',
        meta: {
          title: '药品明细汇总',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analysedrugDetail.vue'], resolve)
      },
      {
        path: '/analysematerial',
        meta: {
          title: '耗材明细汇总',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseMaterialDetail.vue'], resolve)
      },
      {
        path: '/analyseDrugstock',
        meta: {
          title: '药品出入库分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseDrugstock.vue'], resolve)
      },
      {
        path: '/analyseMaterialstock',
        meta: {
          title: '耗材出入库分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseMaterialstock.vue'], resolve)
      },
      {
        path: '/analyseDeptCharge',
        meta: {
          title: '科室收费分析',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../views/analysis/analyseDeptCharge.vue'], resolve)
      },
      {
        path: '/deptChargeBymonth',
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
    meta: {
      title: '系统管理',
      icon: 'el-icon-setting'
    },
    component: resolve => require(['../components/common/Home.vue'], resolve),
    children: [
      {
        name: 'txsystem',
        path: '/system',
        meta: {
          title: '透析套餐',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['../components/page/system.vue'], resolve)
      },
      {
        path: '/diseasedurationDict',
        meta: {
          title: '病程模板字典',
          icon: 'el-icon-menu'
        },
        component: resolve => require(['@/views/system/diseasedurationDict.vue'], resolve)
      }
    ]
  },
  { path: '*',
    redirect: '/404',
    hidden: true
  }
]
