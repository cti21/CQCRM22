<template>
    <div>
        <div style="margin-top: 10px;width: 90%" class="block">
            <el-form :model="touxi" ref="touxi_dataForm"  label-position="left" style='width:100%; margin-left:25px;margin-top: 10px' size="small">
              <el-row type="flex" justify="end">
                 <el-col :span="6">
                    <el-form-item label="医嘱状态:">
                      <div v-if="touxi.state =='0'">未审核</div>
                      <div v-else-if="touxi.state =='1'" style="color: red">已审核</div>
                      <div v-else-if="touxi.state =='2'" style="color: red">已执行</div>
                      <div v-else-if="touxi.state =='3'" style="color: red">已撤销</div>
                      <div v-else style="color: red"></div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="6">
                    <el-form-item label="处方名：">
                      <div>{{touxi.txtype}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="6">
                    <el-form-item label="审核护士:">
                      <div>{{touxi.checknur}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="6">
                   <el-form-item label="执行护士:">
                      <div>{{touxi.executenur}}</div>
                    </el-form-item>
                 </el-col>
              </el-row>
              <el-row type="flex" justify="end">
                 <el-col :span="6">
                    <el-form-item label="透析方式:" prop="txtype">
                      <div>{{touxi.txtype}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="6">
                   <el-form-item label="透析时长(h):" prop="period">
                      <div>{{touxi.period}}</div>
                   </el-form-item>
                 </el-col>
                 <el-col :span="12">
                    <el-form-item label="血管通路:" prop="xueguantonglu">
                      <div>
                        <div style="float: left;margin-left: 30px;">{{touxi.xueguantonglu}}</div>
                        <div style="float: left;margin-left: 30px;">{{touxi.xueguantype}}</div>
                      </div>
                    </el-form-item>
                 </el-col>
               </el-row>
              <el-row  type="flex" justify="end">
                <el-col :span="8">
                    <el-form-item label="血透器:" prop="xuetoudevice">
                      <div>{{touxi.xuetoudevice}}</div>
                    </el-form-item>
                 </el-col>
                <el-col :span="8">
                    <el-form-item label="血滤器:" prop="xuetoudevice">
                      <div>{{touxi.xuelvdevice}}</div>
                    </el-form-item>
                 </el-col>
                <el-col :span="8">
                    <el-form-item label="灌流器:" prop="guanliudevice">
                      <div>{{touxi.guanliudevice}}</div>
                    </el-form-item>
                 </el-col>
              </el-row>
              <el-row type="flex">
                 <el-col :span="8">
                   <el-form-item label="周频次:" prop="week">
                      <div>{{touxi.week}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="次数:" prop="times">
                      <div>{{touxi.times}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                    <el-form-item label="医生">
                      <div>{{touxi.cancellnur}}</div>
                    </el-form-item>
                 </el-col>
               </el-row>
               <el-row type="flex">
                 <el-col :span="5">
                   <el-form-item label="钙(mmol/l):" prop="ca">
                      <div>{{touxi.ca}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="5">
                   <el-form-item label="钾(mmol/l):" prop="k">
                      <div>{{touxi.k}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="6">
                   <el-form-item label="钠(mmol/l):" prop="na">
                      <div>{{touxi.na}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="6">
                   <el-form-item label="碳酸氢根(mmol/l):" prop="hco3">
                      <div>{{touxi.hco3}}</div>
                    </el-form-item>
                 </el-col>
               </el-row>
               <el-row type="flex">
                 <el-col :span="8">
                   <el-form-item label="透析液流量(ml/mimn):" prop="touxiyeliuliang">
                      <div>{{touxi.touxiyeliuliang}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="血流量(ml/mimn):" prop="xueliuliang">
                      <div>{{touxi.xueliuliang}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="抗凝剂(mg):" prop="kangning">
                      <div>{{touxi.kangning}}</div>
                    </el-form-item>
                 </el-col>
               </el-row>
               <el-row type="flex">
                 <el-col :span="8">
                   <el-form-item label="首剂(mg):" prop="shouji">
                      <div>{{touxi.shouji}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="追加(mg/h):" prop="zhuijia">
                      <div>{{touxi.zhuijia}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="总量(mg/h):" prop="total">
                      <div>{{touxi.total}}</div>
                    </el-form-item>
                 </el-col>
               </el-row>
               <el-row type="flex">
                 <el-col :span="8">
                   <el-form-item label="透前体重:" prop="weight">
                      <div>{{touxi.weight}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="干体重:" prop="gantizhong">
                      <div>{{touxi.gantizhong}}</div>
                    </el-form-item>
                 </el-col>
                 <el-col :span="8">
                   <el-form-item label="超滤量:" prop="chaolvliang">
                      <el-input v-model="touxi.chaolvliang" type="number" class="myInput" style="width:80px"></el-input>
                    </el-form-item>
                 </el-col>
               </el-row>
               <el-row>
                     <el-col :span="8">
                        <el-form-item label="审核人" prop="checkNur_id">
                          <el-select v-model="touxi.checkNur_id" clearable style="width: 120px" class="myInput">
                            <el-option v-for="item in nurseSelect" :key="item.id" :value="item.id" :label="item.username">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8">
                        <el-form-item label="执行人" prop="exeNur_id">
                          <el-select v-model="touxi.exeNur_id" clearable style="width: 120px" class="myInput">
                            <el-option v-for="item in nurseSelect" :key="item.id" :value="item.id" :label="item.username">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
          </el-form>
          <div slot="footer" align="center" style="margin-bottom: 10px">
            <el-button size="small" onclick="window.history.go(-1)" icon="el-icon-plus">关闭</el-button>
            <el-button
              size="small"
              type="primary"
              icon="el-icon-check"
              v-if="touxi.state =='0'"
              @click="updatetouxiData(5)"
            >保存
            </el-button>
            <el-button
              size="small"
              type="primary"
              icon="el-icon-check"
              v-if="touxi.state =='0'"
              @click="updatetouxiData(2)"
            >审核
            </el-button>
            <el-button
              size="small"
              type="primary"
              icon="el-icon-check"
              v-if="touxi.state =='1'"
              @click="updatetouxiData(3)"
            >执行
            </el-button>
          </div>
        </div>
    </div>
</template>

<script>
import { get_touxi, updateyz_touxi, getNurses } from '@/api/login'
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
  name: 'touxi',
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
  props: ['regid', 'num'],
  data: function() {
    return {
      dialogStatus: 'create',
      touxi_dialogFormVisible: true,
      checkNur_id: '',
      exeNur_id: '',
      nurseSelect: [],
      touxi: {
        id: '',
        yzlinshi: {
          id: '',
          register_id: ''
        },
        checknur: '',
        executenur: '',
        cancellnur: '',
        chaolvliang: '',
        week: '',
        times: '',
        txtype: '',
        period: '',
        xueguantonglu: '',
        xueguantype: '',
        touxidevice: '',
        xuetoudevice: '',
        xuelvdevice: '',
        guanliudevice: '',
        touxiyeliuliang: '',
        xueliuliang: '',
        ca: '',
        k: '',
        na: '',
        hco3: '',
        kangning: '',
        shouji: '',
        zhuijia: '',
        total: '',
        state: '',
        checkNur_id: '',
        exeNur_id: '',
        action: ''
      },
    }
  },
  methods: {
    getTouxi(data) {
      get_touxi(data).then(response => {
        const datalist = response.data.results
        console.log(datalist)
        if (datalist.length > 0) {
          this.touxi = datalist[0]
          this.dialogStatus = 'update'
          this.$nextTick(() => {
            this.$refs['touxi_dataForm'].clearValidate()
          })
        }
      })
    },
    getNurseList(data) {
      getNurses(data).then(response => {
        this.nurseSelect = response.data
        console.log(this.nurseSelect)
      })
    },
    updatetouxiData(flag) {
      this.$refs['touxi_dataForm'].validate((valid) => {
        if (valid) {
          let msg = ''
          if (flag === 2) {
            if (this.touxi.checkNur_id === '') {
              this.$notify({
                title: '提示',
                message: '请选择审核人',
                type: 'success',
                duration: 2000
              })
              return
            }
            msg = '审核成功'
          } else if (flag === 3) {
            if (this.touxi.exeNur_id === '') {
              this.$notify({
                title: '提示',
                message: '请选择执行人',
                type: 'success',
                duration: 2000
              })
              return
            }
            msg = '执行成功'
          } else {
            msg = '保存成功'
          }
          const tempData = Object.assign({}, this.touxi)
          tempData.action = flag // 0有效 1无效 2审核 3执行 4撤销 5保存超滤量 6医生修改
          if (flag === 2) {
            // tempData.checkNur_id = this.checkNur_id
            tempData.exeNur_id = 1
          } else if (flag === 3) {
            tempData.checkNur_id = 1
            // tempData.exeNur_id = this.exeNur_id
          } else {
            tempData.checkNur_id = 1
            tempData.exeNur_id = 1
          }
          console.log('flag=' + flag)
          console.log(tempData)
          updateyz_touxi(tempData).then(() => {
            this.touxi_dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: msg,
              type: 'success',
              duration: 2000
            })
            this.getTouxi(this.regid)
          })
        }
      })
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  watch: {
    num: function() {
      this.getTouxi(this.regid)
    }
  },
  created: function() {
    this.getNurseList('')
    this.getTouxi(this.regid)
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
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
    .block {
        border: 1px solid #ebebeb;
        border-left: none;
        border-right: none;
        border-radius: 3px;
        transition: .2s;
    }
</style>
