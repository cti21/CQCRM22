<template>
    <div>
        <el-row style="margin-top: 10px;">
              <el-button
                size="medium"
                style="margin-right: 40px;float: right;"
                @click="handleCreate"
                type="primary"
                icon="iconfont iconruku">入库
              </el-button>
              <el-input
                v-model="searchname"
                prefix-icon="el-icon-search"
                class="myInput"
                style="width: 240px;float:left;"
                @keyup.enter.native="handleFilter"
                placeholder="请输入药品名称/编号">
              </el-input>
        </el-row>
        <el-row style="margin-top: 10px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="60">
            </el-table-column>
            <el-table-column prop="drug.name" label="药品名称" width="200"  show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="indate" label="入库日期" width="120" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="drug.code" label="药品代码" width="140" align="center">
            </el-table-column>
            <el-table-column prop="amount" label="入库数量" width="120" align="center">
            </el-table-column>
            <el-table-column prop="stock" label="库存数量"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="operator.username" label="操作者" width="110" align="center">
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px"  align="right">
                <el-pagination background
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-sizes="[10,20,30, 50]"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
                </el-pagination>
          </div>
        </el-row>

        <div>
          <el-dialog  title="药品列表" width="60%" :visible.sync="dialogListVisible">
            <div style="float: left">
              <el-input
                v-model="ypname"
                style="width: 240px;margin-right: 10px;"
                suffix-icon="el-icon-search"
                @keyup.enter.native="drug_handleFilter"
                class="myInput"
                placeholder="请输入药品名称/药品代码">
              </el-input>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-search"
                @click="drug_handleFilter"
                style="margin-left: 20px">搜索</el-button>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination background
                     @current-change="drug_handleCurrentChange"
                     :current-page="drug_listQuery.page"
                     :page-size="drug_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="drug_total">
                </el-pagination>
            </div>
            <el-table
              ref="multipleTable"
              :data="drug_list"
              v-loading="listLoading"
              :header-cell-style="{background:'#F8F8F8'}"
              @selection-change="selectChange"
              @row-click="rowClick"
              stripe>
              <el-table-column type="selection" width="55" class="selection" align="center">
              </el-table-column>
              <el-table-column prop="name" label="药品名称" width="140" align="center">
              </el-table-column>
              <el-table-column prop="indicator" label="药品类别"  width="120" align="center">
              </el-table-column>
              <el-table-column prop="spec" label="规格" width="100" align="center">
              </el-table-column>
              <el-table-column prop="code" label="条码" width="100" align="center">
              </el-table-column>
              <el-table-column prop="price" label="单价" width="80" align="center">
              </el-table-column>
              <el-table-column prop="dose_unit" label="剂量单位" width="120" align="center">
              </el-table-column>
            </el-table>
            <div>
               <div style="margin-top: 10px">入库明细</div>
               <el-table
                 :data="multipleSelection"
                 :header-cell-style="{background:'#F8F8F8'}"
                 stripe>
                  <el-table-column type="index" label="序号"  width="60" align="center">
                  </el-table-column>
                  <el-table-column prop="name" label="药品名称" width="140" align="center">
                  </el-table-column>
                  <el-table-column prop="indicator" label="药品类别"  width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="spec" label="规格" width="80" align="center">
                  </el-table-column>
                  <el-table-column prop="code" label="条码" width="80" align="center">
                  </el-table-column>
                  <el-table-column prop="price" label="单价" width="120" align="center">
                  <template slot-scope="scope">
                      <el-input v-model="scope.row.price" type="number" size="small" placeholder="单价">
                      </el-input>
                  </template>
                  </el-table-column>
                  <el-table-column prop="amount" label="人库数量" width="140" align="center">
                  <template slot-scope="scope">
                      <el-input v-model="scope.row.amount" type="number" size="small" placeholder="入库数量">
                      </el-input>
                  </template>
                  </el-table-column>
                </el-table>
                <div style="margin-top: 15px;margin-bottom: 15px">
                  <label style="margin-left: 10px">入库单号：</label>
                  <input type="text" v-model="stockinNo" style="height: 25px;"/>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    style="float: right;margin-right: 20px;" @click="submitStockInData"
                  >提交
                  </el-button>
                  <el-button
                    size="small"
                    style="float: right;margin-right: 20px;"
                    icon="el-icon-close"
                    @click="dialogListVisible = false">关闭
                  </el-button>
                </div>
            </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { createDrug, drugStocks_Person, createDrugStock, updateDrugStock } from '@/api/login'
import { drugs } from '@/api/tx_drug'
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
      drug_list: null,
      drug_total: null,
      drug_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      dialogListVisible: false,
      fromdate: '',
      todate: '',
      searchname: '',
      ypname: '',
      multipleSelection: [],
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      stockinNo: '',
      drug: {
        id: null,
        code: '',
        name: '',
        spec: '',
        units: '',
        form: '',
        toxi_property: '',
        dose_per_unit: '',
        dose_unit: '',
        indicator: '',
        input_code: '',
        price: '',
        amount: 0,
        status: 1,
        feekind: 1,
        patientid: '',
        drugid: null
      },
      drugStock: {
        id: '',
        drug: {
          id: null,
          code: 'a',
          name: '',
          indicator: '',
          units: ''
        },
        sn: '',
        price: '',
        amount: 0,
        stock: 0,
        indate: '',
        outdate: '',
        flag: 0,
        operator: {
          id: null,
          username: ''
        },
        status: '1'
      },
      multipleList: [],
      queryparams: {
        page: 1,
        status: 0,
        name: '',
        code: '',
        fromdate: '',
        todate: '',
        patientid: this.patientid
      },
      params: {
        page: 1,
        name: '',
        code: ''
      }
    }
  },
  methods: {
    getDrugStockList(data) {
      drugStocks_Person(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getDrugList(data) {
      this.drug_list = []
      drugs(data).then(response => {
        this.listLoading = true
        this.drug_list = response.data.results
        this.drug_total = response.data.count
        this.listLoading = false
      })
    },
    resetDrugStock() {
      this.drugStock = {
        id: '',
        drug: {
          id: null,
          code: 'a',
          name: '',
          indicator: '',
          units: ''
        },
        sn: '',
        price: '',
        amount: 0,
        stock: 0,
        indate: '',
        outdate: '',
        flag: 0,
        operator: '',
        status: '0'
      }
    },
    rowClick(row, event, column) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    selectChange: function(val) {
      if (val) {
        this.multipleSelection = []
        this.multipleSelection = val
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.queryparams.fromdate = ''
      this.queryparams.todate = ''
      this.fromdate = ''
      this.todate = ''
      this.searchname = ''
      this.getDrugStockList(this.queryparams)
    },
    handleCreate() {
      this.multipleSelection = []
      this.dialogListVisible = true
      this.getDrugList(this.params) // 查药品列表
    },
    submitStockInData() {

      if (this.multipleSelection.length > 0) {
        if (this.stockinNo === '') {
          this.$notify({
            title: '提示',
            message: '入库单号不能为空',
            type: 'success',
            duration: 2000
          })
        } else {
          this.multipleList = []
          this.multipleSelection.forEach((item) => {
            this.drug = Object.assign({}, item)
            this.drug.sn = this.stockinNo
            this.drug.status = 1 // 入库
            this.drug.price = 10
            this.drug.feekind = 1 // 0为收费1位自备
            this.drug.patientid = this.patientid
            this.drug.drugid = item.id
            this.multipleList.push(this.drug)
          })
          createDrug(this.multipleList).then(() => {
            this.queryparams.page = 1
            this.getDrugStockList(this.queryparams)
            this.$notify({
              title: '成功',
              message: '入库成功',
              type: 'success',
              duration: 2000
            })
          })
          this.dialogListVisible = false
        }
      }
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.drugStock.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createDrugStock(this.drugStock).then(() => {
            this.list.unshift(this.drugStock)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.getDrugStockList(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.drugStock = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.drugStock)
          updateDrugStock(tempData).then(() => {
            for (const v of this.list) {
              if (v.id === this.drugStock.id) {
                const index = this.list.indexOf(v)
                this.list.splice(index, 1, this.drugStock)
                break
              }
            }
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getDrugStockList(this.queryparams)
          })
        }
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.queryparams.fromdate = this.fromdate
      this.queryparams.todate = this.todate
      this.getDrugStockList(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getDrugStockList(this.queryparams)
    },
    drug_handleFilter() {
      this.drug_listQuery.limit = 5
      this.drug_listQuery.offset = 0
      this.params.page = 1
      this.params.name = this.ypname
      this.getDrugList(this.params)
    },
    drug_handleCurrentChange(val) {
      this.drug_listQuery.page = val
      this.drug_listQuery.offset = (val - 1) * this.drug_listQuery.limit
      this.params.page = 1
      this.getDrugList(this.params)
    },
    formatReuse: function(row, column) {
      return row.reuse === true ? '是' : '否'
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  watch: {
    clickcount: function() {
      this.getDrugStockList(this.queryparams)
    },
    patientid: function() {
      this.queryparams.patientid = this.patientid
      this.getDrugStockList(this.queryparams)
    }
  },
  created: function() {
    this.getDrugStockList(this.queryparams)
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
