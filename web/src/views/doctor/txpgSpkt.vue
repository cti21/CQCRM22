<template>
    <div>
        <div style="margin-top: 10px">
          <el-table
            :data="detailList"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="detaillistLoading"
            stripe>
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="Adddatetime" label="登记日期" width="100" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="weight" label="透前体重" width="80" align="center">
            </el-table-column>
            <el-table-column prop="gantizhong" label="干体重" width="80" align="center">
            </el-table-column>
            <el-table-column prop="pgdate" label="评估日期" width="100" :formatter="dateFormat" align="center">
            </el-table-column>
            <el-table-column prop="tqval" label="透前值" width="80" align="center">
            </el-table-column>
            <el-table-column prop="thval" label="透后值" width="80" align="center">
            </el-table-column>
            <el-table-column prop="spkt" label="spkt" width="60" align="center">
            </el-table-column>
            <el-table-column prop="urr" label="urr" width="60" align="center">
            </el-table-column>
            <el-table-column prop="reg_id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <!--<el-button type="text" size="mini" @click="viewLab_Result(scope.row)">查看</el-button>-->
                  <el-button type="text" size="small" @click="handleLinkLab(scope.row)">关联检验</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <div>
          <el-dialog  :title="dlgTitle" width="55%" :visible.sync="LabdialogFormVisible">
              <el-table
                :data="Lablist"
                v-loading="listLoading"
                @row-click="MasterrowClick"
                :header-cell-style="{background:'#F8F8F8'}"
              >
                <el-table-column type="index" label="序号"  width="50" align="center">
                </el-table-column>
                <el-table-column prop="master" v-if="false">
                </el-table-column>
                <el-table-column prop="patient_id" v-if="false">
                </el-table-column>
                <el-table-column prop="adddatetime" label="检验时间" width="160" :formatter="datetimeFormat">
                </el-table-column>
                <el-table-column prop="itemdictname" label="检验项目" width="120">
                </el-table-column>
                <el-table-column prop="itemdictcode" label="项目代码" width="100">
                </el-table-column>
                <el-table-column prop="reportdate" label="报告时间" width="160" :formatter="datetimeFormat">
                </el-table-column>
                <el-table-column label="操作" fixed="right" align="center">
                  <template slot-scope="scope">
                        <el-select v-model="scope.row.kind" @change="selectChange(scope.row)" clearable style="width: 110px" class="myInput">
                          <el-option label="透前" value="透前" ></el-option>
                          <el-option label="透后" value="透后" ></el-option>
                        </el-select>
                    </template>
                </el-table-column>
              </el-table>
              <div style="margin-top: 20px;"></div>
                <el-table
                  :data="resultList"
                  v-loading="resultlistLoading"
                  :header-cell-style="{background:'#F8F8F8'}"
                >
                  <el-table-column type="index" label="序号"  width="60">
                  </el-table-column>
                  <el-table-column prop="itemdictname" label="检验项目" width="220">
                  </el-table-column>
                  <el-table-column prop="result" label="结果"  width="120">
                  </el-table-column>
                  <el-table-column prop="units" label="单位" width="120">
                  </el-table-column>
                  <el-table-column prop="refvalue" label="参考值"  width="180">
                  </el-table-column>
                </el-table>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { txpgPatient, txpgspkt } from '@/api/doctor'
import { updatetRegister, lab_result, lab_test_item } from '@/api/login'
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
  props: ['patientid'],
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
      detailList: null,
      detailtotal: null,
      detaillistLoading: false,
      resultList: null,
      resulttotal: null,
      resultlistLoading: false,
      regid: null,
      Lablist: null,
      Labtotal: null,
      Detaillist: null,
      Detailtotal: null,
      searchname: '',
      searchpatientid: '',
      searchchecked: '',
      tempname: '',
      status: 0,
      radio: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      LabdialogFormVisible: false,
      LabdialogStatus: '',
      DetaildialogFormVisible: false,
      DetaildialogStatus: '',
      dlgTitle: '',
      register: {
        id: null,
        state: 'a',
        status: 0,
        labid: '',
        master: null
      },
      params: {
        patientid: '',
        registerid: ''
      },
      queryparams: {
        page: 1,
        name: '',
        patientid: '',
        checked: ''
      }
    }
  },
  methods: {
    getPatientList(data) {
      txpgPatient(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getPatientTxpgspkt(data) {
      this.detailList = null
      txpgspkt(data).then(response => {
        this.detaillistLoading = true
        this.detailList = response.data.results
        this.detailtotal = response.data.count
        this.detaillistLoading = false
      })
    },
    getLab_master(data) {
      lab_test_item(data).then(response => {
        const masterData = response.data.results
        if (masterData.length > 0) {
          this.Lablist = masterData
          this.Labtotal = response.data.count
        }
      })
    },
    getLab_Result(data) {
      lab_result(data).then(response => {
        this.resultlistLoading = true
        this.resultList = response.data.results
        this.resulttotal = response.data.count
        this.resultlistLoading = false
      })
    },
    resetRegister() {
      this.register = {
        id: null,
        state: 'a',
        status: 0
      }
    },
    selectChange(row) {
      this.register = Object.assign({}, row)
      if (row.kind === '透前'){
        this.linkLabData(2)
      } else {
        this.linkLabData(3)
      }
    },
    checkboxSelect(val) {
      if (val === true){
        this.queryparams.page = 1
        this.queryparams.name = ''
        this.searchname = ''
        this.queryparams.patientid = ''
        this.searchpatientid = ''
        this.queryparams.checked = '1'
        this.getPatientList(this.queryparams)
      }
    },
    PatientRowClick(row, event, column) {
      this.patientid = row.patientid
      this.getPatientTxpgspkt(this.patientid)
    },
    MasterrowClick(row, event, column) {
      this.getLab_Result(row.master)
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.searchname = ''
      this.queryparams.patientid = ''
      this.searchpatientid = ''
      this.queryparams.checked = ''
      this.searchchecked = ''
      this.getPatientList(this.queryparams)
    },
    viewLab_Result(row) {
      this.DetaildialogFormVisible = true
      this.DetaildialogStatus = 'create'
      lab_test_result(this.regid).then(response => {
        this.Detaillist = response.data.results[0].detail
        this.Detailtotal = response.data.count
      })
    },
    handleLinkLab(row) {
      this.Lablist = null
      this.regid = row.id
      this.params.patientid = this.patientid
      this.params.registerid = row.reg_id
      this.getLab_master(this.params)
      this.LabdialogFormVisible = true
      this.LabdialogStatus = 'create'
      this.dlgTitle = '关联检验记录'
    },
    linkLabData(flag) {
      const tempData = Object.assign({}, this.register)
      tempData.labid = tempData.master
      tempData.id = this.regid
      tempData.state = 'a'
      tempData.status = flag
      console.log(tempData)
      updatetRegister(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '关联成功',
          type: 'success',
          duration: 2000
        })
        this.getPatientTxpgspkt(this.patientid)
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.name = this.searchname
      this.queryparams.patientid = this.searchpatientid
      this.queryparams.checked = this.searchchecked
      this.getPatientList(this.queryparams)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getPatientList(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      else if (date === '') {
        return ''
      }
      else {
        return moment(date).format('YYYY-MM-DD')
      }
    },
    datetimeFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      else if (date === '') {
        return ''
      }
      else {
        return moment(date).format('YYYY-MM-DD HH:mm')
      }
    }
  },
  watch: {
    patientid: function() {
      this.detailList = []
      this.getPatientTxpgspkt(this.patientid)
    }
  },
  created: function() {
    this.getPatientList(this.queryparams)
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
