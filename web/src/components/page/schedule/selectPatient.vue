<template>
  <div>
    <el-input
      @keyup.enter.native="handleFilter"
      style="width: 200px;margin-right: 10px;"
      prefix-icon="el-icon-search"
      class="myInput"
      placeholder="请输入姓名/编号/电话"
      v-model="listQuery.name"
    >
    </el-input>
    <el-button
       size="small"
       class="myInput"
       type="primary"
       @click="handleFilter"
       icon="el-icon-search">搜索
    </el-button>

    <el-table
      :data="tableData"
      border
      style="width: 100%;margin-top: 10px"
      :header-cell-style="{background:'#F8F8F8'}"
      :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
      stripe
    >
        <el-table-column prop="patientid" label="患者编号" width="150" align="center">
        </el-table-column>
        <el-table-column prop="name" label="姓名"  width="150" align="center">
        </el-table-column>
        <el-table-column prop="sex" label="性别" width="130" align="center">
        </el-table-column>
        <el-table-column prop="age" label="年龄" width="150" align="center">
        </el-table-column>
        <el-table-column prop="phone1" label="电话" width="120" align="center" show-overflow-tooltip>
        </el-table-column>
        <el-table-column prop="address" label="地址" width="200" align="center">
        </el-table-column>
        <el-table-column fixed="right" label="操作" align="center">
          <template slot-scope="scope">
            <el-button @click="selectPatient2(scope.row)" type="text" size="small">按日期排班</el-button>
            <el-button @click="selectPatient(scope.row,odddual_week)" type="text" size="small">按单双周排班</el-button>
          </template>
        </el-table-column>
    </el-table>
    <div class="pagination-container" align="right">
      <el-pagination
         background
         @current-change="handleCurrentChange"
         :current-page="listQuery.page"
         :page-sizes="[5,10,20,30, 50]"
         :page-size="listQuery.limit"
         layout="total, prev, pager, next, jumper"
         :total="total">
      </el-pagination>
    </div>
  </div>
</template>

<script>
 import { mapGetters, mapMutations } from 'vuex'
 import { getPatient } from './schedule.js'
 export default {
   data() {
     return {
       tableData:[],
       total:6,
       show222: false,
       listQuery: {
         page: 1,
         limit: 5,
         offset: 0,
         name: undefined,
         sort: '+id'
       }
     }
   },
   methods: {
     // 点击页码
     handleCurrentChange(val) {
       this.listQuery.page = val
       getPatient(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
       }).catch(error => {
         alert(error)
         console.log(error)
       })
     },
     // 查询
     handleFilter() {
       this.listQuery.page = 1
       getPatient(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
       }).catch(error => {
         console.log(error)
       })
     },
     selectPatient2(row, odddual_week) {
       this.$store.commit('panban_patient', {
         odddual_week: odddual_week,
         patientid: row['patientid'],
         patientname: row['name'],
         patientsex: row['city']
       })
       this.$router.push({path: '/day'})
     },
     selectPatient(row, odddual_week) {
       this.$store.commit('panban_patient', {
         odddual_week: odddual_week,
         patientid: row['patientid'],
         patientname: row['name'],
         patientsex: row['city']
       })
       this.$router.push({path: '/odddual'})
     },
     ...mapMutations([
       'panban_patient'
     ])
   },
   created() {
     this.listQuery.page = 1
     getPatient(this.listQuery).then(response => {
       this.tableData = response.data.results
       this.total = response.data.count
     })
   },
   computed:mapGetters([
     'odddual_week',
   ]),
   components: {
   }
 }
</script>
<style>
    .el-table td, .el-table th{
      padding:6px 0;
    }
    .el-table .warm-row {
      background: #c0c4cc;
    }
    .myInput .el-input__inner{
      height: 33px;
      border-top-width: 0px;
      border-left-width: 0px;
      border-right-width: 0px;
      border-bottom-width: 1px;
    }
</style>
