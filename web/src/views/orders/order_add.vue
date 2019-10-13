<template>
    <div>
        <el-form :model="order" ref="dataForm" :rules="rules"  label-position="left" label-width="100px" style='width:95%; margin-left:30px;'>
             <el-row>
               <el-col :span="8">
                    <label class="el-form-item__label">宣教科室</label>
                    <el-select v-model="order.marketdept" clearable style="width: 60%" class="myInput" @change="marketDeptChange">
                        <el-option v-for="item in deptSelect" :key="item.id" :value="item.id" :label="item.deptname">
                        </el-option>
                    </el-select>
               </el-col>
                <el-col :span="8">
                    <label class="el-form-item__label">宣教岗位</label>
                    <el-select v-model="order.marketpost" clearable style="width: 60%" class="myInput">
                        <el-option v-for="(item,index) in marketPostSelect" :key="index" :value="item.postdict" :label="item.postname">
                        </el-option>
                    </el-select>
               </el-col>
               <el-col :span="8">
                    <label class="el-form-item__label">宣教人员</label>
                    <el-select v-model="order.marketman" clearable style="width: 60%" class="myInput">
                        <el-option v-for="item in userSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
               </el-col>
            </el-row>
            <el-row style="margin-top: 10px">
              <el-col :span="8">
                    <label class="el-form-item__label">宣教是否成功</label>
                    <el-select v-model="order.issuccess" clearable style="width: 50%" class="myInput" @change="marketChange">
                        <el-option v-for="item in isSuccessSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
               </el-col>
               <el-col :span="8" style="margin-top: 0px">
                  <label class="el-form-item__label">日期</label>
                  <el-date-picker
                    v-model="order.marketdate" type="date" value-format="yyyy-MM-dd"
                    format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                  </el-date-picker>
               </el-col>
                <el-col :span="8" v-if="marketStatus===0">
                    <label class="el-form-item__label">宣教失败原因</label>
                    <el-select v-model="order.reason" clearable style="width: 50%" class="myInput">
                        <el-option v-for="item in reasonSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
               </el-col>
            </el-row>
            <el-row  v-if="marketStatus===1"  style="margin-top: 10px">
               <el-col :span="8">
                    <label class="el-form-item__label">开单科室</label>
                    <el-select v-model="order.orderdept" clearable style="width: 60%" class="myInput" @change="orderDeptChange">
                        <el-option v-for="item in deptSelect" :key="item.id" :value="item.id" :label="item.deptname">
                        </el-option>
                    </el-select>
               </el-col>
               <el-col :span="8">
                    <label class="el-form-item__label">开单岗位</label>
                    <el-select v-model="order.orderpost" clearable style="width: 60%" class="myInput">
                        <el-option v-for="(item,index) in orderPostSelect" :key="index" :value="item.postdict" :label="item.postname">
                        </el-option>
                    </el-select>
               </el-col>
               <el-col :span="8">
                    <label class="el-form-item__label">开单人员</label>
                    <el-select v-model="order.adduser" clearable style="width: 60%" class="myInput">
                        <el-option v-for="item in userSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
               </el-col>
            </el-row>
            <el-row   v-if="marketStatus===1" style="margin-top: 10px">
               <el-col :span="8" style="margin-top: 10px;">
                  <el-checkbox v-model="order.iszengpin">赠送</el-checkbox>
               </el-col>
                <el-col :span="8" style="margin-top: 10px">
                  <el-checkbox v-model="order.isacquire">是否缴费收单</el-checkbox>
               </el-col>
               <el-col :span="8">
                    <label class="el-form-item__label">是否回访</label>
                    <el-select v-model="order.iscallback" clearable style="width: 60%" class="myInput">
                        <el-option v-for="item in isSuccessSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
               </el-col>
             </el-row>
             <el-row  style="margin-top: 10px">
               <el-col>
                    <label class="el-form-item__label">备注</label>
                    <el-input v-model="order.comment" style="width: 70%;" class="myInput"></el-input>
               </el-col>
             </el-row>
             <el-row style="margin-top: 10px" v-if="marketStatus===1">
               <el-col :span="12">
                 <el-button size="small" style="margin-right: 10px" @click="handleCreate" type="primary">开单项目</el-button>
                 <el-button size="small" style="margin-right: 10px" type="primary" @click="handleMultiDelete">批量删除</el-button>
               </el-col>
               <el-col :span="11" align="right" >
                  <el-button size="small" @click="handleAgree" type="primary">知情同意书</el-button>
               </el-col>
               <el-col :span="1">
               </el-col>
             </el-row>
             <el-row style="margin-top: 10px" v-if="marketStatus===1">
               <el-table
                ref="projectTable"
                :data="multiSelection"
                :header-cell-style="{background:'#F8F8F8'}"
                v-loading="listLoading"
                stripe
                @selection-change="project_SelectChange"
              >
                <el-table-column prop="id" label="id" type="selection" fixed width="40">
                </el-table-column>
                <el-table-column
                  label="项目名称"
                  min-width="110"
                  show-overflow-tooltip
                  prop="name">
                  </el-table-column>
                <el-table-column prop="price" label="价格" width="70">
                </el-table-column>
                <el-table-column prop="times" label="次数" width="80">
                  <template slot-scope="scope">
                     <el-input v-model="scope.row.times" style="width: 80%;" class="myInput"></el-input>
                  </template>
                </el-table-column>
                <el-table-column label="应收金额" width="98">
                  <template slot-scope="scope">
                     <el-input v-if="scope.row.depth===0" v-model="scope.row.receivable" style="width: 90%;" class="myInput"></el-input>
                  </template>
                </el-table-column>
                 <el-table-column label="优惠金额" width="90">
                    <template slot-scope="scope">
                       <el-input v-if="scope.row.depth===0" v-model="scope.row.discount" style="width: 90%;" class="myInput"></el-input>
                    </template>
                  </el-table-column>
                  <el-table-column label="实收金额" width="98">
                    <template slot-scope="scope">
                       <el-input v-if="scope.row.depth===0" v-model="scope.row.receipts" style="width: 90%;" class="myInput"></el-input>
                    </template>
                  </el-table-column>
                  <el-table-column label="立即治疗" width="90">
                    <template slot-scope="scope">
                       <el-checkbox v-if="scope.row.depth===0" v-model="scope.row.isproorder"></el-checkbox>
                    </template>
                  </el-table-column>
                  <!--<el-table-column prop="comment" label="备注" width="100">-->
                  <!--</el-table-column>-->
               </el-table>
             </el-row>
        </el-form>
        <div slot="footer" class="dialog-footer" align="right" style="margin-top: 20px;margin-right: 50px;">
          <el-button
            size="small"
            @click="closeDialog"
            icon="el-icon-close"
          >关闭</el-button>
          <el-button
              size="small"
              type="primary"
              icon="el-icon-check"
              @click="createOrderData">保存
            </el-button>
        </div>

        <!--项目选择界面-->
        <div>
           <el-dialog  title="选择项目" width="50%" :visible.sync="dialogFormVisible" :append-to-body="true">
                <el-table
                    ref="multipleTable"
                    :data="list"
                    :header-cell-style="{background:'#F8F8F8'}"
                    v-loading="listLoading"
                    stripe
                    @selection-change="orderSelectChange"
                  >
                  <el-table-column
                    prop="id"
                    label="id"
                    type="selection"
                    :selectable='checkStatus'
                    fixed>
                  </el-table-column>
                  <el-table-column
                      label="项目名称"
                      show-overflow-tooltip
                      prop="name"
                      align="left">
                  </el-table-column>
                  <el-table-column prop="price" label="价格" width="100">
                  </el-table-column>
                  <el-table-column prop="amount" label="次数" width="100">
                  </el-table-column>
                  <el-table-column prop="comment" label="备注" width="100">
                  </el-table-column>
               </el-table>
              <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="dialogFormVisible=false"
                  >关闭
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    @click="createData">保存
                  </el-button>
              </div>
           </el-dialog>
         </div>
    </div>
</template>

<script>
import { formatDate } from '@/utils/date'
import { depts, dept_posts, projects } from '@/api/system'
import { users } from '@/api/employee'
import { createOrder } from '@/api/order'
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
  props: ['hrmdepartment_id', 'clientid', 'register_id', 'count'],
  data: function() {
    return {
      list: [],
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        register_id: null,
        hrmdepartment_id: '',
        sort: '+id'
      },
      dialogFormVisible: false,
      dialogEditVisible: false,
      dialogStatus: '',
      marketStatus: 0,
      foldList: [],
      tableListData: [],
      projectListData: [],
      deptSelect: [],
      userSelect: [],
      marketPostSelect: [],
      orderPostSelect: [],
      isSuccessSelect: [
        { id: 1, name: '是' },
        { id: 0, name: '否' }
      ],
      reasonSelect: [
        { id: 0, name: '患者本人不同意' },
        { id: 1, name: '家属不同意' },
        { id: 2, name: '医院人员干扰' }
      ],
      multipleOrder: [],
      multiSelection: [],
      multipleProject: [],
      selectionobj: null,
      selectList: [],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
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
        orderdate: formatDate(new Date(), 'yyyy-MM-dd'),
        marketdate: formatDate(new Date(), 'yyyy-MM-dd'),
        comment: ''
      }
    }
  },
  methods: {
    getProjects(data) {
      projects(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getDepts(data) {
      depts(data).then(response => {
        this.deptSelect = response.data.results
      })
    },
    getUsers(data) {
      users(data).then(response => {
        this.userSelect = response.data.results
      })
    },
    marketDeptChange(val) {
      let obj = {}
      obj = this.deptSelect.find(item => {
        return item.id === val
      })
      const par = { name: obj.deptdict }
      dept_posts(par).then(response => {
        this.marketPostSelect = []
        this.marketPostSelect = response.data.results
        console.log('marketPostSelect', this.marketPostSelect)
      })
    },
    marketChange(val) {
      if (val === 0) {
        this.marketStatus = 0
      } else {
        this.marketStatus = 1
      }
    },
    orderDeptChange(val) {
      let obj = {}
      obj = this.deptSelect.find(item => {
        return item.id === val
      })
      const par = { name: obj.deptdict }
      dept_posts(par).then(response => {
        this.orderPostSelect = []
        this.orderPostSelect = response.data.results
      })
    },
    checkStatus(row, rowIndex) {
      if (row.jinjizheng > 0) {
        return false
      } else {
        return true
      }
    },
    resetOrder() {
      this.order = {
        id: null,
        name: '',
        marketdept: '',
        marketpost: '',
        marketman: '',
        orderdept: '',
        orderpost: '',
        adduser: '',
        marketmanname: '',
        orderuser: '',
        issuccess: '',
        iscallback: '',
        reason: '',
        iszengpin: '',
        isacquire: '',
        isproorder: '',
        orderdate: '',
        comment: ''
      }
    },
    orderSelectChange(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    selectProject(selection, row) {
      console.log('selection', selection)
      if (selection.length < 4) {
        this.selectList = []
        this.selectList = selection
      }
    },
    project_SelectChange(val) {
      if (val) {
        this.multipleProject = []
        this.multipleProject = val
        console.log('multipleProject', this.multipleProject)
        console.log('projectListData', this.projectListData)
      }
    },
    project_rowClick(row, event, column) {
      const parentitem = this.$refs.multipleTable.data.find(t => t.id === row.parent)
      const nodename = event.target.nodeName
      this.selectionobj = this.$refs.multipleTable.selection[0]
      console.log('currentSelect', this.selectionobj)
    },
    remote(row, callback) {
      setTimeout(function() {
        callback(row.children)
      }, 800)
    },
    handleCreate() {
      this.dialogFormVisible = true
      this.$nextTick(() => {
      })
    },
    handleMultiDelete() {
      this.multiSelection = []
      this.multiSelection = this.multipleOrder.filter(item => !this.multipleProject.some(ele => ele.id === item.id))
      console.log('multiSelection', this.multiSelection)
    },
    createData() {
      this.multiSelection = []
      this.multiSelection = [...this.multipleOrder]
      for (const item of this.multiSelection) {
        item.times = 1
        item.receivable = item.price
        item.discount = 0
        item.receipts = item.price
      }
      this.dialogFormVisible = false
    },
    createOrderData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.order.id = parseInt(Math.random() * 100) + 1024
          if (this.order.iszengpin === true) {
            this.order.iszengpin = 1
          } else {
            this.order.iszengpin = 0
          }
          if (this.order.isproorder === true) {
            this.order.isproorder = 1
          } else {
            this.order.isproorder = 0
          }
          if (this.order.isacquire === true) {
            this.order.isacquire = 1
          } else {
            this.order.isacquire = 0
          }
          this.order.clientid = this.clientid
          this.order.register_id = this.register_id
          this.order.hrmdepartment_id = this.hrmdepartment_id
          if (this.order.issuccess === 1) {
            if (this.multiSelection.length === 0) {
              this.$notify({
                title: '提示',
                message: '请选择项目',
                type: 'success',
                duration: 2000
              })
              return false
            }
          }
          this.order.projects = this.multiSelection
          console.log('this.order', this.order)
          createOrder(this.order).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            const data = { flag: 1 }
            this.$emit('closeDlg', data)
          })
        }
      })
    },
    closeDialog() {
      const data = { flag: 0 }
      this.$emit('closeDlg', data)
    },
    handleAgree() {
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getProjects(this.listQuery)
    }
  },
  watch: {
    count: function() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.listQuery.register_id = this.register_id
      this.listQuery.hrmdepartment_id = 2
      this.getProjects(this.listQuery)
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.listQuery.register_id = this.register_id
    this.listQuery.hrmdepartment_id = 2
    this.getDepts(this.listQuery)
    this.getUsers(this.listQuery)
    this.getProjects(this.listQuery)
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
