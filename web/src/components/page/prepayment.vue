<template>
    <div>
        <el-row style="margin-top: 10px">
              <el-input
                v-model="searchname"
                style="width: 200px;"
                @keyup.enter.native="handleFilter"
                class="myInput"
                placeholder="患者姓名/患者编号">
              </el-input>
              <el-input
                v-model="searchrcptno"
                style="width: 180px;"
                @keyup.enter.native="handleFilter"
                class="myInput"
                prefix-icon="el-icon-search"
                placeholder="收据号">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <!--<el-button size="small" type="primary" @click="handleReset" icon="el-icon-download">重置</el-button>-->
              <el-button size="small" type="primary" @click="handlePrepay" icon="iconfont iconchongzhiyufukuanguanli">预交金</el-button>
              <el-button size="small" type="primary" @click="handleRefund" icon="iconfont icontuikuan-xi">退款</el-button>
        </el-row>
        <el-row style="margin-top: 10px">
          <el-table
            :data="list"
            :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="80"  align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="140" align="center">
            </el-table-column>
            <el-table-column prop="patient" label="编号"  width="140" align="center">
            </el-table-column>
            <el-table-column prop="leixing" label="类型" width="120">
            </el-table-column>
            <el-table-column prop="rcptno" label="收据号" width="160" align="center">
            </el-table-column>
            <el-table-column prop="amount" label="金额" width="150" align="center">
            </el-table-column>
            <el-table-column prop="operator" label="操作员" width="120" align="center">
            </el-table-column>
            <el-table-column prop="operatedate" label="操作时间" width="180" :formatter="dateFormat" align="center">
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 10px;float:right;margin-right: 40px" align="right">
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
        </el-row>
        <!--弹出dialog窗口-->
        <div>
          <el-dialog  title="收费详细信息" width="55%"  :visible.sync="detailFormVisible">
              <outp_bill_item :list="itemList" :masterid="master_id" :flag="flag" @listenToChildEvent="closeDialog" >
              </outp_bill_item>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="新增预交金" width="60%" :visible.sync="prepay_dialogFormVisible">
              <prepay @showDlg="showPrepay" :clickcount="prepay_btncount" ></prepay>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="退款" width="60%" :visible.sync="refund_dialogFormVisible">
              <refund @showDlg="showRefund" :clickcount="refund_btncount" ></refund>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import outp_bill_item from '@/views/expense/outp_bill_item.vue'
import prepay from '@/views/expense/prepay.vue'
import refund from '@/views/expense/refund.vue'
import { prepayment } from '@/api/expense'
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
    ElCol,
    outp_bill_item,
    prepay,
    refund
  },
  data: function() {
    return {
      list: null,
      itemList: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      flag: 0,
      searchname: '',
      searchrcptno: '',
      prepay_btncount: 0,
      prepay_dialogFormVisible: false,
      refund_btncount: 0,
      refund_dialogFormVisible: false,
      token: getToken,
      detailFormVisible: false,
      dialogStatus: '',
      register_id: '',
      master_id: '',
      master_obj: {
        id: null,
        register: '',
        flag: 0
      },
      queryparams: {
        page: 1,
        patientid: '',
        rcptno: '',
        operatedate: ''
      }
    }
  },
  methods: {
    getPrepayment(data) {
      prepayment(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    handlePrepay() {
      this.prepay_btncount = this.prepay_btncount + 1
      this.prepay_dialogFormVisible = true
    },
    handleRefund() {
      this.refund_btncount = this.refund_btncount + 1
      this.refund_dialogFormVisible = true
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.patientid = ''
      this.queryparams.rcptno = ''
      this.searchname = ''
      this.searchrcptno = ''
      this.getPrepayment(this.queryparams)
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.patientid = this.searchname
      this.queryparams.rcptno = this.searchrcptno
      this.getPrepayment(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getPrepayment(this.queryparams)
    },
    showPrepay() {
      this.prepay_dialogFormVisible = false
      this.getPrepayment(this.queryparams)
    },
    showRefund() {
      this.refund_dialogFormVisible = false
      this.getPrepayment(this.queryparams)
    },
    closeDialog() {
      this.getPrepayment(this.queryparams)
      this.detailFormVisible = false
    },
    currDateFormat: function(date) {
      const y = date.getFullYear()
      let m = date.getMonth() + 1
      m = m < 10 ? ('0' + m) : m
      let d = date.getDate()
      d = d < 10 ? ('0' + d) : d
      return y + '-' + m + '-' + d
    },
    formatFlag: function(row, column) {
      const zt = row.flag
      let s = ''
      switch (zt) {
        case 0:
          s = '未交费'
          break
        case 1:
          s = '正常交费'
          break
        case 2:
          s = '欠费'
          break
        case 3:
          s = '退费'
          break
      }
      return s
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      else if (date === ''){
        return ''
      }
      else if (date === null){
        return ''
      }
      else {
        return moment(date).format('YYYY-MM-DD HH:mm')
      }
    }
  },
  created: function() {
    this.getPrepayment(this.queryparams)
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
