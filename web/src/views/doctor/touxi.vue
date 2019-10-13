<template>
    <div>
        <div style="margin-top: 20px">
            <el-form  :model="yz_touxi" ref="dataForm" :rules="rules" label-position="left" style='width:90%; margin-left:30px;'>
                <el-row>
                   <el-col :span="8">
                      <el-form-item label="透析方式" prop="txtype">
                        <el-select v-model="yz_touxi.txtype" clearable style="width: 180px" class="myInput" placeholder="透析方式">
                          <el-option label="血液透析" value="血液透析" >
                          </el-option>
                          <el-option label="血流灌注" value="血流灌注" >
                          </el-option>
                          <el-option label="血透+血灌" value="血透+血灌" >
                          </el-option>
                          <el-option label="血浆置换" value="血浆置换" >
                          </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="透析时长(h)" prop="period">
                        <el-input v-model="yz_touxi.period"  class="myInput" style="width:160px"></el-input>
                      </el-form-item>
                   </el-col>
                  <el-col :span="8">
                      <el-form-item label="血管通路" prop="xueguantonglu">
                        <el-select v-model="yz_touxi.xueguantonglu" clearable style="width: 110px" class="myInput">
                          <el-option v-for="item in xgtlSelect" :key="item.id" :value="item.name" :label="item.name" >
                          </el-option>
                        </el-select>
                        <el-select v-model="yz_touxi.xueguantype" clearable style="width: 110px" class="myInput">
                          <el-option v-for="item in xgtlTypeSelect" :key="item.id" :value="item.name" :label="item.name">
                          </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                 </el-row>
                <el-row>
                  <el-col :span="8">
                      <el-form-item label="血透器" prop="xuetoudevice">
                        <el-select v-model="yz_touxi.xuetoudevice" clearable style="width: 200px" class="myInput">
                          <el-option v-for="item in xtqSelect" :key="item.id" :value="item.name" :label="item.name">
                          </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                  <el-col :span="8">
                      <el-form-item label="血滤器" prop="xuelvdevice">
                        <el-select v-model="yz_touxi.xuelvdevice" clearable style="width: 210px" class="myInput">
                          <el-option v-for="item in xlqSelect" :key="item.id" :value="item.name" :label="item.name">
                          </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                  <el-col :span="8">
                      <el-form-item label="灌流器" prop="guanliudevice">
                        <el-select v-model="yz_touxi.guanliudevice" clearable style="width: 220px" class="myInput">
                          <el-option v-for="item in glqSelect" :key="item.id" :value="item.name" :label="item.name">
                          </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                </el-row>
                <el-row>
                  <el-col :span="8">
                     <el-form-item label="周频次:" prop="week">
                        <el-input v-model.number="yz_touxi.week"  class="myInput" style="width:180px"></el-input>
                      </el-form-item>
                   </el-col>
                  <el-col :span="8">
                     <el-form-item label="次数:" prop="times">
                        <el-input v-model.number="yz_touxi.times"  class="myInput" style="width:210px"></el-input>
                      </el-form-item>
                  </el-col>
                  <el-col :span="8">
                     <el-form-item label="钙(mmol/l):" prop="ca">
                        <el-input v-model.number="yz_touxi.ca"  class="myInput" style="width:200px"></el-input>
                      </el-form-item>
                   </el-col>
                </el-row>
                 <el-row>
                   <el-col :span="8">
                     <el-form-item label="钾(mmol/l):" prop="k">
                        <el-input v-model.number="yz_touxi.k"  class="myInput" style="width:160px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="钠(mmol/l):" prop="na">
                        <el-input v-model.number="yz_touxi.na"  class="myInput" style="width:170px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="碳酸氢根(mmol/l):" prop="hco3">
                        <el-input v-model.number="yz_touxi.hco3"  class="myInput" style="width:160px"></el-input>
                      </el-form-item>
                   </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="8">
                     <el-form-item label="透析液流量(ml/mimn):" prop="touxiyeliuliang">
                        <el-input v-model.number="yz_touxi.touxiyeliuliang"  class="myInput" style="width:90px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="血流量(ml/mimn):" prop="xueliuliang">
                        <el-input v-model.number="yz_touxi.xueliuliang"  class="myInput" style="width:130px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="抗凝剂类型:" prop="kangning">
                        <el-select v-model="yz_touxi.kangning" clearable style="width: 220px" class="myInput">
                          <el-option label="无肝素" value="无肝素" >
                          </el-option>
                          <el-option label="肝素" value="肝素" >
                          </el-option>
                          <el-option label="小分子肝素" value="小分子肝素" >
                          </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="8">
                     <el-form-item label="首剂(mg):" prop="shouji">
                        <el-input v-model.number="yz_touxi.shouji"  class="myInput" style="width:180px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="追加(mg/h):" prop="zhuijia">
                        <el-input v-model.number="yz_touxi.zhuijia"  class="myInput" style="width:180px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="总量(mg/h):" prop="total">
                        <el-input v-model.number="yz_touxi.total"  class="myInput" style="width:220px"></el-input>
                      </el-form-item>
                   </el-col>
                  </el-row>
                  <!--<el-row>-->
                   <!--<el-col :span="8">-->
                      <!--<el-form-item label="审核人" prop="checknur">-->
                        <!--<el-select v-model="yz_touxi.checknur" clearable style="width: 120px" class="myInput">-->
                          <!--<el-option v-for="item in nurseSelect" :key="item.id" :value="item.id" :label="item.username">-->
                          <!--</el-option>-->
                        <!--</el-select>-->
                      <!--</el-form-item>-->
                   <!--</el-col>-->
                   <!--<el-col :span="8">-->
                      <!--<el-form-item label="执行人" prop="executenur">-->
                        <!--<el-select v-model="yz_touxi.executenur" clearable style="width: 120px" class="myInput">-->
                          <!--<el-option v-for="item in nurseSelect" :key="item.id" :value="item.id" :label="item.username">-->
                          <!--</el-option>-->
                        <!--</el-select>-->
                      <!--</el-form-item>-->
                   <!--</el-col>-->
                <!--</el-row>-->
            </el-form>
            <div slot="footer" align="center" class="dialog-footer">
              <el-button
                size="small"
                icon="el-icon-close"
                onclick="window.history.go(-1)"
              >关闭
              </el-button>
              <el-button
                size="small"
                icon="el-icon-check"
                v-if="yz_touxi.state === 0"
                type="primary" @click="updateData"
              >保存
              </el-button>
            </div>

        </div>
    </div>
</template>

<script>
import { yz_touxi, createyz_touxi, updateyz_touxi, getNurses } from '@/api/login'
import { getXgtonglu, getXgtongluType, getMaterialType } from '@/api/tx_plan'
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
  name: 'touxi',
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
  props: ['regid', 'patientid', 'num'],
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
    const jianchanum = (rule, value, callback) => {
      if (!Number.isInteger(value)) {
        callback(new Error('请输入数值'))
      } else {
        callback()
      }
    }
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
      token: getToken,
      dialogFormVisible: false,
      dialogStatus: '',
      xgtlSelect: [],
      xgtlTypeSelect: [],
      xtqSelect: [],
      xlqSelect: [],
      glqSelect: [],
      nurseSelect: [],
      yz_touxi: {
        id: '',
        yzlinshi: {
          id: '',
          register_id: ''
        },
        doctorid: '',
        week: '',
        times: '',
        txtype: '',
        period: '',
        xueguantonglu: '',
        xueguantype: '',
        touxidevice: '',
        xuetoudevice: '',
        xuelvdevice: '',
        guanliudevice: '',
        touxiyeliuliang: '',
        xueliuliang: '',
        ca: '',
        k: '',
        na: '',
        hco3: '',
        kangning: '',
        shouji: 0,
        zhuijia: 0,
        total: 0,
        checknur: '',
        executenur: '',
        state: '',
        doctor_state: 1,
        checkNur_id: '',
        exeNur_id: '',
        action: ''
      },
      rules: {
        txtype: [{ required: true, message: '请输入透析方式', trigger: 'blur' }],
        period: [{ required: true, message: '请输入时长', trigger: 'blur' }],
        xueguantonglu: [{ required: true, message: '请输入血管通路', trigger: 'blur' }],
        xueguantype: [{ required: true, message: '请输入血管通路类型', trigger: 'blur' }],
        // xuetoudevice: [{ required: true, message: '请输入血透器', trigger: 'blur' }],
        // xuelvdevice: [{ required: true, message: '请输入血滤器', trigger: 'blur' }],
        // guanliudevice: [{ required: true, message: '请输入灌流器', trigger: 'blur' }],
        week: [
          { required: true, message: '频次不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        times: [
          { required: true, message: '次数不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        ca: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        k: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        na: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        hco3: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        touxiyeliuliang: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        xueliuliang: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        shouji: [
          { validator: jianchanum, trigger: 'blur' }
        ],
        zhuijia: [
          { validator: jianchanum, trigger: 'blur' }
        ],
        total: [
          { validator: jianchanum, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    getTouxi() {
      yz_touxi(this.regid).then(response => {
        const data = response.data.results
        if (data.length > 0) {
          this.yz_touxi = data[0]
        }
      })
    },
    getXgtl(data) {
      getXgtonglu(data).then(response => {
        this.xgtlSelect = response.data
      })
    },
    getXgtlType(data) {
      getXgtongluType(data).then(response => {
        this.xgtlTypeSelect = response.data
      })
    },
    getXtq(data) {
      getMaterialType(data).then(response => {
        this.xtqSelect = response.data
      })
    },
    getXlq(data) {
      getMaterialType(data).then(response => {
        this.xlqSelect = response.data
      })
    },
    getGlq(data) {
      getMaterialType(data).then(response => {
        this.glqSelect = response.data
      })
    },
    getNurseList(data) {
      getNurses(data).then(response => {
        this.nurseSelect = response.data
      })
    },
    resetYz_touxi() {
      this.yz_touxi = {
        id: '',
        yzlinshi: {
          id: '',
          register_id: ''
        },
        doctorid: '',
        week: '',
        times: '',
        txtype: '',
        period: '',
        xueguantonglu: '',
        xueguantype: '',
        touxidevice: '',
        xuetoudevice: '',
        xuelvdevice: '',
        guanliudevice: '',
        touxiyeliuliang: '',
        xueliuliang: '',
        ca: '',
        k: '',
        na: '',
        hco3: '',
        kangning: '',
        shouji: 0,
        zhuijia: 0,
        total: 0,
        doctor_state: 1,
        state: 0,
        action: ''
      }
    },
    handleCreate() {
      this.resetYz_touxi()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.yz_touxi.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.yz_touxi.yzlinshi.register_id = this.regid
          this.yz_touxi.action = 2
          createyz_touxi(this.yz_touxi).then(() => {
            this.list.unshift(this.yz_touxi)
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.getTouxi()
          })
        }
      })
    },
    handleUpdate(row) {
      this.yz_touxi = Object.assign({}, row) // copy obj
      this.yz_touxi.yzlinshi.register_id = this.regid
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.yz_touxi.action = 6 // 0有效 1无效 2审核 3执行 4撤销 5护士修改超滤量 6医生修改
          const tempData = Object.assign({}, this.yz_touxi)
          tempData.checkNur_id = 1
          tempData.exeNur_id = 1
          updateyz_touxi(tempData).then(() => {
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getTouxi()
          })
        }
      })
    },
    UpdateState(row, flag) {
      this.yz_touxi = Object.assign({}, row) // copy obj
      this.yz_touxi.yzlinshi.register_id = this.regid
      const tempData = Object.assign({}, this.yz_touxi)
      tempData.action = flag // 0为点击无效按钮，1为有效
      updateyz_touxi(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '设置成功',
          type: 'success',
          duration: 2000
        })
        this.getTouxi()
      })
    },
    formatState: function(row, column) {
      const zt = row.state
      let s = ''
      switch (zt) {
        case 0:
          s = '未核查'
          break
        case 1:
          s = '已核查(未执行)'
          break
        case 2:
          s = '已执行'
          break
        case 3:
          s = '已撤销'
          break
      }
      return s
    },
    formatCol: function(row, column) {
      return row.doctor_state === 1 ? '有效' : '无效'
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
    num: function() {
      this.getTouxi()
    }
  },
  created: function() {
    const para = {
      page: 1,
      patientid: this.patientid
    }
    this.getXgtl(para)
    this.getXgtlType(para)
    const p1 = {
      page: 1,
      kind: '血透器'
    }
    this.getXtq(p1)
    const p2 = {
      page: 1,
      kind: '血滤器'
    }
    this.getXlq(p2)
    const p3 = {
      page: 1,
      kind: '灌流器'
    }
    this.getGlq(p3)
    this.getTouxi()
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
