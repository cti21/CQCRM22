<template>
    <div>
        <el-row>
          <el-button style="float: left;margin-right: 10px"
                     v-if="checkUserPerm('nurse', 'apply', $store.getters.perms)"
                     size="small" type="primary" @click="download">模板下载
          </el-button>
          <el-upload
            class = "upload-demo"
            v-if="checkUserPerm('nurse', 'apply', $store.getters.perms)"
            action = ""
            :auto-upload = 'true'
            :limit = '3'
            :http-request = "uploadFile"
            accept = '.xls,.xlsx'
            :on-change="handleChange"
            :file-list="fileList"
          >
           <el-button size="small"  type="primary" :disabled="processing">{{uploadTip}}</el-button>
           <!--<div slot="tip" class="el-upload__tip">只能上传excel文件</div>-->
          </el-upload>

        </el-row>
        <el-row style="margin:20px;">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <el-table-column type="index" label="序号"  width="160">
            </el-table-column>
            <el-table-column prop="name" label="部门名称" width="220">
            </el-table-column>
            <el-table-column prop="description" label="简称" width="220">
            </el-table-column>
            <el-table-column prop="code" label="编号" width="220">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
              </template>
            </el-table-column>
          </el-table>
          <!--<div class="pagination-container" style="margin-top: 5px" align="right">-->
                <!--<el-pagination background-->
                               <!--@current-change="handleCurrentChange"-->
                               <!--:current-page="listQuery.page"-->
                               <!--:page-size="listQuery.limit"-->
                               <!--layout="total, prev, pager, next"-->
                               <!--:total="total">-->
                <!--</el-pagination>-->
          <!--</div>-->
        <!--<el-table-->
          <!--:data="treegridData"-->
          <!--row-key="id"-->
          <!--:expand-row-keys="expandKeys"-->
          <!--@expand-change="rowExpand"-->
          <!--:row-class-name="getRowClassName"-->
        <!--&gt;-->
          <!--<el-table-column type="expand">-->
            <!--<template slot-scope="props">-->
              <!--<el-table :data="subTableData">-->
                 <!--<el-table-column type="index" label="#">-->
                 <!--</el-table-column>-->
                 <!--<el-table-column label="部门名称" prop="name">-->
                 <!--</el-table-column>-->
                 <!--<el-table-column prop="description" label="简称" width="220">-->
                 <!--</el-table-column>-->
                 <!--<el-table-column prop="code" label="编号" width="220">-->
                 <!--</el-table-column>-->
              <!--</el-table>-->
            <!--</template>-->
           <!--</el-table-column>-->
           <!--<el-table-column prop="id" label="id" type="selection" fixed></el-table-column>-->
           <!--<el-table-tree-column-->
             <!--:remote="remote"-->
             <!--prop="label"-->
             <!--child-key="children"-->
             <!--label="名称"-->
             <!--file-icon="icon icon-file"-->
             <!--folder-icon="icon icon-folder"-->
           <!--&gt;-->
           <!--</el-table-tree-column>-->
           <!--<el-table-column prop="description" label="描述" width="180">-->
           <!--</el-table-column>-->
           <!--<el-table-column label="操作" fixed="right" align="center">-->
              <!--<template slot-scope="scope">-->
                  <!--<el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>-->
              <!--</template>-->
            <!--</el-table-column>-->
        <!--</el-table>-->

        <!--&lt;!&ndash;@row-click="expandChange"&ndash;&gt;-->
        <!--<el-table-->
          <!--ref="refTable"-->
          <!--:data="tableData5"-->
          <!--row-key="id"-->
          <!--:expand-row-keys="expandKeys"-->
          <!--style="width: 100%"-->
        <!--&gt;-->
          <!--<el-table-column  type="expand">-->
            <!--<template slot-scope="props">-->
              <!--<el-table :data="subTableData">-->
                 <!--<el-table-column type="index" label="#">-->
                 <!--</el-table-column>-->
                 <!--<el-table-column label="部门名称" prop="name">-->
                 <!--</el-table-column>-->
                 <!--<el-table-column prop="description" label="简称" width="220">-->
                 <!--</el-table-column>-->
                 <!--<el-table-column prop="code" label="编号" width="220">-->
                 <!--</el-table-column>-->
              <!--</el-table>-->
            <!--</template>-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--label="商品 ID"-->
            <!--prop="id">-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--label="商品名称"-->
            <!--prop="name">-->
          <!--</el-table-column>-->
          <!--<el-table-column-->
            <!--label="描述"-->
            <!--prop="desc">-->
          <!--</el-table-column>-->
        <!--</el-table>-->

        <!--<el-table-->
          <!--ref="mytable"-->
          <!--:data="tableListData"-->
          <!--:row-style="toggleDisplayTr"-->
          <!--stripe-->
          <!--@select="select"-->
          <!--@expand-change="rowExpand"-->
          <!--@selection-change="selectChange"-->
          <!--class="init_table">-->
            <!--<el-table-column prop="id" label="id" type="selection" fixed>-->
            <!--</el-table-column>-->
            <!--<el-table-column  type="expand">-->
              <!--<template slot-scope="props">-->
                <!--<el-table :data="subTableData">-->
                   <!--<el-table-column type="index" label="#">-->
                   <!--</el-table-column>-->
                   <!--<el-table-column label="部门名称" prop="name">-->
                   <!--</el-table-column>-->
                   <!--<el-table-column prop="description" label="简称" width="220">-->
                   <!--</el-table-column>-->
                   <!--<el-table-column prop="code" label="编号" width="220">-->
                   <!--</el-table-column>-->
                <!--</el-table>-->
              <!--</template>-->
            <!--</el-table-column>-->
            <!--<el-table-column-->
              <!--label="权限名称"-->
              <!--min-width="200"-->
              <!--show-overflow-tooltip-->
              <!--align="left">-->
                  <!--<template slot-scope="scope">-->
                    <!--<p :style="`margin-left: ${scope.row.__level * 20}px;margin-top:0;margin-bottom:0`"><i  @click="toggleFoldingStatus(scope.row)" class="permission_toggleFold" :class="toggleFoldingClass(scope.row)"></i>{{scope.row.Name}}</p>-->
                  <!--</template>-->
            <!--</el-table-column>-->
            <!--<el-table-column-->
              <!--align="center"-->
              <!--width="90"-->
              <!--prop="__level"-->
              <!--label="层级">-->
            <!--</el-table-column>-->
            <!--<el-table-column-->
              <!--align="left"-->
              <!--prop="__identity"-->
              <!--label="节点标识">-->
            <!--</el-table-column>-->
            <!--<el-table-column-->
              <!--align="center"-->
              <!--width="80"-->
              <!--label="图标">-->
              <!--<template slot-scope="scope">-->
                <!--<i :class="scope.row.Class"></i>-->
              <!--</template>-->
            <!--</el-table-column>-->
            <!--<el-table-column-->
              <!--align="center"-->
              <!--width="100"-->
              <!--label="操作">-->
                  <!--<template slot-scope="scope">-->
                    <!--<el-button type="text">编辑</el-button>-->
                    <!--<el-button type="text">删除</el-button>-->
                  <!--</template>-->
            <!--</el-table-column>-->
        <!--</el-table>-->
        </el-row>

        <div>
          <el-dialog  title="部门信息" width="40%" :visible.sync="dialogFormVisible">
                  <el-form  :model="area" ref="dataForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:30px;'>
                       <el-row>
                         <el-col>
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="area.name" style="width: 380px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col>
                            <el-form-item label="简称"  prop="description">
                              <el-input v-model="area.description" style="width: 380px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    @click="dialogFormVisible = false"
                    icon="el-icon-close"
                  >关闭</el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    v-if="dialogStatus=='create'"
                    @click="createData">保存
                  </el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="updateData">保存
                  </el-button>
                </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="分部" width="55%" :visible.sync="sub_dialogFormVisible">
              <subcom :action="subAciton" :companyid="companyid"></subcom>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { departments, updateDepartment, uploadFile, downloadFile } from '@/api/login'
import { getToken } from '@/utils/auth'
import subcom from '@/views/organization/subCom_common.vue'
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
  components: {
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    subcom
  },
  props: {
    nodeOject: {
      type: Object
    }
  },
  data: function() {
    return {
      list: [],
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      token: getToken,
      dialogFormVisible: false,
      sub_dialogFormVisible: false,
      companyid: 1,
      subAciton: 'create',
      dialogStatus: '',
      treegridData: [{
        "id": 1,
        "label": "系统",
        "parent_id": null,
        "child_num": 3,
        "depth": 0,
        "Class": "iconfont icon-tuichu",
        "description": "系统管理",
        "children": [{
          "id": 2,
          "label": "医生工作平台",
          "parent_id": 1,
          "child_num": 5,
          "depth": 1,
          "Class": "iconfont icon-tuichu",
          "description": "",
          "children": [{
            "id": 3,
            "label": "菜单",
            "parent_id": 2,
            "child_num": 0,
            "depth": 2,
            "Class": "iconfont icon-tuichu",
            "description": "菜单管理",
          }, {
            "id": 4,
            "label": "角色",
            "parent_id": 2,
            "child_num": 0,
            "depth": 2,
            "Class": "iconfont icon-tuichu",
            "description": "角色管理",
          }, {
            "id": 5,
            "label": "用户",
            "parent_id": 2,
            "child_num": 0,
            "depth": 2,
            "Class": "iconfont icon-tuichu",
            "description": "用户管理"
          }]
        }]
      }, {
        "id": 6,
        "label": "客户",
        "parent_id": null,
        "url": null,
        "depth": 0,
        "Class": "iconfont icon-tuichu",
        "child_num": 2,
        "description": "客户管理",
        "children": [{
          "id": 7,
          "label": "客户列表",
          "parent_id": 6,
          "depth": 1,
          "Class": "iconfont icon-tuichu",
          "child_num": 0,
          "description": "客户列表描述",
        }]
      }, {
        "id": 8,
        "label": "报表",
        "parent_id": null,
        "url": null,
        "depth": 0,
        "Class": "iconfont icon-tuichu",
        "child_num": 0,
        "description": "报表描述",
        "children": [{
          "id": 7,
          "label": "客户列表",
          "parent_id": 6,
          "depth": 1,
          "Class": "iconfont icon-tuichu",
          "child_num": 0,
          "description": "客户列表描述"
        }]
      }],
      subTableData:[],
      expandKeys: [],
      loading: false,
      tableData5: [{
        id: '10102',
        name: '好滋好味鸡蛋仔',
        category: '江浙小吃、小吃零食',
        desc: '荷兰优质淡奶，奶香浓而不腻',
        address: '上海市普陀区真北路',
        shop: '王小虎夫妻店',
        shopId: '10333'
      }, {
        id: '10103',
        name: '好滋好味鸡蛋仔',
        category: '江浙小吃、小吃零食',
        desc: '荷兰优质淡奶，奶香浓而不腻',
        address: '上海市普陀区真北路',
        shop: '王小虎夫妻店',
        shopId: '10333'
      }, {
        id: '10104',
        name: '好滋好味鸡蛋仔',
        category: '江浙小吃、小吃零食',
        desc: '荷兰优质淡奶，奶香浓而不腻',
        address: '上海市普陀区真北路',
        shop: '王小虎夫妻店',
        shopId: '10333'
      }, {
        id: '10105',
        name: '好滋好味鸡蛋仔',
        category: '江浙小吃、小吃零食',
        desc: '荷兰优质淡奶，奶香浓而不腻',
        address: '上海市普陀区真北路',
        shop: '王小虎夫妻店',
        shopId: '10333'
      }],
      mydataList: [{
        "id": 1,
        "Name": "系统管理",
        "parent_id": null,
        "child_num": 3,
        "depth": 0,
        "Class": "iconfont icon-tuichu",
        "description": "系统管理",
        "Children": [{
          "id": 2,
          "Name": "工作平台",
          "parent_id": 1,
          "child_num": 5,
          "depth": 1,
          "Class": "iconfont icon-tuichu",
          "description": "工作平台",
          "Children": [{
            "id": 3,
            "Name": "菜单",
            "parent_id": 2,
            "child_num": 0,
            "depth": 2,
            "Class": "iconfont icon-tuichu",
            "description": "管理",
            "Children": []
          }]
        }]
      }],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      area: {
        id: null,
        name: '',
        description: '',
        aa: []
      },
      importUrl: 'http://127.0.0.1:8000/upload/',
      importHeaders: {
        enctype: 'multipart/form-data',
        cityCode: ''
      },
      name: 'import',
      fileList: [],
      withCredentials: true,
      processing: false,
      uploadTip: '点击上传',
      importFlag: 1,
      queryparams: {
        page: 1,
        name: '',
        code: '',
        kind: 'info'
      },
      tableListData: [],
      foldList: []
    }
  },
  methods: {
    getCompany(data) {
      departments(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        console.log('list', this.list)
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetArea() {
      this.area = {
        id: null,
        name: '',
        description: '',
        web: ''
      }
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.mytable.toggleRowSelection(row)
        })
      } else {
        this.$refs.mytable.clearSelection()
      }
    },
    select(selection, row) {
      const parentrow = this.tableListData.filter(item => item.id === row.parent_id)
      this.toggleSelection([parentrow[0]])
    },
    remote() {
    },
    getRowClassName({row, rowIndex}){
      if (row.depth > 0) {
        return 'row-expand-cover'
      }
    },
    selectChange(val) {
      console.log('val', val)
    },
    rowExpand(row, expandedRows) {
      const params = {
        parentid: row.id
      }
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.queryparams.code = this.nodeOject.code
      this.getCompany(this.queryparams)
      departments(this.queryparams).then(res => {
        this.subTableData = res.data.results
        console.log(this.subTableData)
      })
      // 如果展开行数大于1
      if (expandedRows.length > 1) {
        expandedRows.shift()
      }
    },
    handleChange(file, fileList) {
      this.fileList = fileList.slice(-1)
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.name = ''
      this.getCompany(this.queryparams)
    },
    handleCreate() {
      this.subAciton = 'create'
      this.sub_dialogFormVisible = true
    },
    handleUpdate(row) {
      this.area = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.area)
          let o = [{ name: 'tom', sex: '男' },{name: 'david',sex: '女'}]
          // tempData.aa.push(o)
          tempData.status = 0
          tempData.aa = o
          console.log('tempData:', tempData)
          updateDepartment(tempData).then(() => {
            this.$emit('refreshTree', this.area)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getCompany(this.queryparams)
          })
        }
      })
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getCompany(this.queryparams)
    },
    uploadFile(params) {
      const _file = params.file
      const isLt2M = _file.size / 1024 / 1024 < 2
      const formData = new FormData()
      formData.append('file', _file)
      if (!isLt2M) {
        this.$message.error('请上传2M以下的.xlsx文件')
        return false
      }
      uploadFile(formData).then(res => {
        if (res.status === 200) {
          this.$message({
            type: 'success',
            message: '上传成功'
          })
          params.onSuccess('文件上传成功')
        } else {
          this.$message({
            type: 'warning',
            message: '上传失败'
          })
        }
      }).catch( error => {
        params.onError('文件上传失败')
      })
    },
    download(params) {
      downloadFile(params).then(res => {
        const blob = new Blob([res.data])
        const fileName = '员工模板.xlsx'
        const elink = document.createElement('a')
        elink.download = fileName
        elink.style.display = 'none'
        elink.href = URL.createObjectURL(blob)
        document.body.appendChild(elink)
        elink.click()
        URL.revokeObjectURL(elink.href)
        document.body.removeChild(elink)
        this.$message({
          type: 'success',
          message: '下载成功'
        })
      })
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    },
    toggleFoldingStatus(params) {
      this.foldList.includes(params.__identity) ? this.foldList.splice(this.foldList.indexOf(params.__identity), 1) : this.foldList.push(params.__identity)
    },
    toggleDisplayTr({row, index}) {
      for (let i = 0; i < this.foldList.length; i++) {
        const item = this.foldList[i]
        if (row.__family.includes(item) && row.__identity !== item) return 'display:none;'
      }
      return ''
    },
    toggleFoldingClass(params) {
      return params.Children.length === 0 ? 'permission_placeholder' : (this.foldList.indexOf(params.__identity) === -1 ? 'iconfont icon-minus-square-o' : 'iconfont icon-plussquareo')
    },
    formatConversion(parent, children, index = 0, family = [], elderIdentity = 'x') {
      if (children.length > 0) {
        children.map((x, i) => {
          this.$set(x, '__level', index)
          this.$set(x, '__family', [...family, elderIdentity + '_' + i])
          this.$set(x, '__identity', elderIdentity + '_' + i)
          parent.push(x)
          if (x.Children.length > 0) this.formatConversion(parent, x.Children, index + 1, [...family, elderIdentity + '_' + i], elderIdentity + '_' + i)
        })
      } return parent
    }
  },
  computed: {
    foldAllList() {
      return this.tableListData.map(x => x.__identity)
    }
  },
  watch: {
    'nodeOject.code': {
      handler: function(val, oldVal) {
        this.queryparams.code = val
        this.getCompany(this.queryparams)
      },
      deep: true
    }
  },
  mounted() {
    this.$nextTick(function() {
      this.foldList = this.foldAllList
    })
  },
  created: function() {
    this.queryparams.page = 1
    this.queryparams.name = ''
    this.queryparams.code = this.nodeOject.code
    this.getCompany(this.queryparams)
    this.tableListData = this.formatConversion([], this.mydataList)
    // console.log('value:', this.checkUserPerm('nurse', 'apply', store.getters.perms))
  }
}
</script>

<style lang='stylus' rel='stylesheet/stylus'>
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
    .demo-table-expand {
      font-size: 0;
    }
    .demo-table-expand label {
      width: 90px;
      color: #99a9bf;
    }
    .demo-table-expand .el-form-item {
      margin-right: 0;
      margin-bottom: 0;
      width: 50%;
    }
    .row-expand-cover .el-table__expand-icon{visibility:hidden;}
    .permission_toggleFold
      vertical-align middle
      padding-right 5px
      font-size 16px
      cursor pointer
    .permission_placeholder
        content ' '
        display inline-block
        width 16px
        font-size 16px
    .init_table
        width 100% !important
        max-width 900px !important
        margin 0 auto !important
</style>
