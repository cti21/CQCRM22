import { asyncRouterMap, constantRouterMap } from '@/router'
import Vue from 'vue'
import store from '../index'
import getters from '../getters'
/**
 * 通过meta.role判断是否与当前用户权限匹配
 * @param roles
 * @param route
 */
function hasPermission(roles, route) {
  if (route.meta && route.meta.roles) {
    return roles.some(role => route.meta.roles.indexOf(role) >= 0)
  } else {
    return true
  }
}

/**
 * 递归过滤异步路由表，返回符合用户角色权限的路由表
 * @param asyncRouterMap
 * @param roles
 */
function filterAsyncRouter(asyncRouterMap, roles) {
  const accessedRouters = asyncRouterMap.filter(route => {
    if (hasPermission(roles, route)) {
      if (route.children && route.children.length) {
        route.children = filterAsyncRouter(route.children, roles)
      }
      return true
    }
    return false
  })
  return accessedRouters
}

const permission = {
  state: {
    routers: constantRouterMap,
    addRouters: [],
    perms: [],
    menus: []
  },
  mutations: {
    SET_ROUTERS: (state, routers) => {
      state.addRouters = routers
      state.routers = constantRouterMap.concat(routers)
    },
    SET_PERMS: (state, perms) => {
      state.perms = perms
    },
    SET_MENUS: (state, perms) => {
      state.menus = perms
    }
  },

  actions: {
    GenerateRoutes({ commit }) {
      return new Promise(resolve => {
        let accessedRouters = []
        const userrouter = store.getters.menus
        const fullroute = asyncRouterMap

        let hashMenus = {}
        let hashKey = ''

        let setMenu2Hash = function(array, base) {
        // base 基目錄
          array.map(key => {
            if (key.path) {
              hashKey = ''
              hashKey =  ((base ? base + '/' : '') + key.path).replace(/^\//, '')
              hashKey=hashKey.replace('//', '/')
              if (typeof(hashMenus[hashKey]) === 'undefined')
                hashMenus['/' + hashKey] = true
              if (Array.isArray(key.children)) {
                setMenu2Hash(key.children, key.path)
              }
            }
          })
        }

        setMenu2Hash(userrouter)

        let findLocalRoute = function(array, base) {
          let replyResult = []
          array.forEach(function(route) {
            let pathKey = (base ? base + '/' : '') + route.path;
            pathKey=pathKey.replace('//','/')
            if (hashMenus[pathKey]) {
              if (Array.isArray(route.children)) {
                route.children = findLocalRoute(route.children, route.path)
              }
              replyResult.push(route)
            }
          })
          if (base) {
            return replyResult
          } else {
            accessedRouters = accessedRouters.concat(replyResult)
          }
        }

        findLocalRoute(fullroute)
        const resourcePermission = store.getters.perms
        Vue.prototype.$_has = function(rArray) {
          let permission = true
          if (!resourcePermission[rArray.value.p[0]])
            permission = false
          return permission
        }
        commit('SET_ROUTERS', accessedRouters)
        resolve()
      })
    }
  }


}

export default permission
