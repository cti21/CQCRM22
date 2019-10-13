const getters = {
  token: state => state.user.token,
  name: state => state.user.name,
  avatar: state => state.user.avatar,
  routers: state => state.permission.routers,
  addRouters: state => state.permission.addRouters,
  roles: state => state.user.roles,
  perms: state => state.permission.perms,
  menus: state => state.permission.menus,
  departments: state => state.user.departments,

  // 排班
  patientid: state => state.schedule.patientid,
  patientname: state => state.schedule.patientname,
  patientsex: state => state.schedule.patientsex,
  patient_week: state => state.schedule.patient_week,
  odddual_week: state => state.schedule.odddual_week,
  patient_roomno: state => state.schedule.patient_roomno,
  patient_bedno: state => state.schedule.patient_bedno,
  isShow2: state => state.schedule.isShow2,
  schedule_patient2: state => state.schedule.schedule_patient2

}
export default getters
