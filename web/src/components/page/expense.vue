<template>
    <div>
        <div class="filter-container" style="float: right;margin-right: 50px;margin-bottom: 10px;">
              <el-input
                v-model="searchname"
                style="width: 140px;"
                @keyup.enter.native="handleFilter"
                class="myInput"
                placeholder="输入收据号">
              </el-input>
              <el-date-picker
                v-model="searchStartyear"
                style="width:150px"
                class="myInput"
                type="date"
                placeholder="输入开始时间"
                value-format="yyyy-MM-dd">
              </el-date-picker>
              <el-date-picker
                v-model="searchEndyear"
                style="width:150px" class="myInput"
                type="date"
                placeholder="输入结束时间"
                value-format="yyyy-MM-dd">
              </el-date-picker>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <!--<el-button size="small" type="primary" @click="handleReset" icon="el-icon-download">重置</el-button>-->
        </div>
        <div style="margin-top: 10px">
          <el-table
            :data="list"
            v-loading="listLoading"
            :header-cell-style="{background:'#F8F8F8'}"
            :summary-method="getSummaries"
            show-summary
            stripe>
            <el-table-column type="index" label="序号"  width="50">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="140">
            </el-table-column>
            <el-table-column prop="gg" label="规格"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="dw" label="单位" width="60">
            </el-table-column>
            <el-table-column prop="price" label="价格" width="80" align="center">
            </el-table-column>
            <el-table-column prop="count" label="数量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="charges" label="费用" width="100" align="center">
            </el-table-column>
            <el-table-column prop="type" label="缴费类型" width="80" :formatter="formatFlag" align="center">
            </el-table-column>
            <el-table-column prop="doctor" label="操作人" width="70" align="center">
            </el-table-column>
            <el-table-column prop="operatedate" label="操作时间" width="140" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <!--<el-table-column label="操作" fixed="right" align="center">-->
              <!--<template slot-scope="scope">-->
                  <!--<el-button type="text" size="small" v-if="scope.row.flag === 1" @click="createData(scope.row,3)">退结算</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
          <div class="pagination-container" style="margin-top: 10px;float:right;margin-right: 40px" align="right">
                <el-pagination background
                               @current-change="handleCurrentChange"
                               :current-page="listQuery.page"
                               :page-sizes="[5,10,20,30, 50]"
                               :page-size="listQuery.limit"
                               layout="total, prev, pager, next"
                               :total="total">
                </el-pagination>
          </div>
        </div>
        <!--弹出dialog窗口-->
        <div>
          <el-dialog  title="收费详细信息" width="55%"  :visible.sync="detailFormVisible">
              <outp_bill_item :list="itemList" :masterid="master_id" :flag="flag" @listenToChildEvent="closeDialog" >
              </outp_bill_item>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import outp_bill_item from '@/views/expense/outp_bill_item.vue'
import { updateOutp_rcpt_master,outp_bill_items, myOutp_bill_items } from '@/api/expense'
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
    outp_bill_item
  },
  props: ['patientid'],
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
      searchStartyear: '',
      searchEndyear: '',
      token: getToken,
      detailFormVisible: false,
      dialogStatus: '',
      register_id: '',
      master_id: '',
      master_obj: {
        id: null,
        masterid: '',
        flag: 0
      },
      queryparams: {
        page: 1,
        name: '',
        patientid: this.patientid,
        fromdate: '',
        todate: ''
      },
    }
  },
  methods: {
    getOutp_bill_items(data) {
      myOutp_bill_items(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getOutp_itemList(data) {
      this.itemList = null
      outp_bill_items(data).then(response => {
        this.itemList = response.data.results
      })
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.queryparams.patientid = ''
      this.searchname = ''
      this.queryparams.fromdate = ''
      this.queryparams.todate = ''
      this.getOutp_bill_items(this.queryparams)
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.queryparams.patientid = this.patientid
      this.queryparams.fromdate = this.searchStartyear
      this.queryparams.todate = this.searchEndyear
      this.getOutp_bill_items(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getOutp_bill_items(this.queryparams)
    },
    createData(row,flag) {
      this.flag = flag
      this.master_id = row.id
      this.master_obj.id = row.id
      this.master_obj.masterid = row.id
      this.master_obj.flag = flag
      console.log(this.master_obj)
      updateOutp_rcpt_master(this.master_obj).then(() => {
        this.getOutp_itemList(row.id)
        this.detailFormVisible = true
      })
    },
    closeDialog() {
      this.getOutp_bill_items(this.queryparams)
      this.detailFormVisible = false
    },
    getSummaries(param) {
      const { columns, data } = param
      const sums = []
      columns.forEach((column, index) => {
        if (index === 1) {
          sums[index] = '合计:'
          return
        }
        if (index === 0 || index === 2 || index === 3 || index === 4 || index === 7 || index === 8) {
          sums[index] = ''
          return
        }
        const values = data.map(item => Number(item[column.property]))
        if (!values.every(value => isNaN(value))) {
          sums[index] = values.reduce((prev, curr) => {
            const value = Number(curr);
            if (!isNaN(value)) {
              return prev + curr
            } else {
              return prev
            }
          }, 0)
          sums[index] += ''
        } else {
          sums[index] = ''
        }
      })
      return sums
    },
    formatFlag: function(row, column) {
      let zt = row.type
      let s = ''
      switch (zt) {
        case 0:
          s = '正常交费'
          break
        case 1:
          s = '退费'
          break
      }
      return s
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
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
  watch: {
    patientid: function() {
      this.list = []
      this.queryparams.patientid = this.patientid
      this.queryparams.name = this.searchname
      this.getOutp_bill_items(this.queryparams)
    }
  },
  created: function() {
    this.getOutp_bill_items(this.queryparams)
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
