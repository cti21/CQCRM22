<template>
    <div>
        <div class="filter-container">
              <el-date-picker
                v-model="fromdate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="监测日期开始">
              </el-date-picker>
              <el-date-picker
                v-model="todate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="监测日期结束">
              </el-date-picker>
              <el-input
                v-model="searchname"
                class="myInput"
                style="width: 180px;margin-right: 10px"
                @keyup.enter.native="handleFilter"
                placeholder="设备名称">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
              <el-button size="small" type="primary" @click="handleMpSet">监测位置设置</el-button>
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
            <el-table-column prop="devicename" label="设备名称" width="110" show-overflow-tooltip align="center">
            </el-table-column>
            <el-table-column prop="sn" label="序列号"  width="110" align="center">
            </el-table-column>
            <el-table-column prop="position" label="监测位置" width="100" align="center">
            </el-table-column>
            <el-table-column prop="specific" label="监测点" width="110" align="center">
            </el-table-column>
            <el-table-column prop="monitordate" label="监测时间" width="150" :formatter="dateFormatTime" align="center">
            </el-table-column>
            <el-table-column prop="flag" label="有/无"  width="80" :formatter="formatBoolean" align="center">
            </el-table-column>
            <el-table-column prop="xijun" label="细菌个数" width="110" align="center">
            </el-table-column>
            <el-table-column prop="dusu" label="内毒素mg/l" width="120" align="center">
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
          <el-dialog  title="细菌内毒素监测新增" width="60%" :visible.sync="dialogAddVisible">
                  <div style="margin-bottom: 10px">
                    <el-button-group>
                        <el-button size="small" type="primary" @click="handleSearch('透析设备')">透析设备</el-button>
                        <el-button size="small" type="primary" @click="handleSearch('水处理设备')">水处理设备</el-button>
                        <el-button size="small" type="primary" @click="handleSearch('浓缩液')">浓缩液</el-button>
                    </el-button-group>
                  </div>
                  <div>
                      <el-table
                        ref="deviceTable"
                        :header-cell-style="{background:'#F8F8F8'}"
                        stripe
                        :data="device_list"
                        @row-click="rowClick">
                        <el-table-column label="选中" width="60px">
                            <template slot-scope="scope">
                              <el-radio class="radio" v-model="radio" :label="scope.row.id" @change.native="getCurrentRow(scope.row)">&nbsp</el-radio>
                            </template>
                        </el-table-column>
                        <el-table-column prop="id"  v-if="false" width="120">
                        </el-table-column>
                        <el-table-column prop="name" label="设备名称" width="160">
                        </el-table-column>
                        <el-table-column prop="sn" label="序列号"  width="120">
                        </el-table-column>
                        <el-table-column prop="model" label="型号" width="100">
                        </el-table-column>
                        <el-table-column prop="buydate" label="购买日期" :formatter="dateFormat" width="100">
                        </el-table-column>
                        <el-table-column prop="price" label="价格" width="80">
                        </el-table-column>
                        <el-table-column prop="commany" label="厂家" width="120">
                        </el-table-column>
                      </el-table>
                  </div>
                  <div>
                      <el-table
                        :data="mpd_list"
                        :header-cell-style="{background:'#F8F8F8'}"
                        stripe
                        @selection-change="selectChange">
                        <el-table-column type="selection" width="55" class="selection" >
                        </el-table-column>
                        <el-table-column prop="id"  v-if="false" width="120">
                        </el-table-column>
                        <el-table-column prop="name" label="监测位置" width="100">
                        </el-table-column>
                        <el-table-column prop="specific" label="监测点"  width="120">
                        </el-table-column>
                        <el-table-column prop="flag" label="有/无" width="100">
                          <template slot-scope="scope">
                              <el-switch v-model="scope.row.flag"></el-switch>
                          </template>
                        </el-table-column>
                        <el-table-column prop="xijun" label="细菌个数" width="140">
                          <template slot-scope="scope">
                              <el-input v-model="scope.row.xijun" type="number" placeholder="细菌个数">
                              </el-input>
                          </template>
                        </el-table-column>
                        <el-table-column prop="dusu" label="内毒素(mg/l)" width="140">
                          <template slot-scope="scope">
                              <el-input v-model="scope.row.dusu" type="number" placeholder="内毒素">
                              </el-input>
                          </template>
                        </el-table-column>
                      </el-table>
                  </div>
                  <div slot="footer" class="dialog-footer">
                    <el-button
                      size="small"
                      icon="el-icon-close"
                      @click="dialogAddVisible = false"
                    >关闭
                    </el-button>
                    <el-button
                      size="small"
                      type="primary"
                      icon="el-icon-check"
                      @click="createData"
                    >保存
                    </el-button>
                  </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="细菌内毒素监测修改" width="60%" :visible.sync="dialogFormVisible">
                  <el-form  :model="mpd_obj" ref="dataForm"   label-position="left" label-width="90px" style='width:90%; margin-left:50px;'>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="设备名称"  prop="devicename">
                              <el-input v-model="mpd_obj.devicename" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="序列号" prop="sn">
                              <el-input v-model="mpd_obj.sn" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                         <el-col :span="8">
                            <el-form-item label="监测位置" prop="position">
                              <el-input v-model="mpd_obj.position" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="部位" prop="specific">
                              <el-input v-model="mpd_obj.specific" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="监测时间" prop="monitordate">
                              <el-date-picker v-model="mpd_obj.monitordate" class="myInput" style="width: 135px">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="有/无" prop="flag">
                              <el-input v-model="mpd_obj.flag" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="细菌个数" prop="xijun">
                              <el-input v-model="mpd_obj.xijun" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="内毒素(mg/l)" prop="dusu">
                              <el-input v-model="mpd_obj.dusu" style="width: 120px;"  class="myInput"></el-input>
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
                    icon="el-icon-check"
                    type="primary"
                    @click="updateData"
                  >保存
                  </el-button>
                </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="监测位置设置" width="60%" :visible.sync="mp_dialogFormVisible">
              <monitorPosition @showDlg="showMpDialog" :clickcount="btncount" ></monitorPosition>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { devices, mpds,monitor_records, createmonitor_record, updatemonitor_record, deletemonitor_record } from '@/api/device'
import monitorPosition from '@/views/device/monitorPosition_Set.vue'
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
  name: 'monitor_record',
  components: {
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    monitorPosition
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
      btncount: 0,
      device_list: null,
      device_type: null,
      device_total: null,
      mpd_list: null,
      mpd_total: null,
      multipleSelection: [],
      currentDeviceid: '',
      fromdate: '',
      todate: '',
      searchname: '',
      token: getToken,
      dialogAddVisible: false,
      dialogFormVisible: false,
      mp_dialogFormVisible: false,
      dialogStatus: '',
      radio: '',
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
      mpd_obj: {
        id: null,
        specific: '',
        position: '',
        devicename: '',
        sn: '',
        monitordate: '',
        xijun: '',
        dusu: '',
        flag: '',
        mpd: '',
        device: ''
      },
      mr_list: [],
      queryparams: {
        page: 1,
        name: '',
        fromdate: '',
        todate: ''
      },
      params: {
        page: 1,
        name: null,
        type: null
      }
    }
  },
  methods: {
    getMonitorRecordList(data) {
      monitor_records(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getDeviceList(data) {
      devices(data).then(response => {
        this.device_list = response.data.results
        this.device_total = response.data.count
      })
    },
    getMpdList(data) {
      mpds(data).then(response => {
        this.mpd_list = response.data.results
        this.mpd_total = response.data.count
      })
    },
    resetMPD() {
      this.mpd_obj = {
        id: null,
        specific: '',
        position: '',
        devicename: '',
        sn: '',
        monitordate: new Date(),
        xijun: '',
        dusu: '',
        flag: '',
        mpd: '',
        device: ''
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
      this.getMonitorRecordList(this.queryparams)
    },
    getCurrentRow(row) {
      this.resetMPD()
      this.currentDeviceid = row.id
      const par = {
        id: null,
        type: this.device_type
      }
      this.getMpdList(par)
    },
    selectChange: function(val) {
      if (val) {
        this.multipleSelection = []
        this.multipleSelection = val
      }
    },
    handleMpSet() {
      this.btncount = this.btncount + 1
      this.mp_dialogFormVisible = true
    },
    handleCreate() {
      this.mpd_list = []
      this.device_type = 0
      this.params.type = 0
      this.resetMPD()
      this.getDeviceList(this.params)
      this.dialogAddVisible = true
    },
    createData() {
      if (this.multipleSelection.length > 0) {
        if (this.currentDeviceid === ""){
          this.$notify({
            title: '提示',
            message: '请选择设备',
            type: 'success',
            duration: 2000
          })
        }
        else {
          this.multipleSelection.forEach((item) => {
            this.resetMPD()
            this.mpd_obj.mpd = item.id
            this.mpd_obj.device = this.currentDeviceid
            this.mpd_obj.flag = item.flag
            this.mpd_obj.xijun = item.xijun
            this.mpd_obj.dusu = item.dusu
            this.mpd_obj.position = item.name
            this.mr_list.push(this.mpd_obj)
          })
          createmonitor_record(this.mr_list).then(() => {
            this.$notify({
              title: '成功',
              message: '保存成功',
              type: 'success',
              duration: 2000
            })
            this.dialogAddVisible = false
            this.queryparams.page = 1
            this.getMonitorRecordList(this.queryparams)
          })
        }
      }
    },
    showMpDialog() {
      this.mp_dialogFormVisible = false
    },
    handleSearch(flag) {
      this.device_list = []
      this.mpd_list = []
      this.params.type = flag
      if (flag === '透析设备') {
        this.device_type = 0
      } else if (flag === '水处理设备') {
        this.device_type = 1
      } else {
        this.device_type = 2
      }
      this.getDeviceList(this.params)
    },
    handleUpdate(row) {
      this.mpd_obj = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.mpd_obj)
          updatemonitor_record(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getMonitorRecordList(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.mpd_obj = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.mpd_obj)
        deletemonitor_record(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getMonitorRecordList(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.fromdate = this.fromdate
      this.queryparams.todate = this.todate
      this.queryparams.name = this.searchname
      this.getMonitorRecordList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getMonitorRecordList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getMonitorRecordList(this.queryparams)
    },
    rowClick(row) {
      this.radio = row.id
      const par = {
        id: null,
        type: this.device_type
      }
      this.getMpdList(par)
    },
    formatBoolean: function(row, column) {
      return row.flag === true ? '是' : '否'
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    },
    dateFormatTime: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.getMonitorRecordList(this.queryparams)
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
