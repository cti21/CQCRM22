<template>
    <div>
         <div style="margin-top: 20px;">
            <el-form :model="patient" ref="dataForm" label-position="left" style='width:90%; margin-left:5px;'>
                <el-row type="flex">
                   <el-col :span="6">
                      <el-form-item label="姓名" prop="name">
                       <el-input v-model="patient.patient.name"  class="myInput" style="width:90px"></el-input>
                      </el-form-item>
                   </el-col>
                   <el-col :span="8">
                     <el-form-item label="性别" prop="sex">
                        <el-input v-model="patient.patient.sex"  class="myInput" style="width:90px"></el-input>
                      </el-form-item>
                   </el-col>
                  <el-col :span="8">
                     <el-form-item label="年龄" prop="age">
                        <el-input v-model="patient.patient.age"  class="myInput" style="width:90px"></el-input>
                      </el-form-item>
                   </el-col>
                 </el-row>
            </el-form>
         </div>
         <div>
            <el-card style="width: 90%">
              <div slot="header" class="clearfix">
                  <label style="margin-right: 50px;font-size: 13px">血管通路</label>
                  <el-button
                    type="primary"
                    style="float: right;height: 33px;padding-top: 8px;margin-top: -5px"
                    icon="el-icon-plus"
                    @click="handleCreate"
                    size="small"
                  >新增
                  </el-button>
              </div>
              <el-table
                :data="list"
                v-loading="listLoading"
                :header-cell-style="{background:'#F8F8F8'}"
                @row-click="handleRowClick"
                stripe>
                <el-table-column prop="tltype" label="通路分类" width="160" show-overflow-tooltip  align="center">
                </el-table-column>
                <el-table-column prop="buwei" label="部位" width="120" align="center">
                </el-table-column>
                <el-table-column prop="material" label="材料" width="120" show-overflow-tooltip align="center">
                </el-table-column>
                <el-table-column prop="cewei" label="侧位" width="60" align="center">
                </el-table-column>
                <el-table-column prop="shoushudate" label="手术日期" width="100" align="center">
                </el-table-column>
                <el-table-column prop="usedate" label="首次使用" width="100" align="center">
                </el-table-column>
                <el-table-column label="操作" fixed="right" align="center">
                  <template slot-scope="scope">
                      <el-button type="text" @click="handleUpdate(scope.row)">修改</el-button>
                      <el-button type="text" @click="handleDelete(scope.row)">删除</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </el-card>
         </div>
         <div>
            <el-card style="width: 90%">
              <div slot="header" class="clearfix">
                  <label style="margin-right: 50px;font-size: 13px">不良事件</label>
                  <el-button
                    type="primary"
                    style="float: right;height: 33px;padding-top: 8px;margin-top: -5px"
                    icon="el-icon-plus"
                    @click="adverse_handleCreate"
                    size="small"
                  >新增
                  </el-button>
              </div>
              <el-table
                :data="adverselist"
                :header-cell-style="{background:'#F8F8F8'}"
                stripe
                v-loading="adverselistLoading">
                <el-table-column prop="begindate" label="开始日期" width="120" :formatter="dateFormat">
                </el-table-column>
                <el-table-column prop="enddate" label="结束日期" width="120" :formatter="dateFormat">
                </el-table-column>
                <el-table-column prop="doctor" label="医生" width="80">
                </el-table-column>
                <el-table-column prop="content" label="事件描述" width="140" show-overflow-tooltip>
                </el-table-column>
                <el-table-column prop="result" label="处理结果" width="140" show-overflow-tooltip>
                </el-table-column>
                <el-table-column label="操作" fixed="right">
                  <template slot-scope="scope">
                      <el-button type="text" @click="adverse_handleUpdate(scope.row)">修改</el-button>
                      <el-button type="text" @click="adverse_handleDelete(scope.row)">删除</el-button>
                  </template>
                </el-table-column>
              </el-table>
            </el-card>
         </div>
         <div style="margin-top: 20px;">
           <el-dialog  title="血管通路" width="45%" :visible.sync="dialogFormVisible">
              <el-form :model="xgtonglu" ref="dataForm" :rules="rules" label-position="left" style='width:90%; margin-left:25px;'>
                  <el-row type="flex" justify="end">
                     <el-col :span="12">
                        <el-form-item label="通路分类" prop="tltype">
                          <el-select v-model="xgtonglu.tltype" @change="getBuwei($event)"  style="width: 150px" class="myInput" placeholder="透析方式">
                            <el-option v-for="item in tltypes" :key="item.label" :label="item.label" :value="item.value">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="通路部位" prop="buwei">
                          <el-select v-model="xgtonglu.buwei" clearable style="width: 130px" class="myInput" placeholder="透析方式">
                            <el-option v-for="item in buweis" :key="item.label" :label="item.label" :value="item.value">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row  type="flex" justify="end">
                    <el-col :span="12">
                        <el-form-item label="通路材质" prop="material">
                          <el-select v-model="xgtonglu.material" clearable style="width: 130px" class="myInput">
                            <el-option  v-for="mat in materials" :key="mat.label" :label="mat.label" :value="mat.value" >
                            </el-option>
                          </el-select>
                         </el-form-item>
                     </el-col>
                     <el-col :span="12">
                        <el-form-item label="通路侧位" prop="cewei">
                          <el-select v-model="xgtonglu.cewei" clearable style="width: 130px" class="myInput">
                            <el-option label="左侧" value="左侧" >
                            </el-option>
                            <el-option label="右侧" value="右侧" >
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row  type="flex" justify="end">
                    <el-col :span="12">
                        <el-form-item label="术式" prop="shushi">
                          <el-input v-model="xgtonglu.shushi" style="width: 170px;height: 25px" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                    <el-col :span="12">
                        <el-form-item label="手术日期" prop="shoushudate">
                          <el-date-picker v-model="xgtonglu.shoushudate" type="date" value-format="yyyy-MM-dd"
                                          format="yyyy-MM-dd" clearable style="width: 135px" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                  </el-row>
                   <el-row type="flex">
                     <el-col :span="12">
                       <el-form-item label="首次使用" prop="usedate">
                          <el-date-picker v-model="xgtonglu.usedate" type="date" value-format="yyyy-MM-dd"
                                          format="yyyy-MM-dd" class="myInput" style="width:135px"></el-date-picker>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="首次成功" prop="successdate">
                          <el-date-picker v-model="xgtonglu.successdate" type="date" value-format="yyyy-MM-dd"
                                          format="yyyy-MM-dd" class="myInput" style="width:135px"></el-date-picker>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row  type="flex" justify="end">
                     <el-col :span="12">
                       <el-form-item label="失败日期" prop="faildate">
                          <el-date-picker v-model="xgtonglu.faildate" type="date" value-format="yyyy-MM-dd"
                                          format="yyyy-MM-dd" class="myInput" style="width:135px"></el-date-picker>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="是否用当前通路" prop="use">
                          <el-input v-model="xgtonglu.use"  class="myInput" style="width:80px"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
                   <el-row type="flex">
                     <el-col :span="12">
                       <el-form-item label="失败原因" prop="failcause">
                          <el-input v-model="xgtonglu.failcause"  class="myInput" style="width:135px"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="备注" prop="comment">
                          <el-input v-model="xgtonglu.comment"  class="myInput" style="width:180px"></el-input>
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

         <div style="margin-top: 20px;">
           <el-dialog  title="血管通路不良事件" width="45%" :visible.sync="adversedialogFormVisible">
              <el-form :model="xgtonglu_adverse" ref="adverseForm" :rules="rules_adverse" label-position="left" style='width:90%; margin-left:25px;'>
                  <el-row type="flex" justify="end">
                     <el-col :span="12">
                        <el-form-item label="开始日期" prop="begindate">
                          <el-date-picker
                            v-model="xgtonglu_adverse.begindate"
                            type="date"
                            clearable
                            style="width: 135px"
                            value-format="yyyy-MM-dd"
                            class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                     <el-col :span="12">
                       <el-form-item label="结束日期" prop="enddate">
                          <el-date-picker
                            v-model="xgtonglu_adverse.enddate"
                            type="date"
                            clearable
                            style="width: 135px"
                            value-format="yyyy-MM-dd"
                            class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row  type="flex" justify="end">
                    <el-col :span="24">
                        <el-form-item label="事件描述" prop="content">
                          <el-input v-model="xgtonglu_adverse.content"  class="myInput" style="width:365px"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row  type="flex" justify="end">
                     <el-col :span="24">
                        <el-form-item label="处理过程" prop="handle">
                          <el-input v-model="xgtonglu_adverse.handle"  class="myInput" style="width:365px"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row  type="flex" justify="end">
                    <el-col :span="24">
                        <el-form-item label="处理结果" prop="result">
                          <el-input v-model="xgtonglu_adverse.result" style="width: 365px" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row  type="flex" justify="end">
                    <el-col :span="24">
                        <el-form-item label="备注" prop="comment">
                          <el-input v-model="xgtonglu_adverse.comment" style="width: 365px;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="adversedialogFormVisible = false"
                  >关闭
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    v-if="adversedialogStatus=='create'"
                    @click="adverse_createData">保存
                  </el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="adverse_updateData">保存
                  </el-button>
              </div>
           </el-dialog>
         </div>

    </div>
</template>

<script>
import { patientfee } from '@/api/login'
import { xgtonglus, createxgtonglu, updatexgtonglu, deletexgtonglu } from '@/api/xgtonglu'
import { xgtonglu_adverse, createxgtonglu_adverse, updatexgtonglu_adverse, deletexgtonglu_adverse } from '@/api/xgtonglu'
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
  props: ['patientid','regid'],
  data: function() {
    return {
      // 血管通路
      list: null,
      total: null,
      listLoading: true,
      dialogStatus: '',
      dialogFormVisible: false,

      // 血管通路不良事件
      adverselist: null,
      adversetotal: null,
      adverselistLoading: false,
      adversedialogStatus: '',
      adversedialogFormVisible: false,
      xgtonglu_id: '',

      // 患者信息
      patient: {
        patient: {
          id: undefined,
          patientid: undefined,
          name: '',
          sex: '',
          adddate: new Date(),
          phone1: '',
          age: ''
        },
        charge: 0,
        balance: 0
      },
      token: getToken,
      rules: {
        tltype: [{ required: true, message: '请输入通路分类', trigger: 'blur' }],
        buwei: [{ required: true, message: '请输入通路部位', trigger: 'blur' }],
        material: [{ required: true, message: '请输入通路材质', trigger: 'blur' }],
        cewei: [{ required: true, message: '请输入通路侧位', trigger: 'blur' }],
        shoushudate: [{ required: true, message: '请输入手术日期', trigger: 'blur' }]
      },
      rules_adverse: {
        begindate: [{ required: true, message: '请输入开始日期', trigger: 'blur' }],
        enddate: [{ required: true, message: '请输入结束日期', trigger: 'blur' }]
      },
      xgtonglu: {
        id: '',
        tltype: '',
        buwei: '',
        material: '',
        cewei: '',
        shushi: '',
        shoushudate: null,
        usedate: null,
        successdate: null,
        faildate: null,
        use: 0,
        failcause: '',
        comment: '',
        patient: ''
      },
      xgtonglu_adverse: {
        id: '',
        doctor: '',
        begindate: this.currDateFormat(new Date()),
        enddate: this.currDateFormat(new Date()),
        content: '',
        handle: '',
        result: '',
        comment: '',
        Xgtonglu: null
      },
      tltypes: [
        { label: '中心静脉临时导管置管术', value: '中心静脉临时导管置管术' },
        { label: '中心静脉长期导管置管术', value: '中心静脉长期导管置管术' },
        { label: '自体动静脉内瘘成形术', value: '自体动静脉内瘘成形术' },
        { label: '移植血管搭桥造瘘术', value: '移植血管搭桥造瘘术' }
      ],
      buweis: [],
      materials: [],
      para: {
        patientid: this.patientid,
        registerid: this.regid
      }
    }
  },
  methods: {
    getXgtongluList() {
      xgtonglus(this.patientid).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
        this.dialogStatus = 'create'
      })

      patientfee(this.para).then(response => {
        this.patient = response.data.results[0]
      })
    },
    getXgtonglu_adverseList(data) {
      xgtonglu_adverse(data).then(response => {
        this.adverselistLoading = true
        this.adverselist = response.data.results
        this.adversetotal = response.data.count
        this.adverselistLoading = false
      })
    },
    getBuwei(event) {
      const tempTltype = []
      const tempMaterial = []
      const allbuwei = [
        { tltype: '中心静脉临时导管置管术', label: '锁骨下静脉' },
        { tltype: '中心静脉临时导管置管术', label: '股静脉' },
        { tltype: '中心静脉临时导管置管术', label: '颈内静脉' },
        { tltype: '中心静脉长期导管置管术', label: '颈内静脉' },
        { tltype: '中心静脉长期导管置管术', label: '颈外静脉' },
        { tltype: '自体动静脉内瘘成形术', label: '腕瘘' },
        { tltype: '自体动静脉内瘘成形术', label: '前臂尺侧瘘' },
        { tltype: '自体动静脉内瘘成形术', label: '上臂内漏' },
        { tltype: '自体动静脉内瘘成形术', label: '小腿内漏' },
        { tltype: '移植血管搭桥造瘘术', label: '前臂襻式' },
        { tltype: '移植血管搭桥造瘘术', label: '前臂桥式' },
        { tltype: '移植血管搭桥造瘘术', label: '上臂桥式' },
        { tltype: '移植血管搭桥造瘘术', label: '上臂襻式' },
        { tltype: '移植血管搭桥造瘘术', label: '锁骨下襻式' },
        { tltype: '移植血管搭桥造瘘术', label: '下肢襻式' },
        { tltype: '移植血管搭桥造瘘术', label: '锁骨下动脉-下腔静脉' },
        { tltype: '移植血管搭桥造瘘术', label: '锁骨下动脉-髂静脉' }
      ]
      const allmaterial = [
        { tltype: '中心静脉临时导管置管术', label: '人造血管(国产)' },
        { tltype: '中心静脉临时导管置管术', label: '人造血管(进口)' },
        { tltype: '中心静脉长期导管置管术', label: '人造血管(国产)' },
        { tltype: '中心静脉长期导管置管术', label: '人造血管(进口)' },
        { tltype: '自体动静脉内瘘成形术', label: '自体血管' },
        { tltype: '移植血管搭桥造瘘术', label: '自体血管' },
        { tltype: '移植血管搭桥造瘘术', label: '同种异体血管' },
        { tltype: '移植血管搭桥造瘘术', label: '异种血管' },
        { tltype: '移植血管搭桥造瘘术', label: '人造血管(国产)' },
        { tltype: '移植血管搭桥造瘘术', label: '人造血管(进口)' }
      ]
      for (const item of allbuwei) {
        if (event === item.tltype) {
          tempTltype.push({ label: item.label, value: item.label })
        }
      }
      this.buweis = tempTltype

      for (const mat of allmaterial) {
        if (event === mat.tltype) {
          tempMaterial.push({ label: mat.label, value: mat.label })
        }
      }
      this.materials = tempMaterial
    },
    resetxgtonglu() {
      this.xgtonglu = {
        id: '',
        tltype: '',
        buwei: '',
        material: '',
        cewei: '',
        shushi: '',
        shoushudate: null,
        usedate: null,
        successdate: null,
        faildate: null,
        use: 0,
        failcause: '',
        comment: '',
        patient: ''
      }
    },
    resetxgtonglu_adverse() {
      this.xgtonglu_adverse = {
        id: '',
        doctor: '',
        begindate: this.currDateFormat(new Date()),
        enddate: this.currDateFormat(new Date()),
        content: '',
        handle: '',
        result: '',
        comment: '',
        Xgtonglu: null
      }
    },
    handleRowClick(row, event, column) {
      this.xgtonglu_id = row.id
      this.getXgtonglu_adverseList(this.xgtonglu_id)
    },
    handleCreate() {
      this.resetxgtonglu()
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    adverse_handleCreate() {
      this.resetxgtonglu_adverse()
      this.adversedialogFormVisible = true
      this.adversedialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['adverseForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.xgtonglu.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.xgtonglu.patient = this.patientid
          console.log(this.xgtonglu)
          createxgtonglu(this.xgtonglu).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.getXgtongluList()
          })
        }
      })
    },
    adverse_createData() {
      this.$refs.adverseForm.validate((valid) => {
        if (valid) {
          this.xgtonglu_adverse.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.xgtonglu_adverse.Xgtonglu = this.xgtonglu_id
          createxgtonglu_adverse(this.xgtonglu_adverse).then(() => {
            this.adverselist.unshift(this.xgtonglu_adverse)
            this.adversedialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.getXgtonglu_adverseList(this.xgtonglu_id)
          })
        }
      })
    },
    handleUpdate(row) {
      this.xgtonglu = Object.assign({}, row) // copy obj
      // this.patient.adddate = new Date(this.patient.adddate)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    adverse_handleUpdate(row) {
      this.xgtonglu_adverse = Object.assign({}, row) // copy obj
      this.adversedialogStatus = 'update'
      this.adversedialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['adverseForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          // this.xgtonglu.patient = this.$route.query.patientid
          this.xgtonglu.patient = this.patientid
          const tempData = Object.assign({}, this.xgtonglu)
          updatexgtonglu(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
          })
        }
      })
    },
    adverse_updateData() {
      this.$refs['adverseForm'].validate((valid) => {
        if (valid) {
          this.xgtonglu_adverse.Xgtonglu = this.xgtonglu_id
          const tempData = Object.assign({}, this.xgtonglu_adverse)
          updatexgtonglu_adverse(tempData).then(() => {
            this.adversedialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getXgtonglu_adverseList(this.xgtonglu_id)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.xgtonglu = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.xgtonglu)
        deletexgtonglu(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.getXgtongluList()
        })
      })
    },
    adverse_handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.xgtonglu_adverse = Object.assign({}, row)
        const tempData = Object.assign({}, this.xgtonglu_adverse)
        deletexgtonglu_adverse(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.getXgtonglu_adverseList(this.xgtonglu_id)
        })
      })
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      if (date === null){
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    },
    currDateFormat: function(date) {
      const y = date.getFullYear()
      let m = date.getMonth() + 1
      m = m < 10 ? ('0' + m) : m
      let d = date.getDate()
      d = d < 10 ? ('0' + d) : d
      return y + '-' + m + '-' + d
    }
  },
  created: function() {
    this.getXgtongluList()
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
        height: 30px;
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
