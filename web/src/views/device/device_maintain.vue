<template>
    <div>
        <div class="filter-container">
              <el-date-picker
                v-model="fromdate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd" placeholder="保养日期开始">
              </el-date-picker>
              <el-date-picker
                v-model="todate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="保养日期结束">
              </el-date-picker>
              <el-input
                v-model="searchname"
                class="myInput"
                style="width: 180px;margin-right: 10px;"
                @keyup.enter.native="handleFilter"
                placeholder="设备名称">
              </el-input>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>

        <!--设备保养列表-->
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading"
            @row-click="rowClick">
            <el-table-column type="index" label="序号"  width="50">
            </el-table-column>
            <el-table-column prop="device.name" label="设备名称" width="200" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="device.sn" label="序列号"  width="120" align="center">
            </el-table-column>
            <el-table-column prop="device.model" label="型号" width="100" align="center">
            </el-table-column>
            <el-table-column prop="date" label="保养日期" :formatter="dateFormat" width="100" align="center">
            </el-table-column>
            <el-table-column prop="operator" label="保养人" width="100" align="center">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleDetailCreate(scope.row,0)">新增透析保养明细</el-button>
                  <el-button type="text" size="small" @click="handleDetailCreate(scope.row,1)">新增水处理保养明细</el-button>
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>

          <el-row>
            <div class="pagination-container" style="float:right;margin-top: 5px">
              <el-pagination background
                   @size-change="handleSizeChange"
                   @current-change="handleCurrentChange"
                   :current-page="listQuery.page"
                   :page-sizes="[5,10,20,30, 50]"
                   :page-size="listQuery.limit"
                   layout="total, prev, pager, next"
                   :total="total">
              </el-pagination>
            </div>
            <!--设备保养明细列表-->
            <div style="float: left;margin-top: 10px">保养明细</div>
          </el-row>

          <el-table
            :data="detail_list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="detail_listLoading">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="maintainence.name" label="保养类型" width="180" align="center">
            </el-table-column>
            <el-table-column prop="material.name" label="耗材名称"  width="200" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="amount" label="耗材数量" width="160" align="center">
            </el-table-column>
            <el-table-column prop="comment" label="备注"  width="140" show-overflow-tooltip align="center">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleDetailUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDetailDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <!--设备保养新增-->
        <div>
          <el-dialog  title="设备保养新增" width="55%" :visible.sync="dialogAddVisible">
            <div style="float: left">
              <el-input
                v-model="devicename"
                style="width: 180px"
                @keyup.enter.native="device_handleFilter"
                class="myInput"
                placeholder="设备名称">
              </el-input>
              <el-select v-model="deviceSelect" clearable style="width: 180px" class="myInput" placeholder="设备类型">
                <el-option label="透析设备" value="透析设备" >
                </el-option>
                <el-option label="水处理设备" value="水处理设备" >
                </el-option>
              </el-select>
              <el-button type="primary" size="small" style="margin-left: 20px;" icon="el-icon-search" @click="device_handleFilter">查询</el-button>
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
              ref="devTable"
              :data="device_list"
              v-loading="listLoading"
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              @row-click="rowDeviceClick"
            >
              <el-table-column label="选中" width="60px" align="center">
                  <template slot-scope="scope">
                    <el-radio class="radio" v-model="radio" :label="scope.row.id" @change.native="getCurrentRow(scope.row)">&nbsp</el-radio>
                  </template>
              </el-table-column>
              <el-table-column prop="id"  v-if="false" width="120" align="center">
              </el-table-column>
              <el-table-column prop="name" label="设备名称" width="100"  show-overflow-tooltip align="center">
              </el-table-column>
              <el-table-column prop="sn" label="序列号"  width="120" align="center">
              </el-table-column>
              <el-table-column prop="model" label="型号" width="100" align="center">
              </el-table-column>
              <el-table-column prop="buydate" label="购买日期" :formatter="dateFormat" width="100" align="center">
              </el-table-column>
              <el-table-column prop="price" label="价格" width="80" align="center">
              </el-table-column>
              <el-table-column prop="commany" label="厂家" width="120" show-overflow-tooltip align="center">
              </el-table-column>
            </el-table>
            <div>
                <div style="margin-top: 20px">
                  <el-row style="margin-bottom: 10px">
                    <el-col>
                      <label style="margin-left: 10px">保养时间：</label>
                      <el-date-picker
                        v-model="dmobj.date"
                        class="myInput"
                        value-format="yyyy-MM-dd HH:mm:ss"
                        style="width: 30%">
                      </el-date-picker>
                    </el-col>
                    </el-row>
                    <el-row style="padding-top: 10px">
                      <el-col>
                        <label style="margin-left: 10px;padding-top: 5px;">保养备注：</label>
                        <el-input type="textarea" v-model="dmobj.comment" style="width: 80%" :rows="2">
                        </el-input>
                      </el-col>
                    </el-row>
                    <el-row style="margin-top: 20px;margin-bottom: 15px">
                      <el-col>
                        <el-button
                          size="small"
                          type="primary"
                          icon="el-icon-check"
                          style="float:right;margin-right: 20px;"
                          @click="createData">保存</el-button>
                        <el-button
                          size="small"
                          icon="el-icon-close"
                          style="float: right;margin-right: 10px;"
                          @click="dialogAddVisible = false">关闭</el-button>
                      </el-col>
                    </el-row>
                </div>
            </div>
          </el-dialog>
        </div>

        <!--设备保养修改-->
        <div>
          <el-dialog  title="设备保养" width="55%" :visible.sync="dialogEditVisible">
                  <el-form  :model="dmobj" ref="dataForm" label-position="left" label-width="70px" style='width:90%; margin-left:40px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="设备名称" prop="name">
                              <el-input v-model="dmobj.device.name" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="型号"  prop="model">
                              <el-input v-model="dmobj.device.model" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                      <el-row>
                          <el-col :span="12">
                            <el-form-item label="序列号" prop="sn">
                              <el-input v-model="dmobj.device.sn" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="保养时间" prop="date">
                              <el-date-picker v-model="dmobj.date" class="myInput" style="width: 140px">
                              </el-date-picker>
                            </el-form-item>
                          </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="备注" prop="comment">
                              <el-input type="textarea" v-model="dmobj.comment" style="width: 460px" :rows="2">
                              </el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button size="small" @click="dialogEditVisible = false">取消</el-button>
                  <el-button size="small" type="primary" @click="updateData">保存</el-button>
                </div>
          </el-dialog>
        </div>

        <!--设备保养明细新增-->
        <div>
          <el-dialog  title="新增保养明细" width="55%" :visible.sync="dialogDetailAddVisible">
                  <el-form  :model="dmdobj" ref="detailForm" label-position="left"  style='width:90%; margin-left:40px;'>
                       <el-row>
                          <el-col :span="12">
                            <el-form-item label="保养类型"  prop="name">
                              <el-select v-model="dmdobj.maintainence.name" clearable style="width: 160px" class="myInput" placeholder="保养类型">
                                <el-option v-for="item in maintainence_list" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                          <div style="float: left">
                            <label style="margin-right: 20px">耗材名称</label>
                            <el-input
                              v-model="materialname"
                              @keyup.enter.native="material_handleFilter"
                              suffix-icon="el-icon-search"
                              style="width: 180px"
                              class="myInput"
                              size="small">
                            </el-input>
                          </div>
                          <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                              <el-pagination background
                                   @size-change="material_handleSizeChange"
                                   @current-change="material_handleCurrentChange"
                                   :current-page="material_listQuery.page"
                                   :page-sizes="[5,10,20,30, 50]"
                                   :page-size="material_listQuery.limit"
                                   layout="prev, pager, next"
                                   :total="material_total">
                              </el-pagination>
                          </div>
                          <el-table
                            ref="materialTable"
                            :data="material_list"
                            :header-cell-style="{background:'#F8F8F8'}"
                            stripe
                            @row-click="rowMaterialClick"
                          >
                            <el-table-column width="60px" align="center">
                                <template slot-scope="scope">
                                  <el-radio class="radio" v-model="radio1" :label="scope.row.id" @change.native="getDetailCurrentRow(scope.row)">&nbsp</el-radio>
                                  <!--<el-radio class="radio" v-model="radio1" :label="scope.$index" @change.native="getDetailCurrentRow(scope.row)">&nbsp</el-radio>-->
                                </template>
                            </el-table-column>
                            <el-table-column prop="id"  v-if="false" width="120" align="center">
                            </el-table-column>
                            <el-table-column prop="name" label="耗材名称" width="160" show-overflow-tooltip>
                            </el-table-column>
                            <el-table-column prop="gg" label="规格" width="90" align="center">
                            </el-table-column>
                            <el-table-column prop="jiage" label="价格" width="90" align="center">
                            </el-table-column>
                            <el-table-column prop="kucun" label="库存"  width="90" align="center">
                            </el-table-column>
                            <el-table-column prop="firm" label="厂商" width="200" show-overflow-tooltip>
                            </el-table-column>
                          </el-table>
                       </el-row>
                       <el-row style="margin-top: 10px;">
                         <el-col>
                           <el-form-item label="耗材数量" prop="amount">
                             <el-input-number v-model="dmdobj.amount" style="width: 90px" size="small" :min="1" placeholder="数量">
                             </el-input-number>
                           </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="备注" prop="comment">
                              <el-input type="textarea" v-model="dmdobj.comment" style="width: 460px" :rows="2">
                              </el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button size="small" icon="el-icon-close" @click="dialogDetailAddVisible = false">关闭</el-button>
                  <el-button size="small" icon="el-icon-check" type="primary" @click="createDetailData">保存</el-button>
                </div>
          </el-dialog>
        </div>

        <!--设备保养明细修改-->
        <div>
          <el-dialog  title="修改保养明细" width="55%" :visible.sync="dialogDetailEditVisible">
                  <el-form  :model="dmdobj" ref="dmdForm" label-position="left" label-width="70px" style='width:90%; margin-left:40px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="保养类型" prop="name">
                              <el-select v-model="dmdobj.maintainence.name" clearable style="width: 160px" class="filter-item" placeholder="保养类型">
                                <el-option v-for="item in maintainence_list" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="耗材名称"  prop="name">
                              <el-input v-model="dmdobj.material.name" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                      <el-row>
                          <el-col :span="12">
                            <el-form-item label="耗材代码" prop="code">
                              <el-input v-model="dmdobj.material.code" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="耗材数量" prop="amount">
                              <el-input-number v-model="dmdobj.amount" style="width: 90px" size="small" :min="1" placeholder="数量">
                             </el-input-number>
                            </el-form-item>
                          </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="备注" prop="comment">
                              <el-input type="textarea" v-model="dmdobj.comment" style="width: 460px" :rows="4">
                              </el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button icon="el-icon-close" @click="dialogDetailEditVisible = false">关闭</el-button>
                  <el-button icon="el-icon-check" type="primary" @click="updateDetailData">保存</el-button>
                </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { devices, maintainences, device_maintainences, createdevice_maintainence,
  updatedevice_maintainence, deletedevice_maintainence,
  device_maintainence_details, createdevice_maintainence_detail,
  updatedevice_maintainence_detail, deletedevice_maintainence_detail} from '@/api/device'
import { mymaterialDict } from '@/api/login'
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
import ElButton from '../../../node_modules/element-ui/packages/button/src/button';

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
      dialogAddVisible: false,
      dialogEditVisible: false,
      dialogDetailAddVisible: false,
      dialogDetailEditVisible: false,
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
      detail_list: null,
      detail_total: null,
      detail_listLoading: false,
      detail_listQuery: {
        page: 1,
        limit: 5,
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
        type: '',
        sort: '+id'
      },
      maintainence_list: null,
      maintainence_total: null,
      fromdate: '',
      todate: '',
      deviceSelect: '',
      devicename: '',
      materialname: '',
      searchname: '',
      token: getToken,
      dialogStatus: '',
      stockinNo: '',
      maintainencetype: 0,
      radio: '',
      radio1: '',
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
      dmobj: {
        id: null,
        device: {
          id: null,
          name: '',
          sn: '',
          model: ''
        },
        date: '',
        comment: ''
      },
      dmdobj: {
        id: null,
        maintainence: {
          id: null,
          name: '',
          type: ''
        },
        material: {
          id: null,
          name: '',
          code: '',
          type: '',
          factory: ''
        },
        amount: 0,
        comment: '',
        dm: ''
      },
      queryparams: {
        page: 1,
        name: '',
        fromdate: '',
        todate: ''
      }
    }
  },
  methods: {
    getDeviceMaintainenceList(data) {
      device_maintainences(data).then(response => {
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
    getMaterialList(data) {
      mymaterialDict(data).then(response => {
        this.material_list = response.data.results
        this.material_total = response.data.count
        console.log(this.material_list)
      })
    },
    getDmdList(data) {
      device_maintainence_details(data).then(response => {
        this.detail_listLoading = true
        this.detail_list = response.data.results
        this.detail_total = response.data.count
        this.detail_listLoading = false
      })
    },
    getMaintainenceList(data) {
      maintainences(data).then(response => {
        this.maintainence_list = response.data.results
        this.maintainence_total = response.data.count
      })
    },
    resetDeviceMaintainence() {
      this.dmobj = {
        id: null,
        device: {
          id: null,
          name: '',
          sn: '',
          model: ''
        },
        date: '',
        comment: ''
      }
    },
    resetDeviceMaintainenceDetail() {
      this.dmdobj = {
        id: null,
        maintainence: {
          id: null,
          name: '',
          type: 0
        },
        material: {
          id: null,
          name: '',
          code: '',
          type: 0,
          factory: ''
        },
        amount: 0,
        comment: '',
        dm: ''
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
      this.getDeviceMaintainenceList(this.queryparams)
    },
    getCurrentRow(row) {
      this.dmobj.device.id = row.id
      this.dmobj.device.name = row.name
      this.dmobj.device.model = row.model
      this.dmobj.device.sn = row.sn
    },
    getDetailCurrentRow(row) {
      this.dmdobj.material.id = row.id
      console.log(this.dmdobj)
    },
    handleCreate() {
      this.resetDeviceMaintainence()
      this.dialogAddVisible = true
      this.getDeviceList(this.device_listQuery) // 查设备列表
    },
    createData() {
      this.dmobj.id = parseInt(Math.random() * 100) + 1024 // mock a id
      createdevice_maintainence(this.dmobj).then(() => {
        this.dialogAddVisible = false
        this.$notify({
          title: '成功',
          message: '创建成功',
          type: 'success',
          duration: 2000
        })
        this.queryparams.page = 1
        this.getDeviceMaintainenceList(this.queryparams)
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.dmobj = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.dmobj)
        deletedevice_maintainence(tempData).then(() => {
          this.$notify({
            title: '提示',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getDeviceMaintainenceList(this.queryparams)
        })
      })
    },
    handleDetailCreate(row,flag) {
      this.resetDeviceMaintainenceDetail()
      this.dmdobj.dm = row.id
      this.dmdobj.maintainence.type = flag
      this.dialogDetailAddVisible = true
      this.getMaintainenceList(flag)
      this.getMaterialList(this.material_listQuery)
    },
    createDetailData() {
      createdevice_maintainence_detail(this.dmdobj).then(() => {
        this.dialogDetailAddVisible = false
        this.$notify({
          title: '成功',
          message: '创建成功',
          type: 'success',
          duration: 2000
        })
        this.getDmdList(this.dmobj.id)
      })
    },
    handleUpdate(row) {
      this.dmobj = Object.assign({}, row) // copy obj
      this.dialogEditVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.dmobj)
          updatedevice_maintainence(tempData).then(() => {
            this.dialogEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getDeviceMaintainenceList(this.queryparams)
          })
        }
      })
    },
    handleDetailUpdate(row) {
      this.dmdobj = Object.assign({}, row) // copy obj
      this.dialogDetailEditVisible = true
      this.$nextTick(() => {
        this.$refs['dmdForm'].clearValidate()
      })
    },
    updateDetailData() {
      this.$refs['dmdForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.dmdobj)
          console.log(tempData)
          updatedevice_maintainence_detail(tempData).then(() => {
            this.dialogDetailEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getDmdList(this.dmobj.id)
          })
        }
      })
    },
    handleDetailDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.dmdobj = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.dmdobj)
        deletedevice_maintainence_detail(tempData).then(() => {
          this.$notify({
            title: '提示',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.getDmdList(this.dmobj.id)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.queryparams.fromdate = this.fromdate
      this.queryparams.todate = this.todate
      this.getDeviceMaintainenceList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getDeviceMaintainenceList(0)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getDeviceMaintainenceList(this.queryparams)
    },
    device_handleSizeChange(val) {
      this.device_listQuery.limit = val
      this.getDeviceList(this.device_listQuery)
    },
    device_handleFilter() {
      this.device_listQuery.page = 1
      this.device_listQuery.name = this.devicename
      this.device_listQuery.type = this.deviceSelect
      this.getDeviceList(this.device_listQuery)
    },
    device_handleCurrentChange(val) {
      this.device_listQuery.page = val
      this.device_listQuery.offset = (val - 1) * this.device_listQuery.limit
      this.getDeviceList(this.device_listQuery)
    },
    material_handleFilter() {
      this.material_listQuery.page = 1
      this.material_listQuery.name = this.materialname
      this.getMaterialList(this.material_listQuery)
    },
    material_handleSizeChange(val) {
      this.material_listQuery.limit = val
      this.getMaterialList(this.material_listQuery)
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      this.getMaterialList(this.material_listQuery)
    },
    rowClick(row, event, column) {
      this.getDmdList(row.id)
    },
    rowDeviceClick(row) {
      this.radio = row.id
      this.dmobj.device.id = row.id
      this.dmobj.device.name = row.name
      this.dmobj.device.model = row.model
      this.dmobj.device.sn = row.sn
    },
    rowMaterialClick(row) {
      this.radio1 = row.id
      this.dmdobj.material.id = row.id
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
    this.getDeviceMaintainenceList(this.queryparams)
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
