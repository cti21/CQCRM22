<template>
    <div>
        <el-container>
          <el-aside width="200px">
              <div style="margin-top: 20px">
                <el-input
                  v-model="searchname"
                  class="myInput"
                  style="width: 180px"
                  suffix-icon="el-icon-search"
                  @keyup.enter.native="handleFilter"
                  placeholder="请输入病区名称">
                </el-input>
                <el-table
                  :data="bq_list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  highlight-current-row
                  @row-click="rowClick">
                  <el-table-column prop="name" label="病区" align="center">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false">
                  </el-table-column>
                </el-table>
              </div>
          </el-aside>
          <el-container>
            <el-main style="padding-top: 0px">
                <el-row>
                  <el-input
                    v-model="bedname"
                    class="myInput"
                    style="width: 220px;margin-right: 20px"
                    prefix-icon="el-icon-search"
                    @keyup.enter.native="bed_handleFilter"
                    placeholder="请输入床号">
                  </el-input>
                  <el-button
                    size="small"
                    type="primary"
                    @click="bed_handleFilter"
                    icon="el-icon-search">搜索
                  </el-button>
                  <el-button
                    size="small"
                    style="margin-left: 20px;"
                    @click="handleCreate"
                    type="primary"
                    icon="el-icon-plus">新增
                  </el-button>
                </el-row>
                <el-row style="margin-top: 20px">
                  <el-table
                    ref="multipleTable"
                    :data="list"
                    :header-cell-style="{background:'#F8F8F8'}"
                    stripe
                  >
                    <el-table-column prop="name" label="床号"  width="80" align="center">
                    </el-table-column>
                    <el-table-column prop="flag" label="传染病床位" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="state" label="是否可用" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="device.name" label="设备名称" width="130" align="center">
                    </el-table-column>
                    <el-table-column prop="device.model" label="设备型号" width="130" align="center">
                    </el-table-column>
                    <el-table-column prop="device.type" label="设备类型" width="110" align="center">
                    </el-table-column>
                    <el-table-column prop="device.sn" label="设备编号" width="110" align="center">
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
                </el-row>
                <div class="pagination-container" style="margin-top: 5px" align="right">
                      <el-pagination background
                           @current-change="handleCurrentChange"
                           :current-page="listQuery.page"
                           :page-sizes="[5,10,20,30, 50]"
                           :page-size="listQuery.limit"
                           layout="total, prev, pager, next, jumper"
                           :total="total">
                      </el-pagination>
                </div>
            </el-main>
          </el-container>
        </el-container>

        <div>
          <el-dialog  title="新增床位" width="60%" :visible.sync="dialogListVisible">
            <el-form  :model="bed" ref="addForm" :rules="rules" label-position="left" label-width="90px" style='width:90%; margin-left:40px;'>
              <el-row>
                 <el-col :span="12">
                    <el-form-item label="病床名称" prop="name">
                      <el-input v-model="bed.name"  style="width: 200px;" class="myInput"></el-input>
                    </el-form-item>
                 </el-col>
                 <el-col :span="12">
                    <el-form-item label="设备名称">
                      <el-input v-model="bed.device.name" readonly style="width: 200px;" class="myInput" @focus="deviceVisible=true"></el-input>
                    </el-form-item>
                 </el-col>
               </el-row>
              <el-row>
                 <el-col :span="12">
                    <el-form-item label="设备型号">
                      <el-input v-model="bed.device.model" readonly style="width: 200px;" class="myInput" @focus="deviceVisible=true"></el-input>
                    </el-form-item>
                 </el-col>
                 <el-col :span="12">
                    <el-form-item label="设备编号">
                      <el-input v-model="bed.device.sn" readonly style="width: 200px;" class="myInput" @focus="deviceVisible=true"></el-input>
                    </el-form-item>
                 </el-col>
               </el-row>
              <el-row>
                 <el-col  :span="12">
                    <el-form-item label="传染病床位" prop="flag">
                      <el-radio-group v-model="bed.flag">
                        <el-radio label="否">否</el-radio>
                        <el-radio label="是">是</el-radio>
                      </el-radio-group>
                    </el-form-item>
                  </el-col>
                  <el-col  :span="12">
                    <el-form-item label="是否可用" prop="state">
                      <el-radio-group v-model="bed.state">
                        <el-radio label="是">是</el-radio>
                        <el-radio label="否">否</el-radio>
                      </el-radio-group>
                    </el-form-item>
                  </el-col>
              </el-row>
            </el-form>

            <div v-if="deviceVisible">
                <div style="float: left;margin-left: 30px;">
                  <el-input v-model="devicename" style="width: 150px" class="myInput" placeholder="设备名称">
                  </el-input>
                  <el-select v-model="matSelect" clearable style="width: 140px" class="myInput" placeholder="设备类型">
                    <el-option label="透析设备" value="透析设备" >
                    </el-option>
                    <el-option label="水处理设备" value="水处理设备" >
                    </el-option>
                    <el-option label="通用设备" value="通用设备" >
                    </el-option>
                  </el-select>
                  <el-button size="small" type="primary" style="margin-left: 20px;" icon="el-icon-search" @click="device_handleFilter">查询</el-button>
                </div>

                <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                    <el-pagination background
                         @current-change="device_handleCurrentChange"
                         :current-page="device_listQuery.page"
                         :page-size="device_listQuery.limit"
                         layout="total, prev, pager, next"
                         :total="device_total">
                    </el-pagination>
                </div>
                <div style="margin-left: 20px;">
                  <el-table :data="device_list" highlight-current-row stripe @row-click="device_rowClick">
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
                  <el-table-column prop="model" label="型号" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="buydate" label="购买日期" :formatter="dateFormat" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="price" label="价格" width="80" align="center">
                  </el-table-column>
                  <el-table-column prop="commany" label="厂家" width="160" align="center" show-overflow-tooltip>
                  </el-table-column>
                </el-table>
                </div>
            </div>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button
                size="small"
                style="height:33px;padding-top: 8px"
                icon="el-icon-close"
                @click="dialogListVisible = false"
              >关闭
              </el-button>
              <el-button
                size="small"
                type="primary"
                style="height:33px;padding-top: 8px"
                icon="el-icon-check"
                v-if="dialogStatus=='create'"
                @click="createData"
                >保存
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
import { diseaseArea, beds, xyjhs, createBed, updateBed, deleteBed } from '@/api/system'
import { devices } from '@/api/device'
import { chuzhiDict, huliDict, mydrugDict, mymaterialDict } from '@/api/login'
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
import ElMain from '../../../node_modules/element-ui/packages/main/src/main'

export default {
  components: {
    ElMain,
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
        id: null,
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      device_list: null,
      device_total: null,
      device_listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        type: '',
        sort: '+id'
      },
      bq_list: null,
      bq_total: null,
      radio: '',
      deviceVisible: false,
      dialogListVisible: false,
      matSelect: '',
      searchname: '',
      bedname: '',
      devicename: '',
      bq_id: '',
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      token: getToken,
      dialogStatus: 'create',
      bed: {
        id: null,
        name: '',
        device: {
          id: null,
          name: '',
          model: '',
          sn: ''
        },
        flag: '',
        state: '',
        area_id: '',
        device_id: ''
      },
      params: {
        page: 1,
        name: '',
        type: 0
      }
    }
  },
  methods: {
    getBeds(data) {
      beds(data).then(response => {
        this.list = response.data.results
        this.total = response.data.count
      })
    },
    getDiseaseArea(data) {
      diseaseArea(data).then(response => {
        this.bq_list = response.data.results
        this.bq_total = response.data.count
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
    getCurrentRow(row) {
      this.bed.device.id = row.id
      this.bed.device.name = row.name
      this.bed.device.model = row.model
      this.bed.device.sn = row.sn
    },
    device_rowClick(row) {
      this.radio = row.id
      this.getCurrentRow(row)
    },
    rowClick(row, event, column) {
      this.listQuery.id = row.id
      this.bq_id = row.id
      this.getBeds(this.listQuery)
    },
    resetBed() {
      this.bed = {
        id: null,
        name: '',
        device: {
          id: null,
          name: '',
          model: '',
          sn: ''
        },
        flag: '',
        state: '',
        area_id: '',
        device_id: ''
      }
    },
    handleCreate() {
      if (this.bq_id === '') {
        this.$notify({
          title: '提示',
          message: '请选择病区',
          type: 'success',
          duration: 2000
        })
      } else {
        this.resetBed()
        this.dialogListVisible = true
        this.dialogStatus = 'create'
        this.getDeviceList(this.device_listQuery) // 查设备列表
        this.$nextTick(() => {
          this.$refs['addForm'].clearValidate()
        })
      }
    },
    createData() {
      const tempData = Object.assign({}, this.bed)
      tempData.area_id = this.bq_id
      tempData.device_id = tempData.device.id
      if (tempData.device.sn === '') {
        this.$notify({
          title: '提示',
          message: '请选择设备',
          type: 'success',
          duration: 2000
        })
        return
      }
      createBed(tempData).then(() => {
        this.dialogListVisible = false
        this.$notify({
          title: '成功',
          message: '新建成功',
          type: 'success',
          duration: 2000
        })
        this.listQuery.page = 1
        this.getBeds(this.listQuery)
      })
    },
    handleUpdate(row) {
      this.resetBed()
      this.bed = Object.assign({}, row)
      this.dialogListVisible = true
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['addForm'].clearValidate()
      })
    },
    updateData() {
      const tempData = Object.assign({}, this.bed)
      tempData.area_id = this.bq_id
      tempData.device_id = tempData.device.id
      if (tempData.device.sn === '') {
        this.$notify({
          title: '提示',
          message: '请选择设备',
          type: 'success',
          duration: 2000
        })
        return
      }
      updateBed(tempData).then(() => {
        this.dialogListVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
        this.listQuery.page = 1
        this.getBeds(this.listQuery)
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.bed = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.bed)
        deleteBed(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getBeds(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.params.page = 1
      this.params.name = this.searchname
      this.getDiseaseArea(this.params)
    },
    bed_handleFilter() {
      this.listQuery.page = 1
      this.listQuery.id = this.bq_id
      this.listQuery.name = this.bedname
      this.getBeds(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getBeds(this.listQuery)
    },
    device_handleFilter() {
      this.device_listQuery.limit = 5
      this.device_listQuery.offset = 0
      this.device_listQuery.name = this.devicename
      this.device_listQuery.type = this.matSelect
      this.getDeviceList(this.device_listQuery)
    },
    device_handleCurrentChange(val) {
      this.device_listQuery.page = val
      this.device_listQuery.offset = (val - 1) * this.device_listQuery.limit
      this.getDeviceList(this.device_listQuery)
    },
    dateFormat(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getDiseaseArea(this.params)
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
