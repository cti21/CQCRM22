<template>
    <div>
        <el-form :model="customer" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
         <el-row style="margin-top: 10px">
           <el-col :span="12">
                <label class="el-form-item__label">名称</label>
                <el-input v-model="customer.name" style="width: 60%;" class="myInput"></el-input>
           </el-col>
           <el-col :span="12">
                <label class="el-form-item__label">性别</label>
                <el-select v-model="customer.sex" clearable style="width: 60%" class="myInput">
                  <el-option v-for="item in sexSelect" :key="item.id" :value="item.name" :label="item.name">
                  </el-option>
                </el-select>
           </el-col>
         </el-row>
         <el-row style="margin-top: 10px">
           <el-col :span="12">
                <label class="el-form-item__label">出生日期</label>
                <el-date-picker
                  v-model="customer.birthDate"
                  style="width:50%"
                  class="myInput"
                  type="date"
                  placeholder="出生日期"
                  value-format="yyyy-MM-dd">
                </el-date-picker>
           </el-col>
           <el-col :span="12">
                <label class="el-form-item__label">年龄</label>
                <el-input v-model="age" readonly style="width: 60%;" class="myInput"></el-input>
           </el-col>
         </el-row>
         <el-row style="margin-top: 10px">
           <el-col :span="12">
                <label class="el-form-item__label">手机</label>
                <el-input v-model="customer.phone1" style="width: 60%;" class="myInput"></el-input>
           </el-col>
           <el-col :span="12">
                <label class="el-form-item__label">家长手机</label>
                <el-input v-model="customer.phone2" style="width: 50%;" class="myInput"></el-input>
           </el-col>
         </el-row>
         <el-row style="margin-top: 10px">
           <el-col>
                <label class="el-form-item__label">家庭住址</label>
                <el-input v-model="customer.address" style="width: 75%;" class="myInput"></el-input>
           </el-col>
         </el-row>
         <el-row style="margin-top: 10px">
           <el-table
              :data="registerList"
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
            >
              <el-table-column type="index" label="序号"  width="100">
              </el-table-column>
              <el-table-column prop="registerdate" label="登记日期" width="180">
              </el-table-column>
              <el-table-column prop="clienttype" label="客户类型" width="160">
              </el-table-column>
              <el-table-column prop="registerdeptname" label="登记科室" width="160">
              </el-table-column>
           </el-table>
         </el-row>
        </el-form>
    </div>
</template>

<script>
import { clients, client_registers} from '@/api/client'
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
  props: ['client_id'],
  data: function() {
    return {
      registerList: [],
      sexSelect: [
        { id: 1, name: '男' },
        { id: 2, name: '女' }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }]
      },
      customer: {
        id: null,
        name: '',
        sex: '',
        birthDate: null,
        phone1: '',
        phone2: '',
        address: '',
        hrmdepartment: null,
        username: '',
        comment: ''
      }
    }
  },
  computed:{
    age() {
      let val = ''
      if ( this.customer.birthDate !== null) {
        const birthdays = new Date(this.customer.birthDate.replace(/-/g, '/'))
        const d = new Date()
        val =
          d.getFullYear() -
          birthdays.getFullYear() -
          (d.getMonth() < birthdays.getMonth() ||
          (d.getMonth() === birthdays.getMonth() &&
          d.getDate() < birthdays.getDate()) ? 1 : 0)
      }
      return val
    }
  },
  methods: {
    getClients(data) {
      clients(data).then(response => {
        this.customer = response.data.results[0]
      })
    },
    getClient_registers(data) {
      client_registers(data).then(response => {
        this.registerList = response.data.results
      })
    }
  },
  created: function() {
    const param = {
      clientid: this.client_id
    }
    this.getClients(param)
    this.getClient_registers(param)
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
