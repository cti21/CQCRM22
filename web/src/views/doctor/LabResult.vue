<template>
    <div style="background-color: #f0f2f5">
        <el-container style="border: 1px solid #eee;">
          <el-aside width="320px" style="padding: 5px;background-color: #ffffff">
          <div>
              <el-row style="margin-bottom: 10px;margin-top: 20px">
                <label style="font-size: 14px;color: #606266;">搜索条件</label>
              </el-row>
              <el-row style="margin-bottom: 20px;margin-left: 35px;">
                <label style="font-size: 14px;color: #606266;">最近</label>
                <el-input-number v-model="num" :min="5" style="width: 120px" :max="10" class="myInput" label="描述文字">
                </el-input-number>
                <label style="font-size: 14px;color: #606266;">条记录</label>
              </el-row>
              <el-row style="margin-bottom: 10px;margin-left: 30px;">
                <el-select
                  v-model="reason"
                  clearable
                  style="width: 240px;"
                  @change="selectChange"
                  class="myInput"
                  placeholder="请选择检验项目">
                  <el-option v-for="item in reasonSelect" :key="item.id" :value="item.id" :label="item.name">
                  </el-option>
                </el-select>
              </el-row>

          </div>
          <div style="margin-top: 30px">
            <el-table
              :data="list"
              v-loading="listLoading"
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              highlight-current-row
              @row-click="rowClick">
              <el-table-column type="index" label="序号" width="50" align="center">
              </el-table-column>
              <el-table-column prop="name" label="项目名称" align="center">
              </el-table-column>
              <el-table-column prop="id" v-if="false">
              </el-table-column>
            </el-table>
          </div>
          </el-aside>
          <el-main style="background-color: #ffffff">
             <el-table
               :data="chartData.rows"
               :header-cell-style="{background:'#F8F8F8'}"
               stripe
               highlight-current-row>
                  <el-table-column type="index" label="序号" width="60" align="center">
                  </el-table-column>
                  <el-table-column prop="日期" label="日期" align="center">
                  </el-table-column>
                  <el-table-column :prop="queryparams.itemname" :label="queryparams.itemname" align="center">
                  </el-table-column>
             </el-table>
             <ve-line style="margin-left: 10px;width: 600px;height: 400px" :data="chartData"></ve-line>
          </el-main>
        </el-container>
    </div>
</template>

<script>
import FileSaver from 'file-saver'
import XLSX from 'xlsx'
import { getLabreason, getLabItems, analyseLabResultData } from '@/api/doctor'
import VeLine from 'v-charts/lib/line'
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
    VeLine
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
      chartData: {
        columns: ['日期', 'pth'],
        rows: []
      },
      detai_list: null,
      detai_total: null,
      num: 5,
      reason: '',
      reasonSelect: [],
      token: getToken,
      queryparams: {
        page: 1,
        id: '',
        patientid: this.patientid,
        itemname: '',
        reason: '',
        num: 0
      },
      cols: []
    }
  },
  methods: {
    getLabResultData(data) {
      analyseLabResultData(data).then(response => {
        this.chartData.rows = response.data
      })
    },
    getReason(data) {
      getLabreason(data).then(response => {
        this.reasonSelect = response.data
      })
    },
    getItems(data) {
      getLabItems(data).then(response => {
        this.list = response.data
        this.total = 10000
      })
    },
    handleReset() {
      this.queryparams.num = 0
      this.num = 0
      this.queryparams.reason = ''
      this.reason = ''
      this.getItems(this.queryparams)
    },
    selectChange: function(val) {
      this.reason = val
      console.log(val)
      this.queryparams.reason = val
      this.getItems(this.queryparams)
    },
    rowClick(row, event, column) {
      this.queryparams.reason = this.reason
      this.queryparams.num = this.num
      this.queryparams.id = row.id
      this.queryparams.itemname = row.name
      this.chartData.columns[1] = row.name
      this.getLabResultData(this.queryparams)
    },
    makeTableHeader(data) {
      this.cols = []
      if (data) {
        let s
        for (const key in data) {
          if (key === 'time') {
            s = '月份'
          } else if (key === 'total') {
            s = '合计'
          } else {
            s = key
          }
          this.cols.push({
            prop: key,
            label: s
          })
        }
      }
    },
    exportExcel() {
      const wb = XLSX.utils.table_to_book(document.querySelector('#outTable'))
      const wbout = XLSX.write(wb, { bookType: 'xlsx', bookSST: true, type: 'array' })
      try {
        FileSaver.saveAs(new Blob([wbout], { type: 'application/octet-stream' }), '透析方式统计表.xlsx')
      } catch (e) {
        if (typeof console !== 'undefined') {
          console.log(e, wbout)
        }
      }
      return wbout
    }
  },
  created: function() {
    this.queryparams.num = 0
    this.queryparams.reason = this.reason
    this.queryparams.patientid = this.patientid
    this.getReason(this.queryparams)
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
