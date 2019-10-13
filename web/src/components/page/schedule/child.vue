
<template>
  <div>
   {{rolecheck}}
   <!--</br></br></br></br>-->
     <div  style="margin-top:10px">
      <!-- 左侧部门树 -->
         <!-- @check-change="handleDeptTreeCheckChange" -->
        <div class="block" style="float: left;margin-left:60px ;">
            <span>部门</span>
            <el-tree
              :data= "deptdata"
              show-checkbox
              node-key="id"
              default-expand-all
              :expand-on-click-node="false"
              :check-strictly="true"
              @check="handleDeptTreeNodeClick"
              ref="depttree"
              :default-checked-keys = "deptcheck"
            >
            </el-tree>
        </div>
    <!-- @check="handleMenuTreeNodeClick" -->
       <!--@node-click="handleRoleTreeNodeClick"-->
       <!--@check-change="handleRoleTreeCheckChange"-->
<!--  右侧角色树 -->
      <div class="block" style="margin-left:400px ;" >
        <span>角色</span>
        <el-tree :data="roledata"
                 show-checkbox
                 node-key="id"
                 default-expand-all
                 :expand-on-click-node="false"
                 :check-strictly="true"
                 @check="handleRoleTreeNodeClick"
                 ref="roletree"
                 :default-checked-keys = "rolecheck" >
        </el-tree>
      </div>
      </div>

  </div>
</template>

<script>
  import { setDeptRole, GetDeptRole, getDepRoletList } from './department.js'
export default {
    props: ['dept_id'],
    // props: ['deptdata', 'roledata', 'deptcheck', 'rolecheck', 'dept_id'],
    data() {
      return {
        deptdata: null,
        roledata: null,
        deptcheck: [],
        rolecheck: [],
        roleData: [],
        role_permission_data: [],
        menu_permission_data: [],
      }
    },
    methods: {
      // obj 是否存在于arr中
      contains(arr, obj) {
        let i = arr.length
        while (i--) {
          if (arr[i] === obj) {
            return true
          }
        }
        return false
      },
      // 显示给部门分配角色界面
      getDeptAndRole(data) {
        getDepRoletList(data).then(response => {
          // 根据返回的部门数据构造左侧角色树
          this.deptcheck = []
          this.deptcheck.push(this.dept_id)
          let deptstr = JSON.stringify(response.data.results.d)
          deptstr = deptstr.replace(/name/g, 'label')
          this.deptdata = JSON.parse(deptstr)
          //  根据返回的角色数据构造右侧角色树
          this.roledata = JSON.stringify(response.data.results.g)
          this.roledata = this.roledata.replace(/name/g, 'label')
          this.roledata = JSON.parse(this.roledata)
          // 向后台请求当前部门的角色选项
          const para = {
            id: this.dept_id
          }
          this.$nextTick(function() {
            GetDeptRole(para).then((response) => {
              this.rolecheck = []
              this.rolecheck.push(response.data.results.r.group_id)
              this.$refs.roletree.setCheckedKeys(this.rolecheck)
            })
          })
        })
      },
      handleDeptTreeNodeClick(a,b) {
        // 清空角色节点
        this.$refs.roletree.setCheckedKeys([])

        if (b.checkedKeys.length > 0) {
          this.$refs.depttree.setCheckedKeys([a.id])
          // 向后台请求当前部门的角色选项
          const para = {
            id: a.id
          }
          GetDeptRole(para).then((response) => {
            if (response.data.results.r.group_id !== undefined) {
              this.$refs.roletree.setCheckedKeys([response.data.results.r.group_id])
            }
          })
        }
      },
      handleRoleTreeNodeClick(a,b) {
        if (b.checkedKeys.length > 0) {
          this.$refs.roletree.setCheckedKeys([a.id]);

          // 当前部门选中节点列表
          const selectDeptNode = this.$refs.depttree.getCheckedKeys()[0]
          if (selectDeptNode === undefined) {
            if (b.checkedKeys.length > 0) {
              this.$refs.roletree.setCheckedKeys([])
              return
            }
          }
          const para = {
            deptid: selectDeptNode,
            roleid: a.id,
            action: 'add'
          }
          setDeptRole(para).then((res) => {
          })
        }
      }
    },
    watch: {
      dept_id: function() {
        this.getDeptAndRole('')
      }
    },
    created() {
      this.getDeptAndRole('')
    }

  }
</script>
