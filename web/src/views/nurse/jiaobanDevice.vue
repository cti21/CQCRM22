<template>
    <div>
        <div class="filter-container">
              <el-select v-model="devicetype" class="myInput" clearable style="width: 140px;margin-right: 10px"  placeholder="设备类型">
                <el-option v-for="item in deviceSelect" :key="item.id" :value="item.name" :label="item.name">
                </el-option>
              </el-select>
              <el-input v-model="devicename" class="myInput" style="width: 140px;" placeholder="设备名称"></el-input>
              <el-select v-model="searchbanci" clearable style="width: 120px;margin-right: 20px" class="myInput" placeholder="班次">
                <el-option v-for="item in banciSelect" :key="item.id" :value="item.name" :label="item.name">
                </el-option>
              </el-select>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" type="primary" @click="handleReset" icon="el-icon-download">清空</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            v-loading="listLoading"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
          >
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="bcname" label="班次" width="70" align="center">
            </el-table-column>
            <el-table-column prop="bedno" label="床位" width="80" align="center">
            </el-table-column>
            <el-table-column prop="device.name" label="设备名称" width="120" align="center">
            </el-table-column>
            <el-table-column prop="device.model" label="设备编号" width="120" align="center">
            </el-table-column>
            <el-table-column prop="device.state" label="设备状态" width="90" align="center">
            </el-table-column>
            <el-table-column prop="date" label="交班日期" width="100" align="center">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="200" align="center" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
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
        </div>

        <div>
          <el-dialog  title="备注" width="45%" :visible.sync="dialogFormVisible">
                  <el-form  :model="tc" ref="dataForm" label-position="left" label-width="10px" style='margin-top: 10px;'>
                      <el-row>
                         <el-col>
                            <el-form-item prop="comment">
                              <el-input type="textarea" v-model="tc.comment" style="width: 100%;"></el-input>
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
import { jiaobanDevice, updatejiaobanDevice } from '@/api/nurse'
import { getToken } from '@/utils/auth'
import { banci } from '@/api/system'
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
  props: ['regid',],
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
      tempList: null,
      deviceSelect: [
        { id: '1', name: '透析设备' },
        { id: '2', name: '水处理设备' },
        { id: '3', name: '通用设备' }
      ],
      devicename: '',
      devicetype: '',
      banciSelect: [],
      searchbanci: '',
      tempname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      tc: {
        id: null,
        comment: ''
      },
      queryparams: {
        page: 1,
        name: '',
        banci: '',
        type: ''
      }
    }
  },
  methods: {
    getJiaobanDevice(data) {
      jiaobanDevice(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getBanciList(data) {
      banci(data).then(response => {
        this.banciSelect = response.data.results
      })
    },
    resetTc() {
      this.tc = {
        id:null,
        comment: ''
      }
    },
    selectChange: function (val) {
      this.tc.content = val
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.queryparams.type = ''
      this.queryparams.banci = ''
      this.devicename = ''
      this.devicetype = ''
      this.searchbanci = ''
      this.getJiaobanDevice(this.queryparams)
    },
    handleCreate() {
      this.resetTc()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
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
          updatejiaobanDevice(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getJiaobanDevice(this.queryparams)
          })
        }
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.devicename
      this.queryparams.type = this.devicetype
      this.queryparams.banci = this.searchbanci
      this.getJiaobanDevice(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getJiaobanDevice(this.queryparams)
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
    this.getBanciList('')
    this.getJiaobanDevice(this.queryparams)
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
