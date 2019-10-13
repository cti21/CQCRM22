<template>
    <div>
        <el-row>
             <el-select v-model="searchname" clearable style="width: 200px" class="myInput" placeholder="中心">
                <el-option v-for="item in centerSelect" :key="item.id" :value="item.id" :label="item.name">
                </el-option>
            </el-select>
            <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </el-row>
        <el-row style="margin:20px;">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <el-table-column type="index" label="序号"  width="60">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="220">
            </el-table-column>
            <el-table-column prop="type" label="是否套餐" :formatter="formatCol" width="120">
            </el-table-column>
            <el-table-column prop="isindependent" label="是否独立开单" :formatter="formatCol" width="160">
            </el-table-column>
            <el-table-column prop="tckind" label="套餐类型" width="120">
            </el-table-column>
            <el-table-column prop="price" label="价格" width="120">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" v-if="scope.row.type===false" @click="priceSet(scope.row)">设置价格</el-button>
                  <el-button type="text" size="small" v-if="scope.row.flag===false && scope.row.type===true" @click="handleUpdate(scope.row)">查看</el-button>
                  <el-button type="text" size="small" v-if="scope.row.flag===true" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
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

        <!--中心项目新增-->
        <div>
          <el-dialog  title="中心项目" width="45%" :visible.sync="dialogFormVisible">
            <el-form :model="project" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
                 <el-row style="margin-bottom: 10px;width: 100%" >
                   <el-button-group style="width: 100%">
                      <el-button size="small" style="width: 50%" @click="taocanCreate" type="primary" icon="el-icon-plus">新增套餐</el-button>
                      <el-button size="small" style="width: 50%" @click="taocanImport" type="primary" icon="el-icon-download">导入项目</el-button>
                   </el-button-group>
                 </el-row>
                 <el-row v-if="taocanAddVisable===true">
                   <el-form-item label="套餐名称">
                     <el-input v-model="taocanname" style="width: 90%;" class="myInput" placeholder="套餐名称">
                     </el-input>
                   </el-form-item>
                 </el-row>
                 <el-row v-if="taocanAddVisable===true">
                   <el-form-item label="备注">
                     <el-input v-model="taocancomment" style="width: 90%;" class="myInput" placeholder="套餐名称">
                     </el-input>
                   </el-form-item>
                 </el-row>
                 <el-row>
                   <el-table
                    :data="projectdicts"
                    ref="multipleTable"
                    :header-cell-style="{background:'#F8F8F8'}"
                    stripe
                    highlight-current-row
                    @selection-change="orderSelectChange"
                    @row-click="rowClick">
                    <el-table-column type="selection" width="80" class="selection" align="center">
                    </el-table-column>
                    <el-table-column prop="name"  label="项目名称" width="240">
                    </el-table-column>
                    <el-table-column prop="comment" label="备注" width="200" align="center">
                    </el-table-column>
                   </el-table>
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
                v-if="taocanAddVisable===true"
                @click="taocancreateData">保存
              </el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                v-else
                @click="createData">保存
              </el-button>
            </div>
          </el-dialog>
        </div>

        <!--项目编辑-->
        <div>
          <el-dialog  title="项目信息" width="55%" :visible.sync="dialogEditVisible">
              <el-form  :model="project" ref="editForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:60px;'>
                  <el-row>
                     <el-col>
                        <el-form-item label="名称"  prop="name">
                          <el-input v-model="project.name" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="能否独立开单"  prop="isindependent">
                          <el-switch v-model="project.isindependent"></el-switch>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="是否套餐"  prop="type">
                          <el-switch v-model="project.type"></el-switch>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                      <el-col :span="12">
                        <el-form-item label="规则"  prop="amount">
                          <el-input v-model="project.amount" style="width: 70%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="备注"  prop="comment">
                          <el-input v-model="project.comment" style="width: 70%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row  v-if="project.type===true">
                     <el-button size="small" @click="project_handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
                   </el-row>
                   <el-row v-if="project.type===true">
                     <el-table
                        :data="projectChild"
                        :header-cell-style="{background:'#F8F8F8'}"
                        stripe
                      >
                        <el-table-column type="index" label="序号"  width="60">
                        </el-table-column>
                        <el-table-column prop="name" label="项目名称" width="240">
                        </el-table-column>
                        <el-table-column prop="amount" label="次数" width="80">
                        </el-table-column>
                        <el-table-column prop="comment" label="备注" width="100">
                        </el-table-column>
                         <el-table-column label="操作" fixed="right" align="center">
                          <template slot-scope="scope">
                              <el-button type="text" size="small" @click="project_handleUpdate(scope.row)">修改</el-button>
                              <el-button type="text" size="small" @click="project_handleDelete(scope.row)">删除</el-button>
                          </template>
                        </el-table-column>
                     </el-table>
                   </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  @click="dialogEditVisible = false"
                  icon="el-icon-close"
                >关闭</el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogStatus=='update'"
                  @click="updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

        <!--套餐子项目添加-->
        <div>
          <el-dialog  title="子项目添加" width="40%" :visible.sync="dialogProjectAddVisible">
            <el-form  :model="project" ref="childAddForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
               <el-row>
                 <el-table
                  :data="projectIndividual"
                  ref="multipleTable"
                  :header-cell-style="{background:'#F8F8F8'}"
                  stripe
                  highlight-current-row
                  @selection-change="orderSelectChange"
                  @row-click="rowClick">
                  <el-table-column type="selection" width="80" class="selection" align="center">
                  </el-table-column>
                  <el-table-column prop="name"  label="项目名称" width="180" align="center">
                  </el-table-column>
                  <el-table-column prop="comment" label="备注" width="240" align="center">
                  </el-table-column>
                 </el-table>
               </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button
                size="small"
                @click="dialogProjectAddVisible = false"
                icon="el-icon-close"
              >关闭</el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                @click="project_createData">保存
              </el-button>
            </div>
          </el-dialog>
        </div>

        <!--价格设置-->
        <div>
          <el-dialog  title="价格设置" width="40%" :visible.sync="dialogPriceSetVisible">
            <el-form  :model="child" ref="priceForm" label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
               <el-row>
                 <el-form-item label="项目价格" prop="price">
                    <el-input-number v-model="child.price" style="width: 80%;"  :min="1"></el-input-number>
                 </el-form-item>
               </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button
                size="small"
                @click="dialogPriceSetVisible = false"
                icon="el-icon-close"
              >关闭</el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                @click="priceSet_save">保存
              </el-button>
            </div>
          </el-dialog>
        </div>

        <!--次数设置-->
        <div>
          <el-dialog  title="次数设置" width="40%" :visible.sync="dialogSubVisible">
            <el-form  :model="child" ref="amountForm" label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
               <el-row>
                 <el-form-item label="项目次数" prop="amount">
                    <el-input-number v-model="child.amount" style="width: 80%;"  :min="1"></el-input-number>
                 </el-form-item>
               </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button
                size="small"
                @click="dialogSubVisible = false"
                icon="el-icon-close"
              >关闭</el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                @click="amountSet_save">保存
              </el-button>
            </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { project_dicts, projects, project_dict_individuals, createProject,
  updateProject, deleteProject, project_childs, project_individuals } from '@/api/system'
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
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10000,
        offset: 0,
        name: '',
        isindependent: null,
        sort: '+id'
      },
      projectdicts: [],
      projectChild: [],
      projectIndividual: [],
      multipleOrder: [],
      projectid: null,
      searchname: '',
      taocanname: '',
      taocancomment: '',
      hrmdepartment_id: 2,
      taocanAddVisable: false,
      dialogFormVisible: false,
      dialogEditVisible: false,
      dialogSubVisible: false,
      dialogProjectAddVisible: false,
      dialogPriceSetVisible: false,
      dialogStatus: '',
      centerSelect: [
        {
          id: 2,
          name: '綦江中心'
        },
        {
          id: 3,
          name: '永川中心'
        }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      child: {
        id: null,
        name: '',
        amount: null,
        price: null,
        comment: '',
        action: ''
      },
      project: {
        id: null,
        name: '',
        isindependent: null,
        type: null,
        amount: null,
        price: null,
        comment: '',
        action: ''
      }
    }
  },
  methods: {
    getProject(data) {
      projects(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        console.log('list',this.list)
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getProjectdict(data) {
      project_dicts(data).then(response => {
        this.projectdicts = response.data.results
      })
    },
    getChildData(data) {
      project_childs(data).then(response => {
        this.projectChild = response.data.results
      })
    },
    getIndividualData(data) {
      project_dicts(data).then(response => {
        this.projectIndividual = response.data.results
      })
    },
    resetProject() {
      this.project = {
        id: null,
        name: '',
        isindependent: null,
        type: null,
        amount: null,
        price: null,
        comment: '',
        action: ''
      }
    },
    orderSelectChange: function(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    rowClick(row, event, column) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    taocanCreate() {
      this.taocanname = ''
      this.taocanAddVisable = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    taocanImport() {
      this.taocanname = ''
      this.taocanAddVisable = false
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    taocancreateData() {
      if (this.multipleOrder.length > 0) {
        this.project.id = parseInt(Math.random() * 100) + 1024 // mock a id
        const tempdata = Object.assign({}, this.project)
        tempdata.action = 'taocanAdd'
        tempdata.name = this.taocanname
        tempdata.isindependent = 1
        tempdata.type = 1
        tempdata.hrmdepartment_id = this.searchname
        tempdata.projects = this.multipleOrder
        createProject(tempdata).then(() => {
          this.dialogFormVisible = false
          this.$notify({
            title: '成功',
            message: '创建成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getProject(this.listQuery)
        })
      }
    },
    handleCreate() {
      if (this.searchname === '') {
        this.$notify({
          title: '成功',
          message: '请选择中心',
          type: 'success',
          duration: 2000
        })
        return false
      }
      this.listQuery.isindependent = 1
      this.getProjectdict(this.listQuery)
      this.resetProject()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      if (this.multipleOrder.length > 0) {
        this.project.id = parseInt(Math.random() * 100) + 1024 // mock a id
        const tempdata = Object.assign({}, this.project)
        tempdata.action = 'import'
        tempdata.name = 'aaa'
        tempdata.isindependent = 1
        tempdata.type = 1
        tempdata.hrmdepartment_id = this.searchname
        tempdata.projects = this.multipleOrder
        createProject(tempdata).then(() => {
          this.dialogFormVisible = false
          this.$notify({
            title: '成功',
            message: '创建成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getProject(this.listQuery)
        })
      }
    },
    project_handleCreate() {
      this.projectIndividual = []
      this.listQuery.name = ''
      this.getIndividualData(this.listQuery)
      this.dialogProjectAddVisible = true
      this.$nextTick(() => {
        this.$refs['childAddForm'].clearValidate()
      })
    },
    project_createData() {
      if (this.multipleOrder.length > 0) {
        this.project.id = parseInt(Math.random() * 100) + 1024
        const tempdata = Object.assign({}, this.project)
        tempdata.action = 'childAdd'
        tempdata.name = 'aaa'
        tempdata.hrmdepartment_id = this.searchname
        tempdata.projects = this.multipleOrder
        tempdata.parentid = this.projectid
        createProject(tempdata).then(() => {
          this.dialogProjectAddVisible = false
          this.$notify({
            title: '成功',
            message: '创建成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            name: this.searchname,
            hrmdepartment_id: this.hrmdepartment_id,
            parentid: this.projectid
          }
          this.getChildData(par)
        })
      }
    },
    priceSet(row) {
      this.child = Object.assign({}, row)
      this.dialogPriceSetVisible = true
      this.$nextTick(() => {
        // this.$refs['priceForm'].clearValidate()
      })
    },
    priceSet_save() {
      const tempData = Object.assign({}, this.child)
      tempData.action = 1 // 价格更新
      updateProject(tempData).then(() => {
        this.dialogPriceSetVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
        this.listQuery.page = 1
        this.getProject(this.listQuery)
      })
    },
    handleUpdate(row) {
      this.project = Object.assign({}, row)
      this.projectid = row.id
      this.dialogStatus = 'update'
      const par = {
        name: this.searchname,
        hrmdepartment_id: this.hrmdepartment_id,
        parentid: this.project.id
      }
      this.projectChild = []
      if (row.type === true) {
        this.getChildData(par)
      }
      this.dialogEditVisible = true
      this.$nextTick(() => {
        this.$refs['editForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['editForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.project)
          updateProject(tempData).then(() => {
            this.dialogEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getProject(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.project = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.project)
        deleteProject(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getProject(this.listQuery)
        })
      })
    },
    project_handleUpdate(row) {
      this.child = Object.assign({}, row)
      this.dialogSubVisible = true
      this.$nextTick(() => {
        this.$refs['amountForm'].clearValidate()
      })
    },
    amountSet_save() {
      const tempData = Object.assign({}, this.child)
      tempData.action = 2 // 次数设置
      updateProject(tempData).then(() => {
        this.dialogSubVisible = false
        this.$notify({
          title: '成功',
          message: '次数设置成功',
          type: 'success',
          duration: 2000
        })
        const par = {
          name: this.searchname,
          hrmdepartment_id: this.hrmdepartment_id,
          parentid: this.projectid
        }
        this.getChildData(par)
      })
    },
    project_handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.child = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.child)
        deleteProject(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            name: this.searchname,
            hrmdepartment_id: this.hrmdepartment_id,
            parentid: this.projectid
          }
          this.getChildData(par)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getProjectdict(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getProjectdict(this.listQuery)
    },
    formatCol: function(row, column) {
      const str = row[column.property]
      if (str === false) return '否'
      else return '是'
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.getProject(this.listQuery)
  }
}
</script>

<style>
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
