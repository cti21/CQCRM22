<template>
<div>
	 <el-col :span="24" class="toolbar" style="padding-bottom: 0px;">
     <el-button size="mini" type="primary" @click="addSubmit">新增部门</el-button>
     </el-col>
<!--     <el-dialog title="编辑" :close-on-click-modal="false" :visible.sync="editFormVisible">
	<MyComponent></MyComponent>
    dddddddddddddddddddddddddddd
</el-dialog> -->

 <el-dialog title="分配角色" :visible.sync="editFormVisible"  :close-on-click-modal="false" >
     <MyComponent> :deptdata=deptgroupdata </MyComponent>
  </el-dialog>
</div>
</template>

<script>
 import api from './api.js'
 import Vue from 'vue'
 import {mapGetters,mapMutations} from 'vuex'
 import { getDeptList ,deleteDept,addDept,updateDept,getDept } from './department.js'
import MyComponent from "./child.vue";
export default {
  components: {MyComponent}, // 直接初始化就可以啦，不需要Vue.use();
  data() {
  	return {editFormVisible :false}},
  methods: {

   addSubmit: function ()
   {
   	   this.editFormVisible = true;
   }

  }
};
</script>
