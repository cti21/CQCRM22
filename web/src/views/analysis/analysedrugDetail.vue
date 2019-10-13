<template>
    <div>
        <div class="filter-container">
              <el-date-picker v-model="Startyear" class="myInput"  placeholder="输入开始日期" value-format="yyyy-MM-dd">
              </el-date-picker>
              <el-date-picker v-model="Endyear" class="myInput"  placeholder="输入结束日期" value-format="yyyy-MM-dd">
              </el-date-picker>
              <el-button size="small" style="margin-left: 20px" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <!--<el-button size="small" style="margin-left: 20px"type="primary" @click="handleReset" icon="el-icon-download">重置</el-button>-->
              <el-button size="small" style="margin-left: 20px"type="success" @click="exportExcel" icon="el-icon-upload">导出</el-button>
        </div>
        <el-container>
          <el-aside width="250px">
            <div style="margin-top: 20px">
              <el-table
                :data="list"
                v-loading="listLoading"
                :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
                :header-cell-style="{background:'#F8F8F8'}"
                stripe
                border
                @row-click="rowClick">
                <el-table-column prop="name" label="医嘱项目" align="center">
                </el-table-column>
                <el-table-column prop="total" label="数量" align="center" width="50">
                </el-table-column>
                <el-table-column prop="id" v-if="false">
                </el-table-column>
              </el-table>
            </div>
          </el-aside>
          <el-main>
            <div style="margin-top: 0px">
              <el-table
                :data="detai_list"
                :header-cell-style="{background:'#F8F8F8'}"
                stripe
                id="outTable"
                border>
                <el-table-column type="index" label="序号"  width="100" align="center">
                </el-table-column>
                <el-table-column prop="bedname" label="床号" width="100" align="center">
                </el-table-column>
                <el-table-column prop="patientname" label="透析患者" width="140" align="center">
                </el-table-column>
                <el-table-column prop="executedate" label="医嘱时间" width="180" :formatter="datetimeFormat" align="center">
                </el-table-column>
                <el-table-column prop="drugname" label="医嘱项目" width="140" align="center">
                </el-table-column>
                <el-table-column prop="dw" label="单位" width="120" align="center">
                </el-table-column>
                <el-table-column prop="count" label="数量" width="120" align="center">
                </el-table-column>
              </el-table>
            </div>
          </el-main>
        </el-container>
    </div>
</template>

<script>
import FileSaver from 'file-saver'
import XLSX from 'xlsx'
import { analysedrug, analysedrugDetail } from '@/api/analysis'
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
      detai_list: null,
      detai_total: null,
      Startyear: '',
      Endyear: '',
      token: getToken,
      queryparams: {
        id: '',
        Startyear: '',
        Endyear: ''
      },
      cols: []
    }
  },
  methods: {
    getAnalysedrug(data) {
      analysedrug(data).then(response => {
        this.listLoading = true
        this.list = response.data
        // if (this.list.length > 0) {
        //    this.makeTableHeader(this.list[0])
        // }
        this.total = 10000
        this.listLoading = false
      })
    },
    getAnalysedrugDetail(data) {
      analysedrugDetail(data).then(response => {
        this.detai_list = response.data
        this.detai_total = 10000
      })
    },
    handleReset() {
      this.queryparams.Startyear = ''
      this.Startyear = ''
      this.queryparams.Endyear = ''
      this.Endyear = ''
      this.getAnalysedrug(this.queryparams)
    },
    handleFilter() {
      this.queryparams.Startyear = this.Startyear
      this.queryparams.Endyear = this.Endyear
      this.getAnalysedrug(this.queryparams)
    },
    rowClick(row, event, column) {
      this.queryparams.Startyear = this.Startyear
      this.queryparams.Endyear = this.Endyear
      this.queryparams.id = row.id
      this.getAnalysedrugDetail(this.queryparams)
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
    },
    datetimeFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      } else if (date === '') {
        return ''
      } else if (date === null) {
        return ''
      } else {
        return moment(date).format('YYYY-MM-DD HH:mm:ss')
      }
    }
  },
  created: function() {
    this.queryparams.Startyear = ''
    this.queryparams.Endyear = ''
    this.getAnalysedrug(this.queryparams)
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
