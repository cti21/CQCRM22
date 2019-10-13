<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="设备登记" name="first">
                 <device_register></device_register>
              </el-tab-pane>
              <el-tab-pane label="设备维修" name="second">
                <component :is="sbwxVue"></component>
              </el-tab-pane>
              <el-tab-pane label="设备保养" name="third">
                <component :is="sbbyVue"></component>
              </el-tab-pane>
              <el-tab-pane label="水质检测" name="fourth">
                <component :is="szjcVue"></component>
              </el-tab-pane>
              <el-tab-pane label="细菌内毒素监测" name="fifth">
                <component :is="xjjcVue"></component>
              </el-tab-pane>
              <el-tab-pane label="水处理设备运行记录" name="sixth">
                <component :is="sbyxVue"></component>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
import { getToken } from '@/utils/auth'
const device_register = resolve => require(['@/views/device/device_register.vue'], resolve)
const device_repair = resolve => require(['@/views/device/device_repair.vue'], resolve)
const device_maintain = resolve => require(['@/views/device/device_maintain.vue'], resolve)
const water_examine = resolve => require(['@/views/device/water_examine.vue'], resolve)
const monitor_record = resolve => require(['@/views/device/monitor_record.vue'], resolve)
const waterprocess_record = resolve => require(['@/views/device/waterprocess_record.vue'], resolve)
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
    device_register,
    device_repair,
    device_maintain,
    water_examine,
    monitor_record,
    waterprocess_record
  },
  data: function() {

    return {
      activeName: 'first',
      sbwxVue: '',
      sbbyVue: '',
      szjcVue: '',
      xjjcVue: '',
      sbyxVue: '',
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
          this.sbwxVue = device_repair
          break
        case 'third' :
          this.sbbyVue = device_maintain
          break
        case 'fourth' :
          this.szjcVue = water_examine
          break
        case 'fifth' :
          this.xjjcVue = monitor_record
          break
       case 'sixth' :
          this.sbyxVue = waterprocess_record
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
