<template>
    <div>
        <div class="filter-container">
              <el-select v-model="reportType" multiple collapse-tags class="myInput" clearable style="width: 180px;margin-right: 10px"  placeholder="报表类型">
                <el-option v-for="item in reportSelect" :key="item.id" :value="item.name" :label="item.name">
                </el-option>
              </el-select>
              <el-date-picker v-model="startyear" style="width: 145px" class="myInput" type="year" placeholder="输入起始年份" value-format="yyyy">
              </el-date-picker>
              <el-date-picker v-model="endyear" style="width: 145px" class="myInput" type="year" placeholder="输入结束年份" value-format="yyyy">
              </el-date-picker>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <!--<el-button size="small" style="margin-left: 20px"type="primary" @click="handleReset" icon="el-icon-download">重置</el-button>-->
              <el-button size="small" style="margin-left: 20px"type="success" @click="exportExcel" icon="el-icon-upload">导出</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            v-loading="listLoading"
            :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            id="outTable"
            :span-method="cellMerge">
            <el-table-column v-for="col in cols" :prop="col.prop" :key="col.prop" :label="col.label" align="center" border show-overflow-tooltip>
            </el-table-column>
          </el-table>
        </div>
    </div>
</template>

<script>
import FileSaver from 'file-saver'
import XLSX from 'xlsx'
import { analyseBykind } from '@/api/analysis'
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
  data: function() {
    return {
      rowcount:[],
      mergecount:[],
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
      spanArr: [],
      pos: 0,
      colCount: 0,
      reportType: [],
      reportSelect: [
        { id: '1', name: '付费方式' },
        { id: '2', name: '血管通路' },
        { id: '3', name: '透析方式' }
      ],
      startyear: '',
      endyear: '',
      token: getToken,
      queryparams: {
        startyear: '',
        endyear: '',
        multisel: ''
      }
    }
  },
  methods: {
    getAnalyseBykind(data) {
      analyseBykind(data).then(response => {
        this.listLoading = true
        this.list = response.data
        if (this.list.length > 0) {
          this.makeTableHeader(this.list[0])
          this.getSpanArr(this.list)
        }
        this.total = 10000
        this.listLoading = false
      })
    },
    handleReset() {
      this.queryparams.startyear = ''
      this.startyear = ''
      this.queryparams.endyear = ''
      this.endyear = ''
      this.queryparams.multisel = ''
      this.reportType = []
      this.getAnalyseBykind(this.queryparams)
    },
    handleFilter() {
      this.queryparams.startyear = this.startyear
      this.queryparams.endyear = this.endyear
      this.queryparams.multisel = this.reportType.join(',')
      this.getAnalyseBykind(this.queryparams)
    },
    makeTableHeader(data) {
      this.colCount = 0
      this.cols = []
      if (data) {
        let s
        for (const key in data) {
          this.colCount = this.colCount + 1
          if (key === 'catagory') {
            s = '类别'
          } else if (key === 'feetype') {
            s = '子类'
          } else if (key === 'total') {
            s = '小计'
          } else if (key === 'sum') {
            s = '合计'
          } else {
            s = key.substring(1)
          }
          this.cols.push({
            prop: key,
            label: s
          })
        }
      }
    },
    getSpanArr(data) {
      this.spanArr = []
      for (var i = 0; i < data.length; i++) {
        if (i === 0) {
          this.spanArr.push(1)
          this.pos = 0
        } else {
          // 判断当前元素与上一个元素是否相同
          if (data[i].catagory === data[i - 1].catagory) {
            this.spanArr[this.pos] += 1
            this.spanArr.push(0)
          } else {
            this.spanArr.push(1)
            this.pos = i
          }
        }
      }
    },
    cellMerge({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0 || columnIndex === this.colCount - 1) {
        const _row = this.spanArr[rowIndex]
        const _col = _row > 0 ? 1 : 0
        return {
          rowspan: _row,
          colspan: _col
        }
      }
    },
    exportExcel() {
      const wb = XLSX.utils.table_to_book(document.querySelector('#outTable'))
      const wbout = XLSX.write(wb, { bookType: 'xlsx', bookSST: true, type: 'array' })
      try {
        FileSaver.saveAs(new Blob([wbout], { type: 'application/octet-stream' }), '分类统计表.xlsx')
      } catch (e) {
        if (typeof console !== 'undefined') {
          console.log(e, wbout)
        }
      }
      return wbout
    }
  },
  created: function() {
    this.queryparams.startyear = ''
    this.queryparams.endyear = ''
    this.queryparams.multisel = ''
    this.getAnalyseBykind(this.queryparams)
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
