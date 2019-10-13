<template>
    <div>
        <el-container style="border: 1px solid #eee;">
          <el-aside width="300px" style="border: 1px solid #eee;background-color: #ffffff">
              <div style="height: 500px">
              <el-row style="margin-top:20px;">
                <label style="margin-left: 10px;font-size: small">患者列表</label>
              </el-row>
              <el-row style="margin-top:10px;">
                <label style="margin-left: 10px;margin-right: 20px;font-size: small">时间</label>
                <el-button type="text" id="btn_all" style="margin-left: 20px" @click="handleFilter(0)">不限</el-button>
                <el-button type="text" id="btn_today" style="margin-left: 20px" @click="handleFilter(1)">今天</el-button>
                <el-button type="text" id="btn_yesterday" style="margin-left: 20px" @click="handleFilter(2)">昨天</el-button>
              </el-row>
              <el-row style="margin-bottom: 10px">
                <div>
                  <el-input
                    v-model="scname"
                    class="myInput"
                    prefix-icon="el-icon-search"
                    size="small"
                    @keyup.enter.native="handleFilter('')"
                    style="width:260px;padding: 0 10px"
                    placeholder="请输入患者名称/编号">
                  </el-input>
                </div>
              </el-row>
              <el-table
                :data="list"
                highlight-current-row
                :header-cell-style="{background:'#F8F8F8'}"
                stripe
                @row-click="rowClick"
                style="width: 280px;margin: 5px;">
                <el-table-column type="index" label="序号"  width="60" align="center">
                </el-table-column>
                <el-table-column prop="name" label="姓名" width="90"  align="center">
                </el-table-column>
                <el-table-column prop="patientid" label="编号" width="90"  align="center">
                </el-table-column>
              </el-table>
              <div class="pagination-container" align="center">
                <el-pagination background
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="total">
                </el-pagination>
            </div>
            </div>
          </el-aside>
          <el-container>
            <el-main>
              <div width="100%" :visible.sync="detailVisible">
                  <expenseDetail :patientid="patientid">
                  </expenseDetail>
              </div>
            </el-main>
          </el-container>
        </el-container>
    </div>
</template>

<script>
import { patient_Drug } from '@/api/login'
import { getToken } from '@/utils/auth'
import expenseDetail from '@/views/expense/expense_detail.vue'
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
import ElButton from '../../../node_modules/element-ui/packages/button/src/button'
import ElContainer from '../../../node_modules/element-ui/packages/container/src/main'
import ElMain from '../../../node_modules/element-ui/packages/main/src/main'

export default {
  components: {
    ElMain,
    ElContainer,
    ElButton,
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    expenseDetail
  },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 8,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      detailVisible: false,
      exam_list: null,
      exam_total: null,
      exam_listLoading: false,
      exam_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      detail_list: null,
      detail_total: null,
      detail_listLoading: false,
      detail_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      exam_detail_list: null,
      exam_detail_total: null,
      patientid: '',
      scname: '',
      rq: '',
      tableVisible: true,
      token: getToken,
      queryparams: {
        page: 1,
        patientid: '',
        rq: ''
      }
    }
  },
  methods: {
    getPatients(data) {
      patient_Drug(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    handleFilter(par) {
      if (par === 0) {
        this.rq = ''
        document.getElementById('btn_all').style.color = 'red'
        document.getElementById('btn_today').style.color = ''
        document.getElementById('btn_yesterday').style.color = ''
      } else if (par === 1) {
        this.rq = 1
        document.getElementById('btn_all').style.color = ''
        document.getElementById('btn_today').style.color = 'red'
        document.getElementById('btn_yesterday').style.color = ''
      } else if (par === 2) {
        this.rq = 2
        document.getElementById('btn_all').style.color = ''
        document.getElementById('btn_today').style.color = ''
        document.getElementById('btn_yesterday').style.color = 'red'
      }
      this.queryparams.page = 1
      this.queryparams.rq = this.rq
      this.queryparams.patientid = this.scname
      this.getPatients(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getPatients(this.queryparams)
    },
    rowClick(row, event, column) {
      this.patientid = row.patientid
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      if (date === null) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getPatients(this.queryparams)
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
