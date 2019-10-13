/**
 * Created by david on 2018/7/31.
 */
import request from './request.js'

//  新增用户
export function addUser(data) {
  return request({
    url: 'api/muser/',
    method: 'post',
    params:  data
  })
}

// 得到用户列表
export function getUserList(data) {
  return request({
    url: 'api/muser/',
    method: 'get',
    params:  data
  })
}

// // 得到某部门用户列表
// export function getUserListFromDept(data) {
//   return request({
//     url: `api/user/` + data.deptname + `/`,
//     method: 'get',
//     params:  data
//   })
// }

// 得到某个用户
export function getUser(data) {
  return request({
     url: `api/muser/` + data.id + `/`,
    method: 'get',
    params:  data
  })
}

// 更新用户
export function updateUser(data) {
   return request({
    url: `api/muser/` + data.id + `/`,
    method: 'put',
    data: data
  })
}
// 删除用户
export function deleteUser(data) {
  return request({
    url: `api/muser/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

//  新增部门
export function addDept(data) {
  return request({
    url: 'api/dept/',
    method: 'post',
    data: {
      name: data.name
    }
  })
}

// 得到部门
export function getDeptList(data) {
  return request({
    url: 'api/dept/',
    method: 'get',
    params: data
  })
}
// 得到某个部门
export function getDept(data) {
  return request({
    url: `api/dept/` + data.id + `/`,
    method: 'get',
    data: data
  })
}

// 得到部门名称列表，select
export function getDeptNameList(data) {
  return request({
    url: 'api/deptnamelist/',
    method: 'get',
    data: data
  })
}

// 更新部门
export function updateDept(data) {
  return request({
    url: `api/dept/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 删除部门
export function deleteDept(data) {
  return request({
    url: `api/dept/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

//  新增角色
export function addRole(data) {
  return request({
    url: 'api/role/',
    method: 'post',
    params: data
  })
}

// 得到角色
export function getRoleList(data) {
  return request({
    url: 'api/role/',
    method: 'get',
    params: data
  })
}
// 得到某个角色
export function getRole(data) {
  return request({
    url: `api/role/` + data.id + `/`,
    method: 'get',
    data: data
  })
}

// 更新部门
export function updateRole(data) {
  return request({
    url: `api/role/` + data.id + `/`,
    method: 'put',
    data: data
  })
}

// 删除部门
export function deleteRole(data) {
  return request({
    url: `api/role/` + data.id + `/`,
    method: 'delete',
    data: data
  })
}

// 设置某角色的菜单
export function setRoleMenu(data) {
  return request({
    url: `api/groupmenu/`,
    method: 'post',
    data: data
  })
}

// 得到某个角色的菜单权限
export function GetRoleMenu(data) {
   return request({
    url: `api/groupmenu/?roleid=` + data.id ,
    method: 'get',
    data: data
  })
}

// export function GetRoleMenu(data) {
//    return request({
//     url: `api/groupmenu/` + data.id + `/`,
//     method: 'get',
//     data: data
//   })
// }
// 得到所有角色 ，所有菜单
export function getRoleMenuList(data) {
  return request({
    url: `api/groupmenu/`,
    method: 'get',
    data: data
  })
}
// 得到所有部门，所有角色
export function getDepRoletList(data) {
  return request({
    url: `api/deptgroup/`,
    method: 'get',
    data: data
  })
}

// 得到特定部门的所有角色
export function GetDeptRole(data) {
  return request({
    url: `api/deptgroup/?deptid=` + data.id,
    method: 'get',
    data: data
  })
}

// 设置某部门的角色
export function setDeptRole(data) {
  return request({
    url: `api/deptgroup/`,
    method: 'post',
    data: data
  })
}


