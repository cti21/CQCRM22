<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="病历首页" name="first">
                 <front_page></front_page>
              </el-tab-pane>
              <el-tab-pane label="首次病程" name="second">
                <component :is="scbcVue"></component>
              </el-tab-pane>
              <el-tab-pane label="检验检查" name="third">
                <component :is="jyjcVue"></component>
              </el-tab-pane>
              <el-tab-pane label="手术记录" name="fourth">
                <component :is="ssjlVue"></component>
              </el-tab-pane>
              <el-tab-pane label="血管通路" name="fifth">
                <component :is="xgtlVue"></component>
              </el-tab-pane>
              <el-tab-pane label="透析方案" name="sixth">
                <component :is="txfaVue"></component>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
import { getToken } from '@/utils/auth'
const front_page = resolve => require(['@/views/medical_report/front_page.vue'], resolve)
const operate_record = resolve => require(['@/views/medical_report/operate_record.vue'], resolve)
const firstDiseaseDuration = resolve => require(['@/views/medical_report/firstDiseaseDuration.vue'], resolve)
const lab_test = resolve => require(['@/views/medical_report/lab_test.vue'], resolve)
const mr_xgtl = resolve => require(['@/views/medical_report/mr_xgtl.vue'], resolve)
const fdd = resolve => require(['@/views/medical_report/fdd.vue'], resolve)
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
import ElButton from "../../../node_modules/element-ui/packages/button/src/button";

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
    front_page,
    firstDiseaseDuration,
    lab_test,
    operate_record,
    mr_xgtl,
    fdd
  },
  data: function() {

    return {
      activeName: 'first',
      scbcVue: '',
      jyjcVue: '',
      ssjlVue: '',
      xgtlVue: '',
      txfaVue: '',
      token: getToken
    }
  },
  methods: {
    handleClick(tab, event) {
        this.checkVue(tab.name)
    },
    checkVue (name) {
       switch (name) {
        case 'second' :
          this.scbcVue = firstDiseaseDuration
          break
        case 'third' :
          this.jyjcVue = lab_test
          break
        case 'fourth' :
          this.ssjlVue = operate_record
          break
        case 'fifth' :
          this.xgtlVue = mr_xgtl
          break
       case 'sixth' :
          this.txfaVue = fdd
          break
        }
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
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
