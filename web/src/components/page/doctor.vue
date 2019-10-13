<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="透析参数" name="first">
                 <touxi :patientid="patientid" :regid="register_id" :num="num"></touxi>
              </el-tab-pane>
              <el-tab-pane label="临时医嘱" name="third">
                <component :regid="register_id" :patientid="patientid" :is="lsyzVue" :num="num"></component>
              </el-tab-pane>
              <el-tab-pane label="透析记录" name="fourth">
                <component :regid="register_id" :patientid="patientid" :is="txjlVue" :num="num"></component>
              </el-tab-pane>
              <el-tab-pane label="血管通路" name="fifth">
                <component :regid="register_id" :patientid="patientid" :is="xgtlVue"></component>
              </el-tab-pane>
              <el-tab-pane label="检验结果" name="sixth">
                <component :patientid="patientid" :is="jyjgVue"></component>
              </el-tab-pane>
              <el-tab-pane label="病程记录" name="seventh">
                <component :regid="register_id" :is="bcjlVue"></component>
              </el-tab-pane>
              <el-tab-pane label="转归" name="eighth">
                <component :regid="register_id" :patientid="patientid" :is="brzgVue"></component>
              </el-tab-pane>
              <el-tab-pane label="透析处方" name="second">
                <component :regid="register_id" :patientid="patientid" :is="txcfVue"></component>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
import { getToken } from '@/utils/auth'
const touxi = resolve => require(['@/views/doctor/touxi.vue'], resolve)
const txplan = resolve => require(['@/views/doctor/tx_plan.vue'], resolve)
const drug = resolve => require(['@/views/doctor/drug.vue'], resolve)
const tx_record = resolve => require(['@/views/doctor/tx_record.vue'], resolve)
const xgtonglu = resolve => require(['@/views/doctor/xgtonglu.vue'], resolve)
const labresult = resolve => require(['@/views/doctor/LabResult.vue'], resolve)
const diseaseduration = resolve => require(['@/views/doctor/diseaseduration.vue'], resolve)
const zhuangui = resolve => require(['@/views/doctor/zhuangui.vue'], resolve)
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

export default {
  components: {
    ElButton,
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    txplan,
    touxi,
    drug,
    tx_record,
    xgtonglu,
    labresult,
    diseaseduration,
    zhuangui
  },
  data: function() {
    return {
      num: 0,
      patientid: '',
      register_id: '',
      activeName: 'first',
      token: getToken,
      txcfVue: '',
      lsyzVue: '',
      txjlVue: '',
      xgtlVue: '',
      jyjgVue: '',
      bcjlVue: '',
      brzgVue: ''
    }
  },
  methods: {
    checkVue(name) {
      switch (name) {
        case 'second' :
          this.txcfVue = txplan
          break
        case 'third' :
          this.lsyzVue = drug
          break
        case 'fourth' :
          this.txjlVue = tx_record
          break
        case 'fifth' :
          this.xgtlVue = xgtonglu
          break
        case 'sixth' :
          this.jyjgVue = labresult
          break
        case 'seventh' :
          this.bcjlVue = diseaseduration
          break
        case 'eighth' :
          this.brzgVue = zhuangui
          break
      }
    },
    handleClick(tab, event) {
      this.checkVue(tab.name)
      this.num = this.num + 1
    }
  },
  created: function() {
    this.patientid = this.$route.query.patientid
    this.register_id = this.$route.query.register_id
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
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
