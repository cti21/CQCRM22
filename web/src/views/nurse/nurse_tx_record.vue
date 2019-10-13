<template>
    <div>
      <div>
         <el-table
           :data="record.tx_rec"
           :header-cell-style="{background:'#F8F8F8'}"
           v-loading="listLoading"
           stripe>
              <el-table-column type="index" label="序号"  width="50" align="center">
              </el-table-column>
              <el-table-column prop="Adddatetime" label="时间" :formatter="datetimeFormat" width="150" align="center">
              </el-table-column>
              <el-table-column prop="xueliuliang" label="血流量" width="65" align="center">
              </el-table-column>
              <el-table-column prop="jingmaiya" label="静脉压" width="65" align="center">
              </el-table-column>
              <el-table-column prop="zhy_speed" label="置换液速度" width="100" align="center">
              </el-table-column>
              <el-table-column prop="chaolv_rate" label="超滤率" width="65" align="center">
              </el-table-column>
              <el-table-column prop="chaolv_volume" label="超滤量" width="65" align="center">
              </el-table-column>
              <el-table-column prop="xinlv" label="心率" width="55" align="center">
              </el-table-column>
              <el-table-column prop="huxi" label="呼吸" width="55" align="center">
              </el-table-column>
              <el-table-column prop="xueya" label="高血压" width="65" align="center">
              </el-table-column>
              <el-table-column prop="dixueya" label="低血压" width="65" align="center">
              </el-table-column>
              <el-table-column label="操作" fixed="right" align="center">
                <template slot-scope="scope">
                    <el-button type="text" size="small" @click="treatUpdate(scope.row)">修改</el-button>
                    <el-button type="text" size="small" @click="treatPaste(scope.row)">复制</el-button>
                </template>
              </el-table-column>
         </el-table>
          <div slot="footer" class="dialog-footer" style="margin-top: 10px">
              <el-button size="small" onclick="window.history.go(-1)" icon="el-icon-close">关闭</el-button>
              <el-button
                size="small"
                type="primary"
                icon="el-icon-check"
                @click="treatCreate"
              >新增
              </el-button>
          </div>
        </div>

        <div>
          <el-dialog  title="治疗记录" width="55%" :visible.sync="treat_dialogFormVisible">
              <el-form :model="treat" ref="treat_dataForm" :rules="rules" label-position="left" style='width:90%; margin-left:25px;' size="small">
                <el-row>
                   <el-col>
                     <el-form-item label="治疗时间:" prop="adddate">
                        <el-date-picker type="datetime" class="myInput" v-model="treat.adddate" value-format="yyyy-MM-dd hh:mm:ss">
                        </el-date-picker>
                      </el-form-item>
                   </el-col>
                </el-row>
                <el-row>
                   <el-col :span="6">
                     <el-form-item label="心率:" prop="xinlv">
                        <el-input v-model.number="treat.xinlv"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="6">
                     <el-form-item label="呼吸:" prop="huxi">
                        <el-input v-model.number="treat.huxi"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="6">
                     <el-form-item label="低血压:" prop="dixueya">
                        <el-input v-model.number="treat.dixueya"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="6">
                     <el-form-item label="高血压:" prop="xueya">
                        <el-input v-model.number="treat.xueya"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                </el-row>
                <el-row>
                   <el-col :span="6">
                     <el-form-item label="血流量:" prop="xueliuliang">
                        <el-input v-model.number="treat.xueliuliang"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="6">
                     <el-form-item label="静脉压:" prop="jingmaiya">
                        <el-input v-model.number="treat.jingmaiya"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="6">
                     <el-form-item label="跨膜压:" prop="kuamoya">
                        <el-input v-model.number="treat.kuamoya"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="6">
                     <el-form-item label="超滤率:" prop="chaolv_rate">
                        <el-input v-model.number="treat.chaolv_rate"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                </el-row>
                <el-row>
                   <el-col :span="6">
                     <el-form-item label="超滤量:" prop="chaolv_volume">
                        <el-input v-model.number="treat.chaolv_volume"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="置换液速度:" prop="zhy_speed">
                        <el-input v-model.number="treat.zhy_speed"  class="myInput" style="width:60px"></el-input>
                      </el-form-item>
                   </el-col>
                </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="treat_dialogFormVisible = false"
                  >关闭
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    v-if="treat_dialogStatus=='create'"
                    @click="treatCreateData">保存
                  </el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="treatUpdateData">保存
                  </el-button>
              </div>
          </el-dialog>
        </div>


    </div>
</template>

<script>
import { Tx_records, updatetx_record, createtx_treatRec, updatetx_treatRec } from '@/api/login'
import { getToken } from '@/utils/auth'
import moment from 'moment'
import { formatDate } from '@/utils/date'
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
    ElCol
  },
  props: ['patientid','regid', 'num'],
  data: function() {
    const checknum = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('该项不能为空'))
      }
      if (!Number.isInteger(value)) {
        callback(new Error('请输入数值'))
      } else {
        callback()
      }
    }
    return {
      listLoading: false,
      record_dialogFormVisible: false,
      treat_dialogFormVisible: false,
      treat_dialogStatus: 'create',

      record: {
        tx_rec: [],
        id: '',
        Adddatetime: '',
        th_weight: '',
        tz_xiajiang: '',
        th_tiwen: '',
        th_xinlv: '',
        th_huxi: '',
        th_xueya: '',
        sj_time: '',
        sj_chaolv_volume: '',
        comment: ''
      },
      rules: {
        xinlv: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        huxi: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        dixueya: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        xueya: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        xueliuliang: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        jingmaiya: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        kuamoya: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        chaolv_rate: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        chaolv_volume: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        zhy_speed: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ]
      },
      treat: {
        id: '',
        adddate: this.currDatetimeFormat(new Date()),
        xueliuliang: '',
        jingmaiya: '',
        kuamoya: '',
        zhy_speed: '',
        chaolv_rate: '',
        chaolv_volume: '',
        xinlv: '',
        huxi: '',
        dixueya: '',
        xueya: '',
        state: '',
        process: '',
        recid: ''
      }
    }
  },
  methods: {
    getTreatrecordlist(data) {
      Tx_records(data).then(response => {
        this.listLoading = true
        const datalist = response.data.results
        if (datalist.length > 0) {
          this.record = datalist[0]
        }
        this.listLoading = false
      })
    },
    treatUpdate(row) {
      this.treat.id = row.id
      this.treat.adddate = row.Adddatetime
      this.treat.jingmaiya = row.jingmaiya
      this.treat.kuamoya = row.kuamoya
      this.treat.zhy_speed = row.zhy_speed
      this.treat.chaolv_rate = row.chaolv_rate
      this.treat.chaolv_volume = row.chaolv_volume
      this.treat.xinlv = row.xinlv
      this.treat.huxi = row.huxi
      this.treat.dixueya = row.dixueya
      this.treat.xueya = row.xueya
      this.treat.xueliuliang = row.xueliuliang
      this.treat_dialogStatus = 'update'
      this.treat_dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['treat_dataForm'].clearValidate()
      })
    },
    treatUpdateData() {
      this.$refs['treat_dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.treat)
          tempData.recid = this.regid
          updatetx_treatRec(tempData).then(() => {
            this.treat_dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getTreatrecordlist(this.regid)
          })
        }
      })
    },
    treatPaste(row) {
      this.treat.id = parseInt(Math.random() * 100) + 1024
      this.treat.adddate = row.Adddatetime
      this.treat.jingmaiya = row.jingmaiya
      this.treat.kuamoya = row.kuamoya
      this.treat.zhy_speed = row.zhy_speed
      this.treat.chaolv_rate = row.chaolv_rate
      this.treat.chaolv_volume = row.chaolv_volume
      this.treat.xinlv = row.xinlv
      this.treat.huxi = row.huxi
      this.treat.dixueya = row.dixueya
      this.treat.xueya = row.xueya
      this.treat.xueliuliang = row.xueliuliang
      this.treat.recid = this.regid
      createtx_treatRec(this.treat).then(() => {
        this.getTreatrecordlist(this.regid)
      })
    },
    treatCreate() {
      this.treat_dialogFormVisible = true
      this.treat_dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['treat_dataForm'].clearValidate()
      })
    },
    treatCreateData() {
      this.$refs.treat_dataForm.validate((valid) => {
        if (valid) {
          this.treat.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.treat.recid = this.regid
          createtx_treatRec(this.treat).then(() => {
            this.treat_dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.getTreatrecordlist(this.regid)
          })
        }
      })
    },
    currDatetimeFormat: function(date) {
      const y = date.getFullYear()
      let m = date.getMonth() + 1
      m = m < 10 ? ('0' + m) : m
      let d = date.getDate()
      d = d < 10 ? ('0' + d) : d
      const h = date.getHours()
      let minute = date.getMinutes()
      minute = minute < 10 ? ('0' + minute) : minute
      let second= date.getSeconds()
      second = minute < 10 ? ('0' + second) : second
      return y + '-' + m + '-' + d + ' ' + h + ':' + minute + ':' + second
    },
    datetimeFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  watch: {
    num: function() {
      this.getTreatrecordlist(this.regid)
    }
  },
  created: function() {
    this.getTreatrecordlist(this.regid)
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
        height: 28px;
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
