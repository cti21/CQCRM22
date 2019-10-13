<template>
    <div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <el-table-column type="index" label="序号"  width="50"  align="center">
            </el-table-column>
            <el-table-column prop="opdate" label="手术日期" width="100" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="opdesc" label="手术名称"  width="100" align="center">
            </el-table-column>
            <el-table-column prop="doctor" label="医生" width="80" align="center">
            </el-table-column>
            <el-table-column prop="first" label="第一助手" width="90" align="center">
            </el-table-column>
            <el-table-column prop="second" label="第二助手" width="90" align="center">
            </el-table-column>
            <el-table-column prop="mazuitype" label="麻醉类型"  width="90" align="center">
            </el-table-column>
            <el-table-column prop="qixie" label="器械护士" width="90" align="center">
            </el-table-column>
            <el-table-column prop="xunhui" label="巡回护士" width="90" align="center">
            </el-table-column>
            <el-table-column prop="mazui" label="麻醉医生" width="90" align="center">
            </el-table-column>
            <el-table-column prop="geli" label="是否隔离" width="90" :formatter="formatBoolean" align="center">
            </el-table-column>
          </el-table>
        </div>
    </div>
</template>

<script>
import { operations } from '@/api/login'
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
  name: 'operate_record',
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
  props: ['patientid'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      token: getToken
    }
  },
  methods: {
    getOperationList(data) {
      operations(data).then(response => {
        this.listLoading = true
        this.list = response.data
        this.listLoading = false
      })
    },
    formatBoolean: function(row, column) {
      return row.geli === true ? '是' : '否'
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getOperationList(this.patientid)
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
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
