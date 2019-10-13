<template>
    <div>
        <!--<div>按钮点击次数:{{ clickcount }}</div>-->
        <div slot="footer" class="dialog-footer" style="float: right;margin-right: 10px">
            <el-button
              size="small"
              type="primary"
              icon="el-icon-close"
              @click="closeDlg"
            >关闭
            </el-button>
            <!--<el-button type="primary" @click="submitApplyDrug">提交</el-button>-->
        </div>
        <div>药品申请单</div>
        <el-table
          :data="list"
          :header-cell-style="{background:'#F8F8F8'}"
          stripe
          v-loading="listLoading"
          @row-click="rowClick">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="sn" label="单据号" width="145">
            </el-table-column>
            <el-table-column prop="banname" label="班次" width="100">
            </el-table-column>
            <el-table-column prop="area" label="病区" width="80">
            </el-table-column>
            <el-table-column prop="applydate" label="日期" width="140" :formatter="dateFormat">
            </el-table-column>
            <el-table-column prop="nurse" label="领用人"  width="80">
            </el-table-column>
            <el-table-column prop="flag" label="状态"  width="80" :formatter="formatState">
            </el-table-column>
            <el-table-column  label="操作" width="80">
              <template slot-scope="scope">
                  <el-button type="text" size="small" v-if="scope.row.flag === false" @click="submitApplyDrug(scope.row)">提交</el-button>
              </template>
            </el-table-column>
        </el-table>
        <div style="margin-top: 10px">药品申请单明细</div>
        <el-table :data="total_list" v-loading="total_listLoading" @row-click="totalrowClick">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="drugid" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="drug.name" label="药品名称" width="160">
            </el-table-column>
            <el-table-column prop="drug.code" label="药品编号" width="120">
            </el-table-column>
            <el-table-column prop="drug.spec" label="规格" width="100">
            </el-table-column>
            <el-table-column prop="drug.units" label="单位" width="100">
            </el-table-column>
            <el-table-column prop="amount" label="数量" width="100">
            </el-table-column>
        </el-table>
        <div style="margin-top: 10px">药品申请单(床位)</div>
        <el-table :data="detail_list" v-loading="detail_listLoading">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="name" label="药品名称" width="300">
            </el-table-column>
            <el-table-column prop="bedname" label="床位" width="160">
            </el-table-column>
            <el-table-column prop="patientname" label="患者姓名" width="200">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import { Apply_drugs, updateApply_drug, Apply_drug_total, Apply_drug_detail } from '@/api/login'
import moment from 'moment'

export default {
  name: 'ApplyDrug',
  props: ['regid','clickcount'],
  data() {
    return {
      count: 0,
      list: null,
      total: null,
      listLoading: true,

      total_list: null,
      total_listLoading: false,

      detail_list: null,
      detail_listLoading: false,
      dialogFormVisible: false,
      applyDrug: {
        id: null,
        sn: '',
        applydate: '',
        bc_id: '',
        area_id: ''
      }
    }
  },
  methods:{
    getApplyDrugList() {
      Apply_drugs().then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getApplyDrugTotalList(data) {
      Apply_drug_total(data).then(response => {
        this.total_listLoading = true
        this.total_list = response.data.results
        this.total = response.data.count
        this.total_listLoading = false
      })
    },
    getApplyDrugDetailList(data) {
      Apply_drug_detail(data).then(response => {
        this.detail_listLoading = true
        this.detail_list = response.data.results
        this.total = response.data.count
        this.detail_listLoading = false
      })
    },
    closeDlg() {
      this.$emit('showDlg')
    },
    submitApplyDrug(row) {
      /*
      if (this.list.length > 0) {
        this.list.forEach((item) => {
          this.applyDrug = Object.assign({}, item)
          this.applyDrug.bc_id = 1
          this.applyDrug.area_id = 1
          updateApply_drug(this.applyDrug).then(() => {
            this.$notify({
              title: '成功',
              message: '提交成功',
              type: 'success',
              duration: 2000
            })
          })
          this.$emit('showDlg')
        })
      }
      */
      this.applyDrug = Object.assign({}, row) // copy obj
      this.applyDrug.bc_id = 1
      this.applyDrug.area_id = 1
      console.log(this.applyDrug)
      updateApply_drug(this.applyDrug).then(() => {
        this.$notify({
          title: '成功',
          message: '提交成功',
          type: 'success',
          duration: 2000
        })
        this.$emit('showDlg')
      })
    },
    rowClick(row, event, column) {
      this.getApplyDrugTotalList(row.id)
    },
    totalrowClick(row, event, column) {
      const params = {
        id: row.id,
        drugid: row.drugid
      }
      this.getApplyDrugDetailList(params)
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
      this.getApplyDrugList()
    }
  },
  created: function() {
    this.getApplyDrugList()
  }
}
</script>
