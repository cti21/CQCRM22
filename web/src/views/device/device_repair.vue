<template>
    <div>
        <div class="filter-container">
              <el-input
                v-model="searchname"
                @keyup.enter.native="handleFilter"
                class="myInput" style="width: 180px;"
                placeholder="设备名称">
              </el-input>
              <el-select
                v-model="searchstate"
                class="myInput"
                clearable
                style="width: 180px;margin-right: 10px"
                placeholder="维修状态">
                <el-option v-for="item in stateSelect" :key="item.id" :value="item.id" :label="item.name">
                </el-option>
              </el-select>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading"
          >
            <el-table-column type="index" label="序号"  width="60" align="left">
            </el-table-column>
            <el-table-column prop="device.name" label="设备名称" width="100" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="device.sn" label="序列号"  width="90" align="center">
            </el-table-column>
            <el-table-column prop="device.model" label="型号" width="90" align="center">
            </el-table-column>
            <el-table-column prop="faultdate" label="故障时间" :formatter="dateFormat" width="100" align="center">
            </el-table-column>
            <el-table-column prop="faultdesc" label="故障描述" width="120" show-overflow-tooltip align="center">
            </el-table-column>
            <el-table-column prop="faultreason" label="故障原因" width="120" show-overflow-tooltip align="center">
            </el-table-column>
            <el-table-column prop="process" label="处理过程"  width="100" show-overflow-tooltip align="center">
            </el-table-column>
            <el-table-column prop="state" label="设备状态"  width="90" align="center">
            </el-table-column>
            <el-table-column prop="reporter" label="上报人" width="80" align="center">
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
          <el-dialog  title="设备新增" width="65%" :visible.sync="dialogListVisible">
            <div style="float: left">
              <el-input v-model="devicename" style="width: 160px" class="myInput" placeholder="设备名称">
              </el-input>
              <el-select v-model="matSelect" clearable style="width: 160px" class="myInput" placeholder="设备类型">
                <el-option label="透析设备" value="透析设备" >
                </el-option>
                <el-option label="水处理设备" value="水处理设备" >
                </el-option>
                <el-option label="通用设备" value="通用设备" >
                </el-option>
              </el-select>
              <el-button
                size="small"
                type="primary"
                style="margin-left: 20px;"
                @click="device_handleFilter"
                icon="el-icon-search">查询
              </el-button>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination background
                     @size-change="device_handleSizeChange"
                     @current-change="device_handleCurrentChange"
                     :current-page="device_listQuery.page"
                     :page-sizes="[5,10,20,30, 50]"
                     :page-size="device_listQuery.limit"
                     layout="prev, pager, next"
                     :total="device_total">
                </el-pagination>
            </div>
            <el-table
              :data="device_list"
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              @row-click="device_rowClick"
              v-loading="listLoading">
              <el-table-column label="选中" width="60px" align="center">
                  <template slot-scope="scope">
                    <el-radio class="radio" v-model="radio" :label="scope.row.id" @change.native="getCurrentRow(scope.row)">&nbsp</el-radio>
                  </template>
              </el-table-column>
              <el-table-column prop="id"  v-if="false">
              </el-table-column>
              <el-table-column prop="name" label="设备名称" width="140" align="center" show-overflow-tooltip>
              </el-table-column>
              <el-table-column prop="sn" label="序列号"  width="120" align="center">
              </el-table-column>
              <el-table-column prop="model" label="型号" width="120" align="center">
              </el-table-column>
              <el-table-column prop="buydate" label="购买日期" :formatter="dateFormat" width="120" align="center">
              </el-table-column>
              <el-table-column prop="price" label="价格" width="100" align="center">
              </el-table-column>
              <el-table-column prop="commany" label="厂家" width="160" align="center" show-overflow-tooltip>
              </el-table-column>
            </el-table>
            <div>
                <div style="margin-top: 20px">
                  <el-row>
                    <el-col :span="8">
                      <label style="margin-left: 10px">故障发生时间：</label>
                      <el-date-picker v-model="drobj.faultdate" class="myInput" style="width: 140px">
                      </el-date-picker>
                    </el-col>
                    <el-col :span="8">
                      <label style="margin-left: 10px">维修开始时间：</label>
                      <el-date-picker v-model="drobj.begindate" class="myInput" style="width: 140px">
                      </el-date-picker>
                    </el-col>
                    <el-col :span="8">
                      <label style="margin-left: 10px">维修结束时间：</label>
                      <el-date-picker v-model="drobj.enddate" class="myInput" style="width: 140px">
                      </el-date-picker>
                    </el-col>
                  </el-row>
                  <el-row  style="padding-top: 10px">
                    <el-col>
                      <label style="margin-left: 10px">错误详细信息：</label>
                      <el-input v-model="drobj.faultinfo" style="width: 83%" class="myInput"></el-input>
                    </el-col>
                  </el-row>
                  <el-row style="padding-top: 10px">
                    <el-col :span="8">
                      <label style="margin-left: 10px;margin-right: 28px">故障描述：</label>
                      <el-input type="textarea" v-model="drobj.faultdesc" style="width: 140px" :rows="2">
                      </el-input>
                    </el-col>
                    <el-col :span="8">
                      <label style="margin-left: 10px;margin-right: 28px;">故障原因：</label>
                      <el-input type="textarea" v-model="drobj.faultreason" style="width: 140px;" :rows="2">
                      </el-input>
                    </el-col>
                    <el-col :span="8">
                      <label style="margin-left: 10px;margin-right: 28px;">处理过程：</label>
                      <el-input type="textarea" v-model="drobj.process" style="width: 140px;" :rows="2">
                      </el-input>
                    </el-col>
                  </el-row>
                  <el-row  style="padding-top: 10px;margin-top: 10px">
                    <el-col>
                      <label style="margin-left: 10px">故障是否排除：</label>
                      <el-radio-group v-model="drobj.state">
                        <el-radio :label="0">是</el-radio>
                        <el-radio :label="1">待观察</el-radio>
                        <el-radio :label="2">未完成</el-radio>
                      </el-radio-group>
                    </el-col>
                  </el-row>
                  <el-row style="margin-top: 15px;margin-bottom: 15px;">
                    <el-button
                      size="small"
                      type="primary"
                      style="float: right;margin-right: 40px;"
                      @click="createData"
                      icon="el-icon-check">保存</el-button>
                    <el-button
                      size="small"
                      style="float: right;margin-right: 20px;"
                      icon="el-icon-close"
                      @click="dialogListVisible = false">关闭</el-button>
                  </el-row>
                </div>
            </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="设备维修" width="60%" :visible.sync="dialogFormVisible">
                  <el-form  :model="drobj" ref="dataForm" label-position="left" label-width="70px" style='width:90%; margin-left:40px;'>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="设备名称" prop="name">
                              <el-input v-model="drobj.device.name" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="8">
                            <el-form-item label="型号"  prop="model">
                              <el-input v-model="drobj.device.model" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                          <el-col :span="8">
                            <el-form-item label="序列号" prop="sn">
                              <el-input v-model="drobj.device.sn" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                         <el-col>
                            <el-form-item label="错误信息" prop="faultinfo">
                              <el-input v-model="drobj.faultinfo" style="width: 600px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="故障时间" prop="faultdate">
                              <el-date-picker v-model="drobj.faultdate" class="myInput" style="width: 140px">
                              </el-date-picker>
                            </el-form-item>
                          </el-col>
                          <el-col :span="8">
                            <el-form-item label="维修开始"  prop="begindate">
                              <el-date-picker v-model="drobj.begindate" class="myInput" style="width: 140px">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                          <el-col :span="8">
                            <el-form-item label="维修结束" prop="enddate">
                              <el-date-picker v-model="drobj.enddate" class="myInput" style="width: 140px">
                              </el-date-picker>
                            </el-form-item>
                          </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="故障描述" prop="faultdesc">
                              <el-input type="textarea" v-model="drobj.faultdesc" style="width: 140px" :rows="4">
                              </el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="8">
                            <el-form-item label="故障原因"  prop="faultreason">
                              <el-input type="textarea" v-model="drobj.faultreason" style="width: 140px" :rows="4">
                              </el-input>
                            </el-form-item>
                         </el-col>
                          <el-col :span="8">
                            <el-form-item label="处理过程" prop="process">
                              <el-input type="textarea" v-model="drobj.process" style="width: 140px" :rows="4">
                              </el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="故障排除" prop="state">
                              <el-radio-group v-model="drobj.state">
                                <el-radio :label="0">是</el-radio>
                                <el-radio :label="1">待观察</el-radio>
                                <el-radio :label="2">未完成</el-radio>
                              </el-radio-group>
                            </el-form-item>
                         </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button size="small" @click="dialogFormVisible = false" icon="el-icon-close">关闭</el-button>
                  <el-button size="small" type="primary" @click="updateData"  icon="el-icon-check">保存</el-button>
                </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { devices, device_repairs, createdevice_repair,
  updatedevice_repair, deletedevice_repair } from '@/api/device'
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
import ElButton from "../../../node_modules/element-ui/packages/button/src/button";

export default {
  name: 'device_repair',
  components: {
    ElButton,
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol },
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
      dialogListVisible: false,
      device_list: null,
      device_total: null,
      device_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        type: '',
        sort: '+id'
      },
      fromdate: '',
      todate: '',
      matSelect: '',
      searchname: '',
      searchstate: '',
      devicename: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      stockinNo: '',
      radio: '',
      stateSelect: [
        { id: '0', name: '故障排除' },
        { id: '1', name: '未排除' },
        { id: '2', name: '继续观察' },
        { id: '3', name: '维修' }
      ],
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
      drobj: {
        id: null,
        device: {
          id: null,
          name: '',
          sn: '',
          model: ''
        },
        faultdate: '',
        begindate: '',
        enddate: '',
        faultinfo: '',
        faultdesc: '',
        faultreason: '',
        process: '',
        state: 0
      },
      queryparams: {
        page: 1,
        name: '',
        state: 0
      }
    }
  },
  methods: {
    getDeviceRepairList(data) {
      device_repairs(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getDeviceList(data) {
      devices(data).then(response => {
        this.listLoading = true
        this.device_list = response.data.results
        this.device_total = response.data.count
        this.listLoading = false
      })
    },
    resetDeviceRepair() {
      this.drobj = {
        id: null,
        device: {
          id: null,
          name: '',
          sn: '',
          model: ''
        },
        faultdate: '',
        begindate: '',
        enddate: '',
        faultinfo: '',
        faultdesc: '',
        faultreason: '',
        process: '',
        state: 0
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.state = ''
      this.queryparams.name = ''
      this.searchstate = ''
      this.searchname = ''
      this.getDeviceRepairList(this.queryparams)
    },
    getCurrentRow(row) {
      this.drobj.device.id = row.id
      this.drobj.device.name = row.name
      this.drobj.device.model = row.model
      this.drobj.device.sn = row.sn
    },
    device_rowClick(row) {
      this.radio = row.id
      this.getCurrentRow(row)
    },
    handleCreate() {
      this.resetDeviceRepair()
      this.dialogListVisible = true
      this.getDeviceList(this.device_listQuery) // 查设备列表
    },
    createData() {
      this.drobj.id = parseInt(Math.random() * 100) + 1024 // mock a id
      createdevice_repair(this.drobj).then(() => {
        this.dialogListVisible = false
        this.$notify({
          title: '成功',
          message: '创建成功',
          type: 'success',
          duration: 2000
        })
        this.queryparams.page = 1
        this.getDeviceRepairList(this.queryparams)
      })
    },
    handleUpdate(row) {
      this.drobj = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.drobj)
          updatedevice_repair(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getDeviceRepairList(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.drobj = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.drobj)
        deletedevice_repair(tempData).then(() => {
          this.$notify({
            title: '提示',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getDeviceRepairList(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.queryparams.state = this.searchstate
      this.getDeviceRepairList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getDeviceRepairList(0)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getDeviceRepairList(this.queryparams)
    },
    device_handleFilter() {
      this.device_listQuery.limit = 5
      this.device_listQuery.offset = 0
      this.device_listQuery.page = 1
      this.device_listQuery.name = this.devicename
      this.device_listQuery.type = this.matSelect
      this.getDeviceList(this.device_listQuery)
    },
    device_handleSizeChange(val) {
      this.device_listQuery.limit = val
      this.getDeviceList(this.device_listQuery)
    },
    device_handleCurrentChange(val) {
      this.device_listQuery.page = val
      this.device_listQuery.offset = (val - 1) * this.device_listQuery.limit
      this.getDeviceList(this.device_listQuery)
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
  created: function() {
    this.getDeviceRepairList(this.queryparams)
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
