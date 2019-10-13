<template>
    <div>
        <div class="filter-container">
              <el-select v-model="devicetype" class="myInput" clearable style="width: 180px;margin-right: 10px"  placeholder="设备类型">
                <el-option v-for="item in deviceSelect" :key="item.id" :value="item.name" :label="item.name">
                </el-option>
              </el-select>
              <el-input v-model="devicename" class="myInput" style="width: 180px;margin-right: 10px;" placeholder="设备名称"></el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="50"  align="center">
            </el-table-column>
            <el-table-column prop="adddate" label="登记日期" :formatter="dateFormat" width="100" align="center">
            </el-table-column>
            <el-table-column prop="type" label="设备类型"  width="100" align="center">
            </el-table-column>
            <el-table-column prop="name" label="设备名称" width="160" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="buydate" label="购买日期" :formatter="dateFormat" width="100" align="center">
            </el-table-column>
            <el-table-column prop="price" label="价格" width="100" align="center">
            </el-table-column>
            <el-table-column prop="commany" label="厂家" width="140" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="phone" label="电话"  width="120" align="center">
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
          <el-dialog  title="设备" width="50%" :visible.sync="dialogFormVisible">
                  <el-form  :model="deviceobj" ref="dataForm"   label-position="left" label-width="70px" style='width:90%; margin-left:50px;'>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="类型" prop="type">
                              <el-select v-model="deviceobj.type" clearable style="width: 120px" class="myInput">
                                <el-option v-for="item in deviceSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                         <el-col :span="8">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="deviceobj.name" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="型号" prop="model">
                              <el-input v-model="deviceobj.model" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                      <el-row>
                        <el-col :span="8">
                            <el-form-item label="购买日期" prop="buydate">
                              <el-date-picker v-model="deviceobj.buydate" style="width: 135px;" class="myInput">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="序列号" prop="sn">
                              <el-input v-model="deviceobj.sn" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="价格" prop="price">
                              <el-input v-model="deviceobj.price" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="电话" prop="phone">
                              <el-input v-model="deviceobj.phone" style="width: 120px;"  class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="16">
                            <el-form-item label="厂家" prop="commany">
                              <el-input v-model="deviceobj.commany" style="width: 320px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button size="small" @click="dialogFormVisible = false" icon="el-icon-close">关闭</el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    v-if="dialogStatus=='create'"
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
import { devices, createdevice, updatedevice, deletedevice } from '@/api/device'
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
  name: 'device_register',
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
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      deviceSelect: [
        { id: '1', name: '透析设备' },
        { id: '2', name: '水处理设备' },
        { id: '3', name: '通用设备' }
      ],
      devicetype: '',
      devicename: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      deviceobj: {
        id:null,
        name: '',
        model: '',
        type: '',
        buydate: '',
        sn: '',
        price: '',
        phone: '',
        commany: ''
      },
      queryparams: {
          page: '',
          name: '',
          type: ''
      }
    }
  },
  methods: {
    getDeviceList(data) {
      devices(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetDevice() {
      this.deviceobj = {
        id:null,
        name: '',
        model: '',
        type: '',
        buydate: '',
        sn: '',
        price: '',
        phone: '',
        commany: ''
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.devicetype = ''
      this.devicename = ''
      this.queryparams.name = ''
      this.queryparams.type = ''
      this.getDeviceList(this.queryparams)
    },
    handleCreate() {
      this.resetDevice()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.deviceobj.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createdevice(this.deviceobj).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getDeviceList(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.deviceobj = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.deviceobj)
          updatedevice(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getDeviceList(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.deviceobj = Object.assign({}, row)
        const tempData = Object.assign({}, this.deviceobj)
        deletedevice(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getDeviceList(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.devicename
      this.queryparams.type = this.devicetype
      this.getDeviceList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getDeviceList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getDeviceList(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.queryparams.page = 1
    this.queryparams.name = ''
    this.queryparams.type = ''
    this.getDeviceList(this.queryparams)
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
