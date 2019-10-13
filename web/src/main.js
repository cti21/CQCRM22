/* jshint esversion: 6 */
'use strict'
import Vue from 'vue'
import Vuex from 'vuex'
import App from './App'
import router from './router'
import store from './store'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import '@/assets/icon/iconfont.css'
import './icons'
import '@/permission' // permission control
import 'babel-polyfill'
import './iconfont/iconfont.css'

Vue.use(Vuex)
Vue.use(ElementUI)

Vue.config.productionTip = false

Vue.directive('has',
  {
    bind: function(el,binding) {
      if (!Vue.prototype.$_has(binding)) {
        el.parentNode.removeChild(el)
      }
    }
  })

Vue.prototype.checkUserPerm = (modname, action, arr) => {
  const result = arr.some((item, index, arr) => {
    return item.rights.modName === modname && item.rights.name === action
  })
  return result
}

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
