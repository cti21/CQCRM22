<template>
    <div>
        <div style="margin-top: 10px;margin-bottom: 20px">
              <el-row type="flex">
                 <el-col :span="6" style="margin-left: 10px">
                   <label class="el-form-item__label">姓名</label>
                   <el-input v-model="patient.patient.name"  class="myInput el-form-item__content" style="width:90px"></el-input>
                 </el-col>
                 <el-col :span="6">
                    <label class="el-form-item__label">性别</label>
                    <el-input v-model="patient.patient.sex"  class="myInput el-form-item__content" style="width:60px"></el-input>
                 </el-col>
                <el-col :span="6">
                    <label class="el-form-item__label">年龄</label>
                    <el-input v-model="patient.patient.age"  class="myInput el-form-item__content" style="width:50px"></el-input>
                 </el-col>
                <el-col :span="6">
                    <label class="el-form-item__label">费用</label>
                    <el-input v-model="patient.charge"  class="myInput el-form-item__content" style="width:80px"></el-input>
                 </el-col>
                <el-col :span="6">
                    <label class="el-form-item__label">押金总额</label>
                    <el-input v-model="patient.balance"  class="myInput el-form-item__content" style="width:80px"></el-input>
                 </el-col>
                <el-col :span="6">
                    <label class="el-form-item__label">余额</label>
                    <el-input v-model="yue"  class="myInput el-form-item__content" style="width:80px"></el-input>
                 </el-col>
              </el-row>
        </div>
        <div class="filter-container">
              <el-date-picker
                v-model="searchStartyear"
                style="width:180px"
                class="myInput"
                type="date"
                placeholder="输入开始时间"
                value-format="yyyy-MM-dd">
              </el-date-picker>
              <el-date-picker
                v-model="searchEndyear"
                style="width:180px" class="myInput"
                type="date"
                :picker-options="pickerOptions1"
                placeholder="输入结束时间"
                value-format="yyyy-MM-dd">
              </el-date-picker>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;margin-right: 5px" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
              <el-checkbox v-model="checked" style="margin-right: 10px">医嘱套餐</el-checkbox>
              <el-button size="small" type="primary" @click="subOrder" icon="iconfont iconparent-line">子医嘱</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            ref="multipleTable"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading"
            highlight-current-row
            @selection-change="orderSelectChange"
            @row-click="rowClick">
            <el-table-column type="selection" width="50" class="selection" align="center">
            </el-table-column>
            <el-table-column prop="Adddate" :formatter="datetimeFormat" label="下嘱时间" width="95" align="center">
            </el-table-column>
            <el-table-column prop="state" label="医嘱状态" :formatter="formatState" width="90" align="center">
            </el-table-column>
            <el-table-column prop="name" label="医嘱" width="160">
            </el-table-column>
            <el-table-column prop="gg" label="规格" width="50" align="center">
            </el-table-column>
            <el-table-column prop="dw" label="单位" width="50" align="center">
            </el-table-column>
            <el-table-column prop="week" label="频次" width="50" align="center">
            </el-table-column>
            <el-table-column prop="path" label="用药途径" width="80" align="center">
            </el-table-column>
            <el-table-column prop="count" label="单次剂量" width="80" align="center">
            </el-table-column>
            <el-table-column prop="executedate" label="执行时间" width="160" align="center" :formatter="datetimeFormat">
            </el-table-column>
            <el-table-column prop="exeNurse" label="执行人" width="80" align="center">
            </el-table-column>
            <el-table-column prop="doctor" label="医生" width="80" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center" width="140">
              <template slot-scope="scope">
                  <el-button type="text" size="small" v-if="scope.row.state === 0" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" v-if="scope.row.doctor_state===0 && scope.row.state === 0" @click="UpdateState(scope.row,1)">有效</el-button>
                  <el-button type="text" size="small" v-if="scope.row.doctor_state===1 && scope.row.state === 0" @click="UpdateState(scope.row,0)">无效</el-button>
                  <el-button type="text" size="small" v-if="scope.row.state===0" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <div>
          <el-dialog  title="添加医嘱套餐" width="40%" :visible.sync="dialogFormVisible">
            <el-form :model="taocanobj" ref="taocanForm"   label-position="left" label-width="120px" style='width:90%; margin-left:70px;'>
                 <el-row>
                   <el-col>
                      <el-form-item label="医嘱套餐选择" >
                        <el-select v-model="taocanobj.taocanid" clearable style="width: 200px" class="myInput">
                            <el-option v-for="item in taocanList" :label="item.name" :key="item.id" :value="item.id" >{{item.name}}
                            </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                 </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button
                size="small"
                icon="el-icon-close"
                @click="dialogFormVisible = false"
              >关闭
              </el-button>
              <el-button
                size="small"
                icon="el-icon-check"
                type="primary"
                @click="CreateData"
              >保存
              </el-button>
            </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="新增医嘱" width="65%" :visible.sync="dialogListVisible">
            <div style="float: left">
              <label style="margin-right: 10px">医嘱类型</label>
              <el-radio-group v-model="hctype" @change="selectChange">
                  <el-radio label="药品">药品</el-radio>
                  <el-radio label="护理">护理</el-radio>
                  <el-radio label="自备药">自备药</el-radio>
              </el-radio-group>
              <el-input
                v-model="hcname"
                style="width: 200px;margin-right: 10px;margin-left: 20px"
                class="myInput" placeholder="请输入名称"
                suffix-icon="el-icon-search"
                @keyup.enter.native="material_handleFilter"
              >
              </el-input>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination background
                     @current-change="material_handleCurrentChange"
                     :current-page="material_listQuery.page"
                     :page-size="material_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="material_total">
                </el-pagination>
            </div>

            <el-table
              :data="material_list"
              highlight-current-row
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              @row-dblclick="rowdbclick">
              <el-table-column type="index" label="序号" width="80">
              </el-table-column>
              <el-table-column prop="id" v-if="false">
              </el-table-column>
              <el-table-column prop="name" label="名称" width="180">
              </el-table-column>
              <el-table-column prop="gg" label="规格" align="center" width="90">
              </el-table-column>
              <el-table-column prop="dw" label="剂量单位" align="center" width="100">
              </el-table-column>
              <el-table-column prop="jiage" label="单价" width="90">
              </el-table-column>
              <el-table-column prop="kucun" label="数量" width="90">
              </el-table-column>
              <el-table-column prop="pack_gg" label="包装规格" width="100">
              </el-table-column>
              <el-table-column prop="firm" label="厂商" width="200">
              </el-table-column>
            </el-table>
            <div>
               <div style="margin-top: 10px">医嘱列表</div>
               <el-table
                 :data="multipleSelection"
                 :header-cell-style="{background:'#F8F8F8'}"
                 stripe
                 fit>
                  <el-table-column type="index" label="序号"  width="80" align="center">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false">
                  </el-table-column>
                  <el-table-column prop="name" label="名称" width="180" align="center">
                  </el-table-column>
                  <el-table-column prop="gg" label="规格" width="120" v-if="false">
                  </el-table-column>
                  <el-table-column prop="dw" label="剂量单位" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="week" label="频次" width="120" align="center">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.week" clearable style="width: 75px" class="myInput">
                          <el-option label="QW" value="QW" >
                          </el-option>
                          <el-option label="QD" value="QD" >
                          </el-option>
                          <el-option label="QH" value="QH" >
                          </el-option>
                          <el-option label="ST" value="ST" >
                          </el-option>
                        </el-select>
                    </template>
                  </el-table-column>
                  <el-table-column prop="path" label="用药途径" width="120">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.path" clearable style="width: 110px" class="myInput">
                          <el-option label="静脉注射" value="静脉注射" >
                          </el-option>
                          <el-option label="静脉滴注" value="静脉滴注" >
                          </el-option>
                          <el-option label="肌肉注射" value="肌肉注射" >
                          </el-option>
                          <el-option label="皮下注射" value="皮下注射" >
                          </el-option>
                          <el-option label="局部溶栓" value="局部溶栓" >
                          </el-option>
                          <el-option label="口服" value="口服" >
                          </el-option>
                          <el-option label="舌下含服" value="舌下含服" >
                          </el-option>
                        </el-select>
                    </template>
                  </el-table-column>
                  <el-table-column prop="count" label="单次剂量" width="120">
                    <template slot-scope="scope">
                        <el-input
                          v-model="scope.row.count"
                          size="small"
                          placeholder="单次剂量">
                        </el-input>
                    </template>
                  </el-table-column>
                  <el-table-column label="操作" fixed="right">
                    <template slot-scope="scope">
                      <el-button type="text" size="small" @click="dict_handleDelete(scope.row)">删除</el-button>
                    </template>
                  </el-table-column>
                </el-table>
            </div>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button
                size="small"
                icon="el-icon-check"
                type="primary"
                @click="submitData"
              >提交
              </el-button>
              <el-button
                size="small"
                icon="el-icon-close"
                @click="dialogListVisible = false"
              >关闭</el-button>
            </div>
          </el-dialog>
        </div>

         <div>
            <el-dialog  title="编辑医嘱" width="50%" :visible.sync="tc_dialogVisible">
                <el-form  :model="taocanobj" ref="tc_Form" label-position="left" label-width="70px" style='width:90%; margin-left:50px;'>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="频次" prop="week">
                            <el-select v-model="taocanobj.week" clearable style="width: 140px" class="myInput">
                              <el-option label="QW" value="QW" >
                              </el-option>
                              <el-option label="QD" value="QD" >
                              </el-option>
                              <el-option label="QH" value="QH" >
                              </el-option>
                              <el-option label="ST" value="ST" >
                              </el-option>
                            </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="用药路径" prop="path">
                         <el-select v-model="taocanobj.path" clearable style="width: 140px" class="myInput">
                              <el-option label="静脉注射" value="静脉注射" >
                              </el-option>
                              <el-option label="静脉滴注" value="静脉滴注" >
                              </el-option>
                              <el-option label="肌肉注射" value="肌肉注射" >
                              </el-option>
                              <el-option label="皮下注射" value="皮下注射" >
                              </el-option>
                              <el-option label="局部溶栓" value="局部溶栓" >
                              </el-option>
                              <el-option label="口服" value="口服" >
                              </el-option>
                              <el-option label="舌下含服" value="舌下含服" >
                              </el-option>
                            </el-select>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="单次剂量" prop="count">
                         <el-input-number
                           v-model="taocanobj.count"
                           style="width: 140px"
                           class="myInput"
                           placeholder="单次剂量">
                         </el-input-number>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="是否收费" prop="feetype">
                            <el-select v-model="taocanobj.feetype" clearable style="width: 140px" class="myInput">
                              <el-option label="收费" value="收费" >
                              </el-option>
                              <el-option label="自备" value="自备" >
                              </el-option>
                            </el-select>
                        </el-form-item>
                     </el-col>
                   </el-row>
                </el-form>
                <div slot="footer" class="dialog-footer">
                    <el-button size="small" @click="tc_dialogVisible = false" icon="el-icon-close">关闭</el-button>
                    <el-button size="small" type="primary" @click="updateData" icon="el-icon-check">保存</el-button>
                </div>
            </el-dialog>
          </div>

    </div>
</template>

<script>
import { patientfee, yz_drug, createyz_drug, updateyz_drug, deleteyz_drug, chuzhiDict, huliDict, mydrugDict,
  mymaterialDict } from '@/api/login'
import { xyjhdict } from '@/api/system'
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

export default {
  name: 'drug',
  components: {
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol
  },
  props: ['regid' ,'patientid', 'num'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 1000,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      material_list: null,
      material_total: null,
      material_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        type: 0,
        patientid: '',
        sort: '+id'
      },
      searchStartyear: new Date().toLocaleDateString(),
      searchEndyear: new Date().toLocaleDateString(),
      taocanList: null,
      checked: false,
      ordertype: '',
      hctype: '药品',
      hcname: '',
      feetype: '收费', // 收费类型：收费和自备
      parentid: -1,
      action: 2,
      multipleSelection: [],
      multipleOrder: [],
      token: getToken,
      dialogFormVisible: false,
      dialogListVisible: false,
      tc_dialogVisible: false,
      dialogStatus: '',
      weekchecked: [],
      daysData: ['1', '2', '3', '4', '5', '6', '7'],
      patient: {
        patient: {
          id: undefined,
          patientid: undefined,
          name: '',
          sex: '',
          adddate: new Date(),
          phone1: '',
          age: ''
        },
        charge: 0,
        balance: 0
      },
      yue: 0,
      taocanobj: {
        id: null,
        yztype: '',
        week: '',
        path: '',
        count: 0,
        feetype: '',
        registerid: '',
        taocanid: null,
        orderid: null,
        leixing: '',
        checkNur_id: '',
        exeNur_id: '',
        parentid: -1,
        action: 1,
        kind: ''
      },
      drugobj: {
        id: '',
        yzlinshi_id: '',
        name: '',
        type: '',
        week: '',
        path: '',
        dw: '',
        gg: '',
        count: '',
        Adddate: '',
        doctorid: '',
        state: 0,
        doctor_state: 1,
        action: ''
      },
      multipleList: [],
      queryparams: {
        page: 1,
        registerid: this.regid,
        Startyear: new Date().toLocaleDateString(),
        Endyear: new Date().toLocaleDateString()
      },
      params: {
        page: 1,
        name: '',
        type: 0,
        patientid: ''
      },
      para: {
        patientid: this.patientid,
        registerid: this.regid
      },
      pickerOptions1: {
        disabledDate(time) {
          return time.getTime() > Date.now()
        }
      }
    }
  },
  methods: {
    ConnectServer() {
      this.ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/')
      if ('WebSocket' in window) {
        this.ws.onopen = function() {
          console.log('连接成功')
        }
        this.ws.onmessage = (evt) => {
          const received_msg = evt.data
          console.log('received_msg', received_msg)
        }
        this.ws.onclose = function() {
          console.log('连接已关闭...')
        }
      } else {
        console.log('您的浏览器不支持 WebSocket!')
      }
    },
    SendMsg() {
      this.ws.send(this.patientid)
      console.log('发送的数据 ：', this.patientid)
    },
    getDrug(data) {
      yz_drug(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
      xyjhdict(this.params).then(response => {
        this.taocanList = response.data.results
      })
    },
    getHuliList(data) {
      huliDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getChuzhiList(data) {
      chuzhiDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getMaterialList(data) {
      mymaterialDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getDrugList(data) {
      mydrugDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getPatient(data) {
      patientfee(data).then(response => {
        this.patient = response.data.results[0]
      })
    },
    subOrder() {
      // if (this.parentid === -1) {
      if (this.multipleOrder.length < 1) {
        this.$notify({
          title: '提示',
          message: '请选择项目',
          type: 'success',
          duration: 2000
        })
      } else if (this.multipleOrder.length > 1) {
        this.$notify({
          title: '提示',
          message: '请选择一条记录',
          type: 'success',
          duration: 2000
        })
      } else {
        this.action = 3
        this.multipleSelection = []
        this.dialogListVisible = true
      }
    },
    orderSelectChange: function(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    selectChange(val) {
      this.material_list = []
      this.material_total = null
      this.material_listQuery.page = 1
      this.material_listQuery.name = ''
      this.hcname = ''
      this.ordertype = val
      this.material_listQuery.type = val
      switch (val) {
        case '耗材':
          this.getMaterialList(this.material_listQuery)
          break
        case '药品':
          this.feetype = '收费'
          this.material_listQuery.type = 0
          this.material_listQuery.patientid = ''
          this.getDrugList(this.material_listQuery)
          break
        case '处置':
          this.getChuzhiList(this.material_listQuery)
          break
        case '护理':
          this.getHuliList(this.material_listQuery)
          break
        case '自备药':
          this.feetype = '自备'
          this.material_listQuery.type = 1
          this.material_listQuery.patientid = this.patientid
          this.getDrugList(this.material_listQuery)
      }
    },
    handleCreate() {
      if (this.checked) {
        this.dialogFormVisible = true
        this.$nextTick(() => {
          this.$refs['taocanForm'].clearValidate()
        })
      } else {
        this.parentid = -1 // 只能添加临时医嘱，不能添加临时医嘱的子医嘱
        this.action = 2
        this.getDrugList(this.material_listQuery)
        this.multipleSelection = []
        this.dialogListVisible = true
      }
    },
    CreateData() {
      this.$refs['taocanForm'].validate((valid) => {
        if (valid) {
          const multiList = []
          const tempData = Object.assign({}, this.taocanobj)
          tempData.id = parseInt(Math.random() * 100) + 1024
          tempData.yztype = 'a'
          tempData.week = 'a'
          tempData.path = 'a'
          tempData.count = 1
          tempData.state = 1
          tempData.doctor_state = 1
          tempData.feetype = 'a'
          tempData.registerid = this.regid
          tempData.orderid = 1
          tempData.leixing = 1
          tempData.action = 1 // 1为添加套餐
          tempData.checkNur_id = 1
          tempData.exeNur_id = 1
          tempData.parentid = -1
          multiList.push(tempData)
          createyz_drug(multiList).then((response) => {
            const res = response.data
            // 医生新开医嘱向服务端发送消息
            this.SendMsg()
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '新增成功',
              type: 'success',
              duration: 2000
            })
            this.getPatient(this.para)
            this.getDrug(this.queryparams)
          })
        }
      })
    },
    submitData() {
      if (this.multipleSelection.length > 0) {
        const obj = this.multipleSelection[0]
        if (!obj.count) {
          this.$notify({
            title: '成功',
            message: '单次剂量不能为空',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (!Number.isInteger(Number(obj.count))) {
          this.$notify({
            title: '成功',
            message: '单次剂量必须为数值',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (this.ordertype === '药品') {
          if (!obj.week) {
            this.$notify({
              title: '成功',
              message: '频次不能为空',
              type: 'success',
              duration: 2000
            })
            return
          }
          if (!obj.path) {
            this.$notify({
              title: '成功',
              message: '用药路径不能为空',
              type: 'success',
              duration: 2000
            })
            return
          }
        }
        this.multipleList = []
        this.multipleSelection.forEach((item) => {
          this.taocanobj = Object.assign({}, item)
          this.taocanobj.yztype = 'a'
          if (this.taocanobj.kind !== 3) {
            this.taocanobj.week = 'a'
            this.taocanobj.path = 'a'
            this.taocanobj.feetype = 'a'
          } else {
            this.taocanobj.feetype = this.feetype
          }
          this.taocanobj.state = 1
          this.taocanobj.doctor_state = 1
          this.taocanobj.registerid = this.regid
          this.taocanobj.taocanid = 1
          this.taocanobj.orderid = item.id
          this.taocanobj.leixing = item.kind
          this.taocanobj.action = this.action
          this.taocanobj.parentid = this.parentid
          this.multipleList.push(this.taocanobj)
        })
        createyz_drug(this.multipleList).then(() => {
          // 医生新开医嘱向服务端发送消息
          this.SendMsg()
          this.$notify({
            title: '成功',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogListVisible = false
          this.getPatient(this.para)
          this.getDrug(this.queryparams)
        })
      }

    },
    handleUpdate(row) {
      this.taocanobj = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.tc_dialogVisible = true
      this.$nextTick(() => {
        this.$refs['tc_Form'].clearValidate()
      })
    },
    updateData() {
      this.$refs['tc_Form'].validate((valid) => {
        if (valid) {
          const multiList = []
          const tempData = Object.assign({}, this.taocanobj)
          if (tempData.yztype !== '药品') {
            tempData.week = 'a'
            tempData.path = 'a'
            tempData.feetype = 'a'
          }
          tempData.state = 1
          tempData.doctor_state = 1
          tempData.taocanid = 1
          tempData.registerid = this.regid
          tempData.orderid = 1
          tempData.leixing = 1
          tempData.checkNur_id = 1
          tempData.exeNur_id = 1
          tempData.action = 4
          multiList.push(tempData)
          updateyz_drug(multiList).then(() => {
            this.tc_dialogVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getPatient(this.para)
            this.getDrug(this.queryparams)
          })
        }
      })
    },
    UpdateState(row, flag) {
      const multiList = []
      this.taocanobj = Object.assign({}, row) // copy obj
      const tempData = Object.assign({}, this.taocanobj)
      tempData.yztype = 'a'
      tempData.week = 'a'
      tempData.path = 'a'
      tempData.count = 1
      tempData.state = 1
      tempData.doctor_state = 1
      tempData.feetype = 'a'
      tempData.registerid = this.regid
      tempData.orderid = 1
      tempData.taocanid = 1
      tempData.leixing = 1
      tempData.checkNur_id = 1
      tempData.exeNur_id = 1
      tempData.parentid = -1
      tempData.action = flag // 0为点击无效按钮，1为有效
      multiList.push(tempData)
      updateyz_drug(multiList).then(() => {
        this.$notify({
          title: '成功',
          message: '设置成功',
          type: 'success',
          duration: 2000
        })
        this.getPatient(this.para)
        this.getDrug(this.queryparams)
      })
    },
    handleFilter() {
      this.listQuery.limit = 200
      this.listQuery.offset = 0
      this.queryparams.Startyear = this.searchStartyear
      this.queryparams.Endyear = this.searchEndyear
      this.parentid = -1
      this.getDrug(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getDrug(this.queryparams)
    },
    material_handleFilter() {
      this.material_listQuery.page = 1
      this.material_listQuery.name = this.hcname
      switch (this.hctype) {
        case '耗材':
          this.getMaterialList(this.material_listQuery)
          break
        case '药品':
          this.getDrugList(this.material_listQuery)
          break
        case '处置':
          this.getChuzhiList(this.material_listQuery)
          break
        case '护理':
          this.getHuliList(this.material_listQuery)
          break
      }
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      switch (this.hctype) {
        case '耗材':
          this.getMaterialList(this.material_listQuery)
          break
        case '药品':
          this.getDrugList(this.material_listQuery)
          break
        case '处置':
          this.getChuzhiList(this.material_listQuery)
          break
        case '护理':
          this.getHuliList(this.material_listQuery)
          break
      }
    },
    rowClick(row, event, column) {
      this.parentid = row.id
      // this.parentid = -1 // 是否要在医嘱下面新加子项目，-1为不加子项目
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    rowdbclick(row,event) {
      if (this.hctype === '药品' && row.kucun < 1) {
        this.$notify({
          title: '提示',
          message: '该项目库存已为0！',
          type: 'success',
          duration: 2000
        })
      } else {
        this.multipleSelection = []
        this.multipleSelection.push(row)
      }
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.taocanobj = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.taocanobj)
        deleteyz_drug(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.getPatient(this.para)
          this.getDrug(this.queryparams)
        })
      })
    },
    dict_handleDelete(row) {
      this.multipleSelection.splice(this.multipleSelection.findIndex(v => v.id === row.id), 1)
    },
    changeSelection(){
    },
    handleReset() {
      this.queryparams.Startyear = ''
      this.searchStartyear = ''
      this.queryparams.Endyear = ''
      this.searchEndyear = ''
      this.parentid = -1
      this.getDrug(this.queryparams)
    },
    formatState: function(row, column) {
      const zt = row.state
      let s = ''
      switch (zt) {
        case 0:
          s = '未核查'
          break
        case 1:
          s = '已核查(未执行)'
          break
        case 2:
          s = '已执行'
          break
        case 3:
          s = '已撤销'
          break
      }
      return s
    },
    formatCol: function(row, column) {
      return row.doctor_state === 1 ? '有效' : '无效'
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    },
    datetimeFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      } else if (date === '') {
        return ''
      } else if (date === null) {
        return ''
      } else {
        return moment(date).format('YYYY-MM-DD HH:mm:ss')
      }
    }
  },
  watch: {
    patient: function() {
      this.yue = this.patient.balance - this.patient.charge
    },
    num: function() {
      this.getDrug(this.queryparams)
    }
  },
  created: function() {
    this.ConnectServer()
    this.getPatient(this.para)
    this.getDrug(this.queryparams)
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
      padding:6px 0;
    }
    .el-dialog__body {
        padding: 5px 20px;
        color: #606266;
        line-height: 24px;
        font-size: 14px;
    }
</style>
