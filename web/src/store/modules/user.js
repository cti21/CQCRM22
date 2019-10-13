'use strict'
import { login, logout, getInfo } from '@/api/login'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { Message } from 'element-ui'
import store from '../../store/index'
import router from '../../router'
const user = {
  state: {
    token: getToken(),
    name: '',
    avatar: '',
    roles: [],
    departments: [],
    /* 导航菜单是否折叠 */
    isSidebarNavCollapse: false,
    /* 面包屑导航列表 */
    crumbList: []
  },

  mutations: {
    SET_TOKEN: (state, token) => {
      state.token = token
      console.log('token:', token)
      store.dispatch('GetInfo').then(res => { // 拉取用户信息
        const roles = res.data.roles // note: roles must be a array! such as: ['editor','develop']

      }).catch(() => {
        store.dispatch('FedLogOut').then(() => {
          Message.error('验证失败,请重新登录')
          // next({ path: '/login' })
        })
      })

    },
    SET_NAME: (state, name) => {
      state.name = name
    },
    SET_AVATAR: (state, avatar) => {
      state.avatar = avatar
    },
    SET_ROLES: (state, roles) => {
      state.roles = roles
    },
    SET_DEPARTMENTS: (state, dep) => {
      state.departments = dep
    }
  },

  actions: {
    // 登录
    Login({ commit }, userInfo) {
      const username = userInfo.username.trim()
      return new Promise((resolve, reject) => {
        login(username, userInfo.password).then(response => {
          const data = response.data
          setToken(data.token)
          commit('SET_TOKEN', data.token)
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },

    // 获取用户信息
    GetInfo({ commit, state }) {
      return new Promise((resolve, reject) => {
        getInfo(state.token).then(response => {
          const data = response.data
          const rd = data.UserRouterMap
          const btns = data.UserBtn
          const deps = data.UseDept
          const menu_permission = []
          console.log('UserRouterMap:', rd)
          for (const item in rd) {
            let menuitem = {}
            let exist = 0
            for (menuitem in menu_permission) {
              if ((menu_permission[menuitem]['path'] === rd[item].groupmenu.path) && (rd[item].isvisible === true)) {
                const childmenu = {}
                childmenu.path = rd[item].path
                childmenu.component = ''
                menu_permission[menuitem]['children'].push(childmenu)
                exist = 1
                break
              }
            }
            if ((exist === 0) && (rd[item].groupmenu.isvisible === true)) {
              const m = {}
              m['path'] = rd[item].groupmenu.path
              m['component'] = ''
              m['children'] = []

              if (rd[item].isvisible === true) {
                const childmenu = {}
                childmenu.path = rd[item].path
                childmenu.component = ''
                m['children'].push(childmenu)
              }
              menu_permission.push(m)
            }
          }
          commit('SET_MENUS', menu_permission)
          commit('SET_PERMS', btns)
          commit('SET_DEPARTMENTS', deps)
          // console.log('UseDept:', store.getters.departments)
          store.dispatch('GenerateRoutes').then(() => { // 根据roles权限生成可访问的路由表
            const r = store.getters.addRouters
            console.log('addRouters:', r)
            router.addRoutes(store.getters.addRouters) // 动态添加可访问路由表
            router.replace({ path: '/mainpage' })
          })
          commit('SET_ROLES', data.roles)
          commit('SET_NAME', data.name)
          commit('SET_AVATAR', data.avatar)
          resolve(response)
        }).catch(error => {
          reject(error)
        })
      })
    },

    // 登出
    LogOut({ commit, state }) {
      return new Promise((resolve, reject) => {
        logout(state.token).then(() => {
          commit('SET_ROLES', [])
          removeToken()
          resolve()
        }).catch(error => {
          reject(error)
        })
      })
    },

    // 前端 登出
    FedLogOut({ commit }) {
      return new Promise(resolve => {
        commit('SET_TOKEN', '')
        removeToken()
        resolve()
      })
    }
  }
}

export default user
