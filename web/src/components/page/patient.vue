<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick" tabPosition="top">
              <el-tab-pane label="病历首页" name="first">
                 <front_page :patientid="patientid"></front_page>
              </el-tab-pane>
              <el-tab-pane label="首次病程" name="seventh">
                <component :is="firstDiseaseDurationVue" :patientid="patientid" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="病程记录" name="fourth">
                <component :is="diseasedurationVue" :patientid="patientid" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="透析处方" name="sixth">
                <component :is="tx_planVue" :patientid="patientid" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="血管通路" name="third">
                <component :is="xgtongluVue" :patientid="patientid" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="手术记录" name="eighth">
                <component :is="operate_recordVue" :patientid="patientid" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="检验结果" name="second">
                <component :is="lab_testVue" :patientid="patientid" :clickcount="count"></component >
              </el-tab-pane>
              <el-tab-pane label="转归" name="fifth">
                <component :is="zhuanguiVue" :patientid="patientid" :clickcount="count"></component>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
import { getToken } from '@/utils/auth'
const tx_plan = resolve => require(['@/views/patient/tx_plan.vue'], resolve)
const xgtonglu = resolve => require(['@/views/patient/xgtonglu.vue'], resolve)
const zhuangui = resolve => require(['@/views/patient/zhuangui.vue'], resolve)
const lab_test = resolve => require(['@/views/patient/lab_test.vue'], resolve)
const diseaseduration = resolve => require(['@/views/patient/diseaseduration.vue'], resolve)
const front_page = resolve => require(['@/views/patient/front_page.vue'], resolve)
const firstDiseaseDuration = resolve => require(['@/views/patient/firstDiseaseDuration.vue'], resolve)
const operate_record = resolve => require(['@/views/patient/operate_record.vue'], resolve)
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
    tx_plan,
    xgtonglu,
    zhuangui,
    lab_test,
    diseaseduration,
    front_page,
    firstDiseaseDuration,
    operate_record
  },
  data: function() {
    return {
      activeName: 'first',
      tx_planVue: '',
      xgtongluVue: '',
      zhuanguiVue: '',
      lab_testVue: '',
      diseasedurationVue: '',
      firstDiseaseDurationVue: '',
      operate_recordVue: '',
      token: getToken,
      patientid: '',
      count: 0
    }
  },
  methods: {
    handleClick(tab, event) {
      this.checkVue(tab.name)
      this.count = this.count + 1
    },
    checkVue(name) {
      switch (name) {
        case 'second' :
          this.lab_testVue = lab_test
          break
        case 'third' :
          this.xgtongluVue = xgtonglu
          break
        case 'fourth' :
          this.diseasedurationVue = diseaseduration
          break
        case 'fifth' :
          this.zhuanguiVue = zhuangui
          break
        case 'sixth' :
          this.tx_planVue = tx_plan
          break
        case 'seventh' :
          this.firstDiseaseDurationVue = firstDiseaseDuration
          break
        case 'eighth' :
          this.operate_recordVue = operate_record
          break
      }
    }
  },
  created: function() {
    this.patientid = this.$route.query.patientid
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
</style>
