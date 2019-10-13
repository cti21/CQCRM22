<template>
    <div>
        <div>
           <el-form size="mini" ref="DataForm">
             <el-row>
               <el-col :span="6">
                  <el-form-item label="首次治疗日期">
                    <el-date-picker type="date" v-model="frontpageobj.touxidate"  value-format="yyyy-MM-dd" style="width: 120px;" class="myInput">
                    </el-date-picker>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="医保卡号">
                    <el-input v-model="frontpageobj.yibaoid" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="住院号">
                    <el-input v-model="frontpageobj.inp_no" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="透析号">
                    <el-input v-model="frontpageobj.tx_no" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="12">
                  <el-form-item label="诊断">
                    <el-input v-model="frontpageobj.diagnosis" style="width: 70%;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="12">
                  <el-form-item label="合并症或并发症">
                    <!--<el-input v-model="frontpageobj.yibaoid" style="width: 320px;" class="myInput"></el-input>-->
                    <el-select multiple v-model="bingfazhengVal" clearable style="width: 60%" class="myInput" placeholder="请选择">
                      <el-option v-for="(item,index) in bingfazhengSel" :key="index" :value="item.id" :label="item.name">
                      </el-option>
                    </el-select>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="6">
                  <el-form-item label="姓名">
                    <el-input v-model="frontpageobj.name" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="性别">
                    <el-input v-model="frontpageobj.sex" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="身份证号">
                    <el-input v-model="frontpageobj.idcard" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="邮编">
                    <el-input v-model="frontpageobj.zip" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="12">
                  <el-form-item label="现住址">
                    <el-input v-model="frontpageobj.address" style="width: 70%;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="12">
                  <el-form-item label="户口地址">
                    <el-input v-model="frontpageobj.address" style="width: 70%;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="6">
                  <el-form-item label="电话">
                    <el-input v-model="frontpageobj.phone1" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="手机">
                    <el-input v-model="frontpageobj.phone2" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="教育程度">
                    <el-input v-model="frontpageobj.education" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="6">
                  <el-form-item label="宗教信仰">
                    <el-input v-model="frontpageobj.belief" style="width: 120px;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
             <el-row>
               <el-col :span="12">
                  <el-form-item label="工作单位">
                    <el-input v-model="frontpageobj.company" style="width: 70%;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
               <el-col :span="12">
                  <el-form-item label="传染病">
                    <el-input v-model="chuanranbing" style="width: 70%;" class="myInput"></el-input>
                  </el-form-item>
               </el-col>
             </el-row>
          </el-form>
          <div style="margin-top: 10px">
          <el-table
            :data="frontpageobj.txplan"
            :header-cell-style="{background:'#F8F8F8'}"
            stripe
            v-loading="listLoading">
            <el-table-column type="index" label="序号"  width="80" align="center">
            </el-table-column>
            <el-table-column prop="adddate" label="日期" width="140" align="center">
            </el-table-column>
            <el-table-column prop="gantizhong" label="干体重"  width="100" align="center">
            </el-table-column>
            <el-table-column prop="week" label="每几周" width="100" align="center">
            </el-table-column>
            <el-table-column prop="times" label="次数" width="100" align="center">
            </el-table-column>
            <el-table-column prop="txtype" label="治疗方式" width="120" align="center">
            </el-table-column>
            <el-table-column prop="ca" label="透析液钙浓度" width="140" align="center">
            </el-table-column>
            <el-table-column prop="xueguantonglu" label="血管通路" width="140">
            </el-table-column>
            <el-table-column prop="kangning" label="抗凝剂" width="120" align="center">
            </el-table-column>
          </el-table>
          <div style="margin-top: 20px;" align="center">
            <el-button size="small" type="primary" @click="updateData" icon="el-icon-check">保存</el-button>
          </div>
        </div>

        </div>
    </div>
</template>

<script>
import { front_page, bingfazheng, updatefront_page } from '@/api/login'
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
import ElForm from '../../../node_modules/element-ui/packages/form/src/form'

export default {
  name: 'device_register',
  components: {
    ElForm,
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
      token: getToken,
      listLoading: false,
      dialogStatus: '',
      frontpageobj: {
        id: null,
        touxidate: '',
        diagnosis: '',
        complication: '',
        txplan: [],
        tx_no: '',
        inp_no: '',
        yibaoid: '',
        name: '',
        sex: '',
        yigan: false,
        binggan: false,
        meidu: false,
        aizi: false,
        idcard: '',
        company: '',
        address: '',
        zip: '',
        phone1: '',
        phone2: '',
        education: '',
        belief: '',
        patientid: '',
        bfz: []
      },
      params: {
        page: 1,
        kind: 1
      },
      bingfazhengVal: [],
      bingfazhengSel: []
    }
  },
  methods: {
    getFrontpageList(data) {
      front_page(data).then(response => {
        this.listLoading = true
        this.frontpageobj = response.data.results[0]
        this.bingfazhengVal = []
        for (const i in this.frontpageobj.bfz) {
          this.bingfazhengVal.push(this.frontpageobj.bfz[i][0])
        }
        this.listLoading = false
      })
    },
    getBingfazheng() {
      bingfazheng(this.params).then(response => {
        this.bingfazhengSel = response.data.results
      })
    },
    updateData() {
      this.frontpageobj.patientid = this.patientid
      const tempData = Object.assign({}, this.frontpageobj)
      tempData.bfz = this.bingfazhengVal
      updatefront_page(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '更新成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD')
    }
  },
  computed: {
    chuanranbing: function () {
      let arr = []
      let str = ''
      if (this.frontpageobj){
        if (this.frontpageobj.yigan === true){
          str = '乙肝,'
        }
        if (this.frontpageobj.binggan === true){
          str += '丙肝,'
        }
        if (this.frontpageobj.meidu === true){
          str += '梅毒,'
        }
        if (this.frontpageobj.aizi === true){
          str += '艾滋,'
        }
        arr = str.split(',')
        arr.pop()
        str = arr.join(',')
      }
      return str
    }
  },
  created: function() {
    this.getBingfazheng()
    this.getFrontpageList(this.patientid)
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
