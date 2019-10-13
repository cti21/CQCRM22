<template>
    <div>
        <div class="filter-container">
              <el-date-picker
                v-model="fromdate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="监测日期开始">
              </el-date-picker>
              <el-date-picker
                v-model="todate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="监测日期结束">
              </el-date-picker>
              <el-button
                size="small"
                type="primary"
                style="margin-left: 10px;"
                @click="handleFilter"
                icon="el-icon-search"
              >搜索
              </el-button>
              <el-button
                size="small"
                style="margin-left: 10px;"
                @click="handleCreate"
                type="primary"
                icon="el-icon-plus"
              >新增
              </el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column type="index" label="序号"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="examdate" label="监测日期"  width="100" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="hardness" label="水硬度" width="80" align="center">
            </el-table-column>
            <el-table-column prop="re_cl" label="余氯" width="60" align="center">
            </el-table-column>
            <el-table-column prop="diandao" label="电导" width="60" align="center">
            </el-table-column>
            <el-table-column prop="k" label="钾"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="ca" label="钙" width="50" align="center">
            </el-table-column>
            <el-table-column prop="na" label="钠"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="mg" label="镁" width="50" align="center">
            </el-table-column>
            <el-table-column prop="cl" label="氯离子"  width="90" align="center">
            </el-table-column>
            <el-table-column prop="cl_a" label="氯氨" width="60" align="center">
            </el-table-column>
            <el-table-column prop="examer" label="检测人"  width="90" align="center">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="70" align="center" show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
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
          <el-dialog  title="水质监测" width="55%" :visible.sync="dialogFormVisible">
                  <el-form  :model="waterExam_obj" ref="dataForm" label-position="left" label-width="70px" style='width:90%; margin-left:80px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="保养时间" prop="date">
                              <el-date-picker v-model="waterExam_obj.date" class="myInput" style="width: 140px">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="硬度" prop="hardness">
                              <el-input v-model="waterExam_obj.hardness" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                          <el-col :span="12">
                            <el-form-item label="余氯" prop="re_cl">
                              <el-input v-model="waterExam_obj.re_cl" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="电导"  prop="diandao">
                              <el-input v-model="waterExam_obj.diandao" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>

                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="钾" prop="k">
                              <el-input v-model="waterExam_obj.k" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="钙" prop="ca">
                              <el-input v-model="waterExam_obj.ca" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                          <el-col :span="12">
                            <el-form-item label="钠" prop="na">
                              <el-input v-model="waterExam_obj.na" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                          <el-col :span="12">
                            <el-form-item label="镁"  prop="mg">
                              <el-input v-model="waterExam_obj.mg" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="氯离子" prop="cl">
                              <el-input v-model="waterExam_obj.cl" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="氯氨" prop="cl_a">
                              <el-input v-model="waterExam_obj.cl_a" style="width: 140px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                      <el-row>
                          <el-col>
                            <el-form-item label="备注" prop="comment">
                              <el-input v-model="waterExam_obj.comment" style="width: 460px;" class="myInput"></el-input>
                            </el-form-item>
                          </el-col>
                       </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button size="small" @click="dialogFormVisible = false" icon="el-icon-close">关闭</el-button>
                  <el-button
                    size="small"
                    type="primary"
                    v-if="dialogStatus=='create'"
                    icon="el-icon-check"
                    @click="createData">保存</el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="updateData">保存</el-button>
                </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { water_exams, createwater_exam, updatewater_exam, deletewater_exam } from '@/api/device'
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
    ElCol },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      fromdate: '',
      todate: '',
      matSelect: '',
      token: getToken,
      dialogStatus: '',
      dialogFormVisible: false,
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
      waterExam_obj: {
          id: null,
          examdate: '',
          hardness: '',
          re_cl: '',
          diandao: '',
          k: '',
          ca: '',
          na: '',
          mg: '',
          cl: '',
          cl_a: '',
          examer: '',
          comment: ''
      },
      queryparams: {
        page: 1,
        fromdate: '',
        todate: ''
      }
    }
  },
  methods: {
    getWaterExamList(data) {
      water_exams(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    reseWaterExam() {
        this.waterExam_obj = {
            id: null,
            examdate: new Date(),
            hardness: '',
            re_cl: '',
            diandao: '',
            k: '',
            ca: '',
            na: '',
            mg: '',
            cl: '',
            cl_a: '',
            examer: '',
            comment: ''
        }
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.fromdate = ''
      this.queryparams.todate = ''
      this.fromdate = ''
      this.todate = ''
      this.getWaterExamList(this.queryparams)
    },
    handleCreate() {
      this.reseWaterExam()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.waterExam_obj.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createwater_exam(this.waterExam_obj).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getWaterExamList(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
     this.waterExam_obj = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.waterExam_obj)
          updatewater_exam(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getWaterExamList(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.waterExam_obj = Object.assign({}, row)
        const tempData = Object.assign({}, this.waterExam_obj)
        deletewater_exam(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getWaterExamList(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.fromdate = this.fromdate
      this.queryparams.todate = this.todate
      this.getWaterExamList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getWaterExamList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getWaterExamList(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getWaterExamList(this.queryparams)
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
