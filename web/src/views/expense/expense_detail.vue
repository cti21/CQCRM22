<template>
    <div>
        <div class="filter-container">
          <div style="margin-top: 10px;margin-bottom: 30px">
            <el-table
              :data="prepaymentList"
              v-loading="listLoading"
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              highlight-current-row
              @row-click="rowClick_prepay"
            >
              <el-table-column type="index" label="序号"  width="60">
              </el-table-column>
              <el-table-column prop="id" label="收据号" width="160" v-if="false">
              </el-table-column>
              <el-table-column prop="rcptno" label="收据号" width="150"  show-overflow-tooltip>
              </el-table-column>
              <el-table-column prop="before" label="结前金额" width="100" align="center">
              </el-table-column>
              <el-table-column prop="amount" label="金额" width="80" align="center">
              </el-table-column>
              <el-table-column prop="after" label="结后金额" width="100" align="center">
              </el-table-column>
              <el-table-column prop="type" label="类型" width="70" align="center" :formatter="formatTpye">
              </el-table-column>
              <el-table-column prop="operator" label="操作人" width="70" align="center">
              </el-table-column>
              <el-table-column prop="operatedate" label="操作日期"  width="180" align="center" :formatter="dateFormat">
              </el-table-column>
            </el-table>
          </div>

          <el-date-picker
            v-model="fromdate"
            style="width:180px"
            class="myInput"
            type="date"
            placeholder="输入时间"
            value-format="yyyy-MM-dd">
          </el-date-picker>
          <el-button size="small" type="primary" @click="handleFilter" icon="el-icon-search">搜索</el-button>
          <el-button size="small" type="primary" @click="handleCreate" icon="el-icon-plus">增加</el-button>
          <el-button size="small" type="primary" @click="handleSettle" icon="iconfont iconRectangleCopy">结算</el-button>
          <el-button size="small" type="primary" @click="handleRec" icon="iconfont iconrecord">治疗记录</el-button>
          <el-button size="small" type="primary" @click="getProPostRecord(1)" icon="el-icon-arrow-left">上次治疗</el-button>
          <el-button size="small" type="primary" @click="getProPostRecord(0)" icon="el-icon-arrow-right">下次治疗</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            ref="multipleTable"
            v-loading="listLoading"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            :summary-method="getSummaries"
            show-summary
            @selection-change="expenseSelectChange"
            @row-click="rowClick"
          >
            <el-table-column type="selection" width="60" class="selection" align="center">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="140"  show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="gg" label="规格" width="60" align="center">
            </el-table-column>
            <el-table-column prop="dw" label="单位" width="60" align="center">
            </el-table-column>
            <el-table-column prop="price" label="单价" width="70" align="center">
            </el-table-column>
            <el-table-column prop="count" label="数量" width="70" align="center">
            </el-table-column>
            <el-table-column prop="charges" label="费用" width="80" align="center">
            </el-table-column>
            <el-table-column prop="doctor" label="医生"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="state" label="状态"  width="70" align="center" :formatter="formatState">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center" width="120">
              <template slot-scope="scope">
                  <el-button type="text" size="small" v-if="scope.row.state === 1 && scope.row.type === 0" @click="handleRefund(scope.row)">
                    退费
                  </el-button>
                  <el-button type="text" size="small" v-if="scope.row.state === 0" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <div>
          <el-dialog  title="费用项目" width="60%" :visible.sync="dialogListVisible">
            <div >
              <label style="margin-right: 40px;">类型</label>
              <el-radio-group v-model="hctype" @change="selectChange">
                  <el-radio label="药品">药品</el-radio>
                  <el-radio label="护理">护理</el-radio>
                  <el-radio label="处置">处置</el-radio>
                  <el-radio label="耗材">耗材</el-radio>
              </el-radio-group>
              <el-input
                v-model="hcname"
                style="float: right;width: 200px;margin-left: 50px"
                class="myInput" placeholder="请输入名称"
                suffix-icon="el-icon-search"
                @keyup.enter.native="material_handleFilter"
              >
              </el-input>
            </div>

            <div>
              <el-table
                :data="material_list"
                :header-cell-style="{background:'#F8F8F8'}"
                highlight-current-row
                @row-dblclick="rowdbclick"
                stripe>
                <el-table-column type="index" label="序号"  width="80">
                </el-table-column>
                <el-table-column prop="id" v-if="false">
                </el-table-column>
                <el-table-column prop="name" label="名称" width="200">
                </el-table-column>
                <el-table-column prop="gg" label="规格" align="center"  width="120">
                </el-table-column>
                <el-table-column prop="dw" label="剂量单位" align="center" width="120">
                </el-table-column>
                <el-table-column prop="pack_gg" label="包装规格" width="120">
                </el-table-column>
                <el-table-column prop="firm" label="厂商" width="200">
                </el-table-column>
              </el-table>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination background
                     @current-change="material_handleCurrentChange"
                     :current-page="material_listQuery.page"
                     :page-size="material_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="material_total">
                </el-pagination>
            </div>
            <div>
               <div style="margin-top: 10px">套餐详情</div>
               <div>
                 <el-table
                   :data="multipleSelection"
                   :header-cell-style="{background:'#F8F8F8'}"
                   stripe>
                    <el-table-column type="index" label="序号"  width="50">
                    </el-table-column>
                    <el-table-column prop="id" v-if="false">
                    </el-table-column>
                    <el-table-column prop="name" label="名称" width="160">
                    </el-table-column>
                    <el-table-column prop="dw" label="剂量单位" width="90" align="center">
                    </el-table-column>
                    <el-table-column prop="week" label="频次" width="95" align="center">
                      <template slot-scope="scope">
                          <el-select v-model="scope.row.week" clearable style="width: 75px" class="myInput">
                            <el-option label="QW" value="QW" >
                            </el-option>
                            <el-option label="QD" value="QD" >
                            </el-option>
                            <el-option label="QH" value="QH" >
                            </el-option>
                            <el-option label="ST" value="ST" >
                            </el-option>
                          </el-select>
                      </template>
                    </el-table-column>
                    <el-table-column prop="path" label="用药途径" width="130" align="center">
                      <template slot-scope="scope">
                          <el-select v-model="scope.row.path" clearable style="width: 110px" class="myInput">
                            <el-option label="静脉注射" value="静脉注射" >
                            </el-option>
                            <el-option label="静脉滴注" value="静脉滴注" >
                            </el-option>
                            <el-option label="肌肉注射" value="肌肉注射" >
                            </el-option>
                            <el-option label="皮下注射" value="皮下注射" >
                            </el-option>
                            <el-option label="局部溶栓" value="局部溶栓" >
                            </el-option>
                            <el-option label="口服" value="口服" >
                            </el-option>
                            <el-option label="舌下含服" value="舌下含服" >
                            </el-option>
                          </el-select>
                      </template>
                    </el-table-column>
                    <el-table-column prop="count" label="单次剂量" width="130" align="center">
                      <template slot-scope="scope">
                          <el-input v-model="scope.row.count" type="number" size="small" placeholder="单次剂量">
                          </el-input>
                      </template>
                    </el-table-column>
                    <el-table-column label="操作" fixed="right" align="center">
                      <template slot-scope="scope">
                        <el-button type="text" size="small" @click="dict_handleDelete(scope.row)">删除</el-button>
                      </template>
                    </el-table-column>
                  </el-table>
               </div>
            </div>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                style="height:33px;padding-top: 8px"
                @click="submitData">提交
              </el-button>
              <el-button
                size="small"
                style="height:33px;padding-top: 8px"
                icon="el-icon-close"
                @click="dialogListVisible = false">关闭
              </el-button>
            </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog title="治疗记录" width="40%" :visible.sync="dialogFormVisible">
            <div style="margin-bottom: 30px;">
              <el-table
                :data="recordList"
                :header-cell-style="{background:'#F8F8F8'}"
                highlight-current-row
                @row-click="rowClick_rec"
                style="width: 580px;margin: 5px;">
                <el-table-column type="index" label="序号"  width="200" align="center">
                </el-table-column>
                <el-table-column prop="operatedate" label="透析日期" width="300"  align="center">
                </el-table-column>
              </el-table>
            </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { outp_bill_items, updateOutp_bill_items, deleteOutp_bill_items, prepayment } from '@/api/expense'
import { createxyjh } from '@/api/system'
import { chuzhiDict, huliDict, mydrugDict, mymaterialDict, getProPostRecord, getExpenseRecord } from '@/api/login'
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
  props: ['patientid', 'clickcount'],
  data: function() {
    return {
      list: [],
      total: null,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      material_list: null,
      material_total: null,
      material_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      recordList: [],
      recordtotal: null,
      dialogListVisible: false,
      dialogFormVisible: false,
      hctype: '',
      hcname: '',
      ordertype: '',
      fromdate: this.currDateFormat(new Date()),
      multipleSelection: [],
      multipleList: [],
      expenseSelection: [],
      expenseList: [],
      prepaymentList: [],
      token: getToken,
      drug: {
        id: null,
        state: 0,
        action: null
      },
      material: {
        id: null,
        name: '',
        yztype: '',
        gg: '',
        dw: '',
        kind: '',
        orderid: '',
        count: 0,
        feetype: '',
        leixing: '',
        tcid: '',
        parentid: '',
        path: '',
        week: '',
        tcname: '',
        aciton: 0
      },
      queryparams: {
        page: 1,
        status: 0,
        name: '',
        code: '',
        checked: '',
        Startyear: this.currDateFormat(new Date()),
        masterid: '',
        patientid: this.patientid
      },
      params: {
        page: 1,
        name: '',
        type: 0
      },
      para: {
        page: 1,
        patientid: this.patientid,
        operatedate: this.fromdate
      }
    }
  },
  methods: {
    getOutp_Bill_Items(data) {
      outp_bill_items(data).then(response => {
        this.list = []
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getProPostRecord(flag) {
      const pa = {
        patientid: this.patientid,
        fromdate: this.fromdate,
        type: flag
      }
      getProPostRecord(pa).then(response => {
        this.prepaymentList = []
        this.list = []
        this.list = response.data
        this.total = response.data.count
        if (this.list.length > 0) {
          this.fromdate = this.rqFormat(this.list[0].operatedate)
          this.para.operatedate = this.fromdate
          this.para.patientid = this.patientid
          this.getPrepayment(this.para)
        }
      })
    },
    getExpenseRecord(data) {
      getExpenseRecord(data).then(response => {
        this.recordList = []
        this.recordList = response.data
        this.recordtotal = response.data.count
      })
    },
    getHuliList(data) {
      huliDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getChuzhiList(data) {
      chuzhiDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getMaterialList(data) {
      mymaterialDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getDrugList(data) {
      mydrugDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    material_handleFilter() {
      this.material_listQuery.limit = 5
      this.material_listQuery.offset = 0
      this.params.page = 1
      this.params.name = this.hcname
      switch (this.hctype) {
        case '耗材':
          this.getMaterialList(this.params)
          break
        case '药品':
          this.getDrugList(this.params)
          break
        case '处置':
          this.getChuzhiList(this.params)
          break
        case '护理':
          this.getHuliList(this.params)
          break
      }
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      this.params.page = val
      this.getMaterialList(this.params)
    },
    dict_handleDelete(row) {
      this.multipleSelection.splice(this.multipleSelection.findIndex(v => v.id === row.id), 1)
    },
    rowdbclick(row,event) {
      this.multipleSelection = []
      this.multipleSelection.push(row)
    },
    handleRec() {
      const par = {
        patientid: this.patientid,
        fromdate: this.fromdate
      }
      this.getExpenseRecord(par)
      this.dialogFormVisible = true
    },
    rowClick_rec(row, event, column) {
      this.fromdate = row.operatedate
      this.para.operatedate = this.fromdate
      this.getPrepayment(this.para)
      this.queryparams.Startyear = this.fromdate
      this.queryparams.masterid = ''
      this.getOutp_Bill_Items(this.queryparams)
      this.dialogFormVisible = false
    },
    handleCreate() {
      this.multipleSelection = []
      if (this.patientid === '') {
        this.$notify({
          title: '提示',
          message: '请选择患者',
          type: 'success',
          duration: 2000
        })
      } else {
        this.dialogListVisible = true
      }
    },
    submitData() {
      if (this.multipleSelection.length > 0) {
        const obj = this.multipleSelection[0]
        if (!obj.count) {
          this.$notify({
            title: '提示',
            message: '单次剂量不能为空',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (!Number.isInteger(Number(obj.count))) {
          this.$notify({
            title: '提示',
            message: '单次剂量必须为数值',
            type: 'success',
            duration: 2000
          })
          return
        }
        this.multipleList = []
        this.multipleSelection.forEach((item) => {
          this.material = Object.assign({}, item)
          this.material.orderid = item.id
          this.material.leixing = item.kind
          if (this.material.kind !== 3) {
            this.material.path = 'a'
            this.material.week = 'a'
            this.material.feetype = 'a'
          } else {
            this.material.feetype = this.feetype
          }
          this.material.tcid = 1
          this.material.parentid = -1
          this.material.patientid = this.patientid
          this.material.action = 3 // 向费用明细表插入数据
          this.multipleList.push(this.material)
        })
        createxyjh(this.multipleList).then(() => {
          this.$notify({
            title: '成功',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogListVisible = false
          this.queryparams.page = 1
          this.queryparams.masterid = ''
          this.getOutp_Bill_Items(this.queryparams)
        })
      }
    },
    expenseSelectChange: function(val) {
      if (val) {
        this.expenseSelection = []
        this.expenseSelection = val
      }
    },
    rowClick(row, event, column) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    rowClick_prepay(row, event, column) {
      this.queryparams.masterid = row.id
      this.getOutp_Bill_Items(this.queryparams)
    },
    handleSettle() {
      if (this.expenseSelection.length < 0) {
        this.$notify({
          title: '提示',
          message: '请选择收费记录',
          type: 'success',
          duration: 2000
        })
        return
      }
      this.expenseList = []
      this.expenseSelection.forEach((item) => {
        this.drug = Object.assign({}, item)
        this.drug.id = item.id
        this.drug.action = 1 // 1结算, 2退费
        this.expenseList.push(this.drug)
      })
      updateOutp_bill_items(this.expenseList).then(() => {
        this.$notify({
          title: '成功',
          message: '结算成功',
          type: 'success',
          duration: 2000
        })
        this.para.operatedate = this.fromdate
        this.getPrepayment(this.para)
        this.queryparams.page = 1
        this.queryparams.masterid = ''
        this.getOutp_Bill_Items(this.queryparams)
      })
    },
    handleRefund(row) {
      this.expenseList = []
      this.drug = Object.assign({}, row)
      this.drug.id = row.id
      this.drug.action = 2 // 1结算, 2退费
      this.expenseList.push(this.drug)
      updateOutp_bill_items(this.expenseList).then(() => {
        this.$notify({
          title: '成功',
          message: '退费成功',
          type: 'success',
          duration: 2000
        })
        this.para.operatedate = this.fromdate
        this.getPrepayment(this.para)
        this.queryparams.page = 1
        this.queryparams.Startyear = this.fromdate
        this.queryparams.masterid = ''
        this.getOutp_Bill_Items(this.queryparams)
      })
    },
    handleDelete(row) {
      const tempData = Object.assign({}, row) // copy obj
      deleteOutp_bill_items(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
        this.queryparams.page = 1
        this.queryparams.masterid = ''
        this.getOutp_Bill_Items(this.queryparams)
      })
    },
    getPrepayment(data) {
      prepayment(data).then(response => {
        this.prepaymentList = []
        this.prepaymentList = response.data.results
      })
    },
    selectChange: function(val) {
      this.material_list = null
      this.params.page = 1
      this.params.name = ''
      this.hcname = ''
      this.ordertype = val
      switch (val) {
        case '耗材':
          this.getMaterialList(this.params)
          break
        case '药品':
          this.feetype = '收费'
          this.params.type = 0
          this.getDrugList(this.params)
          break
        case '处置':
          this.getChuzhiList(this.params)
          break
        case '护理':
          this.getHuliList(this.params)
          break
      }
    },
    handleFilter() {
      this.para.operatedate = this.fromdate
      this.getPrepayment(this.para)
      this.queryparams.Startyear = this.fromdate
      this.queryparams.masterid = ''
      this.getOutp_Bill_Items(this.queryparams)
    },
    getSummaries(param) {
      const { columns, data } = param
      const sums = []
      columns.forEach((column, index) => {
        if (index === 0) {
          sums[index] = '合计:'
          return
        }
        if (index === 1 || index === 2 || index === 3 || index === 4 || index === 8) {
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
    formatTpye: function(row, column) {
      const qd = row.type
      let s = ''
      switch (qd) {
        case 0:
          s = '待结算'
          break
        case 1:
          s = '预交金'
          break
        case 2:
          s = '退费'
          break
        case 3:
          s = '结算'
          break
      }
      return s
    },
    formatState: function(row, column) {
      const qd = row.state
      let s = ''
      switch (qd) {
        case 0:
          s = '待结算'
          break
        case 1:
          s = '已结算'
          break
        case 2:
          s = '已退费'
          break
      }
      return s
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm')
    },
    rqFormat: function(rq) {
      if (rq === undefined) {
        return ''
      }
      if (rq === '') {
        return ''
      }
      return moment(rq).format('YYYY-MM-DD')
    },
    currDateFormat: function(date) {
      const y = date.getFullYear()
      let m = date.getMonth() + 1
      m = m < 10 ? ('0' + m) : m
      let d = date.getDate()
      d = d < 10 ? ('0' + d) : d
      return y + '-' + m + '-' + d
    }
  },
  watch: {
    clickcount: function() {
      this.prepaymentList = []
      this.list = []
      this.para.operatedate = this.fromdate
      this.getPrepayment(this.para)
      this.queryparams.masterid = ''
      this.getOutp_Bill_Items(this.queryparams)
    },
    patientid: function() {
      this.prepaymentList = []
      this.list = []
      this.para.operatedate = this.fromdate
      this.para.patientid = this.patientid
      console.log('watch')
      console.log(this.para)
      this.getPrepayment(this.para)
      this.queryparams.patientid = this.patientid
      this.queryparams.masterid = ''
      this.getOutp_Bill_Items(this.queryparams)
    }
  },
  created: function() {
    this.prepaymentList = []
    this.list = []
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
    .current-row > td {
       background: rgba(0, 158, 250, 0.219) !important;
    }
</style>
