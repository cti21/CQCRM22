<template>
    <div>
        <el-row>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary">新增问卷</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="success">新增干预</el-button>
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
            <el-table-column prop="valuedate" label="评估日期" width="120">
            </el-table-column>
            <el-table-column prop="score" label="分数" width="120">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleAnswer(scope.row)">答卷</el-button>
                  <el-button type="text" size="small" @click="">比对</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-row>

        <div>
          <el-dialog  title="问卷选择" width="40%" :visible.sync="dialogFormVisible" :append-to-body="true">
            <el-form  :model="area" ref="dataForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
                 <el-row>
                   <el-table
                      :data="surveyList"
                      ref="multipleTable"
                      :header-cell-style="{background:'#F8F8F8'}"
                      stripe
                      highlight-current-row
                      @selection-change="selectChange"
                      @row-click="rowClick"
                   >
                    <el-table-column type="selection" width="80" class="selection" align="center">
                    </el-table-column>
                    <el-table-column prop="name"  label="问卷名称" width="180" align="center">
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

        <!--答卷-->
        <div>
          <el-dialog  title="答卷" width="60%" :visible.sync="dialogAnswerVisible" :append-to-body="true">
            <surveyAnswer :surveyobj="surveyobj"  @closeDlg="closeAddDialog"></surveyAnswer>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { surveys, treat_surveys, createTreat_survey, deleteTreat_survey } from '@/api/order'
import surveyAnswer from '@/views/orders/survey_answer.vue'
import { getToken } from '@/utils/auth'
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
    ElCol,
    surveyAnswer
  },
  props: {
    parentobj: {
      type: Object
    }
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
      searchname: '',
      token: getToken,
      dialogFormVisible: false,
      dialogAnswerVisible: false,
      dialogStatus: '',
      surveyList: [],
      multipleOrder: [],
      count: 0,
      surveyobj: {
        id: null,
        treat: null,
        count: null
      },
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
    getTreat_surveys(data) {
      treat_surveys(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
        console.log('surveylist', this.list)
      })
    },
    getSurveys(data) {
      surveys(data).then(response => {
        this.surveyList = response.data.results
      })
    },
    resetArea() {
      this.area = {
        id: null,
        name: '',
        comment: ''
      }
    },
    selectChange(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    rowClick(row, event, column) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    handleAnswer(row) {
      this.count = this.count + 1
      this.surveyobj.id = row.survey
      this.surveyobj.treat = row.treat
      this.surveyobj.count = this.count
      this.dialogAnswerVisible = true
    },
    closeAddDialog() {
    },
    handleCreate() {
      this.resetArea()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.area.id = parseInt(Math.random() * 100) + 1024
          this.area.treat_id = this.parentobj.id
          this.area.surveys = this.multipleOrder
          createTreat_survey(this.area).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getTreat_surveys(this.listQuery)
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
        deleteTreat_survey(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getTreat_surveys(this.listQuery)
        })
      })
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.getSurveys(this.listQuery)
    this.getTreat_surveys(this.listQuery)
    console.log('parentobj', this.parentobj)
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
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
