<template>
    <div>
        <div>
          <template>
            <el-tabs v-model="activeName" @tab-click="handleClick">
              <el-tab-pane label="基本信息" name="first">
                 <clientinfo :clientid="clientid" :register_id="register_id" :num="num" :count="count"></clientinfo>
              </el-tab-pane>
              <el-tab-pane label="宣教开单" name="second">
                <clientorder :clientid="clientid" :register_id="register_id" :num="num" :count="count"></clientorder>
              </el-tab-pane>
            </el-tabs>
          </template>
        </div>
    </div>
</template>

<script>
const clientinfo = resolve => require(['@/views/orders/client_info.vue'], resolve)
const clientorder = resolve => require(['@/views/orders/client_order.vue'], resolve)
import ElCol from 'element-ui/packages/col/src/col'
import ElRow from 'element-ui/packages/row/src/row'
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
    ElRow,
    ElCol,
    clientinfo,
    clientorder
  },
  props: ['clientid', 'register_id', 'num'],
  data: function() {
    return {
      activeName: 'second',
      xjkdVue: '',
      count: 0
    }
  },
  methods: {
    checkVue(name) {
      switch (name) {
        case 'second' :
          this.xjkdVue = clientorder
          break
      }
    },
    handleClick(tab, event) {
      this.checkVue(tab.name)
      this.count = this.count + 1
      console.log('clientid', this.clientid, 'num', this.num)
    }
  },
  created: function() {
    //this.clientid = this.$route.query.clientid
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
