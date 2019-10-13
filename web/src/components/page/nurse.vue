<template>
    <div>
        <el-row>
            <el-select v-model="banci" clearable style="width: 120px" class="myInput" placeholder="班次">
              <el-option v-for="item in banciSelect" :key="item.id" :value="item.id" :label="item.name">
              </el-option>
            </el-select>
            <el-select v-model="diseaseArea" clearable style="width: 120px" class="myInput" placeholder="病区">
              <el-option v-for="item in diseaseAreaSelect" :key="item.id" :value="item.id" :label="item.name">
              </el-option>
            </el-select>
            <el-input
              v-model="name"
              @keyup.enter.native="handleFilter"
              style="width: 140px;margin-right: 10px;"
              class="myInput"
              placeholder="患者姓名/编号">
            </el-input>
            <el-checkbox style="margin-left: 5px;margin-right: 5px;" v-model="checked">我的床位</el-checkbox>
            <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
            <el-button size="small" style="margin-left: 10px;" type="primary" @click="apply_Drug" icon="iconfont iconyaopin">药品申请</el-button>
            <el-button size="small" type="primary"  @click="apply_Material" icon="iconfont iconsyringe">耗材申请</el-button>
            <el-button size="small" type="primary"  @click="handleAlert" icon="iconfont iconwarn">自备药预警</el-button>
            <el-button size="small" type="primary"  @click="handleBed" icon="el-icon-setting">床位设置</el-button>
        </el-row>
        <el-row style="margin-top: 20px">
          <el-table
            :data="list"
            v-loading="listLoading"
            :header-cell-style="{background:'#F8F8F8'}"
            :row-class-name="tableRowClass"
            :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
            stripe
            @row-click="rowClick">
            <el-table-column type="index" label="序号"  width="50" align="center">
            </el-table-column>
            <el-table-column prop="isContagion" v-if="false" width="80">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="90" align="left">
              <template slot-scope="scope">
                  <span v-if="scope.row.isContagion===0">{{scope.row.name}}</span>
                  <span v-else style="color: red">{{'* '+ scope.row.name}}</span>
              </template>
            </el-table-column>
            <el-table-column prop="num" v-if="false">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="patient" label="编号" v-if="false">
            </el-table-column>
            <el-table-column prop="bedno" label="床位" width="60" align="center">
            </el-table-column>
            <el-table-column prop="flag" label="状态" width="80" align="center" :formatter="formatFlag">
            </el-table-column>
            <el-table-column prop="reg_id" label="注册号" v-if="false">
            </el-table-column>
            <el-table-column prop="txtype" label="治疗项目" width="80" align="center">
            </el-table-column>
            <el-table-column prop="xuetoudevice" label="净化器" width="120" align="center">
            </el-table-column>
            <el-table-column label="操作" width="70" align="center">
              <template slot-scope="scope">
                <svg-icon class="status-handler" iconClass="qidong" v-if="scope.row.status=='未开始'" @click="startoverTouxi(scope.row,2)"></svg-icon>
                <svg-icon class="status-handler" iconClass="stop" v-if="scope.row.status=='治疗中'" @click="startoverTouxi(scope.row,3)"></svg-icon>
              </template>
            </el-table-column>
            <el-table-column prop="status" label="上机状态" width="80" align="center">
            </el-table-column>
            <el-table-column prop="startdate" label="开始" width="90" :formatter="datetimeFormat" align="center">
            </el-table-column>
            <el-table-column prop="enddate" label="结束"  width="90" :formatter="datetimeFormat" align="center">
            </el-table-column>
            <el-table-column prop="txrecordid" label="id" v-if="false">
            </el-table-column>
            <el-table-column prop="recnum" label="记录次数" width="80" align="center">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" v-if="scope.row.flag === false" @click="handleSign(scope.row)">签到</el-button>
                  <el-button type="text" size="small" v-if="scope.row.flag === true" @click="handleCancelSign(scope.row)">取消签到</el-button>
                  <el-button type="text" size="small" @click="handleDetail(scope.row)">详情</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 10px;float:right;margin-right: 40px">
                <el-pagination
                   background
                   @current-change="handleCurrentChange"
                   :current-page="listQuery.page"
                   :page-size="listQuery.limit"
                   layout="total, prev, pager, next"
                   :total="total">
                </el-pagination>
          </div>
        </el-row>

        <div>
          <el-dialog  title="药品申请" width="60%" :visible.sync="applydrug_dialogFormVisible">
              <ApplyDrug :regid="register_id" v-on:showDlg="showApplyDrug" :clickcount="applydrug_btncount" ></ApplyDrug>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="耗材申请" width="60%" :visible.sync="applymaterial_dialogFormVisible">
              <ApplyMaterial :regid="register_id" @showMatDlg="showApplymaterial" :clickcount="applymaterial_btncount" ></ApplyMaterial>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="自备药预警" width="60%" :visible.sync="dialogListVisible">
            <div style="margin-bottom: 30px">
              <el-table :data="alert_list" highlight-current-row stripe :span-method="cellMerge">
                <el-table-column prop="patientname" label="姓名" width="120">
                </el-table-column>
                <el-table-column prop="name" label="药品名称" align="center" width="160">
                </el-table-column>
                <el-table-column prop="dw" label="单位" align="center" width="120">
                </el-table-column>
                <el-table-column prop="amount" label="当前库存" width="120">
                </el-table-column>
                <el-table-column prop="alert_amount" label="预警数量" width="120">
                </el-table-column>
                <el-table-column prop="firm" label="厂商" width="220">
                </el-table-column>
              </el-table>
            </div>
          </el-dialog>
        </div>

        <!--护士负责床位-->
        <div>
          <el-dialog  title="病床设置" width="55%" :visible.sync="dialogVisible">
            <el-card>
              <div slot="header" class="clearfix">
                  <span>病床信息</span>
                  <el-button
                    size="small"
                    type="primary"
                    style="float:right"
                    icon="iconfont iconbaocun"
                    @click="updateData">保存
                  </el-button>
              </div>
              <el-row>
                <el-radio-group v-model="currDiseaseArea" @change="handleChange">
                    <!--<el-radio-button small v-for="item in diseaseAreaSelect" :key="item.id" :label="item.id">{{item.name}}</el-radio-button>-->
                    <el-radio v-for="item in diseaseAreaSelect" :key="item.id" :label="item.id">{{item.name}}</el-radio>
                </el-radio-group>
              </el-row>
              <el-row type="flex" style="margin-top: 40px;">
                 <el-checkbox-group v-model="checkedArr" >
                    <el-checkbox v-for="item in areaArr" :key="item.id" :label="item.id">{{item.name}}
                    </el-checkbox>
                 </el-checkbox-group>
              </el-row>
           </el-card>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { Register_Nur, getDrugAlert, Tx_records, updatetx_record, updatetRegister,
  createApply_drug, createApply_material, bedNurses, createBedNurse } from '@/api/login'
import { banci, diseaseArea } from '@/api/system'
import { getToken } from '@/utils/auth'
import ApplyDrug from '@/views/nurse/ApplyDrug.vue'
import ApplyMaterial from '@/views/nurse/ApplyMaterial.vue'
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
import SvgIcon from '../SvgIcon/index'
import ElIcon from '../../../node_modules/element-ui/packages/icon/src/icon'

export default {
  components: {
    ElIcon,
    SvgIcon,
    ElButton,
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    ApplyDrug,
    ApplyMaterial
  },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10,
        offset: 0,
        name: undefined,
        diseaseArea: '',
        banci: '',
        checked: false,
        sort: '+id'
      },
      alert_list: [],
      alert_total: null,
      register_id: '',
      dialogListVisible: false,
      dialogVisible: false,
      // 药品申请
      applydrug_list: null,
      applydrug_listLoading: false,
      applydrug_btncount: 0,
      applydrug_dialogFormVisible: false,

      // 耗材申请
      applymaterial_list: null,
      applymaterial_listLoading: false,
      applymaterial_btncount: 0,
      applymaterial_dialogFormVisible: false,

      banciSelect: [],
      banci: '',
      diseaseAreaSelect: [],
      diseaseArea: '',
      bedSelect: [],
      areaArr: [],
      checkedArr: [],
      checked: false,
      currDiseaseArea: 1,
      spanArr: [],
      timer: null,
      pos: 0,
      colCount: 0,
      name: '',
      token: getToken,
      dialogStatus: '',
      multipleSelection: [],
      register: {},
      tx_record: {
        id: '',
        th_weight: 0,
        tz_xiajiang: 0,
        th_tiwen: 0,
        th_xinlv: 0,
        th_huxi: 0,
        th_xueya: 0,
        th_dixueya: 0,
        sj_chaolv_volume: 0,
        comment: '',
        action: 0
      },
      multipleList: []
    }
  },
  methods: {
    getRegisterList(data) {
      Register_Nur(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    ConnectServer() {
      const ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/')
      if ('WebSocket' in window) {
        ws.onopen = function() {
          console.log('连接成功')
        }
        ws.onmessage = (evt) => {
          const received_msg = evt.data
          console.log('received_msg', received_msg)
          this.getRegisterList(this.listQuery)
        }
        ws.onclose = function() {
          console.log('连接已关闭...')
        }
      } else {
        console.log('您的浏览器不支持 WebSocket!')
      }
    },
    getTreatrecordlist(registerid) {
      Tx_records(registerid).then(response => {
        this.listLoading = true
        this.record = response.data.results[0]
        this.listLoading = false
      })
    },
    getDrugAlertList(data) {
      getDrugAlert(data).then(response => {
        this.alert_list = response.data
        this.alert_total = response.data.count
        if (this.alert_list.length > 0) {
          this.colCount = this.alert_list[0].length
          this.getSpanArr(this.alert_list)
        }
      })
    },
    getBanciList(data) {
      banci(data).then(response => {
        this.banciSelect = response.data.results
      })
    },
    getDiseaseAreaList(data) {
      diseaseArea(data).then(response => {
        this.diseaseAreaSelect = response.data.results
      })
    },
    getBedList() {
      bedNurses('').then(response => {
        this.bedSelect = response.data.results
        this.makeInitialData()
      })
    },
    showApplyDrug() {
      this.applydrug_dialogFormVisible = false
    },
    showApplymaterial() {
      this.applymaterial_dialogFormVisible = false
    },
    handleChange(val) {
      this.areaArr = []
      this.areaArr = this.bedSelect.filter(v => v.area_id === val)
      if (this.areaArr.length > 0) {
        const selectArr = this.areaArr.filter(v => v.selected === 1)
        if (selectArr.length > 0) {
          this.checkedArr = selectArr.map(v => v.id)
        } else {
          this.checkedArr = []
        }
      }
    },
    makeInitialData() {
      this.areaArr = []
      const selectArr = this.bedSelect.filter(v => v.selected === 1)
      if (selectArr.length > 0) {
        this.currDiseaseArea = selectArr[0].area_id
        this.areaArr = this.bedSelect.filter(v => v.area_id === this.currDiseaseArea)
        this.checkedArr = selectArr.map(v => v.id)
      } else {
        this.areaArr = this.bedSelect.filter(v => v.area_id === 1)
        this.checkedArr = []
        this.currDiseaseArea = 1
      }
    },
    handleBed() {
      this.dialogVisible = true
    },
    updateData() {
      if (this.checkedArr.length > 0) {
        const ids = this.checkedArr.join(',')
        const bed = {
          id: parseInt(Math.random() * 100) + 1024,
          name: 'a',
          ids: ids
        }
        createBedNurse(bed).then(response => {
          this.$notify({
            title: '提示',
            message: '保存成功',
            type: 'success',
            duration: 2000
          })
        })
      }
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.diseaseArea = this.diseaseArea
      this.listQuery.banci = this.banci
      this.listQuery.name = this.name
      this.listQuery.checked = this.checked
      this.getRegisterList(this.listQuery)
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getRegisterList(this.listQuery)
    },
    handleDetail(row) {
      this.$router.push({
        path: '/nurse_detail',
        query: { register_id: row.reg_id, patientid: row.patient, activeName: 'first' }
      })
    },
    startoverTouxi(row,flag) {
      let msg = ''
      let status = ''
      if (flag === 2) {
        msg = '开始透析'
        status = '治疗中'
      } else {
        msg = '透析结束'
        status = '下机'
      }
      const txrecordid = row.txrecordid
      if (txrecordid === null || txrecordid === undefined || txrecordid === '') {
        this.$notify({
          title: '提示',
          message: '请先进行医嘱审核以及执行',
          type: 'success',
          duration: 2000
        })
        return
      }
      this.tx_record.id = txrecordid
      this.tx_record.status = status
      this.tx_record.action = flag
      updatetx_record(this.tx_record).then(() => {
        this.getRegisterList(this.listQuery)
        this.$router.push({
          name: 'nurse_detail',
          query: { register_id: row.reg_id,patientid: row.patient, activeName: 'third' }
        })
      })
    },
    handleAlert() {
      this.getDrugAlertList()
      this.dialogListVisible = true
    },
    apply_Drug() {
      if (this.arrangeSelect === ''){
        this.$notify({
          title: '提示',
          message: '请选择班次',
          type: 'success',
          duration: 2000
        })
      } else {
        const appdrug = {
          id: parseInt(Math.random() * 100) + 1024,
          sn: '201809220001',
          bc_id: this.banci,
          area_id: this.diseaseArea,
          applydate: new Date()
        }
        createApply_drug(appdrug).then(response => {
          this.applydrug_btncount = this.applydrug_btncount + 1
          this.applydrug_dialogFormVisible = true
        })
      }
    },
    apply_Material() {
      if (this.arrangeSelect === '') {
        this.$notify({
          title: '提示',
          message: '请选择班次',
          type: 'success',
          duration: 2000
        })
      } else {
        const appmaterial = {
          id: parseInt(Math.random() * 100) + 1024,
          sn: '201809220001',
          bc_id: this.banci,
          area_id: this.diseaseArea,
          applydate: new Date()
        }
        createApply_material(appmaterial).then(response => {
          this.applymaterial_btncount = this.applymaterial_btncount + 1
          this.applymaterial_dialogFormVisible = true
        })
      }
    },
    getSpanArr(data) {
      this.spanArr = []
      for (let i = 0; i < data.length; i++) {
        if (i === 0) {
          this.spanArr.push(1)
          this.pos = 0
        } else {
          // 判断当前元素与上一个元素是否相同
          if (data[i].patientname === data[i - 1].patientname) {
            this.spanArr[this.pos] += 1
            this.spanArr.push(0)
          } else {
            this.spanArr.push(1)
            this.pos = i
          }
        }
      }
    },
    cellMerge({ row, column, rowIndex, columnIndex }) {
      if (columnIndex === 0 || columnIndex === this.colCount - 1) {
        const _row = this.spanArr[rowIndex]
        const _col = _row > 0 ? 1 : 0
        return {
          rowspan: _row,
          colspan: _col
        }
      }
    },
    selectChange: function(val) {
      if (val) {
        this.multipleSelection=[]
        this.multipleSelection = val
      }
    },
    handleSign(row) {
      const tempData = {
        id: row.id,
        state: 1,
        status: 4,
        labid: 1
      }
      updatetRegister(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '签到成功',
          type: 'success',
          duration: 2000
        })
        this.getRegisterList(this.listQuery)
      })
    },
    handleCancelSign(row) {
      const tempData = {
        id: row.id,
        state: 1,
        status: 5,
        labid: 1
      }
      updatetRegister(tempData).then(() => {
        this.$notify({
          title: '成功',
          message: '取消签到成功',
          type: 'success',
          duration: 2000
        })
        this.getRegisterList(this.listQuery)
      })
    },
    formatFlag: function(row, column) {
      const qd = row.flag
      let s = ''
      switch (qd) {
        case false:
          s = '待签到'
          break
        case true:
          s = '已签到'
          break
      }
      return s
    },
    formatState: function(row, column) {
      if (row.state === 0){
        return '未审核'
      }
      else if (row.state === 1){
        return '已审核'
      }
      else if (row.state === 2){
        return '已执行'
      }
      else if (row.state === 3){
        return '已撤销'
      } else {
        return '未审核'
      }
    },
    tableRowClass(row, column) {
      const yznum = row.row.num
      if (yznum > 0) {
        return 'warm-row'
      }
    },
    rowClick(row, event, column) {
      this.register = {}
      this.register = Object.assign({}, row)
      this.register_id = row.reg_id
    },
    dateFormat(row, column) {
      const date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm')
    },
    datetimeFormat(row, column) {
      const date = row[column.property]
      if (date === undefined || date === null || date === '') {
        return ''
      } else {
        return moment(date).format('HH:mm:ss')
      }
    }
  },
  created: function() {
    this.getRegisterList(this.listQuery)
    this.ConnectServer()
    this.getBanciList('')
    this.getDiseaseAreaList('')
    this.getBedList()
  }
//  mounted() {
//    if (this.timer) {
//      clearInterval(this.timer)
//    } else {
//      this.timer = setInterval(() => {
//        // this.getRegisterList(this.listQuery)
//      }, 10000)
//    }
//  },
//  destroyed() {
//    clearInterval(this.timer)
//  }
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
    .status-handler{
      width: 20px;
      height: 20px;
      color: red;
      cursor: pointer;
    }
    .el-table .warm-row {
      background: #c0c4cc;
    }
</style>
