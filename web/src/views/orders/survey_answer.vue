<template>
    <div>
        <el-row style="margin:20px;">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8',align:'center'}"
            v-loading="listLoading"
            stripe
          >
            <!--<el-table-column type="index" label="序号"  width="80">-->
            <!--</el-table-column>-->
            <el-table-column prop="title" :label="columnname" width="300">
            </el-table-column>
            <el-table-column label="选项" fixed="right" header-align="center">
              <template slot-scope="scope">
                <span v-if="scope.row.type===0">
                  <el-radio-group v-model="scope.row.val">
                    <el-radio v-for="item in scope.row.items" :key="item.id" :label="item.id" :value="item.id">
                      {{item.answer}}</el-radio>
                  </el-radio-group>
                </span>
                <span v-else-if="scope.row.type===1">
                  <el-input v-model="scope.row.val" style="width: 80%;" class="myInput"></el-input>
                </span>
                <span v-else>
                </span>
              </template>
            </el-table-column>
          </el-table>
        </el-row>
        <el-row align="center">
          <el-col :span="11"><div>&nbsp;</div></el-col>
          <el-col :span="2">
            <el-button size="small" style="margin-bottom:10px;" @click="createData" type="success" icon="el-icon-check">
              保存
            </el-button>
          </el-col>
          <el-col :span="11"><div>&nbsp;</div></el-col>
        </el-row>

    </div>
</template>

<script>
import { survey_titles, createSurvey_title } from '@/api/order'
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
    ElCol
  },
  props: {
    surveyobj: {
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
        survey_id: null,
        treat_id: null,
        sort: '+id'
      },
      columnname: '近2星期,您有多少时间受以下问题困扰,请选择',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      surveyList: [],
      multipleOrder: [],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      title: {
        id: null,
        survey_id: null,
        treat_id: null,
        type: null
      }
    }
  },
  methods: {
    getSurvey_answers(data) {
      survey_titles(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
        console.log('titlelist', this.list)
      })
    },
    createData() {
      if (this.list.length > 0) {
        this.title.id = parseInt(Math.random() * 100) + 1024
        this.title.survey_id = this.surveyobj.id
        this.title.treat_id = this.surveyobj.treat
        this.title.titles = this.list
        createSurvey_title(this.title).then(() => {
          this.$notify({
            title: '成功',
            message: '保存成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getTreat_surveys(this.listQuery)
        })
      }
    }
  },
  watch: {
    'surveyobj.count': {
      handler(val, oldVal) {
        if (this.surveyobj.id === 1) {
          this.columnname = '近2星期,您有多少时间受以下问题困扰,请选择'
        } else if (this.surveyobj.id === 2) {
          this.columnname = '近2星期,您有多少时间受以下问题困扰,请选择'
        } else if (this.surveyobj.id === 3) {
          this.columnname = '就产后感受,请在四个答案中选择一个'
        } else if (this.surveyobj.id === 4) {
          this.columnname = '近1个月的睡眠情况,请您如实选择或填写'
        }
        this.list = []
        this.listQuery.survey_id = this.surveyobj.id
        this.listQuery.treat_id = this.surveyobj.treat
        this.getSurvey_answers(this.listQuery)
      },
      deep: true
    }
  },
  created: function() {
    this.listQuery.page = 1
    this.listQuery.name = ''
    if (this.surveyobj.id === 1) {
      this.columnname = '近2星期,您有多少时间受以下问题困扰,请选择'
    } else if (this.surveyobj.id === 2) {
      this.columnname = '近2星期,您有多少时间受以下问题困扰,请选择'
    } else if (this.surveyobj.id === 3) {
      this.columnname = '就产后感受,请在四个答案中选择一个'
    } else if (this.surveyobj.id === 4) {
      this.columnname = '近1个月的睡眠情况,请您如实选择或填写'
    }
    this.listQuery.survey_id = this.surveyobj.id
    this.listQuery.treat_id = this.surveyobj.treat
    this.getSurvey_answers(this.listQuery)
    console.log('surveyobj', this.surveyobj)
  }
}
</script>

<style scoped>
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
    .el-dialog__body {
        padding: 0px 20px;
        line-height: 34px;
    }
</style>
