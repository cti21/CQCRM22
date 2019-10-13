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
                  placeholder="请输入套餐名称">
                </el-input>
                <el-table
                  :data="tc_list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  highlight-current-row
                  @row-click="rowClick">
                  <el-table-column prop="name" label="套餐名称">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false">
                  </el-table-column>
                </el-table>
              </div>
          </el-aside>
          <el-container>
            <el-main style="padding-top: 0px">
              <!--<div style="width: 100%">-->
                <el-row>
                      <el-button
                        size="small"
                        type="primary"
                        style="margin-right: 50px;float:right;margin-left: 20px"
                        icon="iconfont iconparent-line"
                        @click="subOrder">子医嘱
                      </el-button>
                      <el-button
                        size="small"
                        style="margin-left: 20px;float:right"
                        icon="iconfont iconyonghu6"
                        @click="handleSubCreate"
                        type="primary">新增子项
                      </el-button>
                      <el-button
                        size="small"
                        style="margin-left: 20px;float:right"
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
                    @selection-change="orderSelectChange"
                    @row-click="detailRowClick"
                  >
                    <el-table-column type="selection" width="80" class="selection" align="center">
                    </el-table-column>
                    <el-table-column prop="yztype" label="类型"  width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="医嘱" width="140">
                    </el-table-column>
                    <el-table-column prop="gg" label="规格" width="80" align="center">
                    </el-table-column>
                    <el-table-column prop="path" label="给药途径" width="80" align="center">
                    </el-table-column>
                    <el-table-column prop="week" label="频次" width="80" align="center">
                    </el-table-column>
                    <el-table-column prop="count" label="单次剂量" width="80" align="center">
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
              <!--</div>-->
            </el-main>
          </el-container>
        </el-container>

        <div>
          <el-dialog  title="血透套餐" width="60%" :visible.sync="dialogListVisible">
            <div style="margin-left: 10px;">
              <label style="margin-right: 40px;">医嘱类型</label>
              <el-radio-group v-model="hctype" @change="selectChange">
                  <el-radio label="药品">药品</el-radio>
                  <el-radio label="护理">护理</el-radio>
                  <el-radio label="处置">处置</el-radio>
                  <el-radio label="耗材">耗材</el-radio>
              </el-radio-group>
              <el-input
                v-model="hcname"
                style="float: right;width: 240px;margin-left: 50px;padding-bottom: 5px;margin-right: 30px;"
                class="myInput" placeholder="请输入名称"
                suffix-icon="el-icon-search"
                @keyup.enter.native="material_handleFilter"
              >
              </el-input>
            </div>

            <div style="margin-left: 10px;">
              <el-table :data="material_list" highlight-current-row  @row-dblclick="rowdbclick" stripe>
                <el-table-column type="index" label="序号"  width="80">
                </el-table-column>
                <el-table-column prop="id" v-if="false">
                </el-table-column>
                <el-table-column prop="name" label="名称" width="200">
                </el-table-column>
                <el-table-column prop="gg" label="规格" align="center"  width="120">
                </el-table-column>
                <el-table-column prop="dw" label="剂量单位" align="center" width="120">
                </el-table-column>
                <el-table-column prop="pack_gg" label="包装规格" width="120">
                </el-table-column>
                <el-table-column prop="firm" label="厂商" width="200">
                </el-table-column>
              </el-table>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination background
                     @current-change="material_handleCurrentChange"
                     :current-page="material_listQuery.page"
                     :page-size="material_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="material_total">
                </el-pagination>
            </div>
            <div style="margin-left: 10px;">
               <div style="margin-top: 10px">套餐详情</div>
               <div>
                 <el-table :data="multipleSelection" stripe="">
                    <el-table-column type="index" label="序号"  width="50">
                    </el-table-column>
                    <el-table-column prop="id" v-if="false">
                    </el-table-column>
                    <el-table-column prop="name" label="名称" width="160">
                    </el-table-column>
                    <el-table-column prop="dw" label="剂量单位" width="90" align="center">
                    </el-table-column>
                    <el-table-column prop="week" label="频次" width="95" align="center">
                      <template slot-scope="scope">
                          <el-select v-model="scope.row.week" clearable style="width: 75px" class="myInput">
                            <el-option label="QW" value="QW" >
                            </el-option>
                            <el-option label="QD" value="QD" >
                            </el-option>
                            <el-option label="QH" value="QH" >
                            </el-option>
                            <el-option label="ST" value="ST" >
                            </el-option>
                          </el-select>
                      </template>
                    </el-table-column>
                    <el-table-column prop="path" label="用药途径" width="130" align="center">
                      <template slot-scope="scope">
                          <el-select v-model="scope.row.path" clearable style="width: 110px" class="myInput">
                            <el-option label="静脉注射" value="静脉注射" >
                            </el-option>
                            <el-option label="静脉滴注" value="静脉滴注" >
                            </el-option>
                            <el-option label="肌肉注射" value="肌肉注射" >
                            </el-option>
                            <el-option label="皮下注射" value="皮下注射" >
                            </el-option>
                            <el-option label="局部溶栓" value="局部溶栓" >
                            </el-option>
                            <el-option label="口服" value="口服" >
                            </el-option>
                            <el-option label="舌下含服" value="舌下含服" >
                            </el-option>
                          </el-select>
                      </template>
                    </el-table-column>
                    <el-table-column prop="count" label="单次剂量" width="130" align="center">
                      <template slot-scope="scope">
                          <el-input v-model="scope.row.count" type="number" size="small" placeholder="单次剂量">
                          </el-input>
                      </template>
                    </el-table-column>
                    <el-table-column label="操作" fixed="right" align="center">
                      <template slot-scope="scope">
                        <el-button type="text" size="small" @click="dict_handleDelete(scope.row)">删除</el-button>
                      </template>
                    </el-table-column>
                  </el-table>
               </div>
            </div>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button
                size="small"
                type="primary"
                style="height:33px;padding-top: 8px"
                icon="el-icon-check"
                @click="submitData">提交
              </el-button>
              <el-button
                size="small"
                style="height:33px;padding-top: 8px"
                icon="el-icon-close"
                @click="dialogListVisible = false"
              >关闭
              </el-button>
            </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="套餐编辑" width="55%" :visible.sync="editFormVisible">
                  <el-form  :model="material" ref="editForm"   label-position="left" label-width="70px" style='width:90%; margin-left:40px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="套餐名称"  prop="tcname">
                              <el-input v-model="material.tcname"  style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="医嘱名称"  prop="name">
                              <el-input v-model="material.name"  style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                      <el-row>
                         <el-col  :span="12">
                            <el-form-item label="类型" prop="yztype">
                              <el-input v-model="material.yztype" style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col  :span="12">
                            <el-form-item label="规格" prop="gg">
                              <el-input v-model="material.gg"  style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                      </el-row>
                      <el-row>
                         <el-col  :span="12">
                            <el-form-item label="频次" prop="week">
                              <el-select v-model="material.week" clearable style="width: 140px" class="myInput">
                                <el-option label="QW" value="QW" >
                                </el-option>
                                <el-option label="QD" value="QD" >
                                </el-option>
                                <el-option label="QH" value="QH" >
                                </el-option>
                                <el-option label="ST" value="ST" >
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                          <el-col  :span="12">
                            <el-form-item label="用药途径" prop="path">
                              <el-select v-model="material.path" clearable style="width: 140px" class="myInput">
                                <el-option label="静脉注射" value="静脉注射" >
                                </el-option>
                                <el-option label="静脉滴注" value="静脉滴注" >
                                </el-option>
                                <el-option label="肌肉注射" value="肌肉注射" >
                                </el-option>
                                <el-option label="皮下注射" value="皮下注射" >
                                </el-option>
                                <el-option label="局部溶栓" value="局部溶栓" >
                                </el-option>
                                <el-option label="口服" value="口服" >
                                </el-option>
                                <el-option label="舌下含服" value="舌下含服" >
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                      </el-row>
                      <el-row>
                         <el-col  :span="12">
                            <el-form-item label="剂量单位" prop="dw">
                              <el-input v-model="material.dw"  style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col  :span="12">
                            <el-form-item label="单次剂量" prop="count">
                              <el-input-number v-model="material.count"  style="width: 200px;" class="myInput"></el-input-number>
                            </el-form-item>
                          </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="editFormVisible = false"
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


    </div>
</template>

<script>
import { xyjh_search, xyjhs, createxyjh, updatexyjh, deletexyjh } from '@/api/system'
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
        limit: 10,
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
        type: 0,
        sort: '+id'
      },
      tc_list: null,
      tc_total: null,
      multipleOrder: [],
      dialogListVisible: false,
      matSelect: '',
      searchname: '',
      hctype: '药品',
      hcname: '',
      feetype: '收费',
      tc_id: '',
      parentid: '',
      action: 0,
      ordertype: '',
      multipleSelection: [],
      token: getToken,
      dialogFormVisible: false,
      editFormVisible: false,
      dialogStatus: '',
      materialSelect: [
        { id: '1', name: '降压静脉' },
        { id: '2', name: '抗凝' },
        { id: '3', name: '浓钠' },
        { id: '4', name: '降压长效' }
      ],
      material: {
        id: null,
        name: '',
        yztype: '',
        gg: '',
        dw: '',
        kind: '',
        orderid: '',
        count: 0,
        feetype: '',
        leixing: '',
        tcid: '',
        parentid: '',
        path: '',
        week: '',
        tcname: '',
        patientid: '',
        aciton: 0
      },
      multipleList: [],
      queryparams: {
        page: 1,
        id: null,
        name: ''
      },
      params: {
        page: 1,
        name: '',
        type: 0
      }
    }
  },
  methods: {
    getXyjhs(data) {
      xyjhs(data).then(response => {
        this.list = response.data.results
        this.total = response.data.count
      })
    },
    getTcDict(data) {
      xyjh_search(data).then(response => {
        this.tc_list = response.data.results
        this.tc_total = response.data.count
      })
    },
    getHuliList(data) {
      huliDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getChuzhiList(data) {
      chuzhiDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getMaterialList(data) {
      mymaterialDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getDrugList(data) {
      mydrugDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    rowClick(row, event, column) {
      this.parentid = -1
      this.queryparams.id = row.id
      this.tc_id = row.id
      this.getXyjhs(this.queryparams)
    },
    detailRowClick(row, event, column) {
      this.parentid = row.id
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    dict_handleDelete(row) {
      this.multipleSelection.splice(this.multipleSelection.findIndex(v => v.id === row.id), 1)
    },
    handleReset() {
      this.params.page = 1
      this.params.name = ''
      this.searchname = ''
      this.tc_id = ''
      this.parentid = -1
      this.getTcDict(this.params)
    },
    orderSelectChange: function(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    selectChange(val) {
      this.material_list = []
      this.material_total = null
      this.material_listQuery.page = 1
      this.material_listQuery.name = ''
      this.hcname = ''
      this.ordertype = val
      switch (val) {
        case '耗材':
          this.getMaterialList(this.material_listQuery)
          break
        case '药品':
          this.feetype = '收费'
          this.material_listQuery.type = 0
          this.getDrugList(this.material_listQuery)
          break
        case '处置':
          this.getChuzhiList(this.material_listQuery)
          break
        case '护理':
          this.getHuliList(this.material_listQuery)
          break
      }
    },
    rowdbclick(row,event) {
      this.multipleSelection = []
      this.multipleSelection.push(row)
    },
    handleCreate() {
      this.multipleSelection = []
      this.parentid = -1
      if (this.tc_id === '') {
        this.$notify({
          title: '提示',
          message: '请选择套餐',
          type: 'success',
          duration: 2000
        })
      } else {
        this.action = 0 // 向套餐添加医嘱
        this.feetype = '收费'
        this.material_listQuery.type = 0
        this.getDrugList(this.material_listQuery)
        this.dialogListVisible = true
      }
    },
    handleSubCreate() {
      this.multipleSelection = []
      if (this.multipleOrder.length < 1) {
        this.$notify({
          title: '提示',
          message: '请选择项目',
          type: 'success',
          duration: 2000
        })
      } else if (this.multipleOrder.length > 1) {
        this.$notify({
          title: '提示',
          message: '请选择一条记录',
          type: 'success',
          duration: 2000
        })
      } else {
        this.action = 2 // 向套餐里的医嘱添加子项目
        this.feetype = '收费'
        this.material_listQuery.type = 0
        this.getDrugList(this.material_listQuery)
        this.dialogListVisible = true
      }
    },
    subOrder() {
      if (this.multipleOrder.length < 1) {
        this.$notify({
          title: '提示',
          message: '请选择项目',
          type: 'success',
          duration: 2000
        })
      } else if (this.multipleOrder.length > 1) {
        this.$notify({
          title: '提示',
          message: '请选择一条记录',
          type: 'success',
          duration: 2000
        })
      } else {
        this.multipleSelection = []
        this.action = 1 // 向套餐里的医嘱添加子医嘱
        this.feetype = '收费'
        this.material_listQuery.type = 0
        this.getDrugList(this.material_listQuery)
        this.dialogListVisible = true
      }
    },
    submitData() {
      if (this.multipleSelection.length > 0) {
        const obj = this.multipleSelection[0]
        if (!obj.count) {
          this.$notify({
            title: '提示',
            message: '单次剂量不能为空',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (!Number.isInteger(Number(obj.count))) {
          this.$notify({
            title: '提示',
            message: '单次剂量必须为数值',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (this.ordertype === '药品') {
          if (!obj.week) {
            this.$notify({
              title: '提示',
              message: '频次不能为空',
              type: 'success',
              duration: 2000
            })
            return
          }
          if (!obj.path) {
            this.$notify({
              title: '提示',
              message: '用药路径不能为空',
              type: 'success',
              duration: 2000
            })
            return
          }
        }
        this.multipleList = []
        this.multipleSelection.forEach((item) => {
          this.material = Object.assign({}, item)
          this.material.orderid = item.id
          this.material.leixing = item.kind
          if (this.material.kind !== 3) {
            this.material.path = 'a'
            this.material.week = 'a'
            this.material.feetype = 'a'
          } else {
            this.material.feetype = this.feetype
          }
          this.material.tcid = this.tc_id
          this.material.parentid = this.parentid
          this.material.patientid = 'A000'
          this.material.action = this.action
          this.multipleList.push(this.material)
          console.log('this.multipleList')
          console.log(this.multipleList)
        })
        createxyjh(this.multipleList).then(() => {
          this.$notify({
            title: '成功',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogListVisible = false
          this.queryparams.page = 1
          this.getXyjhs(this.queryparams)
        })
      }
    },
    handleUpdate(row) {
      this.material = Object.assign({}, row) // copy obj
      console.log(this.material)
      this.editFormVisible = true
      this.$nextTick(() => {
        this.$refs['editForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['editForm'].validate((valid) => {
        if (valid) {
          if (this.material.yztype !== '药品') {
            this.material.week = 'a'
            this.material.path = 'a'
          }
          this.material.orderid = 1
          this.material.leixing = 1
          this.material.tcid = 1
          this.material.tcid = this.tc_id
          this.material.parentid = this.parentid
          this.material.action = this.action
          const tempData = Object.assign({}, this.material)
          updatexyjh(tempData).then(() => {
            this.editFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getXyjhs(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.material = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.material)
        deletexyjh(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getXyjhs(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.params.page = 1
      this.params.name = this.searchname
      this.parentid = -1
      this.getTcDict(this.params)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getXyjhs(this.queryparams)
    },
    material_handleFilter() {
      this.material_listQuery.page = 1
      this.material_listQuery.name = this.hcname
      switch (this.hctype) {
        case '耗材':
          this.getMaterialList(this.material_listQuery)
          break
        case '药品':
          this.feetype = '收费'
          this.material_listQuery.type = 0
          this.getDrugList(this.material_listQuery)
          break
        case '处置':
          this.getChuzhiList(this.material_listQuery)
          break
        case '护理':
          this.getHuliList(this.material_listQuery)
          break
      }
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      switch (this.hctype) {
        case '耗材':
          this.getMaterialList(this.material_listQuery)
          break
        case '药品':
          this.feetype = '收费'
          this.material_listQuery.type = 0
          this.getDrugList(this.material_listQuery)
          break
        case '处置':
          this.getChuzhiList(this.material_listQuery)
          break
        case '护理':
          this.getHuliList(this.material_listQuery)
          break
      }
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
    // this.getXyjhs(this.queryparams)
    this.getTcDict(this.params)
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
