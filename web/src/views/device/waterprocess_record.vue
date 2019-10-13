<template>
    <div>
        <div class="filter-container">
              <el-date-picker
                v-model="fromdate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="检测日期开始">
              </el-date-picker>
              <el-date-picker
                v-model="todate"
                style="width: 160px"
                class="myInput"
                type="date"
                value-format="yyyy-MM-dd"
                placeholder="检测日期结束">
              </el-date-picker>
              <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
              <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
        </div>
        <div style="margin-top: 20px">
          <el-table
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column prop="date" label="监测时间" width="100" :formatter="dateFormat">
            </el-table-column>
            <el-table-column prop="alerm" label="报警" width="60" align="center">
            </el-table-column>
            <el-table-column prop="alarmlevel" label="报警等级"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="cl_jinshuip" label="进水压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="cl_nongshuip" label="浓水压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="cl_jinshuif" label="进水流量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="cl_chanshuip" label="产水流量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_jinshuip" label="进水压力"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_zhongjianp" label="中间压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_chanshuip" label="产水压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_chanshuif" label="产水流量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_nongshuif" label="浓水流量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_jinshuidd" label="进水电导" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst1_chanshuidd" label="产水电导"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst2_jinshuip" label="进水压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst2_zhongjianp" label="中间压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst2_chanshuip" label="产水压力" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst2_chanshuif" label="产水流量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst2_nongshuif" label="浓水流量" width="60" align="center">
            </el-table-column>
            <el-table-column prop="fst2_chanshuidd" label="产水电导"  width="60" align="center">
            </el-table-column>
            <el-table-column prop="recorder" label="记录人" width="60" align="center">
            </el-table-column>
            <el-table-column prop="comment" label="备注"  width="60" show-overflow-tooltip align="center">
            </el-table-column>
            <el-table-column label="操作" width="100px" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination background
                     @size-change="handleSizeChange"
                     @current-change="handleCurrentChange"
                     :current-page="listQuery.page"
                     :page-sizes="[5,10,20,30, 50]"
                     :page-size="listQuery.limit"
                     layout="total, prev, pager, next, jumper"
                     :total="total">
                </el-pagination>
          </div>
        </div>

        <div>
          <el-dialog  title="水质监测记录" width="50%" :visible.sync="dialogFormVisible">
                <el-form  :model="wpr_obj" ref="dataForm" label-position="left" label-width="140px" style='width:90%; margin-left:30px;'>
                     <el-row>
                       <el-col :span="12">
                          <el-form-item label="监测时间" prop="date">
                            <el-date-picker v-model="wpr_obj.date" class="myInput" style="width: 140px">
                            </el-date-picker>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="是否报警" prop="alerm">
                            <el-input v-model="wpr_obj.alerm" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                    <el-row>
                        <el-col :span="12">
                          <el-form-item label="报警等级" prop="alarmlevel">
                            <el-input v-model="wpr_obj.alarmlevel" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                        <el-col :span="12">
                          <el-form-item label="超滤机进水压力"  prop="cl_jinshuip">
                            <el-input v-model="wpr_obj.cl_jinshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                     </el-row>
                     <el-row>
                       <el-col :span="12">
                          <el-form-item label="超滤机浓水压力" prop="cl_nongshuip">
                            <el-input v-model="wpr_obj.cl_nongshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="超滤机进水流量" prop="cl_jinshuif">
                            <el-input v-model="wpr_obj.cl_jinshuif" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                    <el-row>
                        <el-col :span="12">
                          <el-form-item label="超滤机产水流量" prop="cl_chanshuip">
                            <el-input v-model="wpr_obj.cl_chanshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                        <el-col :span="12">
                          <el-form-item label="一级反渗透进水压力"  prop="fst1_jinshuip">
                            <el-input v-model="wpr_obj.fst1_jinshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                     <el-row>
                       <el-col :span="12">
                          <el-form-item label="一级反渗透中间压力" prop="fst1_zhongjianp">
                            <el-input v-model="wpr_obj.fst1_zhongjianp" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="一级反渗透产水压力" prop="fst1_chanshuip">
                            <el-input v-model="wpr_obj.fst1_chanshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                    <el-row>
                       <el-col :span="12">
                          <el-form-item label="一级反渗透产水流量" prop="fst1_chanshuif">
                            <el-input v-model="wpr_obj.fst1_chanshuif" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="一级反渗透浓水流量" prop="fst1_nongshuif">
                            <el-input v-model="wpr_obj.fst1_nongshuif" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                    <el-row>
                        <el-col :span="12">
                          <el-form-item label="一级反渗透进水电导" prop="fst1_jinshuidd">
                            <el-input v-model="wpr_obj.fst1_jinshuidd" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                        <el-col :span="12">
                          <el-form-item label="一级反渗透产水电导"  prop="fst1_chanshuidd">
                            <el-input v-model="wpr_obj.fst1_chanshuidd" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                     </el-row>
                     <el-row>
                       <el-col :span="12">
                          <el-form-item label="二级反渗透进水压力" prop="fst2_jinshuip">
                            <el-input v-model="wpr_obj.fst2_jinshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="二级反渗透中间压力" prop="fst2_zhongjianp">
                            <el-input v-model="wpr_obj.fst2_zhongjianp" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                    <el-row>
                        <el-col :span="12">
                          <el-form-item label="二级反渗透产水压力" prop="fst2_chanshuip">
                            <el-input v-model="wpr_obj.fst2_chanshuip" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                        <el-col :span="12">
                          <el-form-item label="二级反渗透产水流量"  prop="fst2_chanshuif">
                            <el-input v-model="wpr_obj.fst2_chanshuif" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                     <el-row>
                       <el-col :span="12">
                          <el-form-item label="二级反渗透浓水流量" prop="fst2_nongshuif">
                            <el-input v-model="wpr_obj.fst2_nongshuif" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                       </el-col>
                       <el-col :span="12">
                          <el-form-item label="二级反渗透产水电导" prop="fst2_chanshuidd">
                            <el-input v-model="wpr_obj.fst2_chanshuidd" style="width: 140px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                    <el-row>
                        <el-col>
                          <el-form-item label="备注" prop="comment">
                            <el-input v-model="wpr_obj.comment" style="width: 420px;" class="myInput"></el-input>
                          </el-form-item>
                        </el-col>
                     </el-row>
                </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  icon="el-icon-close"
                  @click="dialogFormVisible = false"
                >关闭
                </el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogStatus=='create'"
                  @click="createData"
                >保存
                </el-button>
                <el-button
                  size="small"
                  v-else
                  type="primary"
                  icon="el-icon-check"
                  @click="updateData"
                >保存
                </el-button>
              </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { water_process_recs, createwater_process_rec, updatewater_process_rec,
         deletewater_process_rec } from '@/api/device'
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
    ElCol },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      fromdate: '',
      todate: '',
      matSelect: '',
      dialogFormVisible: false,
      token: getToken,
      dialogStatus: '',
      materialSelect: [
        { id: '1', name: '透析器' },
        { id: '2', name: '滤过透析器' },
        { id: '3', name: '血滤器' },
        { id: '4', name: '血管路' },
        { id: '5', name: '内漏穿刺针'},
        { id: '6', name: '留置导管' },
        { id: '7', name: '碳肾' },
        { id: '8', name: '树脂罐' },
        { id: '9', name: '透析粉' },
        { id: '10', name: '透析A粉'},
        { id: '11', name: '透析干粉桶' },
        { id: '12', name: '血浆分离器' },
        { id: '13', name: '细菌过滤器' },
        { id: '14', name: '补液管' },
        { id: '15', name: '消毒液'},
        { id: '16', name: '活检针' },
        { id: '17', name: '套盘' }
      ],
      wpr_obj: {
        id: null,
        date: '',
        alerm: '',
        alarmlevel: '',
        cl_jinshuip: '',
        cl_nongshuip: '',
        cl_jinshuif: '',
        cl_chanshuip: '',
        fst1_jinshuip: '',
        fst1_zhongjianp: '',
        fst1_chanshuip: '',
        fst1_chanshuif: '',
        fst1_nongshuif: '',
        fst1_jinshuidd: '',
        fst1_chanshuidd: '',
        fst2_jinshuip: '',
        fst2_zhongjianp: '',
        fst2_chanshuip: '',
        fst2_chanshuif: '',
        fst2_nongshuif: '',
        fst2_chanshuidd: '',
        recorder: '',
        comment: ''
      },
      queryparams: {
        page: 1,
        fromdate: '',
        todate: ''
      }
    }
  },
  methods: {
    getMonitorRecList(data) {
      water_process_recs(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    reseWaterProcessRec() {
      this.wpr_obj = {
        id: null,
        date: new Date(),
        alerm: '',
        alarmlevel: '',
        cl_jinshuip: '',
        cl_nongshuip: '',
        cl_jinshuif: '',
        cl_chanshuip: '',
        fst1_jinshuip: '',
        fst1_zhongjianp: '',
        fst1_chanshuip: '',
        fst1_chanshuif: '',
        fst1_nongshuif: '',
        fst1_jinshuidd: '',
        fst1_chanshuidd: '',
        fst2_jinshuip: '',
        fst2_zhongjianp: '',
        fst2_chanshuip: '',
        fst2_chanshuif: '',
        fst2_nongshuif: '',
        fst2_chanshuidd: '',
        recorder: '',
        comment: ''
      }
    },
    handleReset() {
      this.queryparams.page = 1
      this.queryparams.fromdate = ''
      this.queryparams.todate = ''
      this.fromdate = ''
      this.todate = ''
      this.getMonitorRecList(this.queryparams)
    },
    handleCreate() {
      this.reseWaterProcessRec()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.wpr_obj.id = parseInt(Math.random() * 100) + 1024 // mock a id
          createwater_process_rec(this.wpr_obj).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getMonitorRecList(this.queryparams)
          })
        }
      })
    },
    handleUpdate(row) {
      this.wpr_obj = Object.assign({}, row) // copy obj
      this.dialogFormVisible = true
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.wpr_obj)
          updatewater_process_rec(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.queryparams.page = 1
            this.getMonitorRecList(this.queryparams)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.wpr_obj = Object.assign({}, row)
        const tempData = Object.assign({}, this.wpr_obj)
        deletewater_process_rec(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.queryparams.page = 1
          this.getMonitorRecList(this.queryparams)
        })
      })
    },
    handleFilter() {
      this.listQuery.limit = 5
      this.listQuery.offset = 0
      this.queryparams.page = 1
      this.queryparams.fromdate = this.fromdate
      this.queryparams.todate = this.todate
      this.getMonitorRecList(this.queryparams)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getMonitorRecList()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.queryparams.page = val
      this.getMonitorRecList(this.queryparams)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]

      if (date === undefined || date === null) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  created: function() {
    this.getMonitorRecList(this.queryparams)
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
    .el-table td{
      padding:6px 0;
    }
    .el-table th{
      padding:6px 0;
      height: 50px;
    }
</style>
