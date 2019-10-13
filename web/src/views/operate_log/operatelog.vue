<template>
    <div>
        <el-row>
              <el-input
                v-model="searchname"
                prefix-icon="el-icon-search"
                class="myInput"
                size="small"
                @keyup.enter.native="handleFilter"
                style="width: 240px;float: right;margin-right: 40px;"
                placeholder="请输入用户姓名">
              </el-input>
        </el-row>
        <el-row style="margin-top: 10px;">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="60">
            </el-table-column>
            <el-table-column prop="requested_at" label="操作日期"  width="220" :formatter="dateFormat">
            </el-table-column>
            <el-table-column prop="response_ms" label="反应时间" width="120">
            </el-table-column>
            <el-table-column prop="status_code" label="状态码" width="100">
            </el-table-column>
            <el-table-column prop="name" label="用户" width="100">
            </el-table-column>
            <el-table-column prop="method" label="动作" width="80">
            </el-table-column>
            <el-table-column prop="path" label="路径" width="160">
            </el-table-column>
            <el-table-column prop="remote_addr" label="ip" width="180">
            </el-table-column>
            <el-table-column prop="host" label="服务器" width="180">
            </el-table-column>
            <!--<el-table-column prop="query_params" label="查询参数" width="220">-->
            <!--</el-table-column>-->
          </el-table>
          <div class="pagination-container" style="margin-top: 10px;float:right;margin-right: 40px">
            <el-pagination
              background
              @current-change="handleCurrentChange"
              :current-page="listQuery.page"
              :page-sizes="[10,20,30, 50]"
              :page-size="listQuery.limit"
              layout="total, prev, pager, next"
              :total="total">
            </el-pagination>
          </div>
        </el-row>

    </div>
</template>

<script>
import { operateLog } from '@/api/login'
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
        userid: null
      }
    }
  },
  methods: {
    getLogList(data) {
      operateLog(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    handleReset() {
      this.listQuery.name = ''
      this.searchname = ''
      this.getLogList(this.listQuery)
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getLogList(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getLogList(this.listQuery)
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.getLogList(this.listQuery)
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
