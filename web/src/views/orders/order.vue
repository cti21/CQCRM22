<template>
    <div>
        <el-row>
          <el-card style="margin-left: 15px;margin-right: 10px">
            <el-row>
                <el-col :span="6">
                  <label class="el-form-item__label">日期从</label>
                  <el-date-picker
                    v-model="listQuery.begindate"
                    style="width:50%;margin-left: 20px"
                    class="myInput"
                    type="date"
                    placeholder="日期开始"
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
                    placeholder="日期结束"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">项目名称</label>
                  <el-select v-model="listQuery.project" clearable style="width:60%" class="myInput">
                      <el-option v-for="item in projectSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">宣教是否成功</label>
                  <el-select v-model="listQuery.issuccess" clearable style="width:40%" class="myInput">
                      <el-option v-for="item in marketSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="6">
                  <label class="el-form-item__label">是否缴费收单</label>
                  <el-select v-model="listQuery.isacquire" clearable style="width:40%" class="myInput">
                    <el-option v-for="item in marketSelect" :key="item.id" :value="item.id" :label="item.name">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">是否立即治疗</label>
                  <el-select v-model="listQuery.isproorder" clearable style="width:40%" class="myInput">
                    <el-option v-for="item in marketSelect" :key="item.id" :value="item.id" :label="item.name">
                    </el-option>
                </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">客户姓名</label>
                  <el-input
                    v-model="listQuery.name"
                    class="myInput"
                    style="width: 180px;margin-right: 20px"
                    clearable
                    placeholder="请输入姓名">
                  </el-input>
                </el-col>
                <!--<el-col :span="6">-->
                  <!--<label class="el-form-item__label">预开单已经治疗</label>-->
                  <!--<el-select v-model="listQuery.ykdtreated" clearable style="width:40%" class="myInput">-->
                    <!--<el-option v-for="item in marketSelect" :key="item.id" :value="item.id" :label="item.name">-->
                    <!--</el-option>-->
                <!--</el-select>-->
                <!--</el-col>-->
                <el-col :span="6">
                  <label class="el-form-item__label">开单人员</label>
                  <el-select v-model="listQuery.orderuser" clearable style="width:60%" class="myInput">
                      <el-option v-for="item in userSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
            </el-row>
            <el-row>
              <el-col :span="6">
                  <label class="el-form-item__label">宣教人员</label>
                  <el-select v-model="listQuery.marketuser" clearable style="width:60%" class="myInput">
                      <el-option v-for="item in userSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
                 <el-col :span="6">
                    <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">查询</el-button>
                 </el-col>
            </el-row>
          </el-card>
        </el-row>
        <el-row style="margin:20px;">
          <el-col :span="3">
            <el-button size="small" style="margin-left: 10px;" @click="handleOrder" type="primary">宣教开单</el-button>
          </el-col>
          <el-col :span="8">
            <el-button size="small" style="margin-left: 5px;" @click="handleShoudan(1)" type="primary">缴费收单</el-button>
            <el-button size="small" style="margin-left: 5px;" @click="handleShoudan(0)" type="primary">取消缴费收单</el-button>
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
          >
            <el-table-column prop="id" label="id" type="selection" fixed>
            </el-table-column>
            <el-table-column
              label="日期"
              min-width="130"
              show-overflow-tooltip
              :formatter="dateFormat"
              align="left">
                  <template slot-scope="scope">
                    <p :style="`margin-left: ${scope.row.__level * 20}px;margin-top:0;margin-bottom:0`"><i  @click="toggleFoldingStatus(scope.row)" class="permission_toggleFold" :class="toggleFoldingClass(scope.row)"></i>{{scope.row.marketdate}}</p>
                  </template>
            </el-table-column>
            <el-table-column prop="clientname" label="客户姓名" width="90">
            </el-table-column>
            <el-table-column prop="orderdeptname" label="科室" width="80">
            </el-table-column>
            <el-table-column prop="projectname" label="项目" width="80">
            </el-table-column>
            <el-table-column prop="marketmanname" label="宣教人员" width="80">
            </el-table-column>
            <el-table-column prop="issuccess" label="宣教成功" width="80" :formatter="formatCol">
            </el-table-column>
            <el-table-column prop="orderuser" label="开单人员" width="80">
            </el-table-column>
            <el-table-column prop="orderdeptname" label="开单科室" width="80">
            </el-table-column>
            <el-table-column prop="times" label="开单次数" width="80">
            </el-table-column>
            <el-table-column prop="receivable" label="应收金额" width="80">
            </el-table-column>
            <el-table-column prop="discount" label="优惠金额" width="80">
            </el-table-column>
            <el-table-column prop="receipts" label="实收金额" width="80">
            </el-table-column>
            <el-table-column prop="isproorder" label="立即治疗" width="80" :formatter="formatCol">
            </el-table-column>
            <el-table-column prop="isacquire" label="是否收单" width="80" :formatter="formatCol">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="80">
            </el-table-column>
            <el-table-column label="操作" width="140">
              <template slot-scope="scope">
                  <el-button type="text" v-if="false" size="small" @click="handleTreat(scope.row)">治疗</el-button>
                  <el-button type="text" size="small" @click="handleInfo(scope.row)">档案</el-button>
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
                  <el-form  :model="order" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="order.name" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="性别"  prop="sex">
                              <el-select v-model="order.sex" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in sexSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="出生日期"  prop="birthDate">
                              <el-date-picker
                                v-model="order.birthDate"
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
                              <el-select v-model="order.profession" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in professionSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="学历"  prop="education">
                              <el-select v-model="order.education" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in educationSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="职工类型"  prop="type">
                              <el-select v-model="order.type" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in typeSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="电话1"  prop="phone1">
                              <el-input v-model="order.phone1" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="电话2"  prop="phone2">
                              <el-input v-model="order.phone2" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="入职日期"  prop="hiredate">
                              <el-date-picker
                                v-model="order.hiredate"
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
                              <el-select v-model="order.state" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in stateSelect" :key="item.id" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                        <el-row>
                         <el-col :span="12">
                            <el-form-item label="账号"  prop="username">
                              <el-input v-model="order.username" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="部门"  prop="hrmdepartment">
                              <el-select v-model="order.hrmdepartment" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in typeSelect" :key="item.id" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="备注"  prop="comment">
                              <el-input v-model="order.comment" style="width: 90%;" class="myInput"></el-input>
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

        <!--员工档案-->
        <div>
          <el-dialog  title="员工档案" width="50%" :visible.sync="dialogArchiveVisible">
            <archive :client_id="clientid"></archive>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { orders, createOrder, updateOrder, deleteOrder, getOrderSelectData } from '@/api/order'
import archive from '@/views/client/archives.vue'
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
    ElCol,
    archive
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
        name: '',
        issuccess: '',
        isacquire: '',
        isproorder: '',
        ykdtreated: '',
        project: '',
        orderuser: '',
        marketuser: '',
        hrmdepartment_id: this.hrmdepartment_id,
        sort: '+id'
      },
      clientid: null,
      dialogArchiveVisible: false,
      hrmdepartment_id: 2,
      searchname: '',
      dialogFormVisible: false,
      dialogStatus: '',
      sexSelect: [
        { id: 1, name: '男' },
        { id: 2, name: '女' }
      ],
      marketSelect: [
        { id: 1, name: '是' },
        { id: 0, name: '否' }
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
      userSelect: [],
      projectSelect: [],
      multipleOrder: [],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }]
      },
      order: {
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
    getOrders(data) {
      orders(data).then(response => {
        this.list = []
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.tableListData = []
        this.tableListData = this.formatConversion([], this.list)
        this.listLoading = false
      })
    },
    resetOrder() {
      this.order = {
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
      this.getOrders(this.listQuery)
    },
    orderSelectChange(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    handleOrder() {
      this.$router.push({
        path: '/client_index',
        query: { hrmdepartment_id: this.hrmdepartment_id }
      })
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
      this.resetOrder()
      this.order = this.multipleOrder[0]
      this.order.action = flag // 0为取消1缴费收单2为治疗操作
      this.order.orders = this.multipleOrder.map(v => v.id)
      updateOrder(this.order).then(() => {
        this.listQuery.page = 1
        this.listQuery.hrmdepartment_id = this.hrmdepartment_id
        this.getOrders(this.listQuery)
        this.$notify({
          title: '成功',
          message: '收单状态已更新',
          type: 'success',
          duration: 2000
        })
      })
    },
    handleInfo(row) {
      this.clientid = row.client
      this.dialogArchiveVisible = true
      this.$nextTick(() => {
      })
    },
    handleCreate() {
      this.resetOrder()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.order.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createOrder(this.order).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getOrders(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.order = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.order)
          updateOrder(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getOrders(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.order = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.order)
        deleteOrder(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.listQuery.hrmdepartment_id = this.hrmdepartment_id
          this.getOrders(this.listQuery)
        })
      })
    },
    handleTreat(row) {
      const tempData = Object.assign({}, row)
      tempData.action = 2 // 点击治疗按钮时
      updateOrder(tempData).then(() => {
        this.dialogFormVisible = false
        this.$notify({
          title: '成功',
          message: '添加治疗成功',
          type: 'success',
          duration: 2000
        })
        this.$router.push({
          path: '/treat',
          query: { hrmdepartment_id: this.hrmdepartment_id }
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.hrmdepartment_id = this.hrmdepartment_id
      console.log(this.listQuery)
      this.getOrders(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.listQuery.hrmdepartment_id = this.hrmdepartment_id
      this.getOrders(this.listQuery)
    },
    formatCol: function(row, column) {
      const str = row[column.property]
      const str1 = row.depth
      if (str === 0 ) {
        if (str1 === 0) return '否'
        else return ''
      } else {
        if (str1 === 0) return '是'
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
      }
//      this.foldList  = []
//      this.foldList = parent.map(x => x.__identity)
      return parent
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    const param = { hrmdepartment_id: this.hrmdepartment_id }
    getOrderSelectData(param).then(res => {
      console.log('res.data', res.data)
      this.userSelect = res.data.users
      this.projectSelect = res.data.projects
    })
    const par = {
      hrmdepartment_id: 2,
      page: 1
    }
    this.getOrders(par)
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
