<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="库存状况" name="first">
                 <drug_stock
                   :patientid="patientid"
                   :clickcount="count">
                 </drug_stock>
              </el-tab-pane>
              <el-tab-pane label="药品入库" name="second">
                <component :is="druginVue"
                           :patientid="patientid"
                           :clickcount="count">
                </component >
              </el-tab-pane>
              <el-tab-pane label="药品出库" name="third">
                <component :is="drugoutVue"
                           :patientid="patientid"
                           :clickcount="count">
                </component>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
import { getToken } from '@/utils/auth'
const drug_in = resolve => require(['@/views/drug_person/drug_in.vue'], resolve)
const drug_out = resolve => require(['@/views/drug_person/drug_out.vue'], resolve)
const drug_stock = resolve => require(['@/views/drug_person/drug_stock.vue'], resolve)
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
    drug_in,
    drug_out,
    drug_stock
  },
  props: ['patientid'],
  data: function() {
    return {
      activeName: 'first',
      druginVue: '',
      drugoutVue: '',
      drugstockVue: '',
      token: getToken,
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
          this.druginVue = drug_in
          break
        case 'third' :
          this.drugoutVue = drug_out
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
