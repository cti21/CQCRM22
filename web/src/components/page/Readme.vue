<template>
    <div>
        <el-row :gutter="40" class="panel-group">
          <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
            <div class="card-panel" @click="handleSetLineChartData('newVisitis')">
              <div class="card-panel-icon-wrapper icon-people">
                <svg-icon icon-class="peoples" class-name="card-panel-icon" />
              </div>
              <div class="card-panel-description">
                <div class="card-panel-text">
                  新增客户
                </div>
                <count-to :start-val="0" :end-val="102400" :duration="2600" class="card-panel-num" />
              </div>
            </div>
          </el-col>
          <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
            <div class="card-panel" @click="handleSetLineChartData('messages')">
              <div class="card-panel-icon-wrapper icon-message">
                <svg-icon icon-class="message" class-name="card-panel-icon" />
              </div>
              <div class="card-panel-description">
                <div class="card-panel-text">
                  消息
                </div>
                <count-to :start-val="0" :end-val="81212" :duration="3000" class="card-panel-num" />
              </div>
            </div>
          </el-col>
          <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
            <div class="card-panel" @click="handleSetLineChartData('purchases')">
              <div class="card-panel-icon-wrapper icon-money">
                <svg-icon icon-class="money" class-name="card-panel-icon" />
              </div>
              <div class="card-panel-description">
                <div class="card-panel-text">
                  订单金额
                </div>
                <count-to :start-val="0" :end-val="9280" :duration="3200" class="card-panel-num" />
              </div>
            </div>
          </el-col>
          <el-col :xs="12" :sm="12" :lg="6" class="card-panel-col">
            <div class="card-panel" @click="handleSetLineChartData('shoppings')">
              <div class="card-panel-icon-wrapper icon-shopping">
                <svg-icon icon-class="shopping" class-name="card-panel-icon" />
              </div>
              <div class="card-panel-description">
                <div class="card-panel-text">
                  订单
                </div>
                <count-to :start-val="0" :end-val="13600" :duration="3600" class="card-panel-num" />
              </div>
            </div>
          </el-col>
        </el-row>
        <el-row style="background:#fff;padding:16px 16px 0;margin-bottom:20px;">
          <line-chart :chart-data="lineChartData" />
        </el-row>
        <!--<el-row style="background:#fff;padding:16px 16px 0;margin-bottom:20px;">-->
          <!--<div style="width:100%;height: 200px">-->
            <!--<el-steps :active="1">-->
              <!--<el-step title="签到" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="制定透析方案" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="开立医嘱" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="审核透析方案" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="审核执行医嘱" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="填写透析记录单" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="透析评估" description="这是一段很长很长很长的描述性文字"></el-step>-->
              <!--<el-step title="透析结束" description="这是一段很长很长很长的描述性文字"></el-step>-->
            <!--</el-steps>-->
          <!--</div>-->
        <!--</el-row>-->
        <!--<ve-line style="width: 800px;height: 400px" :data="chartData"></ve-line>-->
        <!--<ve-pie style="width: 800px;height: 400px" :data="chartData"></ve-pie>-->
    </div>
</template>

<script>
import LineChart from '@/components/LineChart'
import CountTo from 'vue-count-to'
import { txtypeBymonthData } from '@/api/analysis'
//import { products, createProduct, updateProduct } from '@/api/login'
import VeLine from 'v-charts/lib/line'
import VePie from 'v-charts/lib/pie'
import { getToken } from '@/utils/auth'
import moment from 'moment'
import ElCol from 'element-ui/packages/col/src/col'
import ElRow from 'element-ui/packages/row/src/row'
import * as signin from '@/permission/signin'
const lineChartData = {
  newVisitis: {
    expectedData: [100, 120, 161, 134, 105, 160, 165],
    actualData: [120, 82, 91, 154, 162, 140, 145]
  },
  messages: {
    expectedData: [200, 192, 120, 144, 160, 130, 140],
    actualData: [180, 160, 151, 106, 145, 150, 130]
  },
  purchases: {
    expectedData: [80, 100, 121, 104, 105, 90, 100],
    actualData: [120, 90, 100, 138, 142, 130, 130]
  },
  shoppings: {
    expectedData: [130, 140, 141, 142, 145, 150, 160],
    actualData: [120, 82, 91, 154, 162, 140, 130]
  }
}

export default {
  components: {
    ElRow,
    ElCol,
    VeLine,
    VePie,
    CountTo,
    LineChart
  },
  data: function() {
    return {
      lineChartData: lineChartData.newVisitis,
      chartData: {
        columns: ['月份', '血液透析', '血流灌注', '血透血灌', '血浆置换'],
        rows: []
      },
      signin: signin,
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
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      sheng: '北京',
      leixing: 'good',
      sex: '男',
      product: {
        id: undefined,
        name: '',
        describe: '',
        created: new Date(),
        price: ''
      },
      rules: {
        name: [{
          required: true,
          message: '名称不能为空',
          trigger: 'blur'
        }],
        describe: [{
          required: true,
          message: '描述不能为空',
          trigger: 'change'
        }]
      }
    }
  },
  methods: {
    getTxTypeBymonthData(data) {
      txtypeBymonthData(data).then(response => {
        const res = response.data
        this.chartData.rows = res
      })
    },
//    getProductList() {
//      products(this.listQuery).then(response => {
//        this.listLoading = true
//        this.list = response.data.results
//        this.total = response.data.count
//        this.listLoading = false
//      }).catch(error => {
//        console.log(error)
//      })
//    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      //this.getProductList()
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      //this.getProductList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      //this.getProductList()
    },
    resetProduct() {
      this.product = {
        id: undefined,
        name: '',
        describe: '',
        created: new Date(),
        price: ''
      }
    },
    handleCreate() {
      this.resetProduct()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
//    createData() {
//      this.$refs.dataForm.validate((valid) => {
//        if (valid) {
//          this.product.id = parseInt(Math.random() * 100) + 1024 // mock a id
//          createProduct(this.product).then(() => {
//            this.list.unshift(this.product)
//            this.dialogFormVisible = false
//            this.$notify({
//              title: '成功',
//              message: '创建成功',
//              type: 'success',
//              duration: 2000
//            })
//          })
//        }
//      })
//    },
    handleUpdate(row) {
      this.product = Object.assign({}, row) // copy obj
      this.product.created = new Date(this.product.created)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
//    updateData() {
//      this.$refs['dataForm'].validate((valid) => {
//        if (valid) {
//          const tempData = Object.assign({}, this.product)
//          tempData.created = +new Date(tempData.created) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
//          updateProduct(tempData).then(() => {
//            for (const v of this.list) {
//              if (v.id === this.product.id) {
//                const index = this.list.indexOf(v)
//                this.list.splice(index, 1, this.product)
//                break
//              }
//            }
//            this.dialogFormVisible = false
//            this.$notify({
//              title: '成功',
//              message: '更新成功',
//              type: 'success',
//              duration: 2000
//            })
//          })
//        }
//      })
//    },
    handleDelete(row) {
      this.$notify({
        title: '成功',
        message: '删除成功',
        type: 'success',
        duration: 2000
      })
      const index = this.list.indexOf(row)
      this.list.splice(index, 1)
    },
    // 时间格式化
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    //this.getProductList()
    //this.getTxTypeBymonthData('2018')
  }
}
</script>

<style lang="scss" scoped>
  .panel-group {
    margin-top: 18px;
    .card-panel-col {
      margin-bottom: 32px;
    }
    .card-panel {
      height: 108px;
      cursor: pointer;
      font-size: 12px;
      position: relative;
      overflow: hidden;
      color: #666;
      background: #fff;
      box-shadow: 4px 4px 40px rgba(0, 0, 0, .05);
      border-color: rgba(0, 0, 0, .05);
      &:hover {
        .card-panel-icon-wrapper {
          color: #fff;
        }
        .icon-people {
          background: #40c9c6;
        }
        .icon-message {
          background: #36a3f7;
        }
        .icon-money {
          background: #f4516c;
        }
        .icon-shopping {
          background: #34bfa3
        }
      }
      .icon-people {
        color: #40c9c6;
      }
      .icon-message {
        color: #36a3f7;
      }
      .icon-money {
        color: #f4516c;
      }
      .icon-shopping {
        color: #34bfa3
      }
      .card-panel-icon-wrapper {
        float: left;
        margin: 14px 0 0 14px;
        padding: 16px;
        transition: all 0.38s ease-out;
        border-radius: 6px;
      }
      .card-panel-icon {
        float: left;
        font-size: 48px;
      }
      .card-panel-description {
        float: right;
        font-weight: bold;
        margin: 26px;
        margin-left: 0px;
        .card-panel-text {
          line-height: 18px;
          color: rgba(0, 0, 0, 0.45);
          font-size: 16px;
          margin-bottom: 12px;
        }
        .card-panel-num {
          font-size: 20px;
        }
      }
    }
  }
  @media (max-width:550px) {
    .card-panel-description {
      display: none;
    }
    .card-panel-icon-wrapper {
      float: none !important;
      width: 100%;
      height: 100%;
      margin: 0 !important;
      .svg-icon {
        display: block;
        margin: 14px auto !important;
        float: none !important;
      }
    }
  }
</style>
