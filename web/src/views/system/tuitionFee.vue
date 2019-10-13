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
          <div class="pagination-container" style="margin-top: 5px" align="right">
            <el-pagination background
                           @current-change="handleCurrentChange"
                           :current-page="listQuery.page"
                           :page-size="listQuery.limit"
                           layout="total, prev, pager, next"
                           :total="total">
            </el-pagination>
          </div>
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            @row-click="rowClick_tuitionfee"
            highlightCurrentRow
            stripe
          >
            <el-table-column type="index" label="序号"  width="100">
            </el-table-column>
            <el-table-column prop="deptname" label="名称" width="140">
            </el-table-column>
            <el-table-column prop="tuitionname" label="类型" width="120">
            </el-table-column>
            <el-table-column prop="value" label="数值" width="120">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="180">
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
        </el-row>

        <el-row style="margin:20px;">
          <el-button size="small" style="float: left" @click="detail_handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
          <el-table
            :data="detail_list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
          >
            <el-table-column type="index" label="序号"  width="100">
            </el-table-column>
            <el-table-column prop="projectname" label="项目名称" width="140">
            </el-table-column>
            <el-table-column prop="tuitionname" label="类型" width="120">
            </el-table-column>
            <el-table-column prop="value" label="数值" width="120">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="180">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="detail_handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="detail_handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-row>

        <!--带教费新增-->
        <div>
          <el-dialog  title="选择科室" width="40%" :visible.sync="dialogAddVisible">
            <el-form  :model="area" ref="addForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
                 <el-row>
                   <el-table
                    :data="deptList"
                    ref="multipleTable"
                    :header-cell-style="{background:'#F8F8F8'}"
                    stripe
                    highlight-current-row
                    @selection-change="orderSelectChange"
                    @row-click="rowClick">
                    <el-table-column type="selection" width="80" class="selection" align="center">
                    </el-table-column>
                    <el-table-column prop="deptname"  label="科室名称" width="180" align="center">
                    </el-table-column>
                    <el-table-column prop="comment" label="备注" width="240" align="center">
                    </el-table-column>
                   </el-table>
                 </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button
                size="small"
                @click="dialogAddVisible = false"
                icon="el-icon-close"
              >关闭</el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                @click="createData">保存
              </el-button>
            </div>
          </el-dialog>
        </div>

        <!--带教费修改-->
        <div>
          <el-dialog  title="带教费编辑" width="50%" :visible.sync="dialogEditVisible">
              <el-form  :model="area" ref="editForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="科室名称"  prop="deptname">
                          <el-input readonly v-model="area.deptname" style="width: 90%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                      <el-col :span="12">
                        <el-form-item label="类型"  prop="tuition">
                          <el-select v-model="area.tuition" clearable style="width: 200px" class="myInput" placeholder="中心">
                              <el-option v-for="item in tuitionSelect" :key="item.id" :value="item.id" :label="item.name">
                              </el-option>
                          </el-select>

                        </el-form-item>
                     </el-col>
                   </el-row>
                  <el-row>
                     <el-col :span="12">
                        <el-form-item label="数值"  prop="value">
                          <el-input v-model="area.value" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col>
                        <el-form-item label="备注"  prop="comment">
                          <el-input v-model="area.comment" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
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
                  @click="updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

        <!--带教费详细新增-->
        <div>
          <el-dialog  title="选择项目" width="40%" :visible.sync="dialogDetailAddVisible">
            <el-form  :model="detail" ref="detailAddForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
                 <el-row>
                   <el-table
                    :data="projectList"
                    ref="detailTable"
                    :header-cell-style="{background:'#F8F8F8'}"
                    stripe
                    highlight-current-row
                    @selection-change="detail_orderSelectChange"
                    @row-click="detail_rowClick">
                    <el-table-column type="selection" width="60" class="selection" align="center">
                    </el-table-column>
                    <el-table-column prop="name"  label="项目名称" width="160">
                    </el-table-column>
                     <el-table-column prop="tckind"  label="套餐类型" width="100">
                    </el-table-column>
                    <el-table-column prop="comment" label="备注" width="160">
                    </el-table-column>
                   </el-table>
                 </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button
                size="small"
                @click="dialogDetailAddVisible = false"
                icon="el-icon-close"
              >关闭</el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                @click="detail_createData">保存
              </el-button>
            </div>
          </el-dialog>
        </div>

        <!--带教费详细修改-->
        <div>
          <el-dialog  title="带教费编辑" width="50%" :visible.sync="dialogDetailEditVisible">
              <el-form  :model="detail" ref="detailEditForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                   <el-row>
                     <el-col :span="12">
                        <el-form-item label="项目名称"  prop="detail">
                          <el-input readonly v-model="detail.projectname" style="width: 90%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                      <el-col :span="12">
                        <el-form-item label="类型"  prop="tuition">
                          <el-select v-model="detail.tuition" clearable style="width: 200px" class="myInput" placeholder="中心">
                              <el-option v-for="item in tuitionSelect" :key="item.id" :value="item.id" :label="item.name">
                              </el-option>
                          </el-select>

                        </el-form-item>
                     </el-col>
                   </el-row>
                  <el-row>
                     <el-col :span="12">
                        <el-form-item label="数值"  prop="value">
                          <el-input v-model="detail.value" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row>
                     <el-col>
                        <el-form-item label="备注"  prop="comment">
                          <el-input v-model="detail.comment" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  @click="dialogDetailEditVisible = false"
                  icon="el-icon-close"
                >关闭</el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  @click="detail_updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>


    </div>
</template>

<script>
import { tuition_fees, depts, createTuition_fee, updateTuition_fee, deleteTuition_fee,
  tuitionfee_details, createTuitionfee_detail, updateTuitionfee_detail,
  deleteTuitionfee_detail, projects } from '@/api/system'
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
      detail_list: [],
      detail_total: null,
      deptList: [],
      projectList: [],
      searchname: '',
      tuitionfee_id: '',
      dialogAddVisible: false,
      dialogEditVisible: false,
      dialogDetailAddVisible: false,
      dialogDetailEditVisible: false,
      centerSelect: [
        {
          id: 2, name: '綦江中心'
        },
        {
          id: 3, name: '永川中心'
        }
      ],
      tuitionSelect: [
        {
          id: 1, name: '固定'
        },
        {
          id: 2, name: '比例'
        }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      multipleSelection: [],
      multipleOrder: [],
      area: {
        id: null,
        deptname: '',
        tuition: '',
        tuitionname: '',
        value: '',
        comment: ''
      },
      detail: {
        id: null,
        project: '',
        projectname: '',
        tuition: '',
        tuitionname: '',
        value: '',
        comment: ''
      }
    }
  },
  methods: {
    getDepts(data) {
      depts(data).then(response => {
        this.deptList = response.data.results
      })
    },
    getProjects(data) {
      projects(data).then(response => {
        this.projectList = response.data.results
      })
    },
    getTuition_fees(data) {
      tuition_fees(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getTuitionDetail(data) {
      tuitionfee_details(data).then(response => {
        this.detail_list = response.data.results
        this.detail_total = response.data.count
      })
    },
    resetArea() {
      this.area = {
        id: null,
        deptname: '',
        tuition: '',
        tuitionname: '',
        value: '',
        comment: ''
      }
    },
    resetDetail() {
      this.detail = {
        id: null,
        project: '',
        projectname: '',
        tuition: '',
        tuitionname: '',
        value: '',
        comment: ''
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getTuition_fees(this.listQuery)
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
    detail_orderSelectChange: function(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    detail_rowClick(row, event, column) {
      this.$refs.detailTable.toggleRowSelection(row)
    },
    rowClick_tuitionfee(row, event, column) {
      this.tuitionfee_id = row.id
      this.detail_list = []
      const par = {
        name: row.id
      }
      this.getTuitionDetail(par)
    },
    handleCreate() {
      this.resetArea()
      if (this.searchname === '') {
        this.$notify({
          title: '提示',
          message: '请选择中心',
          type: 'success',
          duration: 2000
        })
        return false
      }
      const par = {
        name: this.searchname
      }
      this.getDepts(par)
      this.dialogAddVisible = true
      this.$nextTick(() => {
        this.$refs['addForm'].clearValidate()
      })
    },
    createData() {
      if (this.multipleOrder.length > 0) {
        this.area.id = parseInt(Math.random() * 100) + 1024
        this.area.hrmdepartment_id = this.searchname
        this.area.depts = this.multipleOrder
        createTuition_fee(this.area).then(() => {
          this.dialogAddVisible = false
          this.$notify({
            title: '成功',
            message: '创建成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getTuition_fees(this.listQuery)
        })
      }
    },
    handleUpdate(row) {
      this.area = Object.assign({}, row) // copy obj
      console.log('area',this.area)
      this.dialogEditVisible = true
      this.$nextTick(() => {
        this.$refs['editForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['editForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.area)
          updateTuition_fee(tempData).then(() => {
            this.dialogEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getTuition_fees(this.listQuery)
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
        deleteTuition_fee(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getTuition_fees(this.listQuery)
        })
      })
    },
    detail_handleCreate() {
      this.resetDetail()
      if (this.tuitionfee_id === '') {
        this.$notify({
          title: '提示',
          message: '请选择科室',
          type: 'success',
          duration: 2000
        })
        return false
      }
      if (this.searchname === '') {
        this.$notify({
          title: '提示',
          message: '请选择中心',
          type: 'success',
          duration: 2000
        })
        return false
      }
      this.dialogDetailAddVisible = true
      const par = {
        name: this.searchname
      }
      this.getProjects(par)
      this.$nextTick(() => {
        // this.$refs['detailForm'].clearValidate()
      })
    },
    detail_createData() {
      if (this.multipleOrder.length > 0) {
        this.detail.id = parseInt(Math.random() * 100) + 1024
        this.detail.tuitionfee_id = this.tuitionfee_id
        this.detail.project = 1
        this.detail.tuition = 1
        this.detail.value = 0
        this.detail.projects = this.multipleOrder
        createTuitionfee_detail(this.detail).then(() => {
          this.dialogDetailAddVisible = false
          this.$notify({
            title: '成功',
            message: '创建成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            name: this.tuitionfee_id
          }
          this.getTuitionDetail(par)
        })
      }
    },
    detail_handleUpdate(row) {
      this.resetDetail()
      this.detail = Object.assign({}, row) // copy obj
      console.log('detail', this.detail)
      this.dialogDetailEditVisible = true
      this.$nextTick(() => {
        this.$refs['detailEditForm'].clearValidate()
      })
    },
    detail_updateData() {
      this.$refs['detailEditForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.detail)
          updateTuitionfee_detail(tempData).then(() => {
            this.dialogDetailEditVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            const par = {
              name: this.tuitionfee_id
            }
            this.getTuitionDetail(par)
          })
        }
      })
    },
    detail_handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.detail = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.detail)
        deleteTuitionfee_detail(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          const par = {
            name: this.tuitionfee_id
          }
          this.getTuitionDetail(par)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getTuition_fees(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getTuition_fees(this.listQuery)
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
    this.getTuition_fees(this.listQuery)
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
    /*.el-table__body tr.current-row>td {*/
        /*background: lightskyblue!important;*/
    /*}*/
</style>
