<template>
    <div>
        <el-row style="margin-top: 10px">
              <el-input
                v-model="searchname"
                prefix-icon="el-icon-search"
                class="myInput"
                size="small"
                @keyup.enter.native="handleFilter"
                style="width: 240px;float: left;margin-right: 40px;"
                placeholder="请输入药品名称/编号">
              </el-input>
        </el-row>
        <el-row style="margin-top: 10px" >
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <el-table-column type="index" label="序号"  width="100">
            </el-table-column>
            <el-table-column prop="drug.name" label="药品名称"  width="220">
              <template slot-scope="scope">
                  <span v-if="scope.row.state === 1" style="color:red">{{ scope.row.drug.name }}</span>
                  <span v-else>{{ scope.row.drug.name }}</span>
                </template>
            </el-table-column>
            <el-table-column prop="drug.spec" label="规格" width="160" align="center">
            </el-table-column>
            <el-table-column prop="drug.units" label="单位" width="160" align="center">
            </el-table-column>
            <el-table-column prop="amount" label="结余" width="160" align="center" show-overflow-tooltip>
            </el-table-column>
          </el-table>
        </el-row>

    </div>
</template>

<script>
import { dep_drugStore } from '@/api/login'
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
  props: ['patientid', 'clickcount'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 10000,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      fromdate: '',
      todate: '',
      searchname: '',
      token: getToken,
      queryparams: {
        page: 1,
        status: 2,
        begindate: '',
        enddate: '',
        name: '',
        patientid: this.patientid
      }
    }
  },
  methods: {
    getStockList(data) {
      dep_drugStore(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.queryparams.begindate = ''
      this.queryparams.enddate = ''
      this.fromdate = ''
      this.todate = ''
      this.searchname = ''
      this.getStockList(this.queryparams)
    },
    handleFilter() {
      this.listQuery.limit = 10000
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.begindate = this.fromdate
      this.queryparams.enddate = this.todate
      this.queryparams.name = this.searchname
      this.getStockList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getStockList(2)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getStockList(this.queryparams)
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  watch: {
    clickcount: function() {
      this.queryparams.patientid = this.patientid
      this.getStockList(this.queryparams)
    },
    patientid: function() {
      this.queryparams.patientid = this.patientid
      this.getStockList(this.queryparams)
    }
  },
  created: function() {
    this.queryparams.patientid = this.patientid
    // this.getStockList(this.queryparams)
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
</style>
