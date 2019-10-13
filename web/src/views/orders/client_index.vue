<template>
    <div>
        <el-container>
          <el-aside id="personInfo" width="260px" style="background-color: #f0f2f5;padding: 0px 0px 0px 0px;display: block;">
              <div style="height:100%;background-color: #ffffff">
                  <el-row style="margin-bottom: 20px">
                    <el-input
                      v-model="listQuery.name"
                      class="myInput"
                      clearable
                      style="width: 80%;margin-left: 20px"
                      clearable
                      prefix-icon="el-icon-search"
                      placeholder="请输入姓名或手机">
                    </el-input>
                  </el-row>
                  <el-row style="margin-bottom: 20px">
                      <el-select
                        v-model="listQuery.clienttype" clearable
                        style="width:80%;margin-left: 20px"
                        @change="selectChange"
                        class="myInput"
                        placeholder="请选择客户类型">
                          <el-option v-for="item in clienttypeSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                  </el-row>
                  <el-row style="margin-bottom: 20px">
                    <el-date-picker
                        v-model="listQuery.indate"
                        style="width:80%;margin-left: 20px"
                        class="myInput"
                        type="date"
                        @change="dateChange"
                        clearable
                        placeholder="入院日期"
                        value-format="yyyy-MM-dd">
                      </el-date-picker>
                  </el-row>
                  <el-table
                    :data="list"
                    :header-cell-style="{background:'#F8F8F8'}"
                    :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
                    stripe
                    highlight-current-row
                    @row-click="rowClick"
                    style="width: 255px;margin: 5px;"
                  >
                    <el-table-column type="index" label="序号"  width="60" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="姓名" width="80"  align="center">
                    </el-table-column>
                    <el-table-column prop="clienttype" label="类型" width="90"  align="center">
                    </el-table-column>
                  </el-table>
                  <div class="pagination-container" align="center">
                    <el-pagination background
                         @current-change="handleCurrentChange"
                         :current-page="listQuery.page"
                         :page-size="listQuery.limit"
                         layout="prev, pager, next"
                         :total="total">
                    </el-pagination>
                  </div>
            </div>
          </el-aside>
          <el-container>
            <el-main style="margin-top: 0px;background-color: #f0f2f5">
              <div width="100%"
                   style="height:100%;background-color: #ffffff"
                   :visible.sync="detailVisible"
              >
                <div style="float: left;margin-top: 10px;cursor:pointer" @click="toggleShow">
                  <i id="img_arrow" class="el-icon-arrow-left"></i>
                </div>
                <div style="margin-left: 10px;">
                  <clienttabs :clientid="clientid" :register_id="registerid" :num="num"></clienttabs>
                </div>
              </div>
            </el-main>
          </el-container>
        </el-container>
    </div>
</template>

<script>
import { formatDate } from '@/utils/date'
import { client_registers } from '@/api/client'
import { getAllSelectData } from '@/api/order'
import clienttabs from '@/views/orders/client_tabs.vue'
import moment from 'moment'
import ElCol from 'element-ui/packages/col/src/col'
import ElRow from 'element-ui/packages/row/src/row'
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
    ElRow,
    ElCol,
    clienttabs
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
        clientid: null,
        clienttype: null,
        indate: formatDate(new Date(), 'yyyy-MM-dd'),
        sort: '+id'
      },
      clientid: '',
      registerid: '',
      clienttypeSelect: [],
      num: 0,
      detailVisible: false,
      isShow: 'clienttabs',
      scname: '',
      indate: '',
      clickNum: 0,
      queryparams: {
        page: 1,
        code: 1,
        rq: ''
      }
    }
  },
  methods: {
    getClient_register(data) {
      client_registers(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    rowClick(row) {
      this.registerid = row.id
      this.clientid = row.client
      this.num = this.num + 1
    },
    selectChange(val) {
      console.log('listQuery', this.listQuery)
      this.getClient_register(this.listQuery)
    },
    dateChange(val) {
      console.log('listQuery', this.listQuery)
      this.getClient_register(this.listQuery)
    },
    handleFilter(par) {
    },
    handleCurrentChange() {
    },
    toggleShow() {
      if (document.getElementById('personInfo').style.display === 'none') {
        document.getElementById('personInfo').style.display = 'block'
        document.getElementById('img_arrow').style.transform = 'rotateZ(0deg)'
      } else {
        document.getElementById('personInfo').style.display = 'none'
        document.getElementById('img_arrow').style.transform = 'rotateZ(180deg)'
      }
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
    getAllSelectData(this.listQuery).then(res => {
      this.clienttypeSelect = res.data.clienttype
    })
    this.getClient_register(this.listQuery)
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
    .el-main {
        padding: 0px 0 0 2px;
    }
</style>
