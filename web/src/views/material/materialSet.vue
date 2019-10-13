<template>
    <div>
        <div class="filter-container">
              <el-input
                v-model="materialname"
                class="myInput"
                style="width: 180px;"
                @keyup.enter.native="handleFilter"
                placeholder="耗材名称">
              </el-input>
              <el-select
                v-model="materialtype"
                clearable
                style="width: 200px;margin-right: 10px;"
                class="myInput" placeholder="耗材类型">
                <el-option label="血管路" value="血管路" >
                </el-option>
                <el-option label="留置导管" value="留置导管" >
                </el-option>
              </el-select>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="50">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="160" show-overflow-tooltip>
            </el-table-column>
            <el-table-column prop="code" label="条码"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="type" label="类别" width="90" align="center">
            </el-table-column>
            <el-table-column prop="spec" label="规格" width="60" align="center">
            </el-table-column>
            <el-table-column prop="units" label="单位" width="60" align="center">
            </el-table-column>
            <el-table-column prop="price" label="单价" width="80" align="center">
            </el-table-column>
            <el-table-column prop="reuse" label="是否复用" :formatter="formatReuse" width="80" align="center">
            </el-table-column>
            <el-table-column prop="madein" label="产地" width="120" align="center">
            </el-table-column>
            <el-table-column prop="factory" label="生产厂家" width="140" align="center" show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px">
                <el-pagination background
                               @size-change="handleSizeChange"
                               @current-change="handleCurrentChange"
                               :current-page="listQuery.page"
                               :page-sizes="[5,10,20,30, 50]"
                               :page-size="listQuery.limit"
                               layout="total, prev, pager, next, jumper"
                               :total="total">
                </el-pagination>
          </div>
        </div>

        <div>
          <el-dialog  title="耗材" width="60%" :append-to-body="true" :visible.sync="dialogFormVisible">
                  <el-form  :model="material" ref="dataForm"   label-position="left" label-width="70px" style='width:90%; margin-left:50px;'>
                       <el-row>
                         <el-col :span="8">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="material.name" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="代码" prop="code">
                              <el-input v-model="material.code" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                         <el-col :span="8">
                            <el-form-item label="类型" prop="type">
                              <el-select v-model="material.type" clearable style="width: 120px" class="myInput">
                                <el-option v-for="item in materialSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="规格" prop="spec">
                              <el-input v-model="material.spec" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="单位" prop="units">
                              <el-input v-model="material.units" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                        <el-col :span="8">
                            <el-form-item label="产地" prop="madein">
                              <el-input v-model="material.madein" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="8">
                            <el-form-item label="单价" prop="price">
                              <el-input v-model="material.price" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="是否复用" prop="reuse">
                              <el-switch v-model="material.reuse"></el-switch>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                            <el-form-item label="膜" prop="film">
                              <el-input v-model="material.film" style="width: 120px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col :span="12">
                            <el-form-item label="预警数量" prop="alert_amount">
                              <el-input type="number" v-model="material.alert_amount" style="width: 160px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="预警天数" prop="alert_expire">
                              <el-input type="number" v-model="material.alert_expire" style="width: 160px;"  class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                        <el-col>
                            <el-form-item label="生成厂家" prop="factory">
                              <el-input v-model="material.factory" style="width: 580px;"  class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                      <el-row>
                         <el-col>
                            <el-form-item label="备注" prop="comment">
                              <el-input v-model="material.comment" style="width: 580px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="dialogFormVisible = false"
                  >关闭
                  </el-button>
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
                    icon="el-icon-check"
                    type="primary"
                    @click="updateData"
                  >保存
                  </el-button>
                </div>
          </el-dialog>
        </div>
    </div>
</template>

<script>
import { materials, createMaterial, updateMaterial, deleteMaterial } from '@/api/login'
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
  props: ['clickcount'],
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
      materialtype: '',
      materialname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      materialSelect: [
        { id: '1', name: '透析器' },
        { id: '2', name: '滤过透析器' },
        { id: '3', name: '血滤器' },
        { id: '4', name: '血管路' },
        { id: '5', name: '内漏穿刺针'},
        { id: '6', name: '留置导管' },
        { id: '7', name: '碳肾' },
        { id: '8', name: '树脂罐' },
        { id: '9', name: '透析粉' },
        { id: '10', name: '透析A粉'},
        { id: '11', name: '透析干粉桶' },
        { id: '12', name: '血浆分离器' },
        { id: '13', name: '细菌过滤器' },
        { id: '14', name: '补液管' },
        { id: '15', name: '消毒液'},
        { id: '16', name: '活检针' },
        { id: '17', name: '套盘' }
      ],
      material: {
        id: null,
        code: '',
        name: '',
        type: '',
        spec: '',
        units: '',
        sn: '',
        factory: '',
        madein: '',
        reuse: false,
        film: '',
        price: '',
        comment: '',
        alert_amount: 0,
        alert_expire: 0,
        amount: 0,
        status: 0,
        mat_id: null
      },
      queryparams: {
        page: '',
        name: '',
        type: ''
      }
    }
  },
  methods: {
    getMaterialList(data) {
      materials(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetMaterial() {
      this.material = {
        id:null,
        code: '',
        name: '',
        type: '',
        spec: '',
        units: '',
        sn: '',
        factory: '',
        madein: '',
        reuse: false,
        film: '',
        price: '',
        comment: '',
        amount: 0,
        status: 0,
        mat_id: null
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.materialtype = ''
      this.materialname = ''
      this.queryparams.name = ''
      this.queryparams.type = ''
      this.getMaterialList(this.queryparams)
    },
    handleCreate() {
      this.resetMaterial()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.material.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.material.status = 0
          this.material.amount = 0
          this.material.sn = 'a'
          this.material.mat_id = 1
          createMaterial(this.material).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getMaterialList(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.material = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.material)
          tempData.amount = 1
          tempData.status = 1
          tempData.sn = 1
          tempData.mat_id = 1
          updateMaterial(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getMaterialList(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.material = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.material)
        deleteMaterial(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getMaterialList(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 10
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.materialname
      this.queryparams.type = this.materialtype
      this.getMaterialList(this.queryparams)
    },

    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getMaterialList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getMaterialList(this.queryparams)
    },
    formatReuse: function(row, column) {
      return row.reuse === true ? '是' : '否'
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
    clickcount: function() {
      this.getMaterialList(this.queryparams)
    }
  },
  created: function() {
    this.queryparams.page = 1
    this.queryparams.name = ''
    this.queryparams.type = ''
    this.getMaterialList(this.queryparams)
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
