import Vue from 'vue'
import Vuex from 'vuex'
import user from './modules/user'
import getters from './getters'
import permission from './modules/permission'
import schedule from './modules/schedule'

Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    user,
    permission,
    schedule
  },
  getters
})

export default store
