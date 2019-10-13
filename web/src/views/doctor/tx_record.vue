<template>
    <div>
           <div style="margin-bottom: 10px">
              <el-card style="width: 90%">
                  <div slot="header" class="clearfix">
                    <label style="font-size: 13px">透前情况</label>
                    <el-button
                        type="primary"
                        style="float: right;height: 33px;padding-top: 8px;margin-top: -5px"
                        @click="updateRegisterData"
                        size="small"
                        icon="el-icon-check"
                      >保存</el-button>
                  </div>
                  <el-form  :model="register" ref="RegisterForm"  label-position="left" style='width:90%;margin-left:25px;' size="small">
                    <el-row>
                         <el-col :span="8">
                           <el-form-item label="内瘘:">
                              <el-select multiple v-model="preneilouVal" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                <el-option v-for="(item,index) in neilouSel" :key="index" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                           <el-form-item label="导管:">
                              <el-select multiple v-model="predaoguanVal" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                <el-option v-for="(item,index) in daoguanSel" :key="index" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                         <el-col :span="8">
                           <el-form-item label="身体:" >
                              <el-select multiple v-model="preshentiVal" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                <el-option v-for="(item,index) in shentiSel" :key="index" :value="item.id" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                    </el-row>
                    <el-row>
                         <el-col :span="6">
                            <el-form-item label="治疗日期">
                                 <div v-if="register.Adddatetime">{{register.Adddatetime | formatDate}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="18">
                           <el-form-item label="患者评估">
                              <el-input v-model="register.state"  class="myInput" style="width:78%"></el-input>
                           </el-form-item>
                         </el-col>
                    </el-row>
                    <el-row>
                        <el-col :span="6">
                            <el-form-item label="体温" prop="tiwen">
                                 <div>{{register.tiwen | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                        <el-col :span="6">
                            <el-form-item label="心率" prop="xinlv">
                                   <div>{{register.xinlv | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                        <el-col :span="6">
                            <el-form-item label="呼吸" prop="huxi">
                                    <div>{{register.huxi | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                        <el-col :span="6">
                            <el-form-item label="血压" prop="xueya">
                                    <div>{{register.xueya | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                    </el-row>
                    <el-row>
                         <el-col :span="6">
                           <el-form-item label="干体重" prop="gantizhong">
                              <div>{{yz_touxi.gantizhong | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="透前体重" prop="weight">
                              <div>{{register.weight | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="6">
                           <el-form-item label="体重增加" prop="add_weight">
                              <div>{{register.add_weight | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="治疗方式" prop="txtype">
                              <div>{{yz_touxi.txtype}}</div >
                            </el-form-item>
                         </el-col>
                    </el-row>
                    <el-row>
                         <el-col :span="6">
                           <el-form-item label="治疗时间" prop="period">
                              <div>{{yz_touxi.period}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="血流量" prop="xueliuliang">
                              <div>{{yz_touxi.xueliuliang | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="6">
                           <el-form-item label="透析器" prop="touxidevice">
                              <div>{{yz_touxi.touxidevice}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="透析机" prop="xuetoudevice">
                              <div>{{yz_touxi.xuetoudevice}}</div >
                            </el-form-item>
                         </el-col>
                    </el-row>
                    <el-row>
                         <el-col :span="6">
                           <el-form-item label="钙" prop="ca">
                              <div>{{yz_touxi.ca | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="钠" prop="na">
                              <div>{{yz_touxi.na | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="6">
                           <el-form-item label="hco3" prop="hco3">
                              <div>{{yz_touxi.hco3 | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="血流量" prop="xueliuliang">
                              <div>{{yz_touxi.xueliuliang | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                    </el-row>
                    <el-row>
                         <el-col :span="6">
                           <el-form-item label="肝素/低分子肝素" prop="ca">
                              <div>{{yz_touxi.ca | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="首剂" prop="shouji">
                              <div>{{yz_touxi.shouji | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="6">
                           <el-form-item label="追加" prop="zhuijia">
                              <div>{{yz_touxi.zhuijia | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                         <el-col :span="5">
                           <el-form-item label="总量" prop="total">
                              <div>{{yz_touxi.total | formatStr}}</div >
                            </el-form-item>
                         </el-col>
                    </el-row>
                  </el-form>
              </el-card>
           </div>

             <div v-if="tx_rec.tx_rec">
               <el-card style="width: 90%">
                <div slot="header" class="clearfix">
                    <label style="font-size: 13px">治疗情况</label>
                </div>
                <el-table
                  :data="tx_rec.tx_rec"
                  :header-cell-style="{background:'#F8F8F8'}"
                  v-loading="listLoading"
                  stripe>
                  <el-table-column type="index" label="序号"  width="50">
                  </el-table-column>
                  <el-table-column prop="Adddatetime" label="时间" width="140" :formatter="dateFormat"  align="center">
                  </el-table-column>
                  <el-table-column prop="xueliuliang" label="血流量" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="jingmaiya" label="静脉压" width="100"  align="center">
                  </el-table-column>
                  <el-table-column prop="zhy_speed" label="置换液速度" width="120" align="center">
                  </el-table-column>
                  <el-table-column prop="chaolv_rate" label="超滤率" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="chaolv_volume" label="超滤量" width="100" align="center">
                  </el-table-column>
                  <el-table-column prop="xinlv" label="心率" width="80" align="center">
                  </el-table-column>
                  <el-table-column prop="huxi" label="呼吸" width="80" align="center">
                  </el-table-column>
                  <el-table-column prop="xueya" label="血压" width="80" align="center">
                  </el-table-column>
                </el-table>
               </el-card>
              </div>

             <div style="margin-top:10px">
                <el-card style="width: 90%">
                    <div slot="header" class="clearfix">
                        <label style="font-size: 13px">透后情况</label>
                        <el-button
                          type="primary"
                          style="float: right;height: 33px;padding-top: 8px;margin-top: -5px"
                          @click="updateData"
                          size="small"
                          icon="el-icon-check"
                        >保存</el-button>
                    </div>
                    <el-form  :model="tx_rec" :rules="rules" ref="postForm"  label-position="left" style='margin-left:25px;' size="small">
                      <el-row>
                           <el-col :span="6">
                              <el-form-item label="治疗时间" prop="sj_time">
                                 <div>{{tx_rec.sj_time}}</div >
                              </el-form-item>
                           </el-col>
                           <el-col :span="6">
                             <el-form-item label="超滤总量" prop="sj_chaolv_volume" >
                               <el-input
                                 v-model.number="tx_rec.sj_chaolv_volume"
                                 class="myInput"
                                 style="width:100px;"
                                 auto-complete="off">
                               </el-input>
                             </el-form-item>
                           </el-col>
                          <el-col :span="6">
                              <el-form-item label="透后体重" prop="th_weight" >
                                 <el-input v-model.number="tx_rec.th_weight"  class="myInput" style="width:80px;">
                                 </el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="6">
                              <el-form-item label="体重下降" prop="tz_xiajiang" >
                                   <el-input v-model.number="tx_rec.tz_xiajiang"  class="myInput" style="width:80px;">
                                   </el-input>
                              </el-form-item>
                           </el-col>
                      </el-row>
                      <el-row>
                          <el-col :span="6">
                              <el-form-item label="体温(度)" prop="th_tiwen" >
                                  <el-input v-model.number="tx_rec.th_tiwen"  class="myInput" style="width:80px;">
                                  </el-input>
                              </el-form-item>
                           </el-col>
                          <el-col :span="6">
                              <el-form-item label="心率(次/min)" prop="th_xinlv" >
                                  <el-input v-model.number="tx_rec.th_xinlv"  class="myInput" style="width:80px;">
                                  </el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="12">
                             <el-form-item label="呼吸(次/min):" prop="th_huxi" >
                                <el-input v-model.number="tx_rec.th_huxi"  class="myInput" style="width:300px;">
                                </el-input>
                              </el-form-item>
                           </el-col>
                      </el-row>
                      <el-row>
                           <el-col :span="6">
                             <el-form-item label="透后低血压(mmhg):" prop="th_dixueya" >
                                <el-input v-model.number="tx_rec.th_dixueya"  class="myInput" style="width:50px;">
                                </el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="6">
                             <el-form-item label="透后高血压(mmhg):" prop="th_xueya" >
                                <el-input v-model.number="tx_rec.th_xueya"  class="myInput" style="width:50px;">
                                </el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="12">
                             <el-form-item label="并发症:" >
                                <el-select multiple v-model="bingfazhengVal" clearable style="width: 340px" class="myInput" placeholder="请选择">
                                  <el-option v-for="(item,index) in bingfazhengSel" :key="index" :value="item.id" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                      </el-row>
                      <el-row>
                           <el-col :span="8">
                             <el-form-item label="内瘘:">
                                <el-select multiple v-model="postneilouVal" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                  <el-option v-for="(item,index) in neilouSel" :key="index" :value="item.id" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="导管:">
                                <el-select multiple v-model="postdaoguanVal" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                  <el-option v-for="(item,index) in daoguanSel" :key="index" :value="item.id" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="身体:" >
                                <el-select multiple v-model="postshentiVal" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                  <el-option v-for="(item,index) in shentiSel" :key="index" :value="item.id" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                      </el-row>
                      <el-row>
                           <el-col :span="24">
                             <el-form-item label="透后小结" prop="comment">
                                <el-input type="textarea" v-model="tx_rec.comment"  class="myInput" style="width:50%"></el-input>
                                <!--<el-button style="height: 28px;padding-top: 5px;" @click="updateData">保存</el-button>-->
                                <!--<el-button style="height: 28px;padding-top: 5px" onclick="window.history.go(-1)">返回</el-button>-->
                              </el-form-item>
                           </el-col>
                      </el-row>
                    </el-form>
                </el-card>
             </div>
    </div>
</template>

<script>
import { Tx_records, updatetx_record, neilou, daoguan, shenti, Registers, updatetRegister,
  yz_touxi, bingfazheng } from '@/api/login'
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
  props: ['patientid', 'regid', 'num'],
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
      list: null,
      total: null,
      listLoading: true,

      token: getToken,
      dialogStatus: '',
      yz_touxi: {
        id: undefined,
        yzlinshi: {
          register_id: '',
          Adddatetime: ''
        },
        Nurse: '',
        Nurse2: '',
        adddate: '',
        updatedate: '',
        begindate: '',
        enddate: '',
        gantizhong: '',
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
        shouji: '',
        zhuijia: '',
        total: '',
        state: '',
        doctor_state: ''
      },
      register: {
        id: undefined,
        Adddatetime: '',
        state: '',
        tiwen: '',
        xinlv: '',
        huxi: '',
        xueya: '',
        gantizhong: '',
        weight: '',
        add_weight: '',
        reg_id: '',
        status: 1,
        labid: 1,
        preneilou: [],
        predaoguan: [],
        preshenti: []
      },
      tx_rec: {
        tx_rec: [],
        id: '',
        Adddatetime: '',
        th_weight: '',
        tz_xiajiang: '',
        th_tiwen: '',
        th_xinlv: '',
        th_huxi: '',
        th_xueya: '',
        th_dixueya: '',
        sj_time: '',
        sj_chaolv_volume: '',
        comment: '',
        bfz: [],
        postneilou: [],
        postdaoguan: [],
        postshenti: [],
        action: 1
      },
      params: {
        page: 1,
        kind: 1
      },
      rules: {
        sj_chaolv_volume: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        th_weight: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        tz_xiajiang: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        th_tiwen: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        th_xinlv: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        th_huxi: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        th_dixueya: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        th_xueya: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ]
      },
      bingfazhengVal: [],
      bingfazhengSel: [],
      neilouSel: [],
      daoguanSel: [],
      shentiSel: [],
      preneilouVal: [],
      predaoguanVal: [],
      preshentiVal: [],
      postneilouVal: [],
      postdaoguanVal: [],
      postshentiVal: []
    }
  },
  filters: {
    formatDate(time) {
      const date = new Date(time)
      return formatDate(date, 'yyyy-MM-dd hh:mm')
    },
    formatStr(val) {
      if (val === '' || val === '0' || val === 0) {
        return ''
      } else {
        return val
      }
    }
  },
  methods: {
    getTx_record() {
      Tx_records(this.regid).then(response => {
        this.listLoading = true
        const datalist = response.data.results

        if (datalist.length > 0) {
          this.tx_rec = datalist[0]
          this.bingfazhengVal = []
          for (const i in this.tx_rec.bfz) {
            this.bingfazhengVal.push(this.tx_rec.bfz[i][0])
          }
          this.preneilouVal = []
          for (const i in this.tx_rec.preneilou) {
            this.preneilouVal.push(this.tx_rec.preneilou[i][0])
          }
          this.predaoguanVal = []
          for (const i in this.tx_rec.predaoguan) {
            this.predaoguanVal.push(this.tx_rec.predaoguan[i][0])
          }
          this.preshentiVal = []
          for (const i in this.tx_rec.preshenti) {
            this.preshentiVal.push(this.tx_rec.preshenti[i][0])
          }
          this.postneilouVal = []
          for (const i in this.tx_rec.postneilou) {
            this.postneilouVal.push(this.tx_rec.postneilou[i][0])
          }
          this.postdaoguanVal = []
          for (const i in this.tx_rec.postdaoguan) {
            this.postdaoguanVal.push(this.tx_rec.postdaoguan[i][0])
          }
          this.postshentiVal = []
          for (const i in this.tx_rec.postshenti) {
            this.postshentiVal.push(this.tx_rec.postshenti[i][0])
          }
        }
        this.listLoading = false
        this.dialogStatus = 'create'
      })
      Registers(this.regid).then(response => {
        this.listLoading = true
        this.register = response.data.results[0]
        this.listLoading = false
        this.dialogStatus = 'create'
      })
      yz_touxi(this.regid).then(response => {
        const txparams = response.data.results
        if (txparams.length > 0) {
          this.yz_touxi = txparams[0]
          this.dialogStatus = 'create'
        }
      })
    },
    getBingfazheng() {
      bingfazheng(this.params).then(response => {
        this.bingfazhengSel = response.data.results
      })
    },
    getNeilou() {
      neilou(this.params).then(response => {
        this.neilouSel = response.data.results
      })
    },
    getDaoguan() {
      daoguan(this.params).then(response => {
        this.daoguanSel = response.data.results
      })
    },
    getShenti() {
      shenti(this.params).then(response => {
        this.shentiSel = response.data.results
      })
    },
    resetTx_record() {
      this.tx_rec = {
        tx_rec: null,
        id: '',
        Adddatetime: '',
        th_weight: '',
        tz_xiajiang: '',
        th_tiwen: '',
        th_xinlv: '',
        th_huxi: '',
        th_xueya: '',
        th_dixueya: '',
        sj_time: '',
        sj_chaolv_volume: '',
        comment: '',
        action: 1
      }
    },
    updateData() {
      this.$refs['postForm'].validate((valid) => {
        if (valid) {
          this.register.patient_id = this.patientid
          const tempData = Object.assign({}, this.tx_rec)
          tempData.bfz = this.bingfazhengVal
          tempData.postneilou = this.postneilouVal
          tempData.postdaoguan = this.postdaoguanVal
          tempData.postshenti = this.postshentiVal
          tempData.action = 1
          updatetx_record(tempData).then(() => {
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
    updateRegisterData() {
      this.$refs['RegisterForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.register)
          tempData.status = 1
          tempData.labid = 1
          tempData.preneilou = this.preneilouVal
          tempData.predaoguan = this.predaoguanVal
          tempData.preshenti = this.preshentiVal
          console.log(tempData)
          updatetRegister(tempData).then(() => {
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
    // 时间格式化
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm')
    }
  },
  watch: {
    num: function() {
      this.getNeilou()
      this.getDaoguan()
      this.getShenti()
      this.getBingfazheng()
      this.getTx_record()
    }
  },
  created: function() {
    this.getNeilou()
    this.getDaoguan()
    this.getShenti()
    this.getBingfazheng()
    this.getTx_record()
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
    .block {
        border: 1px solid #ebebeb;
        border-radius: 3px;
        transition: .2s;
    }
</style>
