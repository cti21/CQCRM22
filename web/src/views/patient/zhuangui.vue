<template>
    <div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column type="index" label="序号"  width="80"  align="center">
            </el-table-column>
            <el-table-column prop="date" label="转归日期" width="160" align="center">
            </el-table-column>
            <el-table-column prop="leixing" label="转归类型" width="160" align="center">
            </el-table-column>
            <el-table-column prop="yuanyin" label="转归原因" width="220" align="center">
            </el-table-column>
            <el-table-column prop="otherreason" label="其他原因" width="220" align="center">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="220" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="zgtype" v-if="false">
            </el-table-column>
            <el-table-column prop="zgreason" v-if="false">
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination
                   background
                   @current-change="handleCurrentChange"
                   :current-page="listQuery.page"
                   :page-size="listQuery.limit"
                   layout="total, prev, pager, next"
                   :total="total">
                </el-pagination>
          </div>
        </div>

        <div>
          <el-dialog  title="转归" width="50%" :visible.sync="dialogFormVisible">
                  <el-form  :model="tc" ref="dataForm"   label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="日期"  prop="date">
                              <el-date-picker class="myInput" v-model="tc.date" value-format="yyyy-MM-dd">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="转归类型" prop="zgtype">
                              <el-select v-model="tc.zgtype" clearable style="width: 200px" class="myInput" @change="selectChange">
                                  <el-option v-for="item in zgtypeList" :label="item.name" :key="item.id" :value="item.id" >{{item.name}}
                                  </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                      <el-row>
                       <el-col :span="12">
                          <el-form-item label="转归原因" prop="zgreason">
                            <el-select v-model="tc.zgreason" clearable style="width: 200px" class="myInput" @change="selectChange">
                                <el-option v-for="item in zgreasonList" :label="item.name" :key="item.id" :value="item.id" >{{item.name}}
                                </el-option>
                            </el-select>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="其他原因" prop="otherreason">
                            <el-input type="input" v-model="tc.otherreason" style="width: 200px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                      </el-row>
                      <el-row>
                         <el-col>
                            <el-form-item label="备注" prop="comment">
                              <el-input type="input" v-model="tc.comment" style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button @click="dialogFormVisible = false" icon="el-icon-close">关闭</el-button>
                  <el-button
                    size="small"
                    type="primary"
                    v-if="dialogStatus=='create'"
                    icon="el-icon-check"
                    @click="createData">保存</el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="updateData">保存</el-button>
                </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { pat_zhuangui, zgtype, zgreason, createPat_zhuangui, updatePat_zhuangui, deletePat_zhuangui } from '@/api/login'
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
  props: ['regid', 'patientid'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      zgtypeList: null,
      zgreasonList: null,
      searchname: '',
      tempname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      tc: {
        id: null,
        date: '',
        otherreason: '',
        comment: '',
        patient: '',
        zgtype: '',
        zgreason: ''
      },
      queryparams: {
        page: 1,
        name: '',
        patientid: ''
      },
      params: {
        page: 1
      }
    }
  },
  methods: {
    getZhuangui(data) {
      pat_zhuangui(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getZgtype(data) {
      zgtype(data).then(response => {
        this.zgtypeList = response.data.results
      })
    },
    getZgreason(data) {
      zgreason(data).then(response => {
        this.zgreasonList = response.data.results
      })
    },
    resetTc() {
      this.tc = {
        id: null,
        leixing: '',
        yuanyin: '',
        date: new Date(),
        otherreason: '',
        comment: '',
        patient: '',
        zgtype: '',
        zgreason: ''
      }
    },
    selectChange: function (val) {
      this.tc.content = val
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.searchname = ''
      this.getZhuangui(this.queryparams)
    },
    handleCreate() {
      this.resetTc()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.tc.id = parseInt(Math.random() * 100) + 1024
          this.tc.patient = this.patientid
          createPat_zhuangui(this.tc).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getZhuangui(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.dialogStatus = 'update'
      this.tc = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.tc)
          tempData.patient = this.patientid
          updatePat_zhuangui(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getZhuangui(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.tc = Object.assign({}, row) // copy obj
      const tempData = Object.assign({}, this.tc)
      deletePat_zhuangui(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
        this.queryparams.page = 1
        this.getZhuangui(this.queryparams)
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.getZhuangui(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getZhuangui(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.queryparams.patientid = this.patientid
    this.getZhuangui(this.queryparams)
    this.getZgtype(this.params)
    this.getZgreason(this.params)
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
