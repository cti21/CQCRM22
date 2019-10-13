<template>
    <div>
        <el-row>
            <el-input
              v-model="searchname"
              class="myInput"
              style="width: 220px;margin-right: 20px"
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
            <el-table-column prop="name" label="名称" width="120">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="120">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
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

        <!--项目禁忌症新增-->
        <div>
          <el-dialog  title="禁忌症新增" width="50%" :visible.sync="dialogFormVisible" :append-to-body="true">
              <el-form  :model="area" ref="dataForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
                   <el-row>
                     <el-table
                      :data="jinjizhengList"
                      ref="multipleTable"
                      :header-cell-style="{background:'#F8F8F8'}"
                      stripe
                      highlight-current-row
                      @selection-change="SelectChange"
                      @row-click="rowClick">
                      <el-table-column type="selection" width="80" class="selection" align="center">
                      </el-table-column>
                      <el-table-column prop="name"  label="名称" width="180" align="center">
                      </el-table-column>
                      <el-table-column prop="comment" label="备注" width="240" align="center">
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
                  @click="createData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { jinjizhengs, project_jinjizhengs, createProject_jinjizheng, deleteProject_jinjizheng } from '@/api/client'
import { dept_dicts, createDept_dict, updateDept_dict, deleteDept_dict,
  post_dicts, dept_posts, createDept_post, deleteDept_post } from '@/api/system'
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
  props: ['project_id', 'num'],
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
        project_id: null,
        sort: '+id'
      },
      jinjizhengList: [],
      multipleOrder: [],
      searchname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogPostVisible: false,
      dialogPostAddVisible: false,
      dialogStatus: '',
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      area: {
        id: null,
        name: '',
        comment: ''
      }
    }
  },
  methods: {
    getProject_jinjizheng(data) {
      project_jinjizhengs(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getJinjizheng(data) {
      jinjizhengs(data).then(response => {
        this.jinjizhengList = response.data.results
      })
    },
    SelectChange: function(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    rowClick(row, event, column) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    handleCreate() {
      this.dialogFormVisible = true
      this.multipleOrder = []
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.area.id = parseInt(Math.random() * 100) + 1024
          const tempdata = Object.assign({}, this.area)
          tempdata.action = 'Add'
          tempdata.jinjizhengs = this.multipleOrder.map(x => x.id)
          tempdata.project_id = this.project_id
          createProject_jinjizheng(tempdata).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '导入成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getProject_jinjizheng(this.listQuery)
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
        deleteProject_jinjizheng(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getProject_jinjizheng(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getProject_jinjizheng(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getProject_jinjizheng(this.listQuery)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  watch: {
    num: function() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.listQuery.project_id = this.project_id
      this.getProject_jinjizheng(this.listQuery)
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.listQuery.project_id = this.project_id
    this.getProject_jinjizheng(this.listQuery)
    this.getJinjizheng(this.listQuery)
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
