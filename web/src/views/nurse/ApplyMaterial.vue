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
        </div>
        <div>耗材申请单</div>
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
            <el-table-column prop="sn" label="单据号" width="150">
            </el-table-column>
            <el-table-column prop="banname" label="班次" width="80">
            </el-table-column>
            <el-table-column prop="area" label="病区" width="90">
            </el-table-column>
            <el-table-column prop="applydate" label="日期" width="140" :formatter="dateFormat">
            </el-table-column>
            <el-table-column prop="nurse" label="领用人"  width="80">
            </el-table-column>
            <el-table-column prop="flag" label="状态"  width="80" :formatter="formatState">
            </el-table-column>
            <el-table-column  label="操作" width="80">
              <template slot-scope="scope">
                  <el-button type="text" size="mini" v-if="scope.row.flag === false" @click="submitApplyMaterial(scope.row)">提交</el-button>
              </template>
            </el-table-column>
        </el-table>
        <div style="margin-top: 10px">耗材申请单明细</div>
        <el-table
          :data="total_list"
          :header-cell-style="{background:'#F8F8F8'}"
          stripe
          v-loading="total_listLoading"
          @row-click="totalrowClick">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="materialid" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="material.name" label="耗材名称" width="160">
            </el-table-column>
            <el-table-column prop="material.code" label="耗材编号" width="140">
            </el-table-column>
            <el-table-column prop="material.units" label="单位" width="100">
            </el-table-column>
            <el-table-column prop="amount" label="数量" width="100">
            </el-table-column>
        </el-table>
        <div style="margin-top: 10px">耗材申请单(床位)</div>
        <el-table
          :data="detail_list"
          :header-cell-style="{background:'#F8F8F8'}"
          stripe
          v-loading="detail_listLoading">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="name" label="耗材名称" width="300">
            </el-table-column>
            <el-table-column prop="bedname" label="床位" width="160">
            </el-table-column>
            <el-table-column prop="patientname" label="患者姓名" width="200">
            </el-table-column>
        </el-table>
    </div>
</template>

<script>
import { Apply_materials, updateApply_material, Apply_material_total, Apply_material_detail } from '@/api/login'
import moment from 'moment'

export default {
  name: 'ApplyMaterial',
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
      applyMaterial: {
        id: null,
        sn: '',
        applydate: '',
        bc_id: '',
        area_id: ''
      }
    }
  },
  methods: {
    getApplyMaterialList() {
      Apply_materials().then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getApplyMaterialTotalList(data) {
      Apply_material_total(data).then(response => {
        this.total_listLoading = true
        this.total_list = response.data.results
        this.total = response.data.count
        this.total_listLoading = false
      })
    },
    getApplyMaterialDetailList(data) {
      Apply_material_detail(data).then(response => {
        this.detail_listLoading = true
        this.detail_list = response.data.results
        this.total = response.data.count
        this.detail_listLoading = false
      })
    },
    closeDlg() {
      this.$emit('showMatDlg')
    },
    submitApplyMaterial(row) {
      /*
      if (this.list.length > 0) {
        const multiMaterialList = []
        let listMaterial = []
        listMaterial = this.list.filter(item => item.flag === false)
        listMaterial.forEach((item) => {
          this.applyMaterial = Object.assign({}, item)
          this.applyMaterial.bc_id = 1
          this.applyMaterial.area_id = 1
          multiMaterialList.push(this.applyMaterial)
        })
        console.log(multiMaterialList)
      */
      this.applyMaterial = Object.assign({}, row) // copy obj
      this.applyMaterial.bc_id = 1
      this.applyMaterial.area_id = 1
      console.log(this.applyMaterial)
      updateApply_material(this.applyMaterial).then(() => {
        this.$notify({
          title: '成功',
          message: '提交成功',
          type: 'success',
          duration: 2000
        })
        this.$emit('showMatDlg')
      })
      // }
    },
    rowClick(row, event, column) {
      this.getApplyMaterialTotalList(row.id)
    },
    totalrowClick(row, event, column) {
      const params = {
        id: row.id,
        materialid: row.materialid
      }
      this.getApplyMaterialDetailList(params)
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
      this.getApplyMaterialList()
    }
  },
  created: function() {
    this.getApplyMaterialList()
  }
}
</script>
