<template>
    <div>
        <el-container>
          <el-aside width="200px">
              <div style="margin-top: 20px">
                <el-input
                  v-model="searchname"
                  class="myInput"
                  style="width: 180px"
                  suffix-icon="el-icon-search"
                  @keyup.enter.native="handleFilter"
                  placeholder="请输入疾病名称">
                </el-input>
                <el-table
                  :data="bq_list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  highlight-current-row
                  @row-click="rowClick">
                  <el-table-column type="index" label="序号">
                  </el-table-column>
                  <el-table-column prop="name" label="原发病" align="left">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false">
                  </el-table-column>
                </el-table>
              </div>
          </el-aside>
          <el-container>
            <el-main style="padding-top: 0px">
                <el-row>
                  <el-input
                    v-model="bedname"
                    class="myInput"
                    style="width: 220px;margin-right: 20px"
                    prefix-icon="el-icon-search"
                    @keyup.enter.native="bed_handleFilter"
                    placeholder="请输入病理名称">
                  </el-input>
                  <el-button
                    size="small"
                    type="primary"
                    @click="bed_handleFilter"
                    icon="el-icon-search">搜索
                  </el-button>
                  <el-button
                    size="small"
                    style="margin-left: 20px;"
                    @click="handleCreate"
                    type="primary"
                    icon="el-icon-plus">新增
                  </el-button>
                </el-row>
                <el-row style="margin-top: 20px">
                  <el-table
                    ref="multipleTable"
                    :data="list"
                    :header-cell-style="{background:'#F8F8F8'}"
                    stripe
                  >
                    <el-table-column type="index" label="序号"  width="160">
                    </el-table-column>
                    <el-table-column prop="name" label="名称" width="220">
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
                <div class="pagination-container" style="margin-top: 5px" align="right">
                      <el-pagination background
                           @current-change="handleCurrentChange"
                           :current-page="listQuery.page"
                           :page-sizes="[5,10,20,30, 50]"
                           :page-size="listQuery.limit"
                           layout="total, prev, pager, next, jumper"
                           :total="total">
                      </el-pagination>
                </div>
            </el-main>
          </el-container>
        </el-container>

        <div>
          <el-dialog  title="病理" width="60%" :visible.sync="dialogListVisible">
            <el-form  :model="bed" ref="addForm" :rules="rules" label-position="left" label-width="90px" style='width:90%; margin-left:40px;'>
              <el-row>
                 <el-col :span="12">
                    <el-form-item label="病理名称" prop="name">
                      <el-input v-model="bed.name"  style="width: 200px;" class="myInput"></el-input>
                    </el-form-item>
                 </el-col>
              </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button
                size="small"
                style="height:33px;padding-top: 8px"
                icon="el-icon-close"
                @click="dialogListVisible = false"
              >关闭
              </el-button>
              <el-button
                size="small"
                type="primary"
                style="height:33px;padding-top: 8px"
                icon="el-icon-check"
                v-if="dialogStatus=='create'"
                @click="createData"
                >保存
              </el-button>
              <el-button
                size="small"
                v-else
                type="primary"
                icon="el-icon-check"
                @click="updateData"
              >保存
              </el-button>
            </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { yfdisease, bingli, createBingli, updateBingli, deleteBingli } from '@/api/login'
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
import ElMain from '../../../node_modules/element-ui/packages/main/src/main'

export default {
  components: {
    ElMain,
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        id: null,
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      device_list: null,
      device_total: null,
      device_listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        type: '',
        sort: '+id'
      },
      bq_list: null,
      bq_total: null,
      radio: '',
      dialogListVisible: false,
      matSelect: '',
      searchname: '',
      bedname: '',
      devicename: '',
      bq_id: '',
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      token: getToken,
      dialogStatus: 'create',
      bed: {
        id: null,
        name: '',
        disease_id: ''
      },
      params: {
        page: 1,
        name: '',
        type: 0
      }
    }
  },
  methods: {
    getBeds(data) {
      bingli(data).then(response => {
        this.list = response.data.results
        this.total = response.data.count
      })
    },
    getDiseaseArea(data) {
      yfdisease(data).then(response => {
        this.bq_list = response.data.results
        this.bq_total = response.data.count
      })
    },
    rowClick(row, event, column) {
      this.listQuery.id = row.id
      this.bq_id = row.id
      this.getBeds(this.listQuery)
    },
    resetBed() {
      this.bed = {
        id: null,
        name: '',
        disease_id: ''
      }
    },
    handleCreate() {
      if (this.bq_id === '') {
        this.$notify({
          title: '提示',
          message: '请选择疾病',
          type: 'success',
          duration: 2000
        })
      } else {
        this.resetBed()
        this.dialogListVisible = true
        this.dialogStatus = 'create'
        this.$nextTick(() => {
          this.$refs['addForm'].clearValidate()
        })
      }
    },
    createData() {
      const tempData = Object.assign({}, this.bed)
      tempData.disease_id = this.bq_id
      if (tempData.name === '') {
        this.$notify({
          title: '提示',
          message: '请输入病理名称',
          type: 'success',
          duration: 2000
        })
        return
      }
      createBingli(tempData).then(() => {
        this.dialogListVisible = false
        this.$notify({
          title: '成功',
          message: '新建成功',
          type: 'success',
          duration: 2000
        })
        this.listQuery.page = 1
        this.getBeds(this.listQuery)
      })
    },
    handleUpdate(row) {
      this.resetBed()
      this.bed = Object.assign({}, row)
      this.dialogListVisible = true
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['addForm'].clearValidate()
      })
    },
    updateData() {
      const tempData = Object.assign({}, this.bed)
      tempData.disease_id = this.bq_id
      if (tempData.name === '') {
        this.$notify({
          title: '提示',
          message: '请输入病理名称',
          type: 'success',
          duration: 2000
        })
        return
      }
      updateBingli(tempData).then(() => {
        this.dialogListVisible = false
        this.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
        this.listQuery.page = 1
        this.getBeds(this.listQuery)
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.bed = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.bed)
        deleteBingli(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getBeds(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.params.page = 1
      this.params.name = this.searchname
      this.getDiseaseArea(this.params)
    },
    bed_handleFilter() {
      this.listQuery.page = 1
      this.listQuery.id = this.bq_id
      this.listQuery.name = this.bedname
      this.getBeds(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getBeds(this.listQuery)
    },
    dateFormat(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getDiseaseArea(this.params)
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
