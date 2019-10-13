<template>
    <div>
        <el-row>
            <el-button size="small" style="margin-left: 30px;" @click="chanKangCreate" type="primary" icon="el-icon-plus">产康宣教开单</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">营养</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">心理</el-button>
        </el-row>
        <el-row style="margin:20px;">
          <el-table
            ref="multipleTable"
            :data="tableListData"
            :row-style="toggleDisplayTr"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
          >
            <el-table-column
              label="宣教日期"
              min-width="120"
              width="120"
              show-overflow-tooltip
              :formatter="dateFormat"
              align="left">
                  <template slot-scope="scope">
                    <p :style="`margin-left: ${scope.row.__level * 20}px;margin-top:0;margin-bottom:0`"><i  @click="toggleFoldingStatus(scope.row)" class="permission_toggleFold" :class="toggleFoldingClass(scope.row)"></i>{{scope.row.marketdate}}</p>
                  </template>
            </el-table-column>
            <el-table-column prop="projectname" label="项目" width="80">
            </el-table-column>
            <el-table-column prop="times" label="开单次数" width="80">
            </el-table-column>
            <el-table-column prop="deptname" label="宣教科室" width="80">
            </el-table-column>
            <el-table-column prop="marketPostname" label="宣教岗位" width="80">
            </el-table-column>
            <el-table-column prop="marketmanname" label="宣教人员" width="80">
            </el-table-column>
            <!--<el-table-column prop="orderdate" label="开单日期" width="100" :formatter="dateFormat">-->
            <!--</el-table-column>-->
            <el-table-column prop="orderdeptname" label="开单科室" width="80">
            </el-table-column>
            <el-table-column prop="orderPostname" label="开单岗位" width="80">
            </el-table-column>
            <el-table-column prop="orderuser" label="开单人员" width="80">
            </el-table-column>
            <el-table-column prop="comment" label="备注" width="80">
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination background
                               @current-change="handleCurrentChange"
                               :current-page="listQuery.page"
                               :page-size="listQuery.limit"
                               layout="total, prev, pager, next"
                               :total="total">
                </el-pagination>
          </div>
        </el-row>

        <!--产康宣教开单新增-->
        <div>
          <el-dialog  title="产康宣教开单新增" width="60%" :visible.sync="dialogChanKangAddVisible">
             <orderadd
               :clientid="clientid"
               :register_id="register_id"
               :count="count"
               :hrmdepartment_id="hrmdepartment_id"
               @closeDlg="closeAddDialog"
             ></orderadd>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="岗位" width="40%" :visible.sync="dialogFormVisible">
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
                            <el-form-item label="备注"  prop="comment">
                              <el-input v-model="area.comment" style="width: 380px;" class="myInput"></el-input>
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
    </div>
</template>

<script>
import { orders } from '@/api/order'
import { post_dicts, createPost_dict, updatePost_dict, deletePost_dict } from '@/api/system'
import { getToken } from '@/utils/auth'
import orderadd from '@/views/orders/order_add.vue'
import moment from 'moment'
import ElCol from 'element-ui/packages/col/src/col'
import ElRow from 'element-ui/packages/row/src/row'
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
    ElRow,
    ElCol,
    orderadd
  },
  props: ['clientid', 'register_id', 'num'],
  data: function() {
    return {
      list: [],
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10000,
        offset: 0,
        hrmdepartment_id: 2,
        name: '',
        clientid: '',
        sort: '+id'
      },
      searchname: '',
      token: getToken,
      hrmdepartment_id: 2,
      dialogFormVisible: false,
      dialogChanKangAddVisible: false,
      dialogStatus: '',
      multipleOrder: [],
      count: 0,
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }]
      },
      area: {
        id: null,
        name: '',
        comment: ''
      },
      tableListData: [],
      foldList: []
    }
  },
  methods: {
    getOrders(data) {
      orders(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
        this.tableListData = this.formatConversion([], this.list)
        console.log('this.list', this.list)
      })
    },
    getdiseaseArea(data) {
      post_dicts(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    resetArea() {
      this.area = {
        id: null,
        name: '',
        comment: ''
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getdiseaseArea(this.listQuery)
    },
    remote(row, callback) {
      setTimeout(function() {
        callback(row.children)
      }, 800)
    },
    orderSelectChange(val) {
      if (val) {
        this.multipleOrder = []
        this.multipleOrder = val
      }
    },
    rowClick(row, event, column) {
      this.$refs.multipleTable.toggleRowSelection(row)
    },
    chanKangCreate() {
      this.count = this.count + 1
      if (this.register_id === '') {
        this.$notify({
          title: '提示',
          message: '请选择客户',
          type: 'success',
          duration: 2000
        })
        return false
      }
      this.dialogChanKangAddVisible = true
    },
    handleCreate() {
      this.resetArea()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.area.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createPost_dict(this.area).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getdiseaseArea(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.area = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.area)
          updatePost_dict(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getdiseaseArea(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.area = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.area)
        deletePost_dict(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getdiseaseArea(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getdiseaseArea(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getdiseaseArea(this.listQuery)
    },
    closeAddDialog(data) {
      const flag = data.flag
      if (flag === 0) {
        this.dialogChanKangAddVisible = false
      } else {
        this.dialogChanKangAddVisible = false
        this.listQuery.page = 1
        this.listQuery.clientid = this.clientid
        this.getOrders(this.listQuery)
      }
    },
    formatOrdertype(row, column) {
      const str = row[column.property]
      if (str === 1) return '预开单'
      else return '现场开单'
    },
    formatAquire(row, column) {
      const str = row[column.property]
      if (str === 0) return '已收单'
      else return '未收单'
    },
    formatSuccess(row, column) {
      const str = row[column.property]
      if (str === 0) return '未开单'
      else return '开单'
    },
    formatFee(row, column) {
      const str = row[column.property]
      if (str === 0) return '收费'
      else return '赠品'
    },
    formatCol(row, column) {
      const str = row[column.property]
      if (str === false) return '否'
      else return '是'
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      } else if (date === null) {
        return ''
      } else {
        return moment(date).format('YYYY-MM-DD')
      }
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
      }
      this.foldList  = []
      this.foldList = parent.map(x => x.__identity)
      return parent
    }
  },
  watch: {
    num: function() {
      this.listQuery.page = 1
      this.listQuery.clientid = this.clientid
      this.getOrders(this.listQuery)
    }
  },
  created: function() {
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
