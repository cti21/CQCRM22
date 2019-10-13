<template>
    <div>
        <el-row>
            <el-input
              v-model="searchname"
              class="myInput"
              style="width: 220px;margin-right: 20px"
              @keyup.enter.native="handleFilter"
              suffix-icon="el-icon-search"
              placeholder="请输入名称">
            </el-input>
            <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </el-row>
        <el-row style="margin:20px;">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <el-table-column type="index" label="序号"  width="100">
            </el-table-column>
            <el-table-column prop="name" label="医院名称" width="200">
            </el-table-column>
            <el-table-column prop="begindate" label="开始日期" width="100">
            </el-table-column>
            <el-table-column prop="enddate" label="结束日期" width="100">
            </el-table-column>
            <el-table-column prop="contactman" label="联系人" width="90">
            </el-table-column>
            <el-table-column prop="contactman" label="联系方式" width="100">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination background
                               @current-change="handleCurrentChange"
                               :current-page="listQuery.page"
                               :page-size="listQuery.limit"
                               layout="total, prev, pager, next"
                               :total="total">
                </el-pagination>
          </div>
        </el-row>

        <!--合作医院新增、编辑-->
        <div>
          <el-dialog  title="财务信息" width="55%" :visible.sync="dialogEditVisible">
              <el-form  :model="cooHospital" ref="editForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="名称"  prop="name">
                          <el-input v-model="cooHospital.name" style="width: 90%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                      <el-col :span="12">
                        <el-form-item label="地址"  prop="address">
                          <el-input v-model="cooHospital.address" style="width: 90%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                  <el-row>
                     <el-col :span="12">
                        <el-form-item label="联系人"  prop="contactman">
                          <el-input v-model="cooHospital.contactman" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col  :span="12">
                        <el-form-item label="联系方式"  prop="telphone">
                          <el-input v-model="cooHospital.telphone" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col>
                        <el-form-item label="备注"  prop="comment">
                          <el-input v-model="cooHospital.comment" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-button size="small" @click="invoice_handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
                   </el-row>
                   <el-row>
                     <el-table
                        :data="invoiceList"
                        :header-cell-style="{background:'#F8F8F8'}"
                        stripe
                      >
                        <el-table-column prop="value" label="分成比例" width="100">
                        </el-table-column>
                        <el-table-column prop="percent" label="类型" width="100">
                        </el-table-column>
                        <el-table-column prop="begindate" label="开始日期" width="100">
                        </el-table-column>
                        <el-table-column prop="enddate" label="结束日期" width="100">
                        </el-table-column>
                        <el-table-column prop="invoicename" label="开票名称" width="90">
                        </el-table-column>
                        <el-table-column prop="id" v-if="false">
                        </el-table-column>
                        <el-table-column label="操作" fixed="right" align="center">
                          <template slot-scope="scope">
                              <el-button type="text" size="small" @click="invoice_handleUpdate(scope.row)">修改</el-button>
                              <el-button type="text" size="small" @click="invoice_handleDelete(scope.row)">删除</el-button>
                          </template>
                        </el-table-column>
                     </el-table>
                   </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  @click="dialogEditVisible = false"
                  icon="el-icon-close"
                >关闭</el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogStatus=='update'"
                  @click="updateData">保存
                </el-button>
                <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="createData">保存
                  </el-button>
              </div>
          </el-dialog>
        </div>

        <!--开票设置新增、编辑-->
        <div>
           <el-dialog  title="开票设置" width="50%" :visible.sync="dialogFormVisible">
              <el-form :model="invoice_set" ref="invoiceForm" :rules="rules" label-position="left" style='width:90%; margin-left:50px;'>
                  <el-row>
                     <el-col :span="12">
                        <el-form-item label="分成比例" prop="value">
                          <el-input v-model="invoice_set.value" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="开票名称" prop="invoice_id">
                          <el-select v-model="invoice_set.invoice_id" style="width: 60%" class="myInput" placeholder="开票名称">
                            <el-option v-for="item in invoice" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col :span="12">
                        <el-form-item label="开始日期" prop="begindate">
                          <el-date-picker v-model="invoice_set.begindate" type="date" value-format="yyyy-MM-dd"
                                        format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                    <el-col :span="12">
                        <el-form-item label="分成类型" prop="profit_distri_id">
                          <el-select v-model="invoice_set.profit_distri_id" style="width: 60%" class="myInput" placeholder="分成类型">
                            <el-option v-for="item in profitdivide" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                         </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col :span="12">
                        <el-form-item label="结束日期" prop="enddate">
                          <el-date-picker v-model="invoice_set.enddate" type="date" value-format="yyyy-MM-dd"
                                        format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                            </el-date-picker>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                        <el-form-item label="备注" prop="comment">
                          <el-input v-model="invoice_set.comment" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="dialogFormVisible = false"
                  >关闭
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    v-if="invoice_dialogStatus=='create'"
                    @click="invoice_createData">保存
                  </el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="invoice_updateData">保存
                  </el-button>
              </div>
           </el-dialog>
         </div>

    </div>
</template>

<script>
import { coohospitals, createCoohospital, updateCoohospital, profit_distri_dicts, invoice_sets,
  invoice_dicts, deleteCoohospital, createInvoice_set, updateInvoice_set, deleteInvoice_set} from '@/api/system'
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
      searchname: '',
      invoice: {},
      profitdivide: {},
      invoiceList: [],
      dialogFormVisible: false,
      dialogEditVisible: false,
      dialogStatus: '',
      invoice_dialogStatus: '',
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      invoice_set: {
        hospital_id: null,
        invoice_id: null,
        profit_distri_id: null,
        begindate: null,
        enddate: null,
        value: null,
        comment: null
      },
      cooHospital: {
        id: null,
        name: '',
        address: '',
        contactman: '',
        telphone: '',
        comment: '',
        children: []
      }
    }
  },
  methods: {
    getCoohospitals(data) {
      coohospitals(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getInvoice_set(data) {
      invoice_sets(data).then(response => {
        this.invoiceList = []
        this.invoiceList = response.data.results
      })
    },
    getSelectData(data) {
      invoice_dicts(data).then(res => {
        this.invoice = res.data.results
      })
      profit_distri_dicts(data).then(res => {
        this.profitdivide = res.data.results
      })
    },
    resetCoohospital() {
      this.cooHospital = {
        id: '',
        name: '',
        address: '',
        contactman: '',
        telphone: '',
        comment: '',
        children: []
      }
    },
    resetInvoice_set() {
      this.invoice_set = {
        hospital_id: null,
        invoice_id: null,
        profit_distri_id: null,
        begindate: null,
        enddate: null,
        value: null,
        comment: null
      }
    },
    handleCreate() {
      this.resetCoohospital()
      this.invoiceList = []
      this.dialogEditVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['editForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.editForm.validate((valid) => {
        if (valid) {
          createCoohospital(this.cooHospital).then((res) => {
            this.cooHospital = res.data
            this.dialogEditVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getCoohospitals(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.cooHospital = Object.assign({}, row)
      const par = {
        hospital_id: row.id
      }
      this.getInvoice_set(par)
      this.dialogStatus = 'update'
      this.dialogEditVisible = true
      this.$nextTick(() => {
        this.$refs['editForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['editForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.cooHospital)
          updateCoohospital(tempData).then(() => {
            this.dialogEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getCoohospitals(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.cooHospital = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.cooHospital)
        deleteCoohospital(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getCoohospitals(this.listQuery)
        })
      })
    },
    invoice_handleCreate() {
      this.resetInvoice_set()
      if (this.cooHospital.id === '') {
        this.$refs.editForm.validate((valid) => {
          if (valid) {
            createCoohospital(this.cooHospital).then((res) => {
              this.cooHospital = res.data
              // ------------------------------
              this.dialogStatus = 'update'
              this.dialogFormVisible = true
              this.invoice_dialogStatus = 'create'
              this.$nextTick(() => {
                this.$refs['invoiceForm'].clearValidate()
              })
              // -------------------------------
              this.listQuery.page = 1
              this.getCoohospitals(this.listQuery)
            })
          }
        })
      } else {
        this.dialogFormVisible = true
        this.invoice_dialogStatus = 'create'
        this.$nextTick(() => {
          this.$refs['invoiceForm'].clearValidate()
        })
      }
    },
    invoice_createData() {
      this.$refs.invoiceForm.validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.invoice_set)
          tempData.hospital_id = this.cooHospital.id
          createInvoice_set(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            const par = { hospital_id: this.cooHospital.id }
            this.getInvoice_set(par)
          })
        }
      })
    },
    invoice_handleUpdate(row) {
      this.invoice_set = Object.assign({}, row)
      this.invoice_dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['invoiceForm'].clearValidate()
      })
    },
    invoice_updateData() {
      this.$refs['invoiceForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.invoice_set)
          updateInvoice_set(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            const par = {
              hospital_id: this.cooHospital.id
            }
            this.getInvoice_set(par)
          })
        }
      })
    },
    invoice_handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.invoice_set = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.invoice_set)
        deleteInvoice_set(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            hospital_id: this.cooHospital.id
          }
          this.getInvoice_set(par)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getCoohospitals(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getCoohospitals(this.listQuery)
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.getCoohospitals(this.listQuery)
    this.getSelectData(this.listQuery)
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
