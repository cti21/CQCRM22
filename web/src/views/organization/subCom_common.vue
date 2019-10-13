<template>
    <div>
        <el-form  :model="area" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
             <el-row>
               <el-col :span="12">
                  <el-form-item label="简称"  prop="name">
                    <el-input v-model="area.name" style="width: 180px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="12">
                  <el-form-item label="全称"  prop="description">
                    <el-input v-model="area.description" style="width: 180px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="12">
                  <el-form-item label="上级分部">
                    <el-select v-model="area.supsubcomid" clearable class="myInput" placeholder="请选择">
                      <el-option
                        v-for="item in list"
                        :key="item.id"
                        :label="item.name"
                        :value="item.id">
                      </el-option>
                    </el-select>
                  </el-form-item>
               </el-col>
               <el-col :span="12">
                  <el-form-item label="网站"  prop="url">
                    <el-input v-model="area.url" style="width: 180px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="12">
                  <el-form-item label="显示顺序"  prop="showorder">
                    <el-input v-model="area.showorder" style="width: 180px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="12">
                  <el-form-item label="分部编号"  prop="code">
                    <el-input v-model="area.code" style="width: 180px;" class="myInput"></el-input>
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
            v-if="action=='create'"
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
    </div>
</template>

<script>
import { subComSelect, createSubCompany, updateSubCompany } from '@/api/login'
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
  props: ['action', 'companyid', 'clickcount'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      token: getToken,
      dialogFormVisible: false,
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      area: {
        id: null,
        name: '',
        description: '',
        url: '',
        companyid: null,
        supsubcomid: null,
        showorder: 0,
        code: ''
      },
      queryparams: {
        page: 1,
        name: ''
      }
    }
  },
  methods: {
    getSubCompany(data) {
      subComSelect(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetArea() {
      this.area = {
        id: null,
        name: '',
        flag: '',
        comment: ''
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.getSubCompany(this.queryparams)
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.area.id = parseInt(Math.random() * 100) + 1024 // mock a id
          const tempData = Object.assign({}, this.area)
          if (tempData.supsubcomid === null) {
            tempData.companyid = 1
          } else {
            tempData.companyid = null
          }
          createSubCompany(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getSubCompany(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.area = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.area)
          if (tempData.supsubcomid === null) {
            tempData.companyid = 1
          } else {
            tempData.companyid = null
          }
          updateSubCompany(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getSubCompany(this.queryparams)
          })
        }
      })
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
    this.queryparams.page = 1
    this.queryparams.name = ''
    this.getSubCompany(this.queryparams)
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
