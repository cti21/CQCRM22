<template>
    <div>
        <div>
            <el-form :model="fdd_obj" ref="dataForm" label-position="left" size="mini"  style='width:90%; margin-left:10px;'>
                 <el-row>
                   <el-col>
                      <el-form-item label="主诉">
                        <el-input v-model="fdd_obj.zhusu" style="width: 840px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                <el-row>
                   <el-col>
                      <el-form-item label="现病史" >
                        <el-input v-model="fdd_obj.xianbingshi" style="width: 840px"  class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                <el-row>
                   <el-col :span="8">
                      <el-form-item label="原发疾病">
                        <el-input v-model="fdd_obj.yfjibing"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="病理" >
                        <el-input v-model="fdd_obj.bingli"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="首发症状" >
                        <el-input v-model="fdd_obj.zhengzhuang"  style="width: 220px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                <el-row>
                   <el-col :span="8">
                      <el-form-item label="首发时间">
                        <el-date-picker type="date" v-model="fdd_obj.fabingdate"  value-format="yyyy-MM-dd" style="width: 120px;" class="myInput">
                        </el-date-picker>
                      </el-form-item>
                    </el-col>
                    <el-col :span="8">
                      <el-form-item label="发现肾功能不全时间" >
                        <el-date-picker type="date" v-model="fdd_obj.buquandate"  value-format="yyyy-MM-dd" style="width: 120px;" class="myInput">
                        </el-date-picker>
                      </el-form-item>
                   </el-col>
                    <el-col :span="8">
                      <el-form-item label="首次透析日期" >
                        <el-date-picker type="date" v-model="fdd_obj.touxidate"  value-format="yyyy-MM-dd" style="width: 120px;" class="myInput">
                        </el-date-picker>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="食欲">
                        <el-input v-model="fdd_obj.shiyu"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="睡眠" >
                        <el-input v-model="fdd_obj.shuimian"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="尿量ml/d" >
                        <el-input v-model="fdd_obj.niaoliang"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="6">
                      <el-form-item label="夜尿" >
                        <el-input v-model="fdd_obj.yeniao"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="大便">
                        <el-input v-model="fdd_obj.dabian"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="出血倾向" >
                        <el-input v-model="fdd_obj.chuxueflag"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="出血部位" >
                        <el-input v-model="fdd_obj.chuxue"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="有无心血管病史">
                        <el-input v-model="fdd_obj.xinxueguanflag"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="18">
                      <el-form-item label="心血管疾病" >
                        <el-input v-model="fdd_obj.xinxueguan"  style="width: 420px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="有无脑血栓">
                        <el-input v-model="fdd_obj.naoxueshuanflag"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="18">
                      <el-form-item label="脑血栓" >
                        <el-input v-model="fdd_obj.naoxueshuan"  style="width: 420px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="有无糖尿病">
                        <el-input v-model="fdd_obj.tangniaobingflag"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="18">
                      <el-form-item label="糖尿病" >
                        <el-input v-model="fdd_obj.tangniaobing"  style="width: 420px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="有无其他疾病">
                        <el-input v-model="fdd_obj.otherflag"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="18">
                      <el-form-item label="其他疾病" >
                        <el-input v-model="fdd_obj.other"  style="width: 420px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="有无过敏">
                        <el-input v-model="fdd_obj.guominflag"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="9">
                      <el-form-item label="过敏药物" >
                        <el-input v-model="fdd_obj.guominyao"  style="width: 220px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="9">
                      <el-form-item label="过敏食物" >
                        <el-input v-model="fdd_obj.guominshi"  style="width: 220px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="家族史">
                        <el-input v-model="fdd_obj.jiazuflag"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="18">
                      <el-form-item label="家族史疾病" >
                        <el-input v-model="fdd_obj.jiazu"  style="width: 420px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="5">
                      <el-form-item label="bp(mmHg)">
                        <el-input v-model="fdd_obj.bp"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="5">
                      <el-form-item label="呼吸(次/分)" >
                        <el-input v-model="fdd_obj.r"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="5">
                      <el-form-item label="脉搏(次/分)" >
                        <el-input v-model="fdd_obj.t"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="5">
                      <el-form-item label="T(度)" >
                        <el-input v-model="fdd_obj.h"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="4">
                      <el-form-item label="体重(kg)" >
                        <el-input v-model="fdd_obj.w"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                    <el-col :span="6">
                      <el-form-item label="一般状况" >
                        <el-input v-model="fdd_obj.yiban"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="营养状态" >
                        <el-input v-model="fdd_obj.yingyang"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="6">
                      <el-form-item label="贫血" >
                        <el-input v-model="fdd_obj.pinxue"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="6">
                      <el-form-item label="体位" >
                        <el-input v-model="fdd_obj.tiwei1"  style="width: 50px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.tiwei2"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                    <el-col :span="5">
                      <el-form-item label="浮肿标志" >
                        <el-input v-model="fdd_obj.fuzhongflag"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="5">
                      <el-form-item label="浮肿部位" >
                        <el-input v-model="fdd_obj.fuzhong"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="5">
                      <el-form-item label="浮肿程度" >
                        <el-input v-model="fdd_obj.fuzhongchengdu"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="5">
                      <el-form-item label="出血标志" >
                        <el-input v-model="fdd_obj.chuxueflag"  style="width: 80px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="4">
                      <el-form-item label="出血部位" >
                        <el-input v-model="fdd_obj.chuxue"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="呼吸音">
                        <el-input v-model="fdd_obj.huxiyin"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="胸膜摩擦音" >
                        <el-input v-model="fdd_obj.mocayinflag"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="摩擦音位置" >
                        <el-input v-model="fdd_obj.mocayin"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="6">
                      <el-form-item label="罗音" >
                        <el-input v-model="fdd_obj.luoyinflag"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                    <el-col :span="5">
                      <el-form-item label="心脏大小" >
                        <el-input v-model="fdd_obj.heartsize"  style="width: 60px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="5">
                      <el-form-item label="心包摩擦音" >
                        <el-input v-model="fdd_obj.xinbaomocayin"  style="width: 60px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="5">
                      <el-form-item label="心包积液" >
                        <el-input v-model="fdd_obj.xinbaojiye"  style="width: 60px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="4">
                      <el-form-item label="杂音" >
                        <el-input v-model="fdd_obj.zayin"  style="width: 60px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="5">
                      <el-form-item label="附加音" >
                        <el-input v-model="fdd_obj.fujiayin"  style="width: 60px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>

                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="肝颈静脉回流征">
                        <el-input v-model="fdd_obj.ganjing"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="腹水征" >
                        <el-input v-model="fdd_obj.fushui"  style="width: 50px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="12">
                      <el-form-item label="肝脏">
                        <el-input v-model="fdd_obj.gzcj"  style="width: 100px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.gzyt"  style="width: 100px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.gzkt"  style="width: 100px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                    <el-col :span="12">
                      <el-form-item label="脾脏">
                        <el-input v-model="fdd_obj.pzcj"  style="width: 100px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.pzyt"  style="width: 100px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.pzkt"  style="width: 100px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="12">
                      <el-form-item label="肾脏">
                        <el-input v-model="fdd_obj.szcj"  style="width: 100px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.szyt"  style="width: 100px" class="myInput"></el-input>
                        <el-input v-model="fdd_obj.szkt"  style="width: 100px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                   <el-col :span="6">
                      <el-form-item label="乙肝">
                        <el-input v-model="fdd_obj.yigan"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="丙肝" >
                        <el-input v-model="fdd_obj.binggan"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                    <el-col :span="6">
                      <el-form-item label="梅毒" >
                        <el-input v-model="fdd_obj.meidu"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                   <el-col :span="6">
                      <el-form-item label="艾滋" >
                        <el-input v-model="fdd_obj.aizi"  style="width: 120px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
                 <el-row>
                    <el-col :span="24">
                      <el-form-item label="其他">
                        <el-input v-model="fdd_obj.qita"  style="width: 420px" class="myInput"></el-input>
                      </el-form-item>
                    </el-col>
                 </el-row>
            </el-form>
        </div>
    </div>
</template>

<script>
import { firstDiseaseDurations } from '@/api/login'
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
  props: ['patientid'],
  data: function() {
    return {
      list: null,
      listLoading: false,
      fdd_obj: {
        id: null,
        zhusu: '',
        xianbingshi: '',
        yfjibing: '',
        zhengzhuang: '',
        fabingdate: '',
        buquandate: '',
        touxidate: '',
        niaoliang: '',
        yeniao: '',
        dabian: '',
        shiyu: '',
        shuimian: '',
        yiban: '',
        yingyang: '',
        pinxue: '',
        tiwei1: '',
        tiwei2: '',
        chuxueflag: '',
        chuxue: '',
        fuzhongflag: '',
        fuzhong: '',
        fuzhongchengdu: '',
        xinxueguanflag: '',
        xinxueguan: '',
        naoxueshuanflag: '',
        naoxueshuan: '',
        gaoxueyaflag: '',
        gaoxueya: '',
        tangniaobingflag: '',
        tangniaobing: '',
        otherflag: '',
        other: '',
        guominflag: '',
        guominyao: '',
        guominshi: '',
        jiazuflag: '',
        jiazu: '',
        bp: '',
        h: '',
        r: '',
        t: '',
        w: '',
        huxiyin: '',
        mocayinflag: '',
        mocayin: '',
        luoyinflag: '',
        heartsize: '',
        xinbaomocayin: '',
        xinbaojiye: '',
        zayin: '',
        fujiayin: '',
        ganjing: '',
        fushui: '',
        gzcj: '',
        gzyt: '',
        gzkt: '',
        pzcj: '',
        pzyt: '',
        pzkt: '',
        szcj: '',
        szyt: '',
        szkt: '',
        qita: '',
        yigan: '',
        binggan: '',
        meidu: '',
        aizi: '',
        diagnosis: '',
        complication: '',
        patient: ''
      }
    }
  },
  methods: {
    getFirstDiseaseDuration(data) {
      firstDiseaseDurations(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        if (this.list.length > 0) {
          this.fdd_obj = this.list[0]
        }
        this.listLoading = false
      })
    }
  },
  created: function() {
    this.getFirstDiseaseDuration(this.patientid)
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
    }
    .el-table td, .el-table th{
      padding:6px 0;
    }
</style>
