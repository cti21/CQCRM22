<template>
    <div>
        <!--<div class="filter-container">-->
              <!--<el-select v-model="arrangeSelect" clearable style="width: 90px" class="myInput" placeholder="班次">-->
                <!--<el-option label="上午班" value="1" key="1" >-->
                <!--</el-option>-->
                <!--<el-option label="下午班" value="2" key="2"  >-->
                <!--</el-option>-->
              <!--</el-select>-->
              <!--<el-select v-model="diseaseAreaSelect" clearable style="width: 90px" class="myInput" placeholder="病区">-->
                <!--<el-option label="一病区" value="1" >-->
                <!--</el-option>-->
                <!--<el-option label="二病区" value="2" >-->
                <!--</el-option>-->
              <!--</el-select>-->
              <!--<el-date-picker v-model="signeddate"  class="myInput" type="date" placeholder="签到日期">-->
              <!--</el-date-picker>-->
              <!--<el-button class="filter-item" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>-->
              <!--<el-button class="filter-item" type="primary"  icon="el-icon-download">重置</el-button>-->
        <!--</div>-->

        <div>
          <el-table
            :data="list"
            v-loading="listLoading"
            :header-cell-style="{background:'#F8F8F8'}"
            show-summary
            :summary-method="getTotal"
            stripe>
            <el-table-column type="index" label="序号"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="yztype" label="类型" width="60" align="center">
            </el-table-column>
            <el-table-column prop="name" label="医嘱" width="100" align="center">
            </el-table-column>
            <el-table-column prop="count" label="单次剂量" width="80" align="center">
            </el-table-column>
            <el-table-column prop="dw" label="剂量单位" width="80" align="center">
            </el-table-column>
            <el-table-column prop="gg" label="规格" width="50" align="center">
            </el-table-column>
            <el-table-column prop="price" label="单价" width="80" align="center">
            </el-table-column>
            <el-table-column prop="costs" label="总费用" width="80" align="center">
            </el-table-column>
            <el-table-column prop="charges" label="应收费" width="80" align="center">
            </el-table-column>
          </el-table>
          <div style="margin-top: 10px;margin-right: 40px">
              <el-button size="mini" @click="closeDialog">返回</el-button>
          </div>
        </div>

    </div>
</template>

<script>
import { outp_bill_items, updateOutp_rcpt_master } from '@/api/expense'
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
  name: 'drug',
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
    masterid: Number,
    flag: Number,
    list: Array
  },
  data: function() {
    return {
      total: null,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 10000,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      checked: false,
      hctype: '',
      hcname: '',
      arrangeSelect: '',
      diseaseAreaSelect: '',
      signeddate: '',
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      master_obj: {
        id: null,
        register: '',
        flag: 0
      },
      params: {
        page: 1,
        name: ''
      }
    }
  },
  methods: {
    getDrug(data) {
      outp_bill_items(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    submitData() {
      if (this.list.length > 0) {
        this.master_obj.id = this.masterid
        this.master_obj.register = 'fae5e64a764d47c78ddbb73cea03a48f'
        this.master_obj.flag = this.flag
        updateOutp_rcpt_master(this.master_obj).then(() => {
          this.$notify({
            title: '成功',
            message: '提交成功',
            type: 'success',
            duration: 2000
          })
          this.closeDialog()
        })
      }
    },
    getTotal(param) {
      const { columns, data } = param
      const sums = []
      columns.forEach((column, index) => {
        if (index === 0) {
          sums[index] = '合计'
          return
        }
        const values = data.map(item => Number(item[column.property]))
        let name = column.property
        if (name === 'count' || name === 'costs' || name === 'charges') {
          sums[index] = values.reduce((prev, curr) => {
            const value = Number(curr)
            if (!isNaN(value)) {
              return prev + curr
            }
            else {
              return prev
            }
          }, 0)
          sums[index]
        }
        else {
          sums[index] = ''
        }
      })
      return sums
    },
    closeDialog() {
      this.$emit('listenToChildEvent','colse')
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
