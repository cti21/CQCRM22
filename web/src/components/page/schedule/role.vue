
<template>
  <div>
    <el-col :span="24" class="toolbar" style="margin-bottom: 10px;">
      <el-button
        size="small"
        icon="el-icon-plus"
        type="primary"
        @click="handleAdd"
      >新增
      </el-button>
    </el-col>

    <el-table
      :data="tableData"
      :header-cell-style="{background:'#F8F8F8'}"
      :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
      stripe
      style="width: 100%;margin-top: 20px" >
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
      v-if = false
      width="150">
    </el-table-column>

    <el-table-column
      prop="name"
      label="角色名称"
      align="center"
      >
    </el-table-column>

    <el-table-column
      label="操作"
      align="center"
    >
      <template slot-scope="scope">
       <el-button type="text" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
       <el-button type="text" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
       <el-button type="text" size="small" @click="handlePermission(scope.$index, scope.row)">权限</el-button>
      </template>
    </el-table-column>
  </el-table>
    <div class="pagination-container" style="margin:10px;" align="right">
      <el-pagination background
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-sizes="[15,30,45,60, 75]"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
      </el-pagination>
   </div>

    <!--编辑角色界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible" :close-on-click-modal="false" width="40%">
      <el-form :model="editForm" label-width="100px" :rules="editFormRules" ref="editForm">
        <el-form-item label="角色名称" prop="name">
          <el-input
            v-model="editForm.name"
            style="width: 90%"
            class="myInput"
            auto-complete="off">
          </el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button
          size="small"
          icon="el-icon-close"
          @click.native="editFormVisible = false"
        >关闭
        </el-button>
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
  <!--新增角色界面-->
    <el-dialog title="新增" :visible.sync="addFormVisible"  :close-on-click-modal="false" width="40%">
      <el-form :model="addForm" label-width="80px" :rules="addFormRules" ref="addForm">
        <el-form-item label="角色名称" prop="name">
          <el-input v-model="addForm.name" auto-complete="off" class="myInput" style="width: 90%">
          </el-input>
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

   <!-- 给角色配置菜单权限界面 -->
    <!--@check-change="handleRoleTreeCheckChange"-->
     <el-dialog
       custom-class="permissonclass"
       title="配置权限"
       :visible.sync="configPermission"
       :close-on-click-modal="false"
       @close='closeDialog' >
      <div  style="margin-top:10px;margin-bottom: 20px;">
      <!-- 左侧角色树 -->
        <div style="float: left;margin-left:60px;margin-bottom:20px;">
            <span>角色</span>
            <el-tree
              :data="role_permission_data"
              show-checkbox
              node-key="id"
              default-expand-all
              :expand-on-click-node="false"
              :check-strictly="true"
              @check="handleRoleTreeNodeClick"
              ref="roletree"
              :default-checked-keys = "checkedkeys" >
              <span class="custom-tree-node" slot-scope="{ node, data }">
              <span>{{ node.label }}</span>
              </span>
            </el-tree>
        </div>
        <!--:default-checked-keys = "menucheck"-->
        <!--  右侧菜单树 -->
        <div style="margin-left:300px;margin-bottom:20px" >
            <span>菜单</span>
            <el-tree :data="menu_permission_data2"
                     show-checkbox
                     node-key="id"
                     @check="handleMenuTreeNodeClick"
                     :default-checked-keys = "menucheck"
                     ref="menutree" >
            </el-tree>
        </div>
      </div>
     </el-dialog>
  </div>
</template>

<script>
 import { getRoleList, deleteRole, addRole, updateRole,
   getRoleMenuList, setRoleMenu, GetRoleMenu } from './department.js'

 export default {

   data(){
     return {

       filters: {
         name: ''
       },
       addFormVisible: false,// 新增界面是否显示
       tableData: [],
       roleData: [],

       total: 0,
       checkedkeys: [],
       addLoading: false,
       editLoading: false,
       configPermission: false, // 配置界面是否显示
       editFormVisible: false, // 编辑界面是否显示
       editFormRules: {
         name: [
           { required: true, message: '请输入角色名称', trigger: 'blur' }
         ]
       },
       // 编辑界面数据
       editForm: {
         name: '',
         id: 0
       },
       // 新增界面数据
       addForm: {
         name: ''
       },
       addFormRules: {
         name: [
           { required: true, message: '请输入角色名称', trigger: 'blur' }
         ]
       },
       listQuery: {
         page: 1,
         limit: 5,
         offset: 0,
         name: undefined,
         sort: '+id'
       },
       role_permission_data: [],
       menu_permission_data: [],
       menu_permission_data2: [],
       menutreedata: {
         '医疗管理': {'id': 1,'self': false,'add': true,'update': false,'delete': false,'browser': false},
         '预约签到': {'id': 2,'self': false,'add': true,'update': false,'delete': false,'browser': false}
       },
       rolecheck: [],
       menucheck: []
     }
   },
   methods: {
     buildMenuTree: function(rd) {
       this.menucheck = []
       this.menu_permission_data2 = []

       for (const item in rd) {
         let exist = 0
         for (const menuitem in this.menu_permission_data2) {
           if (this.menu_permission_data2[menuitem]['id'] === rd[item].groupmenu.menu_id) {
             const childmenu = {}
             childmenu['id'] = rd[item].child_menu_id
             childmenu['label'] = rd[item].title
             childmenu['isvisible'] = rd[item].isvisible
             childmenu['url'] = rd[item].path
             childmenu['menu_id'] = rd[item].groupmenu.menu_id
             this.menu_permission_data2[menuitem]['children'].push(childmenu)
             if (rd[item].isvisible === true) {
               this.menucheck.push(rd[item].child_menu_id)
             }
             exist = 1
             break
           }
         }
         if (exist === 0) {
           const m = {}
           m['id'] = rd[item].groupmenu.menu_id
           m['label'] = rd[item].groupmenu.label
           m['url'] = rd[item].groupmenu.path
           m['children'] = []

           const childmenu = {}
           childmenu['id'] = rd[item].child_menu_id
           childmenu['label'] = rd[item].title
           childmenu['isvisible'] = rd[item].isvisible
           childmenu['url'] = rd[item].path
           childmenu['menu_id'] = rd[item].groupmenu.menu_id
           m['children'].push(childmenu)
           this.menu_permission_data2.push(m)

           if (childmenu['isvisible'] === true) {
             this.menucheck.push(childmenu['id'])
           }
         }
       }
       console.log('menu_permission_data2', this.menu_permission_data2)
     },
     closeDialog() {
     // let role = this.role_permission_data
     //         Object.keys(role).forEach((key)=> {
     //            this.$refs.roletree.setChecked(role[key]['id'],false)
     //         })
     //
     // let menu = this.menu_permission_data2
     //         Object.keys(menu).forEach((key)=> {
     //            this.$refs.menutree.setChecked(menu[key]['id'],false)
     //         })
     },
     // obj 是否存在于arr中
     contains(arr, obj) {
       var i = arr.length
       while (i--) {
         if (arr[i] === obj) {
           return true
         }
       }
       return false
     },
     //  点击右侧菜单节点
     handleMenuTreeNodeClick(item,node) {
       let menusid = []
       let keylist = node.checkedKeys
       let checkstate = this.contains(keylist, item.id)
       let parentid
       let selectRoleNode
       let para, node2

       // 当前角色选中节点列表
       selectRoleNode = this.$refs.roletree.getCheckedKeys()[0]
       if (selectRoleNode === undefined) {
         this.$refs.menutree.setCheckedKeys([])
         return
       }
       // 二级菜单
       if (item.id >= 2000) { // 二级菜单
         // 当前选中节点的父节点id
         parentid = this.$refs.menutree.getNode(item.id).parent.key
         node2 = {
           'parentid': parentid,
           'menuid': [item.id]
         }
         // menusid.push(node)
         selectRoleNode = this.$refs.roletree.getCheckedKeys()[0]
         para = {
           roleid: selectRoleNode,
           menuid: node2,
           perm: checkstate
         }
         setRoleMenu(para).then((res) => {
           console.log("ok")
         })
       } else {
         //  item.id < 2000 一级菜单 ,parentid = 节点自己的id
         node2 = {'parentid': item.id,'menuid': null}
         selectRoleNode = this.$refs.roletree.getCheckedKeys()[0]
         para = { roleid: selectRoleNode, menuid: node2, perm: checkstate}
         setRoleMenu(para).then((res) => {
         })
       }
     },
     // roletree 单选角色树 ，对应显示菜单权限在右侧 menutree
     handleRoleTreeNodeClick(a, b) {
       // 清空菜单节点
       this.$refs.menutree.setCheckedKeys([])
       if (b.checkedKeys.length > 0) {
         this.$refs.roletree.setCheckedKeys([ a.id ])
         // 向后台请求当前角色的菜单选项
         const para = { id: a.id }
         GetRoleMenu(para).then((response) => {
           this.menucheck = []
           this.buildMenuTree(response.data.results.m)
           // this.$refs.menutree.setCheckedKeys(this.menucheck)
         })
       }
     },

     // 新增提交
     addSubmit: function() {
       this.$refs.addForm.validate((valid) => {
         if (valid) {
           this.addLoading = true
           this.addFormVisible = false
           const para = Object.assign({}, this.addForm)
           addRole(para).then((res) => {
             this.addLoading = false
             this.$notify({
               title: '成功',
               message: '提交成功',
               type: 'success',
               duration: 2000
             })
             console.log('addrole', para)
             this.listQuery.page = 1
             this.listQuery.name = undefined
             getRoleList(this.listQuery).then(response => {
               this.tableData = response.data.results
               this.total = response.data.count })
           })
         }
       })
     },
     // 编辑提交
     editSubmit: function () {
       this.$refs.editForm.validate((valid) => {
         if (valid) {
           this.editFormVisible = false
           this.addLoading = true
           let para = Object.assign({}, this.editForm)
           updateRole(para).then((res) => {
             this.addLoading = false
             this.listQuery.page = 1
             this.listQuery.name = undefined
             getRoleList(this.listQuery).then(response => {
               this.tableData = response.data.results
               this.total = response.data.count })
           })
         }
       })
     },
     // 删除
     handleDel(index, row) {
       this.$confirm('确认删除该记录吗?', '提示', {
         type: 'warning'
       }).then(() => {
         this.listLoading = true
         const para = { id: row.id }
         deleteRole(para).then((res) => {
           this.listLoading = false
           this.listQuery.page = 1
           getRoleList(this.listQuery).then(response => {
             this.tableData = response.data.results
             this.total = response.data.count
           })
         })
       }).catch(() => {
         console.log('error')
       })
     },
     // 显示编辑界面
     handleEdit: function (index, row) {
       this.editFormVisible = true
       this.editForm = Object.assign({}, row)
     },
     // 显示新增界面
     handleAdd: function () {
       this.addFormVisible = true;
       this.addForm = {
         name: ''
       }
     },
     // 显示角色权限分配界面(左侧角色树，右侧菜单树)
     handlePermission(index, row) {
       this.checkedkeys = []
       this.checkedkeys.push(row.id)
       const par = {
         page: 1
       }
       getRoleMenuList(par).then(response => {
         // 根据返回的角色数据构造左侧角色树
         let rolestr = JSON.stringify(response.data.results.r)
         rolestr = rolestr.replace(/name/g, 'label')
         this.role_permission_data = JSON.parse(rolestr)
         this.buildMenuTree(response.data.results.m)
         this.configPermission = true
       })
       // 清空菜单树
       const para = { id: row.id }
       GetRoleMenu(para).then((response) => {
         this.buildMenuTree(response.data.results.m)
       })
     },
     // 点击页码
     handleCurrentChange(val) {
       this.listQuery.page = val
       this.listQuery.page = val
       this.listQuery.offset = (val - 1) * this.listQuery.limit
       getRoleList(this.listQuery).then(response => {
         this.tableData = response.data.results
         this.total = response.data.count
       }).catch(error => {
         alert(error)
         console.log(error)
       })
     }
   },
   created() {
     this.listQuery.page = 1
     getRoleList(this.listQuery).then(response => {
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
  .permissonclass {
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
