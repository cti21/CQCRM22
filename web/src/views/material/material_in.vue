<template>
    <div>
        <div class="filter-container">
              <el-date-picker
                v-model="fromdate"
                style="width: 160px"
                value-format="yyyy-MM-dd"
                class="myInput"
                type="date"
                placeholder="入库日期开始">
              </el-date-picker>
              <el-date-picker
                v-model="todate"
                style="width: 160px"
                value-format="yyyy-MM-dd"
                class="myInput"
                type="date"
                placeholder="入库日期结束">
              </el-date-picker>
              <el-input
                v-model="materialname"
                class="myInput"
                style="width: 180px;margin-right: 10px;"
                @keyup.enter.native="handleFilter"
                placeholder="耗材名称">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">入库</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column type="index" label="序号"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="indate" label="入库日期" width="100" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="material.type" label="耗材类型"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="material.name" label="耗材名称" width="160" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="material.code" label="条码" width="100" align="center">
            </el-table-column>
            <el-table-column prop="price" label="单价" width="90" align="center">
            </el-table-column>
            <el-table-column prop="amount" label="入库数量" width="80" align="center">
            </el-table-column>
            <el-table-column prop="stock" label="库存数量"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="operator" label="操作者" width="90" align="center">
            </el-table-column>
            <el-table-column prop="factory" label="厂商" width="160" align="center" show-overflow-tooltip>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px">
                <el-pagination
                     background
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-sizes="[5,10,20,30, 50]"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
                </el-pagination>
          </div>
        </div>

        <div>
          <el-dialog  title="耗材字典" width="60%" :visible.sync="dialogListVisible">
            <div style="float: left">
              <el-select v-model="hctype" clearable style="width: 140px" class="myInput" placeholder="耗材类型">
                <el-option label="血管路" value="血管路" >
                </el-option>
                <el-option label="留置导管" value="留置导管" >
                </el-option>
              </el-select>
              <el-input
                v-model="hcname"
                @keyup.enter.native="material_handleFilter"
                style="width: 140px;margin-right: 10px;"
                class="myInput"
                placeholder="耗材名称">
              </el-input>
              <el-button
                type="primary"
                size="small"
                icon="el-icon-search"
                @click="material_handleFilter"
                style="margin-left: 10px;">搜索
              </el-button>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination
                     background
                     @current-change="material_handleCurrentChange"
                     :current-page="material_listQuery.page"
                     :page-size="material_listQuery.limit"
                     layout="prev, pager, next"
                     :total="material_total">
                </el-pagination>
            </div>
            <el-table
              ref="multipleTable"
              :data="material_list"
              @row-click="rowClick"
              v-loading="listLoading"
              @selection-change="selectChange">
              <el-table-column type="selection" width="55" class="selection" >
              </el-table-column>
              <el-table-column prop="name" label="耗材名称" width="160" show-overflow-tooltip>
              </el-table-column>
              <el-table-column prop="type" label="耗材类型"  width="120">
              </el-table-column>
              <el-table-column prop="spec" label="规格" width="100">
              </el-table-column>
              <el-table-column prop="code" label="条码" width="100">
              </el-table-column>
              <el-table-column prop="price" label="单价" width="80">
              </el-table-column>
              <el-table-column prop="factory" label="厂商" width="200" show-overflow-tooltip>
              </el-table-column>
            </el-table>
            <div>
               <div style="margin-top: 10px">入库明细</div>
               <el-table :data="multipleSelection">
                  <el-table-column type="index" label="序号"  width="60">
                  </el-table-column>
                  <el-table-column prop="name" label="耗材名称" width="140">
                  </el-table-column>
                  <el-table-column prop="type" label="耗材类型"  width="120">
                  </el-table-column>
                  <el-table-column prop="spec" label="规格" width="80">
                  </el-table-column>
                  <el-table-column prop="code" label="条码" width="80">
                  </el-table-column>
                  <el-table-column prop="price" label="单价" width="120">
                  <template slot-scope="scope">
                      <el-input v-model="scope.row.price" type="number" size="small" placeholder="单价">
                      </el-input>
                  </template>
                  </el-table-column>
                  <el-table-column prop="amount" label="入库数量" width="120">
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
                    style="float: right;margin-right: 20px;"
                    icon="el-icon-check"
                    @click="submitStockInData"
                  >提交
                  </el-button>
                  <el-button
                    size="small"
                    style="float: right;margin-right: 20px;"
                    icon="el-icon-close"
                    @click="dialogListVisible = false"
                  >关闭
                  </el-button>
                </div>
            </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { materials, createMaterial, materialStocks, createMaterialStock, updateMaterialStock } from '@/api/login'
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
  props: ['clickcount'],
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
      material_list: null,
      material_total: null,
      material_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      dialogListVisible: false,
      fromdate: '',
      todate: '',
      materialname: '',
      hctype: '',
      hcname: '',
      multipleSelection: [],
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      stockinNo: '',
      materialSelect: [
        { id: '1', name: '透析器' },
        { id: '2', name: '滤过透析器' },
        { id: '3', name: '血滤器' },
        { id: '4', name: '血管路' },
        { id: '5', name: '内漏穿刺针'},
        { id: '6', name: '留置导管' },
        { id: '7', name: '碳肾' },
        { id: '8', name: '树脂罐' },
        { id: '9', name: '透析粉' },
        { id: '10', name: '透析A粉'},
        { id: '11', name: '透析干粉桶' },
        { id: '12', name: '血浆分离器' },
        { id: '13', name: '细菌过滤器' },
        { id: '14', name: '补液管' },
        { id: '15', name: '消毒液'},
        { id: '16', name: '活检针' },
        { id: '17', name: '套盘' }
      ],
      material: {
        id: null,
        code: '',
        name: '',
        type: '',
        spec: '',
        units: '',
        factory: '',
        madein: '',
        reuse: false,
        film: '',
        price: '',
        comment: '',
        amount: 0,
        status: 1,
        mat_id: null
      },
      materialStock: {
        id: '',
        material: {
          id: null,
          code: 'a',
          name: '',
          type: '',
          factory: ''
        },
        sn: '',
        price: '',
        amount: 0,
        stock: 0,
        indate: '',
        outdate: '',
        flag: 0,
        operator: '',
        status: '1'
      },
      multipleList: [],
      queryparams: {
        status: 0,
        page: 1,
        begindate: '',
        enddate: '',
        type: '',
        name: ''
      },
      params: {
        page: '',
        name: '',
        type: ''
      }
    }
  },
  methods: {
    getMaterialStockList(data) {
      materialStocks(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getMaterialList(data) {
      materials(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    handleReset() {
      this.queryparams.status = 0
      this.queryparams.page = 1
      this.fromdate = ''
      this.todate = ''
      this.materialname = ''
      this.queryparams.begindate = ''
      this.queryparams.enddate = ''
      this.queryparams.type = ''
      this.queryparams.name = ''
      this.getMaterialStockList(this.queryparams)
    },
    resetMaterialStock() {
      this.materialStock = {
        id: '',
        material: {
          id: null,
          code: '',
          name: '',
          type: '',
          factory: ''
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
    handleCreate() {
      this.dialogListVisible = true
      this.params.page = 1
      this.params.name = ''
      this.params.type = ''
      this.getMaterialList(this.params) // 查耗材字典
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
            this.material = Object.assign({}, item)
            this.material.sn = this.stockinNo
            this.material.status = 1 // 入库
            this.material.mat_id = item.id
            this.multipleList.push(this.material)
          })
          createMaterial(this.multipleList).then(() => {
            this.queryparams.status = 0
            this.queryparams.page = 1
            this.getMaterialStockList(this.queryparams)
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
          this.materialStock.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createMaterialStock(this.materialStock).then(() => {
            this.list.unshift(this.materialStock)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.status = 0
            this.queryparams.page = 1
            this.getMaterialStockList(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.materialStock = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.materialStock)
          updateMaterialStock(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.status = 0
            this.queryparams.page = 1
            this.getMaterialStockList(this.queryparams)
          })
        }
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.status = 0
      this.queryparams.page = 1
      this.queryparams.begindate = this.fromdate
      this.queryparams.enddate = this.todate
      this.queryparams.name = this.materialname
      this.getMaterialStockList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.queryparams.status = 0
      this.getMaterialStockList(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.status = 0
      this.queryparams.page = val
      this.getMaterialStockList(this.queryparams)
    },
    material_handleFilter() {
      this.material_listQuery.limit = 10
      this.material_listQuery.offset = 0
      this.params.page = 1
      this.params.name = this.hcname
      this.params.type = this.hctype
      this.getMaterialList(this.params)
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      this.params.page = val
      this.getMaterialList(this.params)
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
      this.getMaterialStockList(this.queryparams)
    }
  },
  created: function() {
    this.getMaterialStockList(this.queryparams)
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
