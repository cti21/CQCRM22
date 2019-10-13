/* jshint esversion: 6 */
/* jslint node:true */
'use strict'
import axios from 'axios'
import { removeToken } from '@/utils/auth'
import router from '../router'
import store from '../store'
import { getToken } from '@/utils/auth'

// 创建axios实例
const service = axios.create({
  // baseURL: process.env.BASE_API, // api的base_url
  // baseURL: 'http://127.0.0.1:8000',
  baseURL: 'http://127.0.0.1:8000',
  timeout: 1500000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(config => {
  if (store.getters.token) {
    // config.headers['X-Token'] = getToken() // 让每个请求携带自定义token 请根据实际情况自行修改
    config.headers['Authorization'] = 'JWT ' + getToken()
  }
  return config
}, error => {
  // Do something with request error
  console.log('request:', error) // for debug
  Promise.reject(error)
})

// respone拦截器
service.interceptors.response.use(
  response => response,
  error => {
    if (error.response) {
      if (error.response.status === 401) {
        removeToken()
        router.replace( {path: '/login'} )
      }
    }
    return Promise.reject(error)
  }
)

export default service
