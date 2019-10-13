<template>
    <div>
        <div style="margin-right: 50px;margin-bottom: 20px;">
            <el-input
              v-model="searchname"
              class="myInput"
              style="width: 220px;margin-right: 20px"
              prefix-icon="el-icon-search"
              @keyup.enter.native="handleFilter"
              placeholder="药品名称/ 药品代码">
            </el-input>
            <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="60">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="200">
            </el-table-column>
            <el-table-column prop="code" label="代码"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="spec" label="规格" width="60" align="center">
            </el-table-column>
            <el-table-column prop="units" label="单位" width="60" align="center">
            </el-table-column>
            <el-table-column prop="form" label="剂型" width="60" align="center">
            </el-table-column>
            <el-table-column prop="dose_unit" label="剂量单位" width="80" align="center">
            </el-table-column>
            <el-table-column prop="indicator" label="类别"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="input_code" label="输入码" width="90" align="center">
            </el-table-column>
            <el-table-column prop="toxi_property" label="毒理分类" width="90" align="center">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
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

        <div>
          <el-dialog  title="药品信息" width="55%" :visible.sync="dialogFormVisible">
                  <el-form  :model="drug" ref="dataForm" :rules="rules"  label-position="left" label-width="100px" style='width:90%; margin-left:50px;'>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="drug.name" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="代码" prop="code">
                              <el-input v-model="drug.code" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                         <el-col :span="8">
                            <el-form-item label="类别" prop="indicator">
                              <el-select v-model="drug.indicator" clearable style="width: 120px" class="myInput">
                                <el-option v-for="item in materialSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="规格" prop="spec">
                              <el-input v-model="drug.spec" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="单位" prop="units">
                              <el-input v-model="drug.units" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="剂型" prop="form">
                              <el-input v-model="drug.form" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="剂量单位" prop="dose_unit">
                              <el-input v-model="drug.dose_unit" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="输入码" prop="input_code">
                              <el-input v-model="drug.input_code" style="width: 120px;"  class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="毒理分类" prop="toxi_property">
                              <el-input v-model="drug.toxi_property" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="12">
                            <el-form-item label="科室预警数量" prop="alert_amount_dept">
                              <el-input type="number" v-model="drug.alert_amount_dept" style="width: 160px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="科室预警天数" prop="alert_expire_dept">
                              <el-input type="number" v-model="drug.alert_expire_dept" style="width: 160px;"  class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="12">
                            <el-form-item label="自备预警数量" prop="alert_amount">
                              <el-input type="number" v-model="drug.alert_amount" style="width: 160px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="自备预警天数" prop="alert_expire">
                              <el-input type="number" v-model="drug.alert_expire" style="width: 160px;"  class="myInput"></el-input>
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
                    v-if="dialogStatus=='create'"
                    @click="createData">保存
                  </el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="updateData"
                  >保存
                  </el-button>
                </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { createdrug_dict, updateDrug, deleteDrug } from '@/api/login'
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
        name: '',
        sort: '-id'
      },
      searchname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      materialSelect: [
        { id: '1', name: '药品' },
        { id: '2', name: '中草药' },
        { id: '3', name: '原料' },
        { id: '4', name: '化学试剂' },
        { id: '5', name: '敷料'},
        { id: '6', name: '其他' }
      ],
      drug: {
        id: null,
        code: '',
        name: '',
        spec: '',
        units: '',
        form: '',
        toxi_property: '',
        dose_unit: '',
        indicator: '',
        input_code: '',
        sn: '',
        alert_amount_dept: 0,
        alert_expire_dept: 0,
        alert_amount: 0,
        alert_expire: 0,
        drugid: 1,
        price: 0,
        amount: 0,
        feekind: 2,
        patientid: 'A000',
        status: 0
      },
      rules: {
        name: [{ required: true, message: '请输入药品名称', trigger: 'blur' }],
        code: [{ required: true, message: '请输入药品代码', trigger: 'blur' }]
      }
    }
  },
  methods: {
    getDrugList(data) {
      drugs(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetDrug() {
      this.drug = {
        id: null,
        code: '',
        name: '',
        spec: '',
        units: '',
        form: '',
        toxi_property: '',
        dose_unit: '',
        indicator: '',
        input_code: '',
        sn: '',
        pricie: 0,
        amount: 0,
        status: 0
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getDrugList(this.listQuery)
    },
    handleCreate() {
      this.resetDrug()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.drug.id = parseInt(Math.random() * 100) + 1024 // mock a id
          // this.drug.status = 0
          // this.drug.amount = 0
          // this.drug.sn = 'a'
          // this.drug.price = 10
          // this.drug.feekind = 2 // 0为收费1位自备2为假的
          // this.drug.patientid = 'A000'
          // this.drug.drugid = 1
          createdrug_dict(this.drug).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getDrugList(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.drug = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.drug.status = 0
          this.drug.amount = 0
          this.drug.sn = 'a'
          this.drug.price = 10
          this.drug.drugid = 1
          this.drug.feekind = 2 // 0为收费1位自备
          this.drug.patientid = 'A000'
          const tempData = Object.assign({}, this.drug)
          updateDrug(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getDrugList(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.drug = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.drug)
        deleteDrug(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getDrugList(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getDrugList(this.listQuery)
    },

    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getDrugList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.listQuery.page = val
      this.getDrugList(this.listQuery)
    },
    formatReuse: function(row, column) {
      return row.reuse === true ? '是' : '否'
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  watch: {
    clickcount: function() {
      this.getDrugList(this.listQuery)
    }
  },
  created: function() {
    this.getDrugList(this.listQuery)
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
