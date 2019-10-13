<template>
    <div>
        <div slot="footer" class="dialog-footer" style="float: left">
            <el-input
              v-model="searchname"
              style="width: 280px;"
              class="myInput"
              prefix-icon="el-icon-search"
              @keyup.enter.native="handleFilter"
              placeholder="请输入患者姓名/编号">
            </el-input>
        </div>

        <div style="margin-bottom: 20px;">
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
            <el-table
              :data="list"
              v-loading="listLoading"
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              highlightCurrentRow
              @row-click="rowClick">
                <el-table-column type="index" label="序号"  width="50" align="center">
                </el-table-column>
                <el-table-column prop="id" v-if="false" width="160">
                </el-table-column>
                <el-table-column prop="name" label="姓名" width="100">
                </el-table-column>
                <el-table-column prop="patientid" label="编号" width="120">
                </el-table-column>
                <el-table-column prop="sex" label="性别" width="80">
                </el-table-column>
                <el-table-column prop="age" label="年龄" width="80">
                </el-table-column>
                <el-table-column prop="phone1" label="电话"  width="120">
                </el-table-column>
                <el-table-column prop="address" label="地址"  width="180">
                </el-table-column>
                <el-table-column prop="balance" label="预交金" width="80">
                </el-table-column>
            </el-table>
        </div>
        <div slot="footer" class="dialog-footer" style="margin-right: 20px;margin-bottom: 20px;">
            <label style="margin-left: 10px">退款金额：</label>
            <input type="text" v-model="amount" style="height: 25px;"/>
            <el-button
              size="small"
              icon="el-icon-close"
              style="float: right;margin-left: 10px"
              @click="closeDlg">关闭
            </el-button>
            <el-button
              size="small"
              icon="el-icon-check"
              type="primary"
              style="float: right"
              @click="createData">保存
            </el-button>
        </div>
    </div>
</template>

<script>
import { patient_Drug } from '@/api/login'
import { createPrepayment } from '@/api/expense'
import moment from 'moment'

export default {
  name: 'refund',
  props: ['clickcount',],
  data() {
    return {
      count: 0,
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        patientid: '',
        rq: '',
        sort: '+id'
      },
      patientid: '',
      amount: 0,
      searchname: '',
      dialogFormVisible: false
    }
  },
  methods: {
    getPatientList(data) {
      patient_Drug(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    createData() {
      if (this.patientid === '') {
        this.$notify({
          title: '提示',
          message: '请选择患者',
          type: 'success',
          duration: 2000
        })
      } else {
        if (this.amount < 0 ) {
          this.$notify({
            title: '提示',
            message: '请选择患者',
            type: 'success',
            duration: 2000
          })
        } else {
          const data = {
            patientid: '',
            money: 0,
            action: 0
          }
          data.patientid = this.patientid
          data.money = this.amount
          data.action = 2
          createPrepayment(data).then(response => {
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.$emit('showDlg')
          })
        }
      }
    },
    closeDlg() {
      this.$emit('showDlg')
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.listQuery.page = 1
      this.listQuery.patientid = this.searchname
      this.getPatientList(this.listQuery)
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.listQuery.patientid = ''
      this.searchname = ''
      this.getPatientList(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getPrepayment(this.listQuery)
    },
    rowClick(row, event, column) {
      this.patientid = row.patientid
    },
    formatState: function(row, column) {
      return row.flag === true ? '已提交' : '待提交'
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm')
    }
  },
  watch: {
    clickcount: function() {
      this.list = []
      this.getPatientList(this.listQuery)
    }
  },
  created: function() {
    this.getPatientList(this.listQuery)
  }
}
</script>
