<template>
    <div>
        <div class="filter-container">
              <el-date-picker v-model="fromdate" style="width: 160px" value-format="yyyy-MM-dd" class="myInput" type="date" placeholder="日期开始">
              </el-date-picker>
              <el-date-picker v-model="todate" style="width: 160px" value-format="yyyy-MM-dd" class="myInput" type="date" placeholder="日期结束">
              </el-date-picker>
              <el-input
                v-model="searchname"
                class="myInput"
                @keyup.enter.native="handleFilter"
                style="width: 180px;margin-right: 20px;"
                placeholder="药品名称/ 药品代码">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="name" label="药品名称"  width="200">
            </el-table-column>
            <el-table-column prop="spec" label="规格" width="120" align="center">
            </el-table-column>
            <el-table-column prop="units" label="单位" width="120" align="center">
            </el-table-column>
            <el-table-column prop="prejieyu" label="上期结余"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="currinnum" label="当期入库" width="120" align="center" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="curroutnum" label="当期出库" width="120" align="center" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="jieyu" label="结余" width="120" align="center" show-overflow-tooltip>
            </el-table-column>

          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination background
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-sizes="[5,10,20,30, 50]"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
                </el-pagination>
          </div>
        </div>

    </div>
</template>

<script>
import { getDrugStock } from '@/api/login'
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
  props: ['clickcount'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      fromdate: '',
      todate: '',
      searchname: '',
      searchcode: '',
      token: getToken,
      queryparams: {
        page: 1,
        status: 2,
        begindate: '',
        enddate: '',
        name: '',
        code: ''
      }
    }
  },
  methods: {
    getStockList(data) {
      getDrugStock(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.queryparams.code = ''
      this.queryparams.begindate = ''
      this.queryparams.enddate = ''
      this.fromdate = ''
      this.todate = ''
      this.searchcode = ''
      this.searchname = ''
      this.getStockList(this.queryparams)
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.begindate = this.fromdate
      this.queryparams.enddate = this.todate
      this.queryparams.name = this.searchname
      this.queryparams.code = this.searchcode
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
      this.getStockList(this.queryparams)
    }
  },
  created: function() {
    this.getStockList(this.queryparams)
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
