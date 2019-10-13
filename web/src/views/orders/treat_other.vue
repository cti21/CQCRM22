<template>
    <div>
        <div>
          <el-row style="margin-left:20px;margin-bottom: 20px;width: 90%" >
             <el-button-group style="width: 100%">
                <el-button size="small" style="width: 50%" @click="handleTreat" type="primary" icon="el-icon-plus">治疗</el-button>
                <el-button size="small" style="width: 50%" @click="handleCallback" type="success" icon="el-icon-download">回访</el-button>
             </el-button-group>
          </el-row>
        </div>
        <el-form  :model="treat_detail" ref="dataForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
             <div v-if="treatVisible===true">
                 <el-row style="margin-top: 10px">
                   <el-col :span="12" style="margin-top: 10px">
                      <label class="el-form-item__label">治疗次数</label>
                      <el-input-number size="small" :min="1" v-model="treat_detail.amount" style="width:60%;margin-top: 5px">
                      </el-input-number>
                   </el-col>
                   <el-col :span="12" style="margin-top: 10px">
                        <label class="el-form-item__label">禁忌症</label>
                        <el-select multiple
                                   value-key="id"
                                   v-model="treat_detail.jinjizheng"
                                   style="width: 80%" class="myInput">
                          <el-option v-for="(item,index) in jinjizhengSelect" :key="item.id" :label="item.name" :value="item.id">
                          </el-option>
                        </el-select>
                   </el-col>
                   <el-col :span="8" style="margin-top: 10px" v-if="displayField(parentobj.projectname,'wendu')">
                        <label class="el-form-item__label">治疗温度</label>
                        <el-input v-model="treat_detail.wendu" style="width: 60%;" class="myInput"></el-input>
                   </el-col>
                   <el-col :span="8" style="margin-top: 10px" v-if="displayField(parentobj.projectname,'yaling')">
                        <label class="el-form-item__label">是否使用阴道哑铃</label>
                        <el-select v-model="treat_detail.yaling" clearable style="width: 40%" class="myInput">
                            <el-option v-for="item in yalingSelect" :key="item.id" :value="item.id" :label="item.name">
                            </el-option>
                        </el-select>
                   </el-col>
                   <el-col :span="8" style="margin-top: 10px" v-if="displayField(parentobj.projectname,'energy')">
                        <label class="el-form-item__label">治疗能量</label>
                        <el-input v-model="treat_detail.energy" style="width: 60%;" class="myInput"></el-input>
                   </el-col>
                 </el-row>
                 <el-row style="margin-top: 10px" v-if="parentobj.projectname==='盆底评估'">
                   <el-col>
                        <label class="el-form-item__label">评估结果报告</label>
                        <el-input v-model="treat_detail.report" style="width: 80%;" class="myInput"></el-input>
                   </el-col>
                 </el-row>
                 <el-row style="margin-top: 10px">
                   <el-col :span="8">
                        <label class="el-form-item__label">治疗科室</label>
                        <el-select v-model="treat_detail.treatdept" clearable style="width: 60%" class="myInput">
                            <el-option v-for="item in deptSelect" :key="item.id" :value="item.id" :label="item.deptname">
                            </el-option>
                        </el-select>
                   </el-col>
                   <el-col :span="8">
                        <label class="el-form-item__label">治疗人员</label>
                        <el-select v-model="treat_detail.operator" clearable style="width:60%" class="myInput">
                            <el-option v-for="item in userSelect" :key="item.id" :value="item.id" :label="item.name">
                            </el-option>
                        </el-select>
                   </el-col>
                   <el-col :span="8">
                        <label class="el-form-item__label">治疗日期</label>
                        <el-date-picker
                          v-model="treat_detail.operatedate" type="date" value-format="yyyy-MM-dd"
                          format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                        </el-date-picker>
                   </el-col>
                 </el-row>
                 <el-row style="margin-top: 10px" v-if="parentobj.clickfrom === 'current'">
                   <el-col :span="6">
                        <label class="el-form-item__label">预约治疗日期</label>
                   </el-col>
                   <el-col :span="8">
                        <el-date-picker
                          v-model="treat_detail.s_treat" type="date" value-format="yyyy-MM-dd"
                          format="yyyy-MM-dd" clearable style="width: 80%" class="myInput">
                        </el-date-picker>
                   </el-col>
                   <el-col :span="2">
                        <label class="el-form-item__label">到</label>
                   </el-col>
                   <el-col :span="8">
                        <el-date-picker
                          v-model="treat_detail.e_treat" type="date" value-format="yyyy-MM-dd"
                          format="yyyy-MM-dd" clearable style="width: 80%" class="myInput">
                        </el-date-picker>
                   </el-col>
                 </el-row>
                 <el-row style="margin-top: 10px" v-if="parentobj.clickfrom === 'current'">
                   <el-col :span="6">
                        <label class="el-form-item__label">预约回访日期</label>
                   </el-col>
                   <el-col :span="8">
                        <el-date-picker
                          v-model="treat_detail.s_callback" type="date" value-format="yyyy-MM-dd"
                          format="yyyy-MM-dd" clearable style="width: 80%" class="myInput">
                        </el-date-picker>
                   </el-col>
                   <el-col :span="2">
                        <label class="el-form-item__label">到</label>
                   </el-col>
                   <el-col :span="8">
                        <el-date-picker
                          v-model="treat_detail.e_callback" type="date" value-format="yyyy-MM-dd"
                          format="yyyy-MM-dd" clearable style="width: 80%" class="myInput">
                        </el-date-picker>
                   </el-col>
                 </el-row>
                 <el-row style="margin-top: 10px">
                   <el-col>
                        <label class="el-form-item__label">备注</label>
                        <el-input v-model="treat_detail.comment" style="width: 80%;" class="myInput"></el-input>
                   </el-col>
                 </el-row>
             </div>
             <div v-if="callbackVisible===true">
               <el-row style="margin-bottom: 10px;margin-top: 20px;">
                  <el-button size="small" @click="handleCreate" type="primary">新增随访</el-button>
               </el-row>
               <el-row>
                   <el-table
                      :data="list"
                      :header-cell-style="{background:'#F8F8F8'}"
                      stripe
                    >
                      <el-table-column type="index" label="序号"  min-width="80">
                      </el-table-column>
                      <el-table-column prop="begindate" label="开始日期" min-width="100">
                      </el-table-column>
                      <el-table-column prop="enddate" label="结束日期" min-width="100">
                      </el-table-column>
                      <el-table-column prop="handledate" label="回访日期" min-width="100">
                      </el-table-column>
                      <el-table-column prop="deptname" label="回访科室" min-width="100">
                      </el-table-column>
                      <el-table-column prop="handlemanname" label="回访人" min-width="90">
                      </el-table-column>
                        <el-table-column label="操作" fixed="right" align="center">
                        <template slot-scope="scope">
                            <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                            <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
                        </template>
                      </el-table-column>
                   </el-table>
               </el-row>
             </div>
        </el-form>
      <div slot="footer" class="dialog-footer" align="right" style="margin-top: 20px;margin-right: 50px;">
        <el-button
          size="small"
          @click="treatClose"
          icon="el-icon-close"
        >关闭</el-button>
        <el-button
          size="small"
          type="primary"
          icon="el-icon-check"
          v-if="treatVisible===true"
          @click="treatUpdateData">保存
        </el-button>
      </div>

      <!--项目回访-->
        <div>
           <el-dialog  title="回访" width="40%" :visible.sync="dialogCallbackVisible" :append-to-body="true">
              <el-form  :model="callback" ref="callbackForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
                   <el-row>
                     <el-col>
                        <el-form-item label="开始随访日期"  prop="begindate">
                          <el-date-picker
                            v-model="callback.begindate" type="date" value-format="yyyy-MM-dd"
                            format="yyyy-MM-dd" clearable style="width: 90%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col>
                        <el-form-item label="结束随访日期"  prop="enddate">
                          <el-date-picker
                            v-model="callback.enddate" type="date" value-format="yyyy-MM-dd"
                            format="yyyy-MM-dd" clearable style="width: 90%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                   </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="dialogCallbackVisible=false"
                  >关闭
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    v-if="dialogStatus==='create'"
                    icon="el-icon-check"
                    @click="createData">保存
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    v-else
                    icon="el-icon-check"
                    @click="updateData">保存
                  </el-button>
              </div>
           </el-dialog>
        </div>

    </div>
</template>

<script>
import { formatDate } from '@/utils/date'
import { depts } from '@/api/system'
import { users } from '@/api/employee'
import { jinjizhengs } from '@/api/client'
import { callbacks, createCallback, updateCallback, deleteCallback } from '@/api/service'
import { updateTreat, getTcTreatHistroryData, treat_details } from '@/api/order'
import { getToken } from '@/utils/auth'
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
  props: {
    parentobj: {
      type: Object
    }
  },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10000,
        offset: 0,
        name: '',
        treat_id: null,
        project_id: null,
        hrmdepartment_id: null,
        sort: '+id'
      },
      searchname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogCallbackVisible: false,
      treatVisible: true,
      callbackVisible: false,
      dialogStatus: '',
      deptSelect: [],
      userSelect: [],
      jinjizhengSelect: [],
      callback: {
        id: null,
        begindate: null,
        enddate: null,
        treat_id: null
      },
      yalingSelect: [
        { id: 1, name: '是' },
        { id: 0, name: '否' }
      ],
      diagnosisSelect: [
        { id: 1, name: '正常' },
        { id: 2, name: '体重增长过快' },
        { id: 3, name: '体重增长过慢' },
        { id: 4, name: '高体脂率' }
      ],
      healthlxSelect: [
        { id: 1, name: '正常' },
        { id: 2, name: '甲亢' },
        { id: 3, name: '甲减' },
        { id: 4, name: '妊娠糖尿病' },
        { id: 5, name: '缺铁性贫血' },
        { id: 6, name: '地中海贫血' },
        { id: 7, name: '巨幼红细胞性贫血' },
        { id: 8, name: '胎儿生长受限' },
        { id: 9, name: '高血压' },
        { id: 10, name: '子痫前期' },
        { id: 11, name: '其他' }
      ],
      guideSelect: [
        { id: 1, name: '普通饮食' },
        { id: 2, name: '糖尿病膳食' },
        { id: 3, name: '低脂膳食' },
        { id: 4, name: '低蛋白膳食' },
        { id: 5, name: '高蛋白膳食' },
        { id: 6, name: '低胆固醇膳食' },
        { id: 7, name: '低嘌呤膳食' },
        { id: 8, name: '钙磷代谢膳食' },
        { id: 9, name: '低价膳食' },
        { id: 10, name: '低盐、无盐膳食' },
        { id: 11, name: '流质饮食' },
        { id: 12, name: '半流质饮食' }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      healths: [],
      guide: [],
      treat_detail: {
        id: null,
        report: null,
        jinjizheng: [],
        yaling: null,
        energy: null,
        wendu: null,
        amount: 0,
        treatdept: null,
        operator: '',
        operatedate: formatDate(new Date(), 'yyyy-MM-dd'),
        s_treat: null,
        e_treat: null,
        s_callback: null,
        e_callback: null,
        register: {
          sourcedept: null,
          preBMI: null,
          taishu: null
        },
        comment: ''
      }
    }
  },
  methods: {
    getTreats(data) {
      treat_details(data).then(response => {
        this.listLoading = true
        this.treat_detail = response.data.results[0]
        const arr = this.treat_detail.jinjizheng.map(v => v.jinjizheng_id)
        this.treat_detail.jinjizheng = []
        this.treat_detail.jinjizheng = [...arr]
        this.listLoading = false
      })
    },
    getCallbacks(data) {
      callbacks(data).then(response => {
        this.list = response.data.results
        this.total = response.data.count
      })
    },
    getDepts(data) {
      depts(data).then(response => {
        this.deptSelect = response.data.results
      })
    },
    getUsers(data) {
      users(data).then(response => {
        this.userSelect = response.data.results
      })
    },
    displayField(sproject, sfield) {
      let arr = []
      let num = false
      if (sproject === '盆底评估') {
        arr = ['report']
        num = arr.some((item) => { return item === sfield })
      } else if (sproject === '盆底治疗') {
        arr = ['yaling', 'energy']
        num = arr.some((item) => { return item === sfield })
      } else if (sproject === '熏蒸治疗') {
        arr = ['wendu']
        num = arr.some((item) => { return item === sfield })
      } else {
        arr = ['energy']
        num = arr.some((item) => { return item === sfield })
      }
      return num
    },
    resetTreat_detail() {
      this.treat_detail = {
        id: null,
        report: null,
        jinjizheng: [],
        yaling: null,
        energy: null,
        wendu: null,
        amount: 0,
        treatdept: null,
        operator: '',
        operatedate: formatDate(new Date(), 'yyyy-MM-dd'),
        s_treat: null,
        e_treat: null,
        s_callback: null,
        e_callback: null,
        register: {
          sourcedept: null,
          preBMI: null,
          taishu: null
        },
        comment: ''
      }
    },
    resetCallback() {
      this.callback = {
        id: null,
        begindate: null,
        enddate: null,
        treat_id: null
      }
    },
    handleTreat() {
      this.treatVisible = true
      this.callbackVisible = false
    },
    handleCallback() {
      this.treatVisible = false
      this.callbackVisible = true
    },
    treatClose() {
      const data = { flag: 0 }
      this.$emit('closeDlg', data)
    },
    treatUpdateData() {
      const tempData = Object.assign({}, this.treat_detail)
      tempData.id = this.parentobj.treat_id
      if (this.parentobj.clickfrom === 'history') {
        tempData.action = 6 // 除套餐外的产后治疗的修改
      } else {
        tempData.action = 5 // 除套餐外的产后治疗
      }
      console.log('5tempData', tempData)
      updateTreat(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '治疗成功',
          type: 'success',
          duration: 2000
        })
        const data = {flag: 1}
        this.$emit('closeDlg', data)
        const par = {
          hrmdepartment_id: this.parentobj.hrmdepartment_id,
          order_id: this.parentobj.order_id
        }
        this.getCallbacks(par)
      })
    },
    handleCreate() {
      this.resetCallback()
      this.dialogCallbackVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['callbackForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.callbackForm.validate((valid) => {
        if (valid) {
          this.callback.id = parseInt(Math.random() * 100) + 1024
          this.callback.treat_id = this.parentobj.treat_id
          createCallback(this.callback).then(() => {
            this.dialogCallbackVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            const par = {
              hrmdepartment_id: this.parentobj.hrmdepartment_id,
              order_id: this.parentobj.order_id
            }
            this.getCallbacks(par)
          })
        }
      })
    },
    handleUpdate(row) {
      this.callback = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogCallbackVisible = true
      this.$nextTick(() => {
        this.$refs['callbackForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['callbackForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.callback)
          updateCallback(tempData).then(() => {
            this.dialogCallbackVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            const par = {
              hrmdepartment_id: this.parentobj.hrmdepartment_id,
              order_id: this.parentobj.order_id
            }
            this.getCallbacks(par)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.callback = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.callback)
        deleteCallback(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            hrmdepartment_id: this.parentobj.hrmdepartment_id,
            order_id: this.parentobj.order_id
          }
          this.getCallbacks(par)
        })
      })
    },
    closeDialog() {
      const data = { flag: 0 }
      this.$emit('closeDlg', data)
    }
  },
  watch: {
    'parentobj.count': {
      handler: function(val, oldVal) {
        this.resetTreat_detail()
        const arr = this.parentobj.jinjizheng.map(v => v.jinjizheng_id)
        this.treat_detail.jinjizheng = [...arr]
        this.getTreats(this.listQuery)
      },
      deep: true
    }
  },
  created: function() {
    jinjizhengs(this.listQuery).then(response => {
      this.jinjizhengSelect = []
      this.jinjizhengSelect = response.data.results
    })
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.listQuery.treat_id = this.parentobj.treat_id
    this.listQuery.project_id = this.parentobj.project_id
    this.listQuery.hrmdepartment_id = this.parentobj.hrmdepartment_id
    this.getTreats(this.listQuery)
    this.getDepts(this.listQuery)
    this.getUsers(this.listQuery)
    const par = {
      hrmdepartment_id: this.parentobj.hrmdepartment_id,
      order_id: this.parentobj.order_id
    }
    this.getCallbacks(par)
  }
}
</script>

<style>
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
</style>
