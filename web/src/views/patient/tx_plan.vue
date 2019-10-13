<template>
    <div>
      <div>
             <div>
               <el-card style="width: 90%;padding-left: 50px;">
                  <div slot="header" class="clearfix">
                      <!--<i class="el-icon-tickets"></i>-->
                      <label style="margin-left:5px;margin-right: 50px;font-size: 13px">透析处方</label>
                  </div>
                  <el-table
                    :data="list"
                    v-loading="listLoading"
                    :header-cell-style="{background:'#F8F8F8'}"
                    stripe
                    highlight-current-row
                    @row-click="handle_TX_plan_RowClick">
                    <el-table-column type="index" label="序号"  width="80" align="center">
                    </el-table-column>
                    <el-table-column prop="name" label="透析处方名" width="140" align="center">
                    </el-table-column>
                    <el-table-column prop="txtype" label="透析方式" width="140" align="center">
                    </el-table-column>
                    <el-table-column prop="times" label="次数" width="120" align="center">
                    </el-table-column>
                    <el-table-column prop="week" label="周次" width="120" align="center">
                    </el-table-column>
                    <el-table-column prop="doctorname" label="医生" width="120" align="center">
                    </el-table-column>
                    <el-table-column prop="adddate" label="添加时间" width="100" align="center">
                    </el-table-column>
                    <el-table-column prop="state" v-if="false">
                    </el-table-column>
                  </el-table>
               </el-card>
              </div>

             <div style="margin-top: 10px;" class="block">
               <el-card style="width: 90%;padding-left: 50px;">
                    <div slot="header" class="clearfix">
                        <!--<i class="el-icon-tickets"></i>-->
                        <label style="margin-left:5px;margin-right: 50px;font-size: 13px">处方详情</label>
                    </div>
                    <el-form :model="tx_plan" ref="dataForm" :rules="rules" label-position="left" style='width:90%; margin-left:25px;' size="mini">
                        <el-row type="flex" justify="end">
                           <el-col :span="6">
                              <el-form-item>
                                <span v-if="tx_plan.state===1" style="color: red">已确认</span>
                                <span v-else>未确认</span>
                              </el-form-item>
                           </el-col>
                           <el-col :span="6">
                              <el-form-item label="透析处方名:">
                                <span>{{tx_plan.name}}</span>
                              </el-form-item>
                           </el-col>
                           <el-col :span="6">
                              <el-form-item label="医生:">
                                <span >{{tx_plan.doctorname}}</span>
                              </el-form-item>
                           </el-col>
                           <el-col :span="6">
                              <el-form-item >
                              </el-form-item>
                           </el-col>
                        </el-row>
                        <el-row type="flex" justify="end">
                           <el-col :span="8">
                              <el-form-item label="透析方式" prop="txtype">
                                <el-select v-model="tx_plan.txtype" clearable style="width: 180px" class="myInput" placeholder="请选择">
                                  <el-option label="血液透析" value="血液透析" >
                                  </el-option>
                                  <el-option label="血液灌流" value="血液灌流" >
                                  </el-option>
                                  <el-option label="血液透析滤过" value="血液透析滤过" >
                                  </el-option>
                                  <el-option label="血液滤过" value="血液滤过" >
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="透析时长(h)" prop="period">
                                <el-input v-model="tx_plan.period"  class="myInput" style="width:90px"></el-input>
                              </el-form-item>
                           </el-col>
                          <el-col :span="8">
                              <el-form-item label="血管通路" prop="xueguantonglu">
                                <el-select v-model="tx_plan.xueguantonglu" clearable style="width: 180px" class="myInput">
                                  <el-option v-for="item in xgtlSelect" :key="item.id" :value="item.name" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                         </el-row>
                        <el-row  type="flex">
                          <el-col :span="8">
                            <el-form-item label="通路类型" prop="xueguantype">
                                <el-select v-model="tx_plan.xueguantype" clearable style="width: 180px" class="myInput">
                                  <el-option v-for="item in xgtlTypeSelect" :key="item.id" :value="item.name" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                          </el-col>
                          <el-col :span="8">
                              <el-form-item label="血透器" prop="xuetoudevice">
                                <el-select v-model="tx_plan.xuetoudevice" clearable style="width: 180px" class="myInput">
                                  <el-option v-for="item in xtqSelect" :key="item.id" :value="item.name" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                          <el-col :span="8">
                              <el-form-item label="血滤器" prop="xuelvdevice">
                                <el-select v-model="tx_plan.xuelvdevice" clearable style="width: 200px" class="myInput">
                                  <el-option v-for="item in xlqSelect" :key="item.id" :value="item.name" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                        </el-row>
                        <el-row type="flex">
                          <el-col :span="8">
                              <el-form-item label="灌流器" prop="guanliudevice">
                                <el-select v-model="tx_plan.guanliudevice" clearable style="width: 180px" class="myInput">
                                  <el-option v-for="item in glqSelect" :key="item.id" :value="item.name" :label="item.name">
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                          <el-col :span="8">
                             <el-form-item label="干体重:" prop="gantizhong">
                                <el-input v-model.number="tx_plan.gantizhong"   class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="周频次:" prop="week">
                                <el-input v-model.number="tx_plan.week"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                         </el-row>
                         <el-row type="flex">
                           <el-col :span="8">
                             <el-form-item label="次数:" prop="times" >
                                <el-input v-model.number="tx_plan.times" class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="钙(mmol/l):" prop="ca" >
                                <el-input v-model.number="tx_plan.ca"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="钾(mmol/l):" prop="k" >
                                <el-input v-model.number="tx_plan.k"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                         </el-row>
                         <el-row type="flex">
                           <el-col :span="8">
                             <el-form-item label="钠(mmol/l):" prop="na" >
                                <el-input v-model.number="tx_plan.na"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="碳酸氢根(mmol/l):" prop="hco3" >
                                <el-input v-model.number="tx_plan.hco3"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="透析液流量(ml/mimn):" prop="touxiyeliuliang" >
                                <el-input v-model.number="tx_plan.touxiyeliuliang"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                         </el-row>
                         <el-row type="flex">
                           <el-col :span="8">
                             <el-form-item label="血流量(ml/mimn):" prop="xueliuliang" >
                                <el-input v-model.number="tx_plan.xueliuliang"  class="myInput" style="width:80px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="抗凝剂类型:" prop="kangning">
                                <el-select v-model="tx_plan.kangning" clearable style="width: 200px" class="myInput">
                                  <el-option label="无肝素" value="无肝素" >
                                  </el-option>
                                  <el-option label="肝素" value="肝素" >
                                  </el-option>
                                  <el-option label="小分子肝素" value="小分子肝素" >
                                  </el-option>
                                </el-select>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="首剂(mg):" prop="shouji" >
                                <el-input v-model.number="tx_plan.shouji"  class="myInput" style="width:140px"></el-input>
                              </el-form-item>
                           </el-col>
                         </el-row>
                         <el-row>
                           <el-col :span="8">
                             <el-form-item label="追加(mg/h):" prop="zhuijia" >
                                <el-input v-model.number="tx_plan.zhuijia"  class="myInput" style="width:140px"></el-input>
                              </el-form-item>
                           </el-col>
                           <el-col :span="8">
                             <el-form-item label="总量(mg/h):" prop="total" >
                                <el-input v-model.number="tx_plan.total"  class="myInput" style="width:140px"></el-input>
                              </el-form-item>
                           </el-col>
                         </el-row>
                    </el-form>
               </el-card>
             </div>
      </div>

      <div style="margin-top: 20px">
        <el-card style="width: 90%;padding-left: 50px;">
          <div slot="header" class="clearfix">
            <!--<i class="el-icon-tickets"></i>-->
            <label style="margin-right: 20px;font-size: 13px">透析套餐</label>
            <label style="color: red;font-size: 13px">当前透析方式：  {{tx_plan.txtype}}</label>
          </div>
          <el-table
            :data="tc_list"
            v-loading="tc_listLoading"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            style="width: 90%">
            <el-table-column type="index" label="序号"  width="80"  align="center">
            </el-table-column>
            <el-table-column prop="yztype" label="医嘱类型" width="100" align="center">
            </el-table-column>
            <el-table-column prop="name" label="名称" width="200">
            </el-table-column>
            <el-table-column prop="count" label="单次剂量" width="100" align="center">
            </el-table-column>
            <el-table-column prop="week" label="频次" width="120" align="center">
            </el-table-column>
            <el-table-column prop="path" label="用药路径" width="120" align="center">
            </el-table-column>
            <el-table-column prop="feetype" label="是否自备" width="100" align="center">
            </el-table-column>
          </el-table>
        </el-card>
      </div>

      <div>
          <el-dialog  title="新增医嘱" width="60%" :visible.sync="dialogListVisible">
            <div style="float: left">
              <el-radio-group v-model="hctype" @change="selectChange">
                  <el-radio label="药品">药品</el-radio>
                  <el-radio label="护理">护理</el-radio>
                  <el-radio label="自备药">自备药</el-radio>
              </el-radio-group>
              <el-input
                v-model="hcname"
                style="width: 220px;margin-right: 10px;margin-left: 20px"
                class="myInput" placeholder="请输入名称"
                suffix-icon="el-icon-search"
                @keyup.enter.native="material_handleFilter"
              >
              </el-input>
            </div>
            <div class="pagination-container" style="margin-top: 5px;float: right;margin-right: 20px;">
                <el-pagination background
                     @current-change="material_handleCurrentChange"
                     :current-page="material_listQuery.page"
                     :page-size="material_listQuery.limit"
                     layout="total, prev, pager, next"
                     :total="material_total">
                </el-pagination>
            </div>
            <el-table
              :data="material_list"
              highlight-current-row
              :header-cell-style="{background:'#F8F8F8'}"
              stripe
              @row-dblclick="rowdbclick">
              <el-table-column type="index" label="序号" width="80">
              </el-table-column>
              <el-table-column prop="id" v-if="false">
              </el-table-column>
              <el-table-column prop="name" label="名称" width="200">
              </el-table-column>
              <el-table-column prop="gg" label="规格"  align="center" width="120">
              </el-table-column>
              <el-table-column prop="dw" label="剂量单位"  align="center" width="120">
              </el-table-column>
              <el-table-column prop="pack_gg" label="包装规格" width="120">
              </el-table-column>
              <el-table-column prop="firm" label="厂商" width="200">
              </el-table-column>
            </el-table>
            <div>
               <div style="margin-top: 10px">医嘱列表</div>
               <el-table :data="multipleSelection" stripe>
                  <el-table-column type="index" label="序号"  width="80">
                  </el-table-column>
                  <el-table-column prop="id" v-if="false">
                  </el-table-column>
                  <el-table-column prop="name" label="名称" width="180">
                  </el-table-column>
                  <el-table-column prop="gg" label="规格" width="120">
                  </el-table-column>
                  <el-table-column prop="dw" label="剂量单位" width="100">
                  </el-table-column>
                  <el-table-column prop="week" label="频次" width="120">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.week" clearable style="width: 90px" class="myInput">
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
                  <el-table-column prop="path" label="用药途径" width="120">
                    <template slot-scope="scope">
                        <el-select v-model="scope.row.path" clearable style="width: 110px" class="myInput">
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
                  <el-table-column prop="count" label="单次剂量" width="120">
                    <template slot-scope="scope">
                        <el-input v-model="scope.row.count" type="number" size="small" placeholder="单次剂量">
                        </el-input>
                    </template>
                  </el-table-column>
                </el-table>
            </div>
            <div slot="footer" class="dialog-footer" style="margin-right: 40px">
              <el-button size="mini" type="primary" @click="submitData">提交</el-button>
              <el-button size="mini" @click="dialogListVisible = false">取消</el-button>
            </div>
          </el-dialog>
        </div>

      <div>
        <el-dialog  title="编辑医嘱" width="50%" :visible.sync="tc_dialogVisible">
            <el-form  :model="taocanobj" ref="tc_Form" label-position="left" label-width="70px" style='width:90%; margin-left:50px;'>
               <el-row>
                 <el-col :span="12">
                    <el-form-item label="频次" prop="week">
                        <el-select v-model="taocanobj.week" clearable style="width: 140px" class="myInput">
                          <el-option label="QW" value="QW" >
                          </el-option>
                          <el-option label="QD" value="QD" >
                          </el-option>
                          <el-option label="QH" value="QH" >
                          </el-option>
                          <el-option label="ST" value="ST" >
                          </el-option>
                        </el-select>
                    </el-form-item>
                 </el-col>
                 <el-col :span="12">
                    <el-form-item label="用药路径" prop="path">
                     <el-select v-model="taocanobj.path" clearable style="width: 140px" class="myInput">
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
                    </el-form-item>
                 </el-col>
               </el-row>
               <el-row>
                 <el-col :span="12">
                    <el-form-item label="单次剂量" prop="count">
                     <el-input-number v-model="taocanobj.count"  style="width: 140px" class="myInput" placeholder="单次剂量">
                     </el-input-number>
                    </el-form-item>
                 </el-col>
                 <el-col :span="12">
                    <el-form-item label="是否收费" prop="feetype">
                        <el-select v-model="taocanobj.feetype" clearable style="width: 140px" class="myInput">
                          <el-option label="收费" value="收费" >
                          </el-option>
                          <el-option label="自备" value="自备" >
                          </el-option>
                        </el-select>
                    </el-form-item>
                 </el-col>
               </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
                <el-button size="mini" @click="tc_dialogVisible = false">取消</el-button>
                <el-button size="mini" type="primary" @click="tcUpdateData">修改</el-button>
            </div>
        </el-dialog>
    </div>

    <div>
      <el-dialog  title="添加医嘱套餐" width="40%" :visible.sync="dialogFormVisible">
            <el-form ref="taocanForm"  label-position="left" label-width="120px" style='width:90%; margin-left:70px;'>
                 <el-row>
                   <el-col>
                      <el-form-item label="医嘱套餐选择">
                        <el-select v-model="taocanid" clearable style="width: 200px" class="myInput">
                            <el-option v-for="item in taocanList" :label="item.name" :key="item.id" :value="item.id" >{{item.name}}
                            </el-option>
                        </el-select>
                      </el-form-item>
                   </el-col>
                 </el-row>
            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button size="mini" @click="dialogFormVisible = false">取消</el-button>
              <el-button size="mini" type="primary"  @click="taocanCreateData">保存</el-button>
            </div>
      </el-dialog>
    </div>

    </div>
</template>

<script>
import { Tx_plans, createtx_plan, updatetx_plan, deletetx_plan, xyjh_pat,
  createtc, updatetc, deletetc, getXgtonglu, getXgtongluType, getMaterialType } from '@/api/tx_plan'
import { xyjhdict } from '@/api/system'
import { chuzhiDict, huliDict, mydrugDict, mymaterialDict, txtypedict, copyTotouxi_drug, patientfee } from '@/api/login'
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
import ElInputNumber from '../../../node_modules/element-ui/packages/input-number/src/input-number'
import ElCard from '../../../node_modules/element-ui/packages/card/src/main'

export default {
  components: {
    ElCard,
    ElInputNumber,
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
  props: ['regid', 'patientid'],
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
      // 透析处方
      list: null,
      total: null,
      listLoading: true,
      dialogFormVisible: false,
      dialogListVisible: false,

      // 套餐字典
      checked: false,
      taocanList: null,

      // 个人套餐
      tc_list: null,
      tc_total: null,
      tc_listLoading: false,
      tc_dialogVisible: false,

      material_list: null,
      material_total: null,
      material_listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        name: undefined,
        sort: '+id'
      },
      tcAdd_list: null,
      tcAdd_total: null,
      tcAdd_listLoading: false,
      tcAdd_dialogVisible: false,
      multipleSelection: [],
      hctype: '',
      hcname: '',
      feetype: '收费',
      taocanname: '',
      ordertype: '',
      token: getToken,
      dialogStatus: '',
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
      taocanid: '',
      taocanobj: {
        id: null,
        patientid: '',
        txtype: '',
        yztype: '',
        week: '',
        path: '',
        count: 0,
        feetype: '',
        taocanid: null,
        orderid: null,
        leixing: '',
        entrance: 1,
        kind: ''
      },
      tx_plan: {
        id: '',
        patient: {
          id: '',
          patientid: ''
        },
        doctor: '',
        doctorname: '',
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
        shouji: 0,
        zhuijia: 0,
        total: 0,
        state: 0
      },
      multipleList: [],
      xgtlSelect: [],
      xgtlTypeSelect: [],
      xtqSelect: [],
      xlqSelect: [],
      glqSelect: [],
      rules: {
        txtype: [{ required: true, message: '请输入透析方式', trigger: 'blur' }],
        period: [{ required: true, message: '请输入时长', trigger: 'blur' }],
        xueguantonglu: [{ required: true, message: '请输入血管通路', trigger: 'blur' }],
        xueguantype: [{ required: true, message: '请输入血管通路类型', trigger: 'blur' }],
        // xuetoudevice: [{ required: true, message: '请输入血透器', trigger: 'blur' }],
        // xuelvdevice: [{ required: true, message: '请输入血滤器', trigger: 'blur' }],
        // guanliudevice: [{ required: true, message: '请输入灌流器', trigger: 'blur' }],
        gantizhong: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        week: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
          { validator: checknum, trigger: 'blur' }
        ],
        times: [
          { required: true, message: '该项不能为空', trigger: 'blur' },
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
      },
      queryparams: {
        page: 1,
        name: ''
      },
      params: {
        page: 1,
        name: '',
        type: 0,
        patientid: ''
      }
    }
  },
  methods: {
    getTx_planList() {
      Tx_plans(this.patientid).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getPatient(data) {
      patientfee(data).then(response => {
        this.patient = response.data.results[0]
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
    getxyjhDict(data) {
      xyjhdict(data).then(response => {
        this.taocanList = response.data.results
      })
    },
    getHuliList(data) {
      huliDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
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
      mymaterialDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getDrugList(data) {
      mydrugDict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getTxtypeList(data) {
      txtypedict(data).then(response => {
        this.listLoading = true
        this.material_list = response.data.results
        this.material_total = response.data.count
        this.listLoading = false
      })
    },
    getXyjh_pat(txtype) {
      const params = {
        patient_id: this.patientid,
        txtype: txtype
      }
      xyjh_pat(params).then(response => {
        this.tc_listLoading = true
        this.tc_list = response.data.results
        this.tc_total = response.data.count
        this.tc_listLoading = false
      })
    },
    handleApply(row) {
      const para = {
        txtype: row.txtype,
        registerid: this.regid
      }
      copyTotouxi_drug(para).then(() => {
        this.$notify({
          title: '提示',
          message: '导入成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    resetTx_plan() {
      this.tx_plan = {
        id: '',
        patient: {
          id: '',
          patientid: ''
        },
        doctorname: '',
        doctor: '',
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
        state: 0
      }
    },
    handleCreate() {
      this.resetTx_plan()
      this.tc_list = []
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.tx_plan.id = parseInt(Math.random() * 100) + 1024 // mock a id
          this.tx_plan.patient.patientid = this.patientid
          const txlx = this.tx_plan.txtype
          const havenum = this.list.some(function(v) {
            return v.txtype === txlx
          })
          if (havenum) {
            this.$notify({
              title: '提示',
              message: '已有该透析方式的处方',
              type: 'success',
              duration: 2000
            })
            return
          }
          createtx_plan(this.tx_plan).then(response => {
            this.tx_plan = response.data
            this.currTxtype = this.tx_plan.txtype
            this.tcAdd_dialogVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.getTx_planList()
          })
        }
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.tx_plan.patient.patientid = this.patientid
          const txlx = this.tx_plan.txtype
          const txid = this.tx_plan.id
          console.log('update=' + this.dialogStatus)
          let haveplan = []
          haveplan = this.list.filter(v => v.txtype === txlx)
          if (haveplan.length > 0) {
            if (haveplan[0].id !== txid) {
              this.$notify({
                title: '提示',
                message: '已有该透析方式的处方',
                type: 'success',
                duration: 2000
              })
              return
            }
          }
          const tempData = Object.assign({}, this.tx_plan)
          tempData.state = 0
          updatetx_plan(tempData).then(response => {
            // this.tx_plan = response.data
            this.tx_plan.state = 0
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getTx_planList()
          })
        }
      })
    },
    confirm_txplan() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          this.tx_plan.patient.patientid = this.patientid
          const tempData = Object.assign({}, this.tx_plan)
          tempData.state = 1
          updatetx_plan(tempData).then(response => {
            // this.tx_plan = response.data
            this.tx_plan.state = 1
            this.$notify({
              title: '成功',
              message: '确认成功',
              type: 'success',
              duration: 2000
            })
            this.getTx_planList()
          })
        }
      })
    },
    handleDelete(row) {
      this.tx_plan = Object.assign({}, row) // copy obj
      const tempData = Object.assign({}, this.tx_plan)
      deletetx_plan(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
        this.getTx_planList()
      })
    },
    handle_TX_plan_RowClick(row, event, column) {
      this.getXyjh_pat(row.txtype)
      this.tx_plan = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    rowdbclick(row,event) {
      this.multipleSelection = []
      this.multipleSelection.push(row)
    },
    selectChange: function(val) {
      this.material_list = null
      this.params.page = 1
      this.params.name = ''
      this.hcname = ''
      this.ordertype = val
      switch (val) {
        case '耗材':
          this.getMaterialList(this.params)
          break
        case '药品':
          this.feetype = '收费'
          this.params.type = 0
          this.params.patientid = ''
          this.getDrugList(this.params)
          break
        case '处置':
          this.getChuzhiList(this.params)
          break
        case '护理':
          this.getHuliList(this.params)
          break
        case '自备药':
          this.feetype = '自备'
          this.params.type = 1
          this.params.patientid = this.patientid
          this.getDrugList(this.params)
      }
    },
    taocanCreateData() {
      if (this.taocanid === '') {
        this.$notify({
          title: '提示',
          message: '请选择套餐',
          type: 'success',
          duration: 2000
        })
      } else {
        const tempData = Object.assign({}, this.taocanobj)
        tempData.id = parseInt(Math.random() * 100) + 1024
        tempData.txtype = this.tx_plan.txtype
        tempData.yztype = 'a'
        tempData.week = 'a'
        tempData.path = 'a'
        tempData.count = 1
        tempData.feetype = 'a'
        tempData.taocanid = this.taocanid
        tempData.patientid = this.patientid
        tempData.orderid = 1
        tempData.leixing = 1
        tempData.entrance = 1 // 通过套餐增加
        createtc(tempData).then(() => {
          this.dialogFormVisible = false
          this.$notify({
            title: '成功',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.getXyjh_pat(this.tx_plan.txtype)
        })
      }
    },
    tcCreate() {
      if (this.tx_plan.txtype === '') {
        this.$notify({
          title: '提示',
          message: '请选择透析处方',
          type: 'success',
          duration: 2000
        })
        return
      }
      if (this.checked) {
        this.dialogFormVisible = true
        this.taocanid = ''
        this.$nextTick(() => {
          // this.$refs['taocanForm'].clearValidate()
        })
      } else {
        this.multipleSelection = []
        this.dialogListVisible = true
      }
    },
    submitData() {
      if (this.multipleSelection.length > 0) {
        const obj = this.multipleSelection[0]
        if (!obj.count) {
          this.$notify({
            title: '成功',
            message: '单次剂量不能为空',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (!Number.isInteger(Number(obj.count))) {
          this.$notify({
            title: '成功',
            message: '单次剂量必须为数值',
            type: 'success',
            duration: 2000
          })
          return
        }
        if (this.ordertype === '药品' || this.ordertype === '自备药') {
          if (!obj.week) {
            this.$notify({
              title: '成功',
              message: '频次不能为空',
              type: 'success',
              duration: 2000
            })
            return
          }
          if (!obj.path) {
            this.$notify({
              title: '成功',
              message: '用药路径不能为空',
              type: 'success',
              duration: 2000
            })
            return
          }
        }
        this.multipleList = []
        this.multipleSelection.forEach((item) => {
          this.taocanobj = Object.assign({}, item)
          this.taocanobj.txtype = this.tx_plan.txtype
          this.taocanobj.yztype = 'a'
          if (this.taocanobj.kind !== 3) {
            this.taocanobj.week = 'a'
            this.taocanobj.path = 'a'
            this.taocanobj.feetype = 'a'
            if (this.taocanobj.kind === 5) {
              this.taocanobj.count = 1
            }
          } else {
            this.taocanobj.feetype = this.feetype
          }
          this.taocanobj.patientid = this.patientid
          this.taocanobj.taocanid = 1
          this.taocanobj.orderid = item.id
          this.taocanobj.leixing = item.kind
          this.taocanobj.entrance = 2
          this.multipleList.push(this.taocanobj)
        })
        createtc(this.multipleList).then(() => {
          this.$notify({
            title: '成功',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogListVisible = false
          this.getXyjh_pat(this.tx_plan.txtype)
        })
      }
    },
    tcUpdate(row) {
      this.taocanobj = Object.assign({}, row) // copy obj
      this.tc_dialogVisible = true
      this.$nextTick(() => {
        this.$refs['tc_Form'].clearValidate()
      })
    },
    tcUpdateData() {
      this.$refs['tc_Form'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.taocanobj)
          tempData.patientid = 'A0001'
          tempData.taocanid = 1
          tempData.txtype = 'a'
          tempData.orderid = 1
          tempData.leixing = 1
          tempData.entrance = 3
          updatetc(tempData).then(() => {
            this.tc_dialogVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.getXyjh_pat(this.tx_plan.txtype)
          })
        }
      })
    },
    tcDelete(row) {
      this.taocanobj = Object.assign({}, row) // copy obj
      const tempData = Object.assign({}, this.taocanobj)
      deletetc(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
        this.getXyjh_pat(this.tx_plan.txtype)
      })
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
        case '药品':
          this.getDrugList(this.params)
          break
        case '处置':
          this.getChuzhiList(this.params)
          break
        case '护理':
          this.getHuliList(this.params)
          break
      }
    },
    material_handleCurrentChange(val) {
      this.material_listQuery.page = val
      this.material_listQuery.offset = (val - 1) * this.material_listQuery.limit
      this.params.page = val
      this.getMaterialList(this.params)
    },
    dateFormat: function(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  computed: {
    status: function() {
      if (this.tx_plan.state === 1){
        return '已确定'
      }
      else {
        return '未确定'
      }
    }
  },
  created: function() {
    const para = {
      page: 1,
      patientid: this.patientid
    }
    this.getPatient(para)
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
    this.getxyjhDict(this.queryparams)
    this.getTx_planList()
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
    .block {
        border: 1px solid #ebebeb;
        border-left: none;
        border-right: none;
        border-radius: 3px;
        transition: .2s;
    }
    .el-card__header {
        padding: 10px 20px;
        border-bottom: 1px solid #ebeef5;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
    }
</style>
