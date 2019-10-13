<template>
    <div>
        <div class="filter-container">
              <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary">新增计价项目</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column type="index" label="序号"  width="60"  align="center">
            </el-table-column>
            <el-table-column prop="yztype" label="类别" width="100" align="center">
            </el-table-column>
            <el-table-column prop="name" label="项目" width="120" align="center">
            </el-table-column>
            <el-table-column prop="gg" label="规格" width="100" align="center">
            </el-table-column>
            <el-table-column prop="count" label="数量" width="100" align="center">
            </el-table-column>
            <el-table-column prop="dw" label="单位" width="100" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="state" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" v-if="scope.row.state === 0" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" v-if="scope.row.state === 0" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <div>
          <el-dialog  title="耗材、处置项目" width="60%" :visible.sync="dialogFormVisible">
                  <el-form  :model="tc" ref="dataForm"   label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="名称"  prop="name">
                              <el-input type="input" v-model="tc.name" style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="规格" prop="gg">
                              <el-input type="input" v-model="tc.gg" style="width: 200px;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                      <el-row>
                       <el-col :span="12">
                          <el-form-item label="单位" prop="dw">
                            <el-input type="input" v-model="tc.dw" style="width: 200px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="数量" prop="count">
                            <el-input type="input" v-model="tc.count" style="width: 200px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                      </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
                  <el-button @click="dialogFormVisible = false">取消</el-button>
                  <el-button type="primary" @click="updateData">保存</el-button>
                </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="新增计价项目" width="65%" :visible.sync="dialogListVisible">
            <el-row style="margin-bottom: 10px">
              <el-col :span="12">
                <label style="margin-right: 20px">医嘱类型</label>
                <el-select v-model="hctype" clearable style="width: 200px" class="myInput" @change="selectChange" placeholder="请选择医嘱类型">
                    <el-option label="处置" value="处置" >
                    </el-option>
                    <el-option label="耗材" value="耗材" >
                    </el-option>
                </el-select>
              </el-col>
            </el-row>
            <div style="float: right">
              <el-input v-model="hcname" style="width: 200px;margin-right: 10px;" class="myInput" placeholder="名称">
              </el-input>
              <el-button circle icon="el-icon-search" @click="material_handleFilter" style="margin-right: 40px;"></el-button>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: left;margin-right: 20px;">
                <el-pagination background
                     @current-change="material_handleCurrentChange"
                     :current-page="material_listQuery.page"
                     :page-size="material_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="material_total">
                </el-pagination>
            </div>
            <el-table :data="material_list" highlight-current-row stripe @row-dblclick="rowdbclick">
              <el-table-column type="index" label="序号">
              </el-table-column>
              <el-table-column prop="id" v-if="false">
              </el-table-column>
              <el-table-column prop="name" label="名称">
              </el-table-column>
              <el-table-column prop="gg" label="规格">
              </el-table-column>
              <el-table-column prop="dw" label="剂量单位">
              </el-table-column>
              <el-table-column prop="jiage" label="单价">
              </el-table-column>
              <el-table-column prop="kucun" label="库存">
              </el-table-column>
            </el-table>
            <div>
               <div style="margin-top: 10px">医嘱列表</div>
               <el-table :data="multipleSelection">
                  <el-table-column type="index" label="序号"  width="50">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false">
                  </el-table-column>
                  <el-table-column prop="name" label="名称" width="120">
                  </el-table-column>
                  <el-table-column prop="gg" label="规格" width="60" v-if="false">
                  </el-table-column>
                  <el-table-column prop="dw" label="剂量单位" width="100">
                  </el-table-column>
                  <el-table-column prop="week" label="频次" width="100">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.week" clearable style="width: 100px" size="mini">
                          <el-option label="QW" value="QW" >
                          </el-option>
                          <el-option label="QD" value="QD" >
                          </el-option>
                          <el-option label="QH" value="QH" >
                          </el-option>
                          <el-option label="ST" value="ST" >
                          </el-option>
                        </el-select>
                    </template>
                  </el-table-column>
                  <el-table-column prop="path" label="用药途径" width="110">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.path" clearable style="width: 110px" size="mini">
                          <el-option label="静脉注射" value="静脉注射" >
                          </el-option>
                          <el-option label="静脉滴注" value="静脉滴注" >
                          </el-option>
                          <el-option label="肌肉注射" value="肌肉注射" >
                          </el-option>
                          <el-option label="皮下注射" value="皮下注射" >
                          </el-option>
                          <el-option label="局部溶栓" value="局部溶栓" >
                          </el-option>
                          <el-option label="口服" value="口服" >
                          </el-option>
                          <el-option label="舌下含服" value="舌下含服" >
                          </el-option>
                        </el-select>
                    </template>
                  </el-table-column>
                  <el-table-column prop="count" label="单次剂量" width="110">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.count" type="number" size="mini" placeholder="单次剂量">
                        </el-input>
                    </template>
                  </el-table-column>
                  <el-table-column prop="feetype" label="是否自备" width="100">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.feetype" clearable style="width: 100px" size="mini">
                          <el-option label="自备" value="自备" >
                          </el-option>
                          <el-option label="收费" value="收费" >
                          </el-option>
                        </el-select>
                    </template>
                  </el-table-column>
                  <el-table-column label="操作" fixed="right">
                    <template slot-scope="scope">
                      <el-button type="text" size="small" @click="dict_handleDelete(scope.row)">删除</el-button>
                    </template>
                  </el-table-column>
                </el-table>
            </div>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button type="primary" style="height:33px;padding-top: 8px" @click="submitData">提交</el-button>
              <el-button style="height:33px;padding-top: 8px" @click="dialogListVisible = false">取消</el-button>
            </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { chuzhiDict, materialDict } from '@/api/login'
import { yz_material, createyz_material, updateyz_material, deleteyz_material } from '@/api/nurse'
import { getToken } from '@/utils/auth'
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
    ElCol
  },
  props: ['yzdrug_id'],
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: false,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      material_list: null,
      material_total: null,
      material_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      multipleSelection: [],
      hctype: '',
      hcname: '',
      dialogListVisible: false,
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      taocanobj: {
        id: null,
        yztype: '',
        dicid: '',
        name: '',
        dw: '',
        gg: '',
        price: '',
        count: '',
        yz_drug: '',
        kind: ''
      },
      tc: {
        id: null,
        yztype: '',
        dicid: '',
        name: '',
        dw: '',
        gg: '',
        price: '',
        count: '',
        yz_drug: '',
        kind: ''
      },
      queryparams: {
        page: 1,
        yzdrug_id: this.yzdrug_id
      },
      params: {
        page: 1,
        name: ''
      }
    }
  },
  methods: {
    getYz_material(data) {
      yz_material(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getChuzhiList(data) {
      chuzhiDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getMaterialList(data) {
      materialDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    resetTc() {
      this.tc = {
        id: null,
        yztype: '',
        dicid: '',
        name: '',
        dw: '',
        gg: '',
        price: '',
        count: '',
        yz_drug: '',
        kind: ''
      }
    },
    selectChange: function (val) {
      this.material_list = null
      this.params.page = 1
      this.params.name = ''
      this.hcname = ''
      switch (val) {
        case '耗材':
          this.getMaterialList(this.params)
          break
        case '处置':
          this.getChuzhiList(this.params)
          break
      }
    },
    material_handleFilter() {
      this.material_listQuery.limit = 5
      this.material_listQuery.offset = 0
      this.params.page = 1
      this.params.name = this.hcname
      switch (this.hctype) {
        case '耗材':
          this.getMaterialList(this.params)
          break
        case '处置':
          this.getChuzhiList(this.params)
          break
      }
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      this.params.page = val
      this.getMaterialList(this.params)
    },
    rowdbclick(row,event) {
      if (this.hctype === '耗材' && row.kucun === 0) {
        this.$notify({
          title: '提示',
          message: '库存已经为0',
          type: 'warning',
          duration: 2000
        })
      } else {
        this.multipleSelection.push(row)
      }
    },
    dict_handleDelete(row) {
      this.multipleSelection.splice(this.multipleSelection.findIndex(v => v.id === row.id), 1)
    },
    submitData() {
      if (this.multipleSelection.length > 0) {
        this.multipleList = []
        this.multipleSelection.forEach((item) => {
          this.taocanobj = Object.assign({}, item)
          this.taocanobj.yztype = 'a'
          this.taocanobj.dicid = item.id
          this.taocanobj.kind = item.kind
          this.taocanobj.yz_drug = this.yzdrug_id
          this.taocanobj.price = 1
          this.multipleList.push(this.taocanobj)
        })
        createyz_material(this.multipleList).then(() => {
          this.$notify({
            title: '成功',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogListVisible = false
          this.getYz_material(this.queryparams)
          this.$emit('refreshfee')
        })
      }
    },
    handleCreate() {
      this.resetTc()
      this.dialogListVisible = true
    },
    handleUpdate(row) {
      this.dialogStatus = 'update'
      this.tc = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.tc)
          tempData.kind = 1
          tempData.yzdrug_id = this.yzdrug_id
          updateyz_material(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getYz_material(this.queryparams)
            this.$emit('refreshfee')
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.tc = Object.assign({}, row)
        const tempData = Object.assign({}, this.tc)
        deleteyz_material(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getYz_material(this.queryparams)
          this.$emit('refreshfee')
        })
      })
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getYz_material(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  watch: {
    yzdrug_id: function() {
      if (this.yzdrug_id !== '') {
        this.queryparams.yzdrug_id = this.yzdrug_id
        this.getYz_material(this.queryparams)
      }
    }
  },
  created: function() {
    if (this.yzdrug_id !== '') {
      this.queryparams.yzdrug_id = this.yzdrug_id
      this.getYz_material(this.queryparams)
    }
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
</style>
