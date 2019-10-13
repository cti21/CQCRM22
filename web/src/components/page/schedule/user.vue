<template>
  <div>
    <div>
      <el-select
        v-model="value4"
        clearable
        style="width: 150px"
        class="myInput"
        placeholder="请选择部门"
        @change="getUserFromDept($event)" >
          <el-option
            v-for="item in options"
            :key="item.id"
            :label="item.name"
            :value="item.id">
          </el-option>
      </el-select>
      <el-input
        @keyup.enter.native="handleFilter"
        style="width: 200px;margin-left: 20px;margin-right: 30px;"
        class="myInput"
        placeholder="姓名"
        v-model="searchname">
      </el-input>
      <el-button  size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
      <el-button  size="small" type="primary" @click="handleAdd"  icon="el-icon-plus">新增</el-button>
    </div>

    <el-table
      :data="tableData"
      :header-cell-style="{background:'#F8F8F8'}"
      :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
      stripe
      style="width: 90%;margin-top: 20px">
    <el-table-column
      type="index"
      label="序号"
      width="100"
      align="center"
    >
    </el-table-column>
    <el-table-column
      prop="id"
      label="用户id"
      v-if = false
      width="150">
    </el-table-column>
    <el-table-column
      prop="first_name"
      label="姓名"
      width="200"
      align="center"
    >
    </el-table-column>
    <el-table-column
      prop="username"
      label="用户名"
      width="300"
      align="center"
    >
    </el-table-column>
      <el-table-column
      prop="deptname"
      label="部门"
      width="200"
      align="center"
    >
    </el-table-column>
    <el-table-column
      prop="deptid"
      label="部门id"
      width="100"
      align="center"
      v-if = false
    >
    </el-table-column>
    <el-table-column label="操作" align="center">
      <template slot-scope="scope">
        <el-button @click="handleEdit(scope.row)" type="text" size="small">编辑</el-button>
        <el-button @click="handleDelete(scope.row)" type="text" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>

    <div class="pagination-container" style="margin-top: 10px;" align="right">
      <el-pagination background
                     @current-change="handleCurrentChange"
                     :current-page="filters.page"
                     :page-sizes="[15,30,45,60, 75]"
                     :page-size="filters.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
      </el-pagination>
    </div>
    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" style="width: 90%">
      <el-form
        :model="editForm"
        label-width="100px"
        :rules="editFormRules"
        ref="editForm">
        <el-form-item label="姓名" prop="first_name">
          <el-input
            v-model="editForm.first_name"
            class="myInput"
            style="width: 90%"
            auto-complete="off">
          </el-input>
        </el-form-item>
        <el-form-item label="部门" prop="deptid">
         <el-select class="myInput" v-model="editForm.deptid" placeholder="请选择"  >
            <el-option
              v-for="item in options"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>
       </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button
          size="small"
          type="primary"
           icon="el-icon-check"
          @click.native="editSubmit"
          :loading="editLoading">确定
        </el-button>
        <el-button
          size="small"
          icon="el-icon-close"
          @click.native="editFormVisible = false"
        >关闭
        </el-button>
      </div>
    </el-dialog>
  <!--新增界面-->
    <el-dialog title="新增用户" :visible.sync="addFormVisible" width="40%" >
      <el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm" style='width:90%;margin-left:10px;'>
        <el-form-item label="用户" prop="username">
          <el-input v-model="addForm.username" auto-complete="off" class="myInput" style="width: 90%;margin-left: 30px;">
          </el-input>
        </el-form-item>
        <el-form-item label="姓名" prop="first_name">
          <el-input v-model="addForm.first_name" auto-complete="off" class="myInput" style="width: 90%;margin-left: 30px;"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input type="password"
                    v-model="addForm.password"
                    auto-complete="off"
                    class="myInput"
                    style="width: 90%;margin-left: 30px;">
          </el-input>
        </el-form-item>
        <el-form-item  label="确认密码" prop="checkPass">
          <el-input type="password"
                    v-model="addForm.checkPass"
                    auto-complete="off"
                    class="myInput"
                    style="width: 90%;margin-left: 30px;">
          </el-input>
        </el-form-item>
        <el-form-item label="部门" prop="first_name">
          <el-select v-model="addForm.deptid" class="myInput" placeholder="请选择" style="margin-left: 30px;">
            <el-option
              v-for="item in options"
              :key="item.id"
              :label="item.name"
              :value="item.id">
            </el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button
          size="small"
          icon="el-icon-close"
          @click.native="addFormVisible = false"
        >关闭
        </el-button>
        <el-button
          size="small"
          type="primary"
          icon="el-icon-check"
          @click.native="addSubmit"
          :loading="addLoading"
        >提交
        </el-button>
      </div>
    </el-dialog>


  </div>
</template>

<script>
 import { mapGetters, mapMutations } from 'vuex'
 import { getUserList, addUser, updateUser, deleteUser, getDeptNameList } from './department.js'

 export default {
   data() {
     const validatePass = (rule, value, callback) => {
       if (value === '') {
         callback(new Error('请输入密码'))
       } else {
         if (value.length < 6) {
           callback(new Error('密码长度不能小于6位'))
         } else {
           if (!isNaN(value)) {
             callback(new Error('密码不能全为数字'))
           } else {
             if (this.addForm.checkPass !== '') {
               this.$refs.addForm.validateField('checkPass')
             }
           }
         }
         callback()
       }
     }
     const validatePass2 = (rule, value, callback) => {
       if (value === '') {
         callback(new Error('请再次输入密码'))
       } else if (value !== this.addForm.password) {
         callback(new Error('两次输入密码不一致!'))
       } else {
         callback()
       }
     }
     return {
       value4: '全部',
       options: [],
       filters: {
         first_name: '',
         page: 1,
         limit: 5
       },
       addFormVisible: false, // 新增界面是否显示
       dialogStatus: '',
       tableData: [],
       total: 0,
       addLoading: false,
       searchname: null,

       editFormVisible: false, // 编辑界面是否显示
       editLoading: false,
       editFormRules: {
         name: [
           { required: true, message: '请输入姓名', trigger: 'blur' }
         ]
       },
       // 编辑界面数据
       editForm: {
         first_name: '',
         deptid: ''
       },
       // 新增界面数据
       addForm: {
         id: null,
         username: '',
         first_name: '',
         password: '',
         checkPass: '',
         deptid: ''
       },
       addFormRules: {
         username: [
           { required: true, message: '请输入姓名', trigger: 'blur' }
         ],
         password: [
           { validator: validatePass, trigger: 'blur' }
         ],
         checkPass: [
           { validator: validatePass2, trigger: 'blur' }
         ]
       },
       listQuery: {
         page: 1,
         limit: 5,
         offset: 0,
         first_name: undefined,
         deptid: null,
         sort: '+id'
       }
     }
   },
   methods: {
     getUserFromDept(val) {
       this.listQuery.page = 1
       this.listQuery.deptid = val
       this.dept = val
       getUserList(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
         this.filters.page = 1
       })
     },
     resetUser() {
       this.addForm = {
         id: null,
         username: '',
         first_name: '',
         password: '',
         checkPass: '',
         deptid: ''
       }
     },
     // 点击删除按钮
     handleDelete(row) {
       this.$confirm('确认删除该记录吗?', '提示', {
         type: 'warning'
       }).then(() => {
         const data = {'id': row.id}
         deleteUser(data).then(response => {
           this.tableData = response.data.results
           this.total = response.data.count
           this.filters.page = 1
         }).catch(error => {
           console.log(error)
         })
       })
     },
     // 点击编辑按钮
     handleEdit(row) {
       this.listQuery.page = 1
       this.editForm = Object.assign({}, row)
       this.editFormVisible = true
     },
     // 点击新增按钮
     handleAdd() {
       this.resetUser()
       this.dialogStatus = 'create'
       this.addFormVisible = true
       this.$nextTick(() => {
         this.$refs['addForm'].clearValidate()
       })
     },
     // 新增对话框内点击确定
     addSubmit() {
       this.$refs.addForm.validate((valid) => {
         if (valid) {
           this.addForm.id = parseInt(Math.random() * 100) + 1024 // mock a id
           // this.addForm.password = '123qweasd'
           addUser(this.addForm).then(response => {
             this.tableData = response.data.results
             this.total = response.data.count
             this.addFormVisible = false
             this.$notify({
               title: '成功',
               message: '创建成功',
               type: 'success',
               duration: 2000
             })
             this.filters.page = 1
           }).catch(error => {
             console.log(error)
           })
         }
       })
     },
     // 编辑对话框内点击确定
     editSubmit(){
       updateUser(this.editForm).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
         this.editFormVisible = false
         this.$notify({
           title: '成功',
           message: '创建成功',
           type: 'success',
           duration: 2000
         })
         this.filters.page = 1
       }).catch(error => {
         console.log(error)
       })
     },
     // 点击页码
     handleCurrentChange(val) {
       this.listQuery.page = val
       this.listQuery.deptid = this.dept
       getUserList(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
       }).catch(error => {
         console.log(error)
       })
     },
     handleFilter() {
       this.listQuery.page = 1
       this.listQuery.first_name = this.searchname
       getUserList(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
       }).catch(error => {
         console.log(error)
       })
     },
     ...mapMutations([
       'panban_patient'
     ])
   },
   created() {
     this.listQuery.page = 1
     getUserList(this.listQuery).then(response => {
       this.tableData = response.data.results
       this.total = response.data.count
       getDeptNameList(this.listQuery).then(response => {
         this.options = response.data
       })
     })
   },
   computed: mapGetters([
     'odddual_week',
   ]),
   components: {
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
    padding:8px 0;
  }
  .el-table__header td,.el-table__header th{
    padding:8px 0px;
  }
</style>
