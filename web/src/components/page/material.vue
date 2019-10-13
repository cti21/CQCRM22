<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="耗材设置" name="first">
                 <materialSet :clickcount="count"></materialSet>
              </el-tab-pane>
              <el-tab-pane label="耗材入库" name="second">
                <component :is="materialinVue" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="耗材出库" name="third">
                <component :is="materialoutVue" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="库存状况" name="fourth">
                <component :is="materialstockVue" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="使用情况" name="fifth">
                <component :is="materialuseVue" :clickcount="count"></component>
              </el-tab-pane>
              <el-tab-pane label="库存预警" name="sixth">
                <component :is="materialalertVue" :clickcount="count"></component>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
import { getToken } from '@/utils/auth'
const materialSet = resolve => require(['@/views/material/materialSet.vue'], resolve)
const material_in = resolve => require(['@/views/material/material_in.vue'], resolve)
const material_out = resolve => require(['@/views/material/material_out.vue'], resolve)
const material_stock = resolve => require(['@/views/material/material_stock.vue'], resolve)
const material_use = resolve => require(['@/views/material/material_use.vue'], resolve)
const material_alert = resolve => require(['@/views/material/material_alert.vue'], resolve)
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
    materialSet,
    material_in,
    material_out,
    material_stock,
    material_use,
    material_alert
  },
  data: function() {

    return {
      activeName: 'first',
      materialinVue: '',
      materialoutVue: '',
      materialstockVue: '',
      materialuseVue: '',
      materialalertVue: '',
      token: getToken,
      count: 0
    }
  },
  methods: {
    handleClick(tab, event) {
      this.checkVue(tab.name)
      this.count = this.count + 1
    },
    checkVue (name) {
      switch (name) {
        case 'second' :
          this.materialinVue = material_in
          break
        case 'third' :
          this.materialoutVue = material_out
          break
        case 'fourth' :
          this.materialstockVue = material_stock
          break
        case 'fifth' :
          this.materialuseVue = material_use
          break
        case 'sixth' :
          this.materialalertVue = material_alert
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
