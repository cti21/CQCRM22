<template>
    <div>
        <el-container>
          <el-aside id="personInfo" width="240px" style="background-color: #f0f2f5;padding: 0px 0px 0px 0px;display: block;">
              <div style="height:100%;background-color: #ffffff">
                  <el-row style="margin-bottom: 10px">
                    <div>
                      <el-input
                        v-model="scname"
                        class="myInput"
                        prefix-icon="el-icon-search"
                        size="small"
                        @keyup.enter.native="handleFilter('')"
                        style="width:200px;padding: 0 10px"
                        placeholder="请输入分部或部门">
                      </el-input>
                    </div>
                  </el-row>
                  <!--<el-row>-->
                    <!--<el-button size="small" type="primary"  @click="handleRefresh" icon="el-icon-refresh">-->
                      <!--刷新-->
                    <!--</el-button>-->
                  <!--</el-row>-->
                  <el-tree
                    ref="tree"
                    accordion
                    :load="handleLoad"
                    lazy
                    node-key="id"
                    :default-expanded-keys="[rootNode.id]"
                    :default-checked-keys="[]"
                    :props="defaultProps"
                    :expand-on-click-node="true"
                    :highlight-current="true"
                    @node-click="handlenodeclick"
                    :default-expand-all="false">
                  </el-tree>
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
                  	<component
                      :nodeOject="nodeOject"
                      :is="isShow"
                      @refreshTree="handleRefresh">
                    </component>
                </div>
              </div>
            </el-main>
          </el-container>
        </el-container>
    </div>
</template>

<script>
import { Organization } from '@/api/login'
import { getToken } from '@/utils/auth'
import company from '@/views/organization/company.vue'
import subCompany from '@/views/organization/subCompany.vue'
import department from '@/views/organization/department.vue'
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
    ElTabPane,
    ElRow,
    ElCol,
    company,
    subCompany,
    department
  },
  data: function() {
    return {
      list: null,
      children: null,
      detailVisible: false,
      code: '',
      isShow: 'company',
      node: null,
      currentNode: null,
      resolve: null,
      nodeOject: {
        name: '首泰公司',
        code: 1,
        kind: 0
      },
      scname: '',
      rq: '',
      token: getToken,
      clickNum: 0,
      queryparams: {
        page: 1,
        code: 1,
        rq: ''
      },
      defaultProps: {
        children: 'children',
        label: 'label',
        isLeaf: 'leaf'
      },
      content: '',
      treeData: [],
      rootKey: '1',
      rootNode: {
        id: '1',
        label: '首泰公司',
        code: 1,
        status: 0
      },
      checkedKeys: []
    }
  },
  methods: {
    handleFilter(par) {
      if (par === 0) {
        this.rq = ''
        document.getElementById('btn_all').style.color = 'red'
        document.getElementById('btn_today').style.color = ''
        document.getElementById('btn_yesterday').style.color = ''
      } else if (par === 1) {
        this.rq = 1
        document.getElementById('btn_all').style.color = ''
        document.getElementById('btn_today').style.color = 'red'
        document.getElementById('btn_yesterday').style.color = ''
      } else if (par === 2) {
        this.rq = 2
        document.getElementById('btn_all').style.color = ''
        document.getElementById('btn_today').style.color = ''
        document.getElementById('btn_yesterday').style.color = 'red'
      }
      this.queryparams.page = 1
      this.queryparams.rq = this.rq
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
    },
    handleLoad(node, resolve) {
      this.node = node
      this.resolve = resolve
      if (this.$refs.tree !== undefined) this.checkedKeys = this.$refs.tree.getCheckedKeys()
      if (node.level === 0) {
        return resolve([this.rootNode])
      } else {
        this.getIndex(node, resolve)
      }
      if (this.$refs.tree !== undefined) this.$refs.tree.setCheckedKeys(this.checkedKeys)
    },
    getIndex(node, resolve) {
      const param = {
        code: node.data.code
      }
      this.list = []
      Organization(param).then(response => {
        response.data.forEach(val => {
          if (val.status === 4) {
            val.leaf = true // 不为叶子节点
          } else {
            val.leaf = false // 为叶子节点
          }
        })
        this.list = response.data
        resolve(this.list)
      })
    },
    getNodeChildData(node) {
      const param = {
        code: node.data.code
      }
      this.children = []
      Organization(param).then(response => {
        response.data.forEach(val => {
          if (val.status === 4) {
            val.leaf = true // 不为叶子节点
          } else {
            val.leaf = false // 为叶子节点
          }
        })
        this.children = response.data
        node.doCreateChildren(this.children)
      })
    },
    handleRefresh(data) {
      this.currentNode.childNodes = []
      this.getNodeChildData(this.currentNode)
      if (Object.keys(data).length > 0) {
        this.currentNode.data.label = data.name
      }
    },
    handlenodeclick(data, node, value) {
      this.currentNode = node
      const status = data.status
      this.nodeOject.name = data.label
      this.nodeOject.code = data.code
      this.nodeOject.kind = data.status
      switch (status) {
        case 0:
          this.isShow = 'company'
          break
        case 1:
          this.isShow = 'subCompany'
          break
        case 2:
          this.isShow = 'subCompany'
          break
        case 3:
          this.isShow = 'department'
          break
        case 4:
          this.isShow = 'department'
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
