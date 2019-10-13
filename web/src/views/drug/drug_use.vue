<template>
    <div>
        <div class="filter-container">
              <el-input
                v-model="searchname"
                class="myInput"
                @keyup.enter.native="handleFilter"
                style="width: 220px;margin-right: 20px;"
                prefix-icon="el-icon-search"
                placeholder="药品名称/ 药品代码">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe="">
            <el-table-column type="index" label="序号"  width="80"  align="center">
            </el-table-column>
            <el-table-column prop="indate" label="入库日期" width="120" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="outdate" label="出库日期" width="120" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="drug.indicator" label="药品类别"  width="160">
            </el-table-column>
            <el-table-column prop="drug.name" label="药品名称" width="160">
            </el-table-column>
            <el-table-column prop="drug.code" label="条码" width="100" align="center">
            </el-table-column>
            <el-table-column prop="price" label="单价" width="100" align="center">
            </el-table-column>
            <el-table-column prop="amount" label="入/出库数量" width="120" align="center">
            </el-table-column>
            <el-table-column prop="stock" label="库存数量"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="operator.username" label="操作者" width="120" align="center">
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
import { drugStocks, createDrugStock, updateDrugStock } from '@/api/login'
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
  name: 'drug_use',
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
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      searchname: '',
      token: getToken,
      queryparams: {
        page: 1,
        status: 3,
        name: ''
      }
    }
  },
  methods: {
    getDrugUseList(data) {
      drugStocks(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.searchname = ''
      this.getDrugUseList(this.queryparams)
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.getDrugUseList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getDrugUseList(3)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getDrugUseList(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]

      if (date === undefined || date === null) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  watch: {
    clickcount: function() {
      this.getDrugUseList(this.queryparams)
    }
  },
  created: function() {
    this.getDrugUseList(this.queryparams)
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
