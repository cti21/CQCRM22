<template>
    <div>
        <el-container style="border: 1px solid #eee">
          <el-aside width="200px" style="height:100%;background-color: rgb(238, 241, 246)">
            <el-menu :default-openeds="['1','2']" @select="handleSelect">
              <el-submenu index="1">
                <template slot="title">检验报告</template>
                <el-menu-item v-for="(item,i) in labMenu" :key="i" :index="item.id + '_L'"  style="color: black;">
                  {{item.itemname}}
                </el-menu-item>
              </el-submenu>
              <el-submenu index="2">
                <template slot="title">检查报告</template>
                <el-menu-item v-for="(item,i) in examMenu" :key="i" :index="item.id + '_E'"  style="color: black;">
                  {{item.itemname}}
                </el-menu-item>

              </el-submenu>
            </el-menu>
          </el-aside>
          <el-container>
            <el-main>
              <div class="filter-container">
                    <el-date-picker
                      v-model="fromdate"
                      style="width: 160px"
                      class="myInput"
                      type="date"
                      value-format="yyyy-MM-dd"
                      placeholder="报告日期开始">
                    </el-date-picker>
                    <el-date-picker
                      v-model="todate"
                      style="width: 160px"
                      class="myInput"
                      type="date"
                      value-format="yyyy-MM-dd"
                      placeholder="报告日期结束">
                    </el-date-picker>
                    <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
                    <el-button size="small" type="primary" @click="handleReset" icon="el-icon-download">重置</el-button>
              </div>
              <!--检验主记录-->
              <div style="margin-top: 20px">
                <el-table
                  :data="list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  stripe
                  v-loading="listLoading"
                  @row-click="rowClick"
                  v-if="tableVisible==true"
                >
                  <el-table-column type="index" label="序号"  width="60" align="center">
                  </el-table-column>
                  <el-table-column prop="master" v-if="false">
                  </el-table-column>
                  <el-table-column prop="itemdictcode" label="项目代码" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="itemdictname" label="项目名称"  width="180" align="center">
                  </el-table-column>
                  <el-table-column prop="testno" label="序号" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="reason" label="检验目的"  width="200">
                  </el-table-column>
                  <el-table-column prop="adddatetime" label="送检日期" :formatter="dateFormat" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="reportdate" label="报告日期" :formatter="dateFormat" width="100" align="center">
                  </el-table-column>
                </el-table>
                <div class="pagination-container" style="float: right;margin-right: 40px;" align="right" v-if="tableVisible==true">
                    <el-pagination background
                         @current-change="handleCurrentChange"
                         :current-page="listQuery.page"
                         :page-sizes="[5,10,20,30, 50]"
                         :page-size="listQuery.limit"
                         layout="total, prev, pager, next"
                         :total="total">
                    </el-pagination>
                </div>

                <div style="margin-top: 20px;"></div>
                <el-table
                  :data="detail_list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  stripe
                  v-loading="detail_listLoading"
                  v-if="tableVisible==true">
                  <el-table-column type="index" label="序号"  width="100">
                  </el-table-column>
                  <el-table-column prop="itemdictname" label="检验项目" width="200">
                  </el-table-column>
                  <el-table-column prop="result" label="结果"  width="200" align="center">
                  </el-table-column>
                  <el-table-column prop="units" label="单位" width="200" align="center">
                  </el-table-column>
                  <el-table-column prop="refvalue" label="参考值"  width="200" align="center">
                  </el-table-column>
                </el-table>

                <!--检查主记录-->
                <el-table
                  :data="exam_list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  stripe
                  v-if="tableVisible==false"
                  @row-click="exam_rowClick">
                  <el-table-column type="index" label="序号"  width="50" align="center">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false" width="130">
                  </el-table-column>
                  <el-table-column prop="examno" label="检查序号"  width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="classname" label="项目类别" width="130" align="center">
                  </el-table-column>
                  <el-table-column prop="performby" label="执行科室" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="reqdatetime" label="申请时间" :formatter="dateFormat" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="reqdept" label="申请科室"  width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="doctor" label="申请医生" width="100" align="center">
                  </el-table-column>
                </el-table>
                <div class="pagination-container" style="float: right;margin-right: 40px;" align="right" v-if="tableVisible==false">
                      <el-pagination background
                           @current-change="exam_handleCurrentChange"
                           :current-page="exam_listQuery.page"
                           :page-sizes="[5,10,20,30, 50]"
                           :page-size="exam_listQuery.limit"
                           layout="total, prev, pager, next"
                           :total="exam_total">
                      </el-pagination>
                </div>
                <!--检查结果-->
                <div style="margin-top: 20px;"></div>
                <el-table
                  :data="exam_detail_list"
                  :header-cell-style="{background:'#F8F8F8'}"
                  stripe
                  v-if="tableVisible==false">
                  <el-table-column type="index" label="序号"  width="50" align="center">
                  </el-table-column>
                  <el-table-column prop="subclassname" label="子类名称" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="exampara" label="检查参数"  width="110" align="center">
                  </el-table-column>
                  <el-table-column prop="description" label="检查所见" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="impression" label="印象"  width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="suggest" label="建议" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="isnormal" label="是否阳性"  width="120" align="center">
                  </el-table-column>
                </el-table>
              </div>
            </el-main>
          </el-container>
        </el-container>
    </div>
</template>

<script>
import { lab_test_item, lab_result,exam_master, exam_report, getLab_Test_Items,
  getExam_Items } from '@/api/login'
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
import ElButton from '../../../node_modules/element-ui/packages/button/src/button'
import ElContainer from '../../../node_modules/element-ui/packages/container/src/main'
import ElMain from '../../../node_modules/element-ui/packages/main/src/main'

export default {
  name: 'lab_test',
  components: {
    ElMain,
    ElContainer,
    ElButton,
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
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      exam_list: null,
      exam_total: null,
      exam_listLoading: false,
      exam_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      detail_list: null,
      detail_total: null,
      detail_listLoading: false,
      detail_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      exam_detail_list: null,
      exam_detail_total: null,
      labMenu: [],
      examMenu: [],
      fromdate: '',
      todate: '',
      tableVisible: true,
      token: getToken,
      queryparams: {
        page: 1,
        fromdate: '',
        todate: '',
        itemcode: null,
        patientid: this.patientid
      }
    }
  },
  methods: {
    getLab_menu(data) {
      getLab_Test_Items(data).then(response => {
        this.labMenu = response.data
      })
    },
    getExam_menu(data) {
      getExam_Items(data).then(response => {
        this.examMenu = response.data
      })
    },
    getLab_Test_ItemList(data) {
      lab_test_item(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getExam_Master(data) {
      exam_master(data).then(response => {
        this.exam_list = response.data.results
        this.exam_total = response.data.count
      })
    },
    getLab_Result(data) {
      lab_result(data).then(response => {
        this.detail_listLoading = true
        this.detail_list = response.data.results
        this.detail_total = response.data.count
        this.detail_listLoading = false
      })
    },
    getExam_Report(data) {
      exam_report(data).then(response => {
        this.exam_detail_list = response.data.results
        this.exam_detail_total = response.data.count
      })
    },
    handleFilter() {
      this.list = []
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.fromdate = this.fromdate
      this.queryparams.todate = this.todate
      console.log(this.queryparams)
      if (this.tableVisible === true) {
        this.getLab_Test_ItemList(this.queryparams)
      } else {
        this.getExam_Master(this.queryparams)
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.fromdate = ''
      this.todate = ''
      this.queryparams.fromdate = ''
      this.queryparams.todate = ''
      if (this.tableVisible === true) {
        this.getLab_Test_ItemList(this.queryparams)
      } else {
        this.getExam_Master(this.queryparams)
      }
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getLab_Test_ItemList(this.queryparams)
    },
    exam_handleCurrentChange(val) {
      this.exam_listQuery.page = val
      this.exam_listQuery.offset = (val - 1) * this.exam_listQuery.limit
      this.queryparams.page = val
      this.getLab_Test_ItemList(this.queryparams)
    },
    handleSelect(key, keyPath) {
      const isLab = key.includes('_L')
      if (isLab) {
        this.queryparams.itemcode = key.substring(0, key.length - 2)
        this.getLab_Test_ItemList(this.queryparams)
        this.tableVisible = true
      } else {
        this.queryparams.itemcode = key.substring(0, key.length - 2)
        this.tableVisible = false
        this.getExam_Master(this.queryparams)
      }
    },
    rowClick(row, event, column) {
      this.getLab_Result(row.master)
    },
    exam_rowClick(row, event, column) {
      this.getExam_Report(row.id)
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      if (date === null) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getLab_menu(this.queryparams)
    this.getExam_menu(this.queryparams)
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
    .el-menu-item:hover{
        outline: 0 !important;
        color: white !important;
        background: #409EFF !important;
    }
    .el-menu-item.is-active {
        color: white !important;
        background: black !important;
    }
    .el-submenu__title:focus, .el-submenu__title:hover{
        outline: 0 !important;
        color: white !important;
        background: #409EFF !important;
    }
    .el-submenu>.el-submenu__title .el-submenu__icon-arrow{
      -webkit-transform: rotateZ(-90deg);
      -ms-transform: rotate(-90deg);
      transform: rotateZ(-90deg);
      margin-right: 25px;
    }
    .el-submenu.is-opened>.el-submenu__title .el-submenu__icon-arrow{
      -webkit-transform: rotateZ(0deg);
      -ms-transform: rotate(0deg);
      transform: rotateZ(0deg);
      margin-right: 25px;
    }
</style>
