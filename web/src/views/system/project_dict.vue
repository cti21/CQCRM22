<template>
    <div>
        <el-row>
            <el-input
              v-model="searchname"
              class="myInput"
              style="width: 220px;margin-right: 20px"
              clearable
              @keyup.enter.native="handleFilter"
              suffix-icon="el-icon-search"
              placeholder="请输入名称">
            </el-input>
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
            <el-table-column type="index" label="序号"  width="100">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="220">
            </el-table-column>
            <el-table-column prop="type" label="是否套餐" :formatter="formatCol" width="160">
            </el-table-column>
            <el-table-column prop="isindependent" label="是否独立开单" :formatter="formatCol" width="180">
            </el-table-column>
            <!--<el-table-column prop="amount" label="规则" width="80">-->
            <!--</el-table-column>-->
            <el-table-column prop="comment" label="备注" width="120">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleJinjizheng(scope.row)">禁忌症</el-button>
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
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

        <!--项目新增-->
        <div>
          <el-dialog  title="项目" width="40%" :visible.sync="dialogFormVisible">
            <el-form  :model="area" ref="dataForm" :rules="rules"  label-position="left" label-width="100px" style='width:90%; margin-left:30px;'>
                 <el-row>
                   <el-col>
                      <el-form-item label="名称"  prop="name">
                        <el-input v-model="area.name" style="width: 80%;" class="myInput"></el-input>
                      </el-form-item>
                   </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="12">
                      <el-form-item label="能否独立开单"  prop="isindependent">
                        <el-switch v-model="area.isindependent"></el-switch>
                      </el-form-item>
                   </el-col>
                   <el-col :span="12">
                      <el-form-item label="是否套餐"  prop="type">
                        <el-switch v-model="area.type"></el-switch>
                      </el-form-item>
                   </el-col>
                 </el-row>
                 <el-row>
                    <el-col>
                      <el-form-item label="规则"  prop="amount">
                        <el-input v-model="area.amount" style="width: 80%;" class="myInput"></el-input>
                      </el-form-item>
                   </el-col>
                 </el-row>
                 <el-row>
                   <el-col>
                      <el-form-item label="备注"  prop="comment">
                        <el-input v-model="area.comment" style="width: 380px;" class="myInput"></el-input>
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

        <!--项目编辑-->
        <div>
          <el-dialog  title="项目信息" width="55%" :visible.sync="dialogEditVisible">
              <el-form  :model="area" ref="editForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:60px;'>
                  <el-row>
                     <el-col>
                        <el-form-item label="名称"  prop="name">
                          <el-input v-model="area.name" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="能否独立开单"  prop="isindependent">
                          <el-switch v-model="area.isindependent"></el-switch>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="是否套餐"  prop="type">
                          <el-switch v-model="area.type"></el-switch>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                      <el-col :span="12">
                        <el-form-item label="规则"  prop="amount">
                          <el-input v-model="area.amount" style="width: 70%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="备注"  prop="comment">
                          <el-input v-model="area.comment" style="width: 70%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row  v-if="area.type===true">
                     <el-button size="small" @click="project_handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
                   </el-row>
                   <el-row v-if="area.type===true">
                     <el-table
                        :data="projectChild"
                        :header-cell-style="{background:'#F8F8F8'}"
                        stripe
                      >
                        <el-table-column type="index" label="序号"  width="100">
                        </el-table-column>
                        <el-table-column prop="name" label="项目名称" width="220">
                        </el-table-column>
                        <el-table-column prop="comment" label="备注" width="100">
                        </el-table-column>
                         <el-table-column label="操作" fixed="right" align="center">
                          <template slot-scope="scope">
                              <!--<el-button type="text" size="small" @click="project_handleUpdate(scope.row)">修改</el-button>-->
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
            <el-form  :model="area" ref="childAddForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
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
                  <el-table-column prop="name"  label="项目名称" width="220">
                  </el-table-column>
                  <el-table-column prop="comment" label="备注" width="120" align="center">
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

        <!--项目禁忌症-->
        <div>
          <el-dialog  title="项目禁忌症" width="50%" :visible.sync="dialogJinjizhengVisible">
            <jinjizheng :project_id="project_id" :num="num"></jinjizheng>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { project_dicts, project_dict_childs, project_dict_individuals, createProject_dict,
  updateProject_dict, deleteProject_dict } from '@/api/system'
import jinjizheng from '@/views/system/project_jinjizheng.vue'
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
    ElCol,
    jinjizheng
  },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: '',
        sort: '+id'
      },
      num: 0,
      project_id: null,
      projectChild: [],
      projectIndividual: [],
      multipleOrder: [],
      projectid: null,
      searchname: '',
      dialogFormVisible: false,
      dialogEditVisible: false,
      dialogProjectAddVisible: false,
      dialogJinjizhengVisible: false,
      dialogStatus: '',
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      child: {
        id: null,
        name: '',
        comment: ''
      },
      area: {
        id: null,
        name: '',
        isindependent: '',
        type: '',
        amount: '',
        comment: ''
      }
    }
  },
  methods: {
    getProjectdict(data) {
      project_dicts(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getChildData(data) {
      project_dict_childs(data).then(response => {
        this.projectChild = response.data.results
      })
    },
    getIndividualData(data) {
      project_dict_individuals(data).then(response => {
        this.projectIndividual = response.data.results
      })
    },
    resetArea() {
      this.area = {
        id: null,
        name: '',
        comment: ''
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getProjectdict(this.listQuery)
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
    handleCreate() {
      this.resetArea()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.area.id = parseInt(Math.random() * 100) + 1024 // mock a id
          const tempdata = Object.assign({}, this.area) // copy obj
          if (this.area.isindependent === true) {
            tempdata.isindependent = 1
          } else {
            tempdata.isindependent = 0
          }
          if (this.area.type === true) {
            tempdata.type = 1
          } else {
            tempdata.type = 0
          }
          tempdata.action = 'Add'
          createProject_dict(tempdata).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getProjectdict(this.listQuery)
          })
        }
      })
    },
    project_handleCreate() {
      this.projectIndividual = []
      this.getIndividualData(this.listQuery)
      this.dialogProjectAddVisible = true
      this.$nextTick(() => {
        this.$refs['childAddForm'].clearValidate()
      })
    },
    project_createData() {
      if (this.multipleOrder.length > 0) {
        this.area.id = parseInt(Math.random() * 100) + 1024
        const tempdata = Object.assign({}, this.area)
        tempdata.action = 'childAdd'
        tempdata.projectdicts = this.multipleOrder
        tempdata.parentid = this.projectid
        createProject_dict(tempdata).then(() => {
          this.dialogProjectAddVisible = false
          this.$notify({
            title: '成功',
            message: '创建成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            parentid: this.projectid
          }
          this.getChildData(par)
        })
      }
    },
    handleJinjizheng(row) {
      this.num = this.num + 1
      this.project_id = row.id
      this.dialogJinjizhengVisible = true
    },
    handleUpdate(row) {
      this.area = Object.assign({}, row)
      this.projectid = row.id
      const par = {
        parentid: this.projectid
      }
      this.projectChild = []
      if (row.type === true) {
        this.getChildData(par)
      }
      this.dialogStatus = 'update'
      this.dialogEditVisible = true
      this.$nextTick(() => {
        this.$refs['editForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['editForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.area)
          updateProject_dict(tempData).then(() => {
            this.dialogEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getProjectdict(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.area = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.area)
        deleteProject_dict(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getProjectdict(this.listQuery)
        })
      })
    },
    project_handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.child = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.child)
        deleteProject_dict(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          const par = {
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
    this.getProjectdict(this.listQuery)
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
