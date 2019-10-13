<template>
    <div>
        <el-row>
          <el-card style="margin-left: 15px;margin-right: 10px">
            <el-row>
                <el-col :span="6">
                  <label class="el-form-item__label">客户姓名</label>
                  <el-input
                    v-model="listQuery.clientname"
                    class="myInput"
                    style="width: 180px;margin-right: 20px"
                    clearable
                    placeholder="请输入姓名">
                  </el-input>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">手机</label>
                  <el-input
                    v-model="listQuery.phone"
                    class="myInput"
                    style="width: 180px;margin-right: 20px"
                    clearable
                    @keyup.enter.native="handleFilter"
                    placeholder="手机">
                  </el-input>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">治疗日期从</label>
                  <el-date-picker
                    v-model="listQuery.begindate"
                    style="width:50%;margin-left: 20px"
                    class="myInput"
                    type="date"
                    placeholder="治疗日期开始"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
                <el-col :span="1">
                  <label class="el-form-item__label">到</label>
                </el-col>
                <el-col :span="5">
                  <el-date-picker
                    v-model="listQuery.enddate"
                    style="width:60%"
                    class="myInput"
                    type="date"
                    placeholder="治疗日期结束"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>

            </el-row>
            <el-row>
                <el-col :span="6">
                  <label class="el-form-item__label">治疗项目</label>
                  <el-select v-model="listQuery.project" clearable style="width:40%" class="myInput">
                    <el-option v-for="item in projectSelect" :key="item.id" :value="item.id" :label="item.name">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">已缴费收单</label>
                  <el-select v-model="listQuery.shoudan" clearable style="width:40%" class="myInput">
                    <el-option v-for="item in marketSelect" :key="item.id" :value="item.id" :label="item.name">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="4">
                  <el-checkbox v-model="listQuery.treated">已完成治疗患者</el-checkbox>
                </el-col>
                <el-col :span="4">
                  <el-checkbox v-model="listQuery.todaytreated">今天已治疗</el-checkbox>
                </el-col>
                <el-col :span="4">
                  <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">查询</el-button>
                </el-col>
            </el-row>
          </el-card>
        </el-row>
        <el-row style="margin-top: 10px">
          <el-col>
            <label class="el-form-item__label" style="margin-left: 20px">今天中心治疗人数230</label>
            <label class="el-form-item__label" style="margin-left: 20px">中心治疗总项目数430</label>
          </el-col>
        </el-row>
        <el-row>
          <el-col :span="12">
            <label class="el-form-item__label" style="margin-left: 20px">我今天治疗人数30</label>
            <label class="el-form-item__label" style="margin-left: 20px">我治疗总项目数60</label>
          </el-col>
          <el-col :span="12">
            <label class="el-form-item__label">治疗次数</label>
            <el-input-number size="small" :min="1" v-model="times" style="width:20%"></el-input-number>
            <el-button size="small" style="margin-left: 10px;" @click="handleMultiTreat" type="primary">批量治疗</el-button>
            <el-button size="small" style="margin-left: 30px;" @click="handleMultiDelete" type="primary">批量删除</el-button>
          </el-col>
        </el-row>
        <el-row>
          <el-table
            ref="multipleTable"
            :data="tableListData"
            :row-style="toggleDisplayTr"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
            @selection-change="orderSelectChange"
            @expand-change="rowExpand"
            :row-class-name="getRowClassName"
          >
              <el-table-column prop="id" label="id" type="selection" fixed width="40">
              </el-table-column>
              <el-table-column type="expand" width="40">
              <template slot-scope="props">
                <el-table
                  :data="subTableData"
                  @expand-change="detail_rowExpand"
                >
                   <el-table-column label="" width="2">
                   </el-table-column>
                   <el-table-column type="expand" width="60">
                       <template slot-scope="props">
                          <el-table :data="detailTableData">
                             <el-table-column width="100" label="" align="center">
                             </el-table-column>
                             <el-table-column label="治疗项目" prop="projectname" width="220" align="center">
                             </el-table-column>
                             <el-table-column prop="times" label="开单次数" width="120" align="center">
                             </el-table-column>
                             <el-table-column prop="residue" label="剩余次数" width="100" align="center">
                             </el-table-column>
                             <el-table-column prop="treatdeptname" label="治疗科室" width="100" align="center">
                             </el-table-column>
                             <el-table-column prop="operatedate" label="治疗日期" width="120" :formatter="dateFormat">
                             </el-table-column>
                             <el-table-column prop="operatename" label="操作人" width="100">
                             </el-table-column>
                          </el-table>
                        </template>
                   </el-table-column>
                   <el-table-column label="套餐名称" prop="name" width="400" align="center">
                   </el-table-column>
                   <el-table-column prop="cureDate" label="治疗日期" width="400">
                   </el-table-column>
                   <el-table-column prop="parent_id" v-if="false" label="操作人" width="10">
                   </el-table-column>
                </el-table>
              </template>
            </el-table-column>
            <el-table-column
              label="客户姓名"
              min-width="120"
              show-overflow-tooltip
              align="left">
                  <template slot-scope="scope">
                    <p :style="`margin-left: ${scope.row.__level * 20}px;margin-top:0;margin-bottom:0`"><i  @click="toggleFoldingStatus(scope.row)" class="permission_toggleFold" :class="toggleFoldingClass(scope.row)"></i>{{scope.row.clientname}}</p>
                  </template>
            </el-table-column>
            <el-table-column prop="phone" label="手机号码" width="120">
            </el-table-column>
            <el-table-column prop="ordermanname" label="开单人" width="70">
            </el-table-column>
            <el-table-column prop="projectname" label="治疗项目" width="80">
            </el-table-column>
            <el-table-column prop="isacquire" label="是否收单" width="80" :formatter="formatCol">
            </el-table-column>
            <el-table-column prop="times" label="开单次数" width="80">
            </el-table-column>
            <el-table-column prop="residue" label="剩余次数" width="80">
            </el-table-column>
            <el-table-column prop="amount" label="今天治疗" width="80">
            </el-table-column>
            <el-table-column prop="treatdeptname" label="治疗科室" width="80">
            </el-table-column>
            <el-table-column prop="operatedate" label="治疗日期" width="100" :formatter="dateFormat">
            </el-table-column>
            <el-table-column prop="operatename" label="操作人" width="70">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="100">
            </el-table-column>
            <el-table-column label="操作" align="center" width="140">
              <template slot-scope="scope">
                  <el-button type="text" v-if="scope.row.depth===1" size="small" @click="handleUpdate(scope.row)">治疗</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">档案</el-button>
                  <el-button type="text" v-if="scope.row.depth===0" size="small" @click="handleDelete(scope.row)">删除</el-button>
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

        <div>
          <el-dialog  title="员工档案" width="55%" :visible.sync="dialogFormVisible">
                  <el-form  :model="treat" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="treat.name" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="出生日期"  prop="birthDate">
                              <el-date-picker
                                v-model="treat.birthDate"
                                style="width:80%"
                                class="myInput"
                                type="date"
                                placeholder="出生日期"
                                value-format="yyyy-MM-dd">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="职称"  prop="profession">
                              <el-select v-model="treat.profession" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in professionSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="学历"  prop="education">
                              <el-select v-model="treat.education" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in educationSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="职工类型"  prop="type">
                              <el-select v-model="treat.type" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in typeSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="电话1"  prop="phone1">
                              <el-input v-model="treat.phone1" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="电话2"  prop="phone2">
                              <el-input v-model="treat.phone2" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="入职日期"  prop="hiredate">
                              <el-date-picker
                                v-model="treat.hiredate"
                                style="width:80%"
                                class="myInput"
                                type="date"
                                placeholder="入职日期"
                                value-format="yyyy-MM-dd">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="入职状态"  prop="state">
                              <el-select v-model="treat.state" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in stateSelect" :key="item.id" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                        <el-row>
                         <el-col :span="12">
                            <el-form-item label="账号"  prop="username">
                              <el-input v-model="treat.username" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="部门"  prop="hrmdepartment">
                              <el-select v-model="treat.hrmdepartment" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in typeSelect" :key="item.id" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="备注"  prop="comment">
                              <el-input v-model="treat.comment" style="width: 90%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    @click="dialogFormVisible = false"
                    icon="el-icon-close"
                  >关闭</el-button>
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
                    @click="updateData">保存
                  </el-button>
                </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { treats, createTreat, updateTreat, deleteTreat, treat_historys,
  getTcTreatHistroryData, treat_details } from '@/api/order'
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
import ElCard from '../../../node_modules/element-ui/packages/card/src/main'

export default {
  components: {
    ElCard,
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
      list: [],
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        begindate: null,
        enddate: null,
        project: '',
        shoudan: '',
        treated: 0,
        todaytreated: 0,
        clientname: '',
        phone: '',
        hrmdepartment_id: this.hrmdepartment_id,
        sort: '+id'
      },
      subTableData: [],
      detailTableData: [],
      hrmdepartment_id: 2,
      times: 1,
      searchname: '',
      dialogFormVisible: false,
      dialogStatus: '',
      projectSelect: [
        { id: 1, name: '全套' },
        { id: 2, name: '盆底' }
      ],
      marketSelect: [
        { id: 1, name: '是' },
        { id: 2, name: '否' }
      ],
      professionSelect: [
        { id: 1, name: '护士长' },
        { id: 2, name: '员工' }
      ],
      educationSelect: [
        { id: 1, name: '研究生' },
        { id: 2, name: '本科' }
      ],
      typeSelect: [
        { id: 1, name: '公司员工' },
        { id: 2, name: '医院职工' }
      ],
      stateSelect: [
        { id: 1, name: '在职' },
        { id: 2, name: '离职' }
      ],
      multipleOrder: [],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }]
      },
      treat: {
        id: null,
        name: '',
        marketdept: null,
        marketpost: null,
        marketman: null,
        orderdept: null,
        orderpost: null,
        adduser: null,
        marketmanname: '',
        orderuser: '',
        issuccess: '',
        iscallback: '',
        reason: null,
        iszengpin: 0,
        isacquire: 0,
        isproorder: 0,
        orderdate: null,
        comment: ''
      },
      tableListData: [],
      foldList: []
    }
  },
  methods: {
    getTreats(data) {
      treats(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.tableListData = this.formatConversion([], this.list)
        console.log('tableListData', this.tableListData)
        this.listLoading = false
      })
    },
    resetTreat() {
      this.treat = {
        id: null,
        name: '',
        marketdept: null,
        marketpost: null,
        marketman: null,
        orderdept: null,
        orderpost: null,
        adduser: null,
        marketmanname: '',
        orderuser: '',
        issuccess: '',
        iscallback: '',
        reason: null,
        iszengpin: 0,
        isacquire: 0,
        isproorder: 0,
        orderdate: null,
        comment: ''
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getTreats(this.listQuery)
    },
    orderSelectChange(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
        console.log('multipleOrder', this.multipleOrder)
      }
    },
    rowExpand(row, expandedRows) {
      const param = {
        page: 1,
        treat_id: row.id,
        project_id: row.project
      }
      getTcTreatHistroryData(param).then(res => {
        // this.subTableData = res.data.results
        this.subTableData = res.data.tchistorys
        console.log('subTableData', this.subTableData)
      })
      // 如果展开行数大于1
      if (expandedRows.length > 1) {
        expandedRows.shift()
      }
    },
    detail_rowExpand(row, expandedRows) {
      const param = {
        parent_id: row.parent_id,
        treatDate: row.cureDate
      }
      treat_details(param).then(res => {
        this.detailTableData = res.data.results
        console.log('detailTableData', this.detailTableData)
      })
      // 如果展开行数大于1
      if (expandedRows.length > 1) {
        expandedRows.shift()
      }
    },
    getRowClassName({row, rowIndex}){
      if (row.depth > 0) {
        return 'row-expand-cover'
      }
    },
    handleMultiTreat() {
      const treatsArr = this.multipleOrder.filter(item => item.depth === 1)
      if (treatsArr.length === 0) {
        this.$notify({
          title: '提示',
          message: '请选择治疗记录',
          type: 'success',
          duration: 2000
        })
        return false
      }
      this.treat = treatsArr[0]
      this.treat.action = 0 // 0为批量治疗1为单项治疗
      this.treat.num = this.times
      this.treat.treats = treatsArr.map(v => v.id)
      updateTreat(this.treat).then(() => {
        this.listQuery.page = 1
        this.listQuery.hrmdepartment_id = this.hrmdepartment_id
        this.getTreats(this.listQuery)
        this.$notify({
          title: '成功',
          message: '批量治疗成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    handleMultiDelete() {

    },
    handleShoudan(flag) {
      if (this.multipleOrder.length === 0) {
        this.$notify({
          title: '提示',
          message: '请选择订单',
          type: 'success',
          duration: 2000
        })
        return false
      }
      this.resetTreat()
      this.treat = this.multipleOrder[0]
      this.treat.action = flag // 0为取消1缴费收单
      this.treat.orders = this.multipleOrder.map(v => v.id)
      updateTreat(this.treat).then(() => {
        this.listQuery.page = 1
        this.listQuery.hrmdepartment_id = this.hrmdepartment_id
        this.getTreats(this.listQuery)
        this.$notify({
          title: '成功',
          message: '收单状态已更新',
          type: 'success',
          duration: 2000
        })
      })
    },
    handleCreate() {
      this.resetTreat()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.treat.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createTreat(this.treat).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getTreats(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.treat = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.treat)
          updateTreat(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getTreats(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.treat = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.treat)
        deleteTreat(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.listQuery.hrmdepartment_id = this.hrmdepartment_id
          this.getTreats(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getTreats(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getTreats(this.listQuery)
    },
    formatCol: function(row, column) {
      const str = row[column.property]
      const str1 = row.operatedate
      if (str === 0 ) {
        if (str1 === null) return '否'
        else return ''
      } else {
        if (str1 === null) return '是'
        else return ''
      }
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      } else if (date === null) {
        return ''
      } else {
        return moment(date).format('YYYY-MM-DD')
      }
    },
    toggleFoldingStatus(params) {
      this.foldList.includes(params.__identity) ? this.foldList.splice(this.foldList.indexOf(params.__identity), 1) : this.foldList.push(params.__identity)
    },
    toggleDisplayTr({row, index}) {
      for (let i = 0; i < this.foldList.length; i++) {
        const item = this.foldList[i]
        if (row.__family.includes(item) && row.__identity !== item) return 'display:none;'
      }
      return ''
    },
    toggleFoldingClass(params) {
      return params.Children.length === 0 ? 'permission_placeholder' : (this.foldList.indexOf(params.__identity) === -1 ? 'iconfont icon-minus-square-o' : 'iconfont icon-plussquareo')
    },
    formatConversion(parent, children, index = 0, family = [], elderIdentity = 'x') {
      if (children.length > 0) {
        children.map((x, i) => {
          this.$set(x, '__level', index)
          this.$set(x, '__family', [...family, elderIdentity + '_' + i])
          this.$set(x, '__identity', elderIdentity + '_' + i)
          parent.push(x)
          if (x.Children.length > 0) this.formatConversion(parent, x.Children, index + 1, [...family, elderIdentity + '_' + i], elderIdentity + '_' + i)
        })
      } return parent
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    const par = {
      hrmdepartment_id: 2,
      page: 1
    }
    this.getTreats(par)
  }
}
</script>


<style lang='stylus' rel='stylesheet/stylus'>
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
    .row-expand-cover .el-table__expand-icon{visibility:hidden;}
    .permission_toggleFold
      vertical-align middle
      padding-right 5px
      font-size 16px
      cursor pointer
    .permission_placeholder
        content ' '
        display inline-block
        width 16px
        font-size 16px
    .init_table
        width 100% !important
        max-width 900px !important
        margin 0 auto !important
</style>

