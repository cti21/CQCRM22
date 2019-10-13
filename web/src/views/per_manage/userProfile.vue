<template>
    <div>
        <el-row>
            <el-select v-model="hrmdepartment_id" clearable style="width: 200px" class="myInput" placeholder="中心">
                <el-option v-for="item in centerSelect" :key="item.id" :value="item.id" :label="item.name">
                </el-option>
            </el-select>
            <el-input
              v-model="searchname"
              class="myInput"
              style="width: 220px;margin-right: 20px"
              clearable
              @keyup.enter.native="handleFilter"
              suffix-icon="el-icon-search"
              placeholder="请输入姓名或电话">
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
            <el-table-column type="index" label="序号"  width="60">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="120">
            </el-table-column>
            <el-table-column prop="sex" label="性别" width="60">
            </el-table-column>
            <el-table-column prop="birthDate" label="出生日期" width="120">
            </el-table-column>
            <el-table-column prop="profession" label="职称" width="90">
            </el-table-column>
            <el-table-column prop="education" label="学历" width="90">
            </el-table-column>
            <el-table-column prop="type" label="员工类别" width="120">
            </el-table-column>
            <el-table-column prop="phone1" label="手机" width="120">
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
                  <el-form  :model="employee" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="employee.name" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="性别"  prop="sex">
                              <el-select v-model="employee.sex" clearable style="width: 80%" class="myInput">
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
                                v-model="employee.birthDate"
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
                              <el-select v-model="employee.profession" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in professionSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="学历"  prop="education">
                              <el-select v-model="employee.education" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in educationSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="职工类型"  prop="type">
                              <el-select v-model="employee.type" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in typeSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="电话1"  prop="phone1">
                              <el-input v-model="employee.phone1" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="电话2"  prop="phone2">
                              <el-input v-model="employee.phone2" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="入职日期"  prop="hiredate">
                              <el-date-picker
                                v-model="employee.hiredate"
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
                              <el-select v-model="employee.state" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in stateSelect" :key="item.id" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                        <!--<el-row>-->
                         <!--<el-col :span="12">-->
                            <!--<el-form-item label="账号"  prop="username">-->
                              <!--<el-input v-model="employee.username" style="width: 80%;" class="myInput"></el-input>-->
                            <!--</el-form-item>-->
                         <!--</el-col>-->
                         <!--<el-col :span="12">-->
                            <!--<el-form-item label="部门"  prop="hrmdepartment">-->
                              <!--<el-select v-model="employee.hrmdepartment" clearable style="width: 80%" class="myInput">-->
                                <!--<el-option v-for="item in typeSelect" :key="item.id" :value="item.id" :label="item.name">-->
                                <!--</el-option>-->
                              <!--</el-select>-->
                            <!--</el-form-item>-->
                         <!--</el-col>-->
                       <!--</el-row>-->
                       <el-row>
                         <el-col>
                            <el-form-item label="备注"  prop="comment">
                              <el-input v-model="employee.comment" style="width: 90%;" class="myInput"></el-input>
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
import { users, createUser, updateUser, deleteUser } from '@/api/employee'
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
        sort: '+id'
      },
      searchname: '',
      hrmdepartment_id: 2,
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      sexSelect: [
        { id: 1, name: '男' },
        { id: 2, name: '女' }
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
      centerSelect: [
        { id: 2, name: '綦江中心' },
        { id: 3, name: '永川中心' }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }]
      },
      employee: {
        id: null,
        user: 10,
        name: '',
        sex: '',
        birthDate: null,
        profession: '',
        education: '',
        type: '',
        phone1: '',
        phone2: '',
        hiredate: null,
        state: '',
        hrmdepartment: null,
        username: '',
        comment: ''
      }
    }
  },
  methods: {
    getUsers(data) {
      users(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetUser() {
      this.employee = {
        id: null,
        user: 1,
        name: '',
        sex: '',
        birthDate: null,
        profession: '',
        education: '',
        type: '',
        phone1: '',
        phone2: '',
        hiredate: null,
        state: '',
        hrmdepartment: null,
        username: '',
        comment: ''
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getUsers(this.listQuery)
    },
    handleCreate() {
      this.resetUser()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.employee.id = parseInt(Math.random() * 100) + 1024
          this.employee.username = '111'
          this.employee.hrmdepartment = this.hrmdepartment_id
          createUser(this.employee).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getUsers(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.employee = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.employee)
          updateUser(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getUsers(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.employee = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.employee)
        deleteUser(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getUsers(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getUsers(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getUsers(this.listQuery)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.listQuery.hrmdepartment_id = 2
    this.getUsers(this.listQuery)
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
