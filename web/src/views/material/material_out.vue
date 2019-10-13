<template>
    <div>
        <div class="filter-container">
              <el-date-picker v-model="fromdate" style="width: 160px" value-format="yyyy-MM-dd" class="myInput" type="date" placeholder="出库日期开始">
              </el-date-picker>
              <el-date-picker v-model="todate" style="width: 160px" value-format="yyyy-MM-dd" class="myInput" type="date" placeholder="出库日期结束">
              </el-date-picker>
              <el-input
                v-model="materialname"
                class="myInput"
                style="width: 180px;"
                @keyup.enter.native="handleFilter"
                placeholder="耗材名称">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" @click="handleCreate" type="primary" icon="el-icon-plus">出库</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column type="index" label="序号"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="outdate" label="出库日期" width="100" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="material.type" label="耗材类型"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="material.name" label="耗材名称" width="160" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="material.code" label="条码" width="100" align="center">
            </el-table-column>
            <el-table-column prop="price" label="单价" width="90" align="center">
            </el-table-column>
            <el-table-column prop="amount" label="出库数量" width="80" align="center">
            </el-table-column>
            <el-table-column prop="stock" label="库存数量"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="operator" label="操作者" width="90" align="center">
            </el-table-column>
            <el-table-column prop="factory" label="厂商" width="140" align="center" show-overflow-tooltip>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px">
                <el-pagination background
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
          <el-dialog  title="耗材库存" width="60%" :visible.sync="dialogListVisible">
            <div style="float: left">
              <el-select v-model="hctype" clearable style="width: 140px" class="myInput" placeholder="耗材类型">
                <el-option label="血管路" value="血管路" >
                </el-option>
                <el-option label="留置导管" value="留置导管" >
                </el-option>
              </el-select>
              <el-input
                v-model="hcname"
                @keyup.enter.native="stock_handleFilter"
                style="width: 140px;margin-right: 10px;"
                class="myInput" placeholder="耗材名称">
              </el-input>
              <el-button
                type="primary"
                size="small"
                icon="el-icon-search"
                @click="stock_handleFilter"
                style="margin-left: 20px;">
              </el-button>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination
                  background
                  @current-change="stock_handleCurrentChange"
                  :current-page="stock_listQuery.page"
                  :page-size="stock_listQuery.limit"
                  layout="prev, pager, next"
                  :total="stock_total">
                </el-pagination>
            </div>
            <el-table
              ref="multipleTable"
              @row-click="rowClick"
              :data="stock_list"
              v-loading="listLoading"
              @selection-change="selectChange">
              <el-table-column type="selection" width="55" class="selection">
              </el-table-column>
              <el-table-column prop="name" label="耗材名称" width="160" show-overflow-tooltip>
              </el-table-column>
              <el-table-column prop="gg" label="规格"  width="120" align="center">
              </el-table-column>
              <el-table-column prop="dw" label="单位" width="100" align="center">
              </el-table-column>
              <el-table-column prop="jiage" label="单价" width="100" align="center">
              </el-table-column>
              <el-table-column prop="kucun" label="库存数量"  width="80" align="center">
              </el-table-column>
              <el-table-column prop="firm" label="厂商" width="200" show-overflow-tooltip align="center">
              </el-table-column>
            </el-table>
            <div>
               <div style="margin-top: 10px">出库明细</div>
               <el-table :data="multipleSelection">
                  <el-table-column type="index" label="序号"  width="60">
                  </el-table-column>
                 <el-table-column prop="name" label="耗材名称" width="140">
                  </el-table-column>
                  <el-table-column prop="gg" label="规格"  width="140">
                  </el-table-column>
                  <el-table-column prop="dw" label="单位" width="120">
                  </el-table-column>
                  <el-table-column prop="kucun" label="库存数量"  width="120">
                  </el-table-column>
                  <el-table-column prop="amount" label="出库数量" width="120">
                  <template slot-scope="scope">
                      <el-input v-model="scope.row.amount" type="number" size="small" placeholder="出库数量">
                      </el-input>
                  </template>
                  </el-table-column>
                </el-table>
                <div style="margin-top: 15px;margin-bottom: 20px">
                  <label style="margin-left: 10px">出库单号：</label>
                  <input type="text" v-model="stockoutNo" style="height: 25px;"/>
                  <label style="margin-left: 40px">出库方式：</label>
                  <el-select v-model="outtype" style="margin-right: 40px;width: 140px" class="myInput">
                      <el-option label="正常出库" value="正常出库" ></el-option>
                      <el-option label="过期出库" value="过期出库" ></el-option>
                      <el-option label="其他" value="其他" ></el-option>
                  </el-select>
                  <el-button
                    size="small"
                    type="primary"
                    style="float: right;margin-right: 20px;"
                    icon="el-icon-check"
                    @click="submitStockOutData"
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

        <div>
          <el-dialog  title="耗材出库" width="60%" :visible.sync="dialogFormVisible">
                  <el-form  :model="materialStock" ref="dataForm"   label-position="left" label-width="70px" style='width:90%; margin-left:50px;'>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="类型" prop="type">
                              <el-select v-model="materialStock.material.type" clearable style="width: 120px" class="myInput">
                                <el-option v-for="item in materialSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                            </el-select>
                            </el-form-item>
                          </el-col>
                          <el-col :span="8">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="materialStock.material.name" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                          <el-col :span="8">
                            <el-form-item label="单价" prop="price">
                              <el-input v-model="materialStock.price" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="入库数量" prop="amount">
                              <el-input v-model="materialStock.amount" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="入库单号" prop="sn">
                              <el-input v-model="materialStock.sn" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button size="small" @click="dialogFormVisible = false">取消</el-button>
                  <el-button size="small" type="primary" v-if="dialogStatus=='create'" @click="createData">保存</el-button>
                  <el-button size="small" v-else type="primary" @click="updateData">保存</el-button>
                </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { mymaterialDict, createMaterial, materialStocks, createMaterialStock, updateMaterialStock } from '@/api/login'
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
      stock_list: null,
      stock_total: null,
      stock_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      fromdate: '',
      todate: '',
      materialname: '',
      hcname: '',
      hctype: '',
      multipleSelection: [],
      token: getToken,
      dialogFormVisible: false,
      dialogListVisible: false,
      dialogStatus: '',
      stockoutNo: '',
      outtype: '',
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
      },
      multipleList: [],
      queryparams: {
        status: 1,
        page: 1,
        begindate: '',
        enddate: '',
        type: '',
        name: ''
      },
      params: {
        page: 1,
        status: 2,
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
    getStockList(data) {
      mymaterialDict(data).then(response => {
        this.listLoading = true
        this.stock_list = response.data.results
        this.stock_total = response.data.count
        this.listLoading = false
      })
    },
    handleReset() {
      this.queryparams.status = 1
      this.queryparams.page = 1
      this.fromdate = ''
      this.todate = ''
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
    submitStockOutData() {
      if (this.multipleSelection.length > 0) {
        if (this.stockoutNo === '') {
          this.$notify({
            title: '提示',
            message: '出库单号不能为空',
            type: 'success',
            duration: 2000
          })
        } else {
          this.multipleSelection.forEach((item) => {
            this.material = Object.assign({}, item)
            this.material.sn = this.stockoutNo
            this.material.status = 2 // 出库
            this.material.mat_id = item.id
            this.multipleList.push(this.material)
          })
          createMaterial(this.multipleList).then(() => {
            this.queryparams.status = 1
            this.queryparams.page = 1
            this.getMaterialStockList(this.queryparams)
            this.$notify({
              title: '成功',
              message: '出库成功',
              type: 'success',
              duration: 2000
            })
          })
          this.dialogListVisible = false
        }
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
      this.queryparams.status = 2
      this.queryparams.page = 1
      this.getStockList(this.queryparams) // 查库存
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
            this.queryparams.status = 1
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
            this.queryparams.status = 1
            this.queryparams.page = 1
            this.getMaterialStockList(this.queryparams)
          })
        }
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.status = 1
      this.queryparams.page = 1
      this.queryparams.begindate = this.fromdate
      this.queryparams.enddate = this.todate
      this.queryparams.name = this.materialname
      this.getMaterialStockList(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.status = 1
      this.queryparams.page = val
      this.getMaterialStockList(this.queryparams)
    },
    stock_handleFilter() {
      this.stock_listQuery.limit = 5
      this.stock_listQuery.offset = 0
      this.params.page = 1
      this.params.type = this.hctype
      this.params.name = this.hcname
      this.getStockList(this.params)
    },
    stock_handleCurrentChange(val) {
      this.stock_listQuery.page = val
      this.stock_listQuery.offset = (val - 1) * this.stock_listQuery.limit
      this.queryparams.page = val
      this.getStockList(this.queryparams)
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
