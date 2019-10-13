<template>
  <div>
    <el-col :span="24" class="toolbar" style="margin-bottom: 10px;">
      <el-button
        size="small"
        type="primary"
        icon="el-icon-plus"
        @click="handleAdd"
      >新增</el-button>
    </el-col>

    <el-table
      :data="tableData"
      :header-cell-style="{background:'#F8F8F8'}"
      :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
      stripe style="width: 100%">
      <el-table-column
        type="index"
        label="序号"
        width="150"
        align="center"
      >
      </el-table-column>

      <el-table-column
        prop="id"
        label="用户id"
        align="center"
        v-if = false
        width="150">
      </el-table-column>

      <el-table-column
        prop="name"
        label="部门名称"
        align="center"
        >
      </el-table-column>

      <el-table-column
        label="操作"
        align="center"
      >
        <template slot-scope="scope">
           <el-button size="small" type="text" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
           <el-button size="small" type="text" @click="handleDel(scope.$index, scope.row)">删除</el-button>
           <el-button size="small" type="text" @click="handleRole(scope.row, scope.row)">角色</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination-container" style="margin-top: 10px" align="right">
      <el-pagination background
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-sizes="[15,30,45,60, 75]"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
      </el-pagination>
    </div>

    <!--编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false" width="40%">
      <el-form :model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
        <el-form-item label="部门名称" prop="name">
          <el-input v-model="editForm.name" auto-complete="off" class="myInput" style="width: 90%">
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="small" @click.native="editFormVisible = false" icon="el-icon-close">关闭</el-button>
        <el-button
          size="small"
          type="primary"
          icon="el-icon-check"
          @click.native="editSubmit"
          :loading="editLoading"
        >提交
        </el-button>
      </div>
    </el-dialog>

  <!--新增界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible"  :close-on-click-modal="false" width="40%" >
      <el-form :model="department" label-width="80px" :rules="addFormRules" ref="addForm">
        <el-form-item label="部门名称" prop="name">
          <el-input v-model="department.name" auto-complete="off" class="myInput" style="width: 90%">
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="small" type="primary" @click="addSubmit" icon="el-icon-check">确定</el-button>
        <el-button size="small" @click.native="addFormVisible = false" icon="el-icon-close">关闭</el-button>
      </div>
    </el-dialog>

   <!--为部门分配角色，目前每部门只能分配一个角色，分配多角色时，如果各角色有相同的菜单
   子菜单只需保留一个， 有时间再加-->
  <el-dialog custom-class="permclass" title="分配角色" :visible.sync="roleFormVisible"  :close-on-click-modal="false" >
    <MyComponent :dept_id="dept_id">
    </MyComponent>
  </el-dialog>

  </div>
</template>

<script>
 import { getDeptList, deleteDept, addDept, updateDept, getDepRoletList, GetDeptRole } from './department.js'
 import MyComponent from './child.vue'
 export default {
   components: {
     MyComponent
   },
   data() {
     return {
       deptdata: [],
       dept_id: null,
       filters: {
         name: ''
       },
       addFormVisible: false, // 新增界面是否显示
       tableData: [],
       total: 0,
       roledata: [],
       checkroledata: [], // 部门角色页面默认选项
       checkdeptdata: [], // 部门角色页面默认选项
       deptgroupcount: 0,
       addLoading: false,

       editFormVisible: false, // 编辑界面是否显示
       editLoading: false,
       roleFormVisible: false,
       editFormRules: {
         name: [
           { required: true, message: '请输入部门名称', trigger: 'blur' }
         ]
       },
       // 编辑界面数据
       editForm: {
         name: ''
       },
       // 新增界面数据
       department: {
         name: ''
       },
       addFormRules: {
         name: [
           { required: true, message: '请输入部门名称', trigger: 'blur' }
         ]
       },
       show222: false,
       listQuery: {
         page: 1,
         limit: 100,
         offset: 0,
         name: '',
         sort: '+id'
       }
     }
   },
   methods: {
     addSubmit: function() {
       this.$refs['addForm'].validate((valid) => {
         if (valid) {
           const para = Object.assign({}, this.department)
           console.log(this.department)
           addDept(para).then((res) => {
             this.addFormVisible = false
             this.listQuery.page = 1
             getDeptList(this.listQuery).then(response => {
               this.tableData = response.data.results
               this.total = response.data.count
             })
           })
         }
       })
     },
     editSubmit: function() {
       this.$refs.editForm.validate((valid) => {
         if (valid) {
           // this.$confirm('确认提交吗？', '提示', {}).then(() => {
           this.addLoading = true;
           const para = Object.assign({}, this.editForm);
           updateDept(para).then((res) => {
             this.addLoading = false;
             this.editFormVisible = false;
             this.listQuery.page = 1
             this.listQuery.name = undefined
             getDeptList(this.listQuery).then(response => {
               this.tableData = response.data.results
               this.total = response.data.count })
           })
         }
       })
     },
     // 删除
     handleDel: function(index, row) {
       this.$confirm('确认删除该记录吗?', '提示', {
         type: 'warning'
       }).then(() => {
         this.listLoading = true;
         const para = { id: row.id };
         deleteDept(para).then((res) => {
           this.listLoading = false;
           this.listQuery.page = 1
           getDeptList(this.listQuery).then(response => {
             this.tableData = response.data.results
             this.total = response.data.count })
         })
       }).catch(() => {
       })
     },
     // 显示编辑界面
     handleEdit: function(index, row) {
       this.editFormVisible = true
       this.editForm = Object.assign({}, row)
     },
     // 显示给部门分配角色界面
     handleRole: function(index, row) {
       this.dept_id = row.id
       this.roleFormVisible = true
     },
     // 显示新增界面
     handleAdd: function() {
       this.addFormVisible = true
       this.addForm = {
         name: ''
       }
     },
     // 点击页码
     handleCurrentChange(val) {
       this.listQuery.page = val
       getDeptList(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
       }).catch(error => {
         console.log(error)
       })
     }
   },
   created() {
     this.listQuery.page = 1
     getDeptList(this.listQuery).then(response => {
       this.tableData = response.data.results
       this.total = response.data.count
     })
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
  .permclass {
      height: 400px;
      width: 700px;
  }
  .el-table td, .el-table th{
    padding:8px 0;
  }
  .el-table__header td,.el-table__header th{
    padding:8px 0px;
  }
</style>
