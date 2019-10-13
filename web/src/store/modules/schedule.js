import Vue from 'vue';
import store from "../index";
import getters from '../getters'

const schedule = {

 state : {
    patientid:'',
    patientname:'',
    patientsex:'',
    patient_week:'',
    patient_roomno:'',
    patient_bedno:'',
    odddual_week:0,
    isShow2:false,
    schedule_patient2:''
},

//////////////////////////////////////////////////////
// actions 异步测试
 actions : {
    asyncMul(context,payload){
        //返回promise给触发的store.dispatch
        return new Promise((resolve,reject) => {
            setTimeout(() => {
                context.commit('multiplication',payload)
                resolve("async over")
            },5000)
        })
    },


   actiona({dispatch,commit},payload){
       return dispatch('asyncMul',payload).then(() => {
            commit('multiplication',payload);
            return "async over";
       })
    },
     // actiona 的另一种写法
    async actionb({dispatch,commit},payload){
        await dispatch('asyncMul',payload);
        commit('multiplication',payload);
    }
},

/////////////////////////////////////////////////////
// 定义 mutations ，处理状态（数据） 的改变
 mutations :{
    //与上方 commit 中的 ‘increment’ 相对应
    increment(state,payload){
         state.count += payload.n;
    },
    panban_patient(state,payload){
         state.patientid = payload.patientid
         state.patientname =  payload.patientname
         state.patientsex =  payload.patientsex
    },
    patient_week(state,payload){
      state.patient_week = payload.patient_week
      state.patient_roomno = payload.patient_roomno
      state.patient_bedno = payload.patient_bedno
      state.odddual_week = payload.odddual_week
  },
   setpopmenu(state,payload){
      state.isShow2 = payload.isShow2
      state.schedule_patient2 = payload.schedule_patient2
  }
}

}

// 导出 store 对象
export default schedule;
