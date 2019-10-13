<template>
    <div>
        <div class="filter-container">
              <el-select v-model="banci" clearable style="width: 120px" class="myInput" placeholder="班次">
                <el-option v-for="item in banciSelect" :key="item.id" :value="item.name" :label="item.name">
                </el-option>
              </el-select>
              <el-select v-model="diseaseArea" clearable style="width: 120px" class="myInput" placeholder="病区">
                <el-option v-for="item in diseaseAreaSelect" :key="item.id" :value="item.name" :label="item.name">
                </el-option>
              </el-select>
              <el-input
                v-model="name"
                @keyup.enter.native="handleFilter"
                style="width: 120px;margin-right: 10px;"
                class="myInput"
                placeholder="患者姓名/编号">
              </el-input>
              <el-button size="medium" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="medium" type="primary" @click="handleCreate" icon="el-icon-plus">患者导入</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            stripe
            v-loading="listLoading"
            :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
            :header-cell-style="{background:'#F8F8F8'}"
            >
            <el-table-column type="index" label="序号"  width="80" align="left">
            </el-table-column>
            <el-table-column prop="isContagion" v-if="false" width="80">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="90" align="left">
              <template slot-scope="scope">
                  <span v-if="scope.row.isContagion===0">{{scope.row.name}}</span>
                  <span v-else style="color: red">{{'* '+ scope.row.name}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="patient" label="编号" v-if="false" width="80">
            </el-table-column>
            <el-table-column prop="area" label="病区" width="90" align="left">
            </el-table-column>
            <el-table-column prop="bedno" label="床位" width="90" align="left">
            </el-table-column>
            <el-table-column prop="flag" label="状态" width="90" align="left" :formatter="formatFlag">
            </el-table-column>
            <el-table-column prop="txtype" label="治疗项目" width="100" align="left">
            </el-table-column>
            <el-table-column prop="reg_id" label="注册号" v-if="false" width="90">
            </el-table-column>
            <el-table-column prop="xuetoudevice" label="净化器" width="120" align="left">
            </el-table-column>
            <el-table-column prop="status" label="上机状态" width="100">
            </el-table-column>
            <el-table-column prop="startdate" label="开始" width="90" :formatter="dateFormat" align="left">
            </el-table-column>
            <el-table-column prop="enddate" label="结束" width="90" :formatter="dateFormat" align="left">
            </el-table-column>
            <el-table-column prop="recnum" label="记录次数" width="100">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="left">
              <template slot-scope="scope">
                  <el-button
                    type="text" size="small" v-if="checkUserPerm('nurse', 'add', $store.getters.perms)"
                    @click="handleValue(scope.row)">透前评估</el-button>
                  <el-button type="text" size="small" @click="handleDetail(scope.row)">详情</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 10px;float:right;margin-right: 40px">
            <el-pagination
              background
              @current-change="handleCurrentChange"
              :current-page="listQuery.page"
              :page-sizes="[5,10,20,30, 50]"
              :page-size="listQuery.limit"
              layout="total, prev, pager, next"
              :total="total">
            </el-pagination>
          </div>
        </div>

        <div>
          <el-dialog  title="患者管理" width="60%" :visible.sync="dialogFormVisible">
            <div style="float: right;margin-right: 30px;margin-bottom: 20px;">
              <el-input
                v-model="pname"
                @keyup.enter.native="pat_handleFilter"
                suffix-icon="el-icon-search"
                style="width: 300px;margin-right: 10px;"
                class="myInput"
                placeholder="请输入患者姓名/编号">
              </el-input>
            </div>
            <el-table :data="pat_list" v-loading="pat_listLoading" highlight-current-row>
              <el-table-column prop="name" label="姓名" width="90" align="center">
              </el-table-column>
              <el-table-column prop="patientid" label="编号"  width="90" align="center">
              </el-table-column>
              <el-table-column prop="sex" label="性别" width="80" align="center">
              </el-table-column>
              <el-table-column prop="age" label="年龄" width="80" align="center">
              </el-table-column>
              <el-table-column prop="phone1" label="电话" width="120" align="center">
              </el-table-column>
              <el-table-column prop="address" label="地址" width="240" align="center">
              </el-table-column>
              <el-table-column label="操作" fixed="right">
                <template slot-scope="scope">
                  <el-button type="text" @click="pat_handleImport(scope.row)">导入</el-button>
                </template>
              </el-table-column>
            </el-table>
            <div class="pagination-container" style="margin-top: 15px;margin-bottom: 20px" align="right">
                <el-pagination background
                     @current-change="pat_handleCurrentChange"
                     :current-page="pat_listQuery.page"
                     :page-size="pat_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="pat_total">
                </el-pagination>
            </div>
          </el-dialog>
        </div>

        <!--透前评估-->
        <div>
          <el-dialog  title="透前评估" width="55%" :visible.sync="dialogVisible">
            <el-card>
              <div slot="header" class="clearfix">
                  <span>信息</span>
                  <el-button
                    size="small"
                    type="primary"
                    style="float: right;margin-right: 50px;padding-top: 5px"
                    icon="iconfont iconbaocun"
                    @click="updateData_pre">保存
                  </el-button>
              </div>
              <el-form :model="register" ref="preForm" label-position="left" style='width:100%; margin-left:25px;' size="mini">
                  <el-row type="flex" justify="end">
                     <el-col :span="12">
                        <el-form-item label="前次透析并发症" prop="prebfz">
                          <el-input v-model="register.prebfz"  class="myInput" style="width:50%">
                          </el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="合并症" prop="hbz">
                          <el-input v-model="register.hbz"  class="myInput" style="width:70%"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                  <el-row  type="flex">
                    <el-col :span="6">
                        <el-form-item label="干体重" prop="ganweight">
                          <el-input v-model="register.ganweight"  class="myInput" style="width:30%"></el-input>
                        </el-form-item>
                     </el-col>
                    <el-col :span="6">
                      <el-form-item label="上次透后体重" prop="thweight">
                          <el-input v-model="register.thweight"  class="myInput" style="width:90px"></el-input>
                        </el-form-item>
                    </el-col>
                    <el-col :span="6">
                        <el-form-item label="本次透前体重" prop="tqweight">
                          <el-input v-model="register.tqweight"  class="myInput" style="width:90px"></el-input>
                        </el-form-item>
                     </el-col>
                    <el-col :span="6">
                        <el-form-item label="体温()" prop="tw">
                          <el-input v-model="register.tw"  class="myInput" style="width:90px"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row type="flex">
                    <el-col :span="6">
                        <el-form-item label="呼吸" prop="hx">
                         <el-input v-model="register.hx"  class="myInput" style="width:90px"></el-input>
                        </el-form-item>
                     </el-col>
                    <el-col :span="6">
                       <el-form-item label="心率:" prop="xl">
                          <el-input v-model="register.xl"   class="myInput" style="width:80px"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="血压:">
                          <el-input v-model="register.dxy"  class="myInput" style="width:120px"></el-input>
                          /
                          <el-input v-model="register.gxy" class="myInput" style="width:120px"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row type="flex">
                     <el-col :span="24">
                       <el-form-item label="患者症状:" prop="zz" >
                          <el-select multiple v-model="register.zz" clearable style="width: 80%" class="myInput" placeholder="请选择">
                            <el-option v-for="(item,index) in bingfazhengSel" :key="index" :value="item.id" :label="item.name">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                   </el-row>
              </el-form>
           </el-card>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import doctor from '@/components/page/doctor.vue'
import { Register_Nur, patient_Drug, createPatient, updatePatient,
  PatientsToRegister, register_pres, updateRegister_pre, bingfazheng } from '@/api/login'
import { banci, diseaseArea } from '@/api/system'
import { getToken } from '@/utils/auth'
import moment from 'moment'
import ElCol from 'element-ui/packages/col/src/col'
import ElRow from 'element-ui/packages/row/src/row'
import ElTabPane from '../../../node_modules/element-ui/packages/tabs/src/tab-pane'
import ElSlPanel from '../../../node_modules/element-ui/packages/color-picker/src/components/sv-panel'
import ElFormItem from '../../../node_modules/element-ui/packages/form/src/form-item'
import ElRadioGroup from '../../../node_modules/element-ui/packages/radio/src/radio-group'
import ElCheckboxGroup from '../../../node_modules/element-ui/packages/checkbox/src/checkbox-group'
import ElCheckbox from '../../../node_modules/element-ui/packages/checkbox/src/checkbox'
import ElInput from '../../../node_modules/element-ui/packages/input/src/input'
import ElIcon from '../../../node_modules/element-ui/packages/icon/src/icon'

export default {
  components: {
    ElIcon,
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    doctor
  },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        diseaseArea: '',
        banci: '',
        sort: '+id'
      },
      pat_list: null,
      pat_total: null,
      pat_listLoading: true,
      pat_listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        patientid: undefined,
        sort: '+id'
      },
      banciSelect: [],
      bingfazhengVal: [],
      bingfazhengSel: [],
      banci: '',
      diseaseArea: '',
      diseaseAreaSelect: [],
      name: '',
      pname: '',
      multiplePatients: [],
      token: getToken,
      detailFormVisible: false,
      dialogFormVisible: false,
      dialogVisible: false,
      dialogStatus: '',
      register_id: '',
      patient_id: '',
      register: {
        id: null,
        prebfz: '',
        hbz: '',
        zz: [],
        ganweight: '',
        tqweight: '',
        thweight: '',
        tiwen: '',
        xinlv: '',
        huxi: '',
        xueya: '',
        dixueya: '',
        weight: '',
        tw: '',
        xl: '',
        hx: '',
        gxy: '',
        dxy: ''
      },
      patient: {
        id: undefined,
        patientid: undefined,
        name: '',
        sex: '',
        adddate: new Date(),
        phone1: ''
      }
    }
  },
  methods: {
    getScheduleList(data) {
      Register_Nur(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getRegister_pre(data) {
      this.bingfazhengVal = []
      register_pres(data).then(response => {
        const mdata = response.data.results
        if (mdata.length > 0) {
          this.register = mdata[0]
          this.dialogVisible = true
          this.$nextTick(() => {
          })
        }
      })
    },
    getPatients(data) {
      patient_Drug(data).then(response => {
        this.pat_listLoading = true
        this.pat_list = response.data.results
        this.pat_total = response.data.count
        this.pat_listLoading = false
      })
    },
    getBingfazheng() {
      const par = {
        page: 1,
        kind: 1
      }
      bingfazheng(par).then(response => {
        this.bingfazhengSel = response.data.results
      })
    },
    getBanciList(data) {
      banci(data).then(response => {
        this.banciSelect = response.data.results
      })
    },
    getDiseaseAreaList(data) {
      diseaseArea(data).then(response => {
        this.diseaseAreaSelect = response.data.results
      })
    },
    selectChange: function(val) {
      if (val) {
        this.multiplePatients = []
        this.multiplePatients = val
      }
    },
    pat_handleImport(row) {
      const pid = row.patientid
      PatientsToRegister(pid).then(() => {
        this.$notify({
          title: '成功',
          message: '导入成功',
          type: 'success',
          duration: 2000
        })
        this.getScheduleList(this.listQuery)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.diseaseArea = this.diseaseArea
      this.listQuery.banci = this.banci
      this.listQuery.name = this.name
      this.getScheduleList(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getScheduleList(this.listQuery)
    },
    pat_handleFilter() {
      this.pat_listQuery.page = 1
      this.pat_listQuery.patientid = this.pname
      this.getPatients(this.pat_listQuery)
    },
    pat_handleCurrentChange(val) {
      this.pat_listQuery.page = val
      this.pat_listQuery.offset = (val - 1) * this.pat_listQuery.limit
      this.getPatients(this.pat_listQuery)
    },
    resetPatient() {
      this.patient = {
        id: undefined,
        patientid: undefined,
        name: '',
        sex: '',
        adddate: new Date(),
        phone1: ''
      }
    },
    handleCreate() {
      this.resetPatient()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.patient.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createPatient(this.patient).then(() => {
            this.list.unshift(this.patient)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDetail(row) {
      this.$router.push({
        path: '/doctor',
        query: { register_id: row.reg_id,patientid: row.patient }
      })
    },
    handleValue(row) {
      const par = {
        register_id: row.reg_id
      }
      this.getRegister_pre(par)
    },
    handleUpdate(row) {
      patient_Drug(row.patient.patientid).then(response => {
        this.patient = response.data.results[0]
        this.dialogStatus = 'update'
        this.dialogFormVisible = true
        this.$nextTick(() => {
        })
      })
    },
    updateData_pre() {
      const tempData = Object.assign({}, this.register)
      tempData.weight = this.register.tqweight
      tempData.tiwen = tempData.tw
      tempData.huxi = tempData.hx
      tempData.xinlv = tempData.xl
      tempData.dixueya = tempData.dxy
      tempData.xueya = tempData.gxy
      updateRegister_pre(tempData).then(() => {
        this.dialogVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.patient)
          tempData.adddate = +new Date(tempData.adddate) //
          updatePatient(tempData).then(() => {
            for (const v of this.list) {
              if (v.id === this.patient.id) {
                const index = this.list.indexOf(v)
                this.list.splice(index, 1, this.patient)
                break
              }
            }
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    handleDelete(row) {
      this.$notify({
        title: '成功',
        message: '删除成功',
        type: 'success',
        duration: 2000
      })
      const index = this.list.indexOf(row)
      this.list.splice(index, 1)
    },
    formatFlag: function(row, column) {
      const qd = row.flag
      let s = ''
      switch (qd) {
        case false:
          s = '待签到'
          break
        case true:
          s = '已签到'
          break
      }
      return s
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined || date === null || date === '') {
        return ''
      } else {
        return moment(date).format('HH:mm:ss')
      }
    }
  },
  created: function() {
    this.getScheduleList(this.listQuery)
    this.getPatients(this.pat_listQuery)
    this.getBanciList('')
    this.getDiseaseAreaList('')
    this.getBingfazheng()
  }
}
</script>

<style>
    .ms-doc{
        width:100%;
        max-width: 980px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    }
    .ms-doc h3{
        padding: 9px 10px 10px;
        margin: 0;
        font-size: 14px;
        line-height: 17px;
        background-color: #f5f5f5;
        border: 1px solid #d8d8d8;
        border-bottom: 0;
        border-radius: 3px 3px 0 0;
    }
    .ms-doc article{
        padding: 45px;
        word-wrap: break-word;
        background-color: #fff;
        border: 1px solid #ddd;
        border-bottom-right-radius: 3px;
        border-bottom-left-radius: 3px;
    }
    .ms-doc article h1{
        font-size:32px;
        padding-bottom: 10px;
        margin-bottom: 15px;
        border-bottom: 1px solid #ddd;
    }
    .ms-doc article h2 {
        margin: 24px 0 16px;
        font-weight: 600;
        line-height: 1.25;
        padding-bottom: 7px;
        font-size: 24px;
        border-bottom: 1px solid #eee;
    }
    .ms-doc article p{
        margin-bottom: 15px;
        line-height: 1.5;
    }
    .ms-doc article .el-checkbox{
        margin-bottom: 5px;
    }
    .myInput .el-input__inner{
        height: 33px;
        border-top-width: 0px;
        border-left-width: 0px;
        border-right-width: 0px;
        border-bottom-width: 1px;
    }
    .el-table td, .el-table th{
      padding:8px 0;
    }
    .el-table__header td,.el-table__header th{
      padding:8px 0px;
    }
    .el-dialog__body {
        padding: 0px 20px 15px 20px;
    }
</style>
