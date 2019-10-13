<template>
  <div>
    <el-row>
      <span class="el-form-item__label">当前患者编号:{{patientid}}</span>
      <span class="el-form-item__label">当前患者姓名:{{patientname}}</span>
      <span class="el-form-item__label">当前患者性别:{{patientsex}}</span>
      <span class="el-form-item__label">{{odddual_week==1 ? "单周":"双周"}}</span>
    </el-row>
    <el-row>
      <el-radio-group
        v-model="weektype"
        style="margin-left: 10px;"
        @change="selectChange">
          <el-radio label="单周">单周</el-radio>
          <el-radio label="双周">双周</el-radio>
      </el-radio-group>
        <el-button
          size="small"
          type="primary"
          style="margin-left: 50px;"
          icon="iconfont iconzidongshengcheng"
          @click.native="createschedule">生成数据
        </el-button>
        <el-button
          size="small"
          type="primary"
          icon="iconfont iconyingyong"
          @click.native="createsdaychedule">计划应用
        </el-button>
        <el-button
          size="small"
          type="primary"
          icon="el-icon-check"
          @click.native="returnpatient">选择患者
        </el-button>

      <!--test-->

  <el-button
          size="small"
          type="primary"
          icon="el-icon-check"
          @click.native="ConnectServer">ConnectServer
        </el-button>

        <el-button
          size="small"
          type="primary"
          icon="el-icon-check"
          @click.native="SendMsg">SendMsg
        </el-button>


    </el-row>
    <div :style="style" v-show="isShow" class="right-menu">
      <a href="javascript:;" @click="treat_hd">HD</a>
      <a href="javascript:;" @click="treat_hdf">HDF</a>
      <a href="javascript:;" @click="setcurpatient">设为当前患者</a>
      <a href="javascript:;" @click="resetschedule">取消排班</a>
    </div>
    <el-table
        :data="tableData"
        stripe
        style="width: 100%;height: 100% ;margin-left: 5px ;margin-top: 5px"
        header-row-class-name="center"
        :header-cell-style="{background:'#F8F8F8'}"
        :height="tableHeight"
        :row-style="{height: '40px', fontSize: '14px', lineHeight: '40px'}"
        @cell-click='handlecell'
        @row-contextmenu='handleright'
    >
      <el-table-column label="病区" prop="roomno" width="40">
      </el-table-column>
      <el-table-column label="床号" prop="bedno" width="30">
      	<template slot-scope="scope">
            <span v-if="scope.row.flag == 1">
            <span  style="color: red">{{ scope.row.bedno }}</span>
            </span>
            <span  v-else>
            <span  style="color: blue">{{ scope.row.bedno }}</span>
            </span>
          </template>
      </el-table-column>
      <el-table-column :label="mon">
        <el-table-column :width="colwidth" height=10 prop="mon_morning" label="早" patientid="">
          <template slot-scope="scope">
            <span v-if="scope.row.mon_morning != ''">
            <span style="color: red">{{ scope.row.mon_morning }}
            </span>
            </span>
           </template>
        </el-table-column>
        <el-table-column :width="colwidth" prop="mon_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="mon_evening" label="晚">
        </el-table-column>
      </el-table-column>
      <el-table-column :label="tue">
        <el-table-column :width="colwidth" prop="tue_morning" label="早">
        </el-table-column>
        <el-table-column :width="colwidth" prop="tue_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="tue_evening" label="晚">
        </el-table-column>
      </el-table-column>
      <el-table-column :label="wed">
        <el-table-column :width="colwidth" prop="wed_morning" label="早">
        </el-table-column>
        <el-table-column :width="colwidth" prop="wed_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="wed_evening" label="晚">
        </el-table-column>
      </el-table-column>
      <el-table-column :label="thu">
        <el-table-column :width="colwidth" prop="thu_morning" label="早">
        </el-table-column>
        <el-table-column :width="colwidth" prop="thu_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="thu_evening" label="晚">
        </el-table-column>
      </el-table-column>
      <el-table-column :label="fri">
        <el-table-column :width="colwidth" prop="fri_morning" label="早">
        </el-table-column>
        <el-table-column :width="colwidth" prop="fri_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="fri_evening" label="晚">
        </el-table-column>
      </el-table-column>
      <el-table-column :label="sat">
        <el-table-column :width="colwidth" prop="sat_morning" label="早">
        </el-table-column>
        <el-table-column :width="colwidth" prop="sat_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="sat_evening" label="晚">
        </el-table-column>
      </el-table-column>
      <el-table-column :label="sun">
        <el-table-column :width="colwidth" prop="sun_morning" label="早">
        </el-table-column>
        <el-table-column :width="colwidth" prop="sun_afternoon" label="中">
        </el-table-column>
        <el-table-column :width="colwidth" prop="sun_evening" label="晚">
        </el-table-column>
      </el-table-column>
    </el-table>
  </div>
</template>
<style>
/* 设置table header的背景颜色 */
/*.el-table__header th, .el-table__header tr {*/
/*background-color: #17B3A3;*/
/*color: black;*/
/*}*/
/* 设置表主体的高度 */
.el-table__body td,
.el-table__body th {
  padding: 1px;
}
/* 设置表头的高度 */
.el-table__header td,
.el-table__header th {
  padding: 3px 0px;
}
/* 设置分页器的高度 */
.site-wrapper .el-pagination {
  margin-top: 5px;
  text-align: right;
}
.el-pager li.active {
  color: #080909;
  cursor: default;
  background-color: #17B3A3;
  border-radius: 2px;
}

.el-table .cell {
  /*background:#f5b5a1 !important;*/
  font-size: 14px;
}

.el-table .cell,
  child .cell {
    padding-left: 5px;
    padding-right: 5px;
}
</style>
<script>
// bus.js 处理右键
import bus from './bus.js'
import api from './api.js'
import { getschedule_odddual, setschedule_patient, create_schedule, create_dayschedule } from './schedule.js'
import PDialog from './dialog.vue'
import request from '@/utils/request'
// 准备与个人治疗方案对照，1.0版暂不加入
// import patientTreat from './table1patientData.js'
import { mapGetters, mapMutations } from 'vuex'
import ElRow from 'element-ui/packages/row/src/row'

export default {
  components: { ElRow },
  data() {
    return {
      style: {},
      mon: '星期一',
      tue: '星期二',
      wed: '星期三',
      thu: '星期四',
      fri: '星期五',
      sat: '星期六',
      sun: '星期日',
      isShow: false,
      tableData: [],
      colwidth: 54,
      // show222: false,
      // 当前是单周还是双周
      odddual_week: '1',
      updateSchudual: 0,
      weektype: '',
      tableHeight: window.innerHeight - 300,
      ws: ''
    }
  },
  watch: {
    updateSchudual(curVal, oldVal) {
      const data = { 'areaid': 1, 'odddual': this.odddual_week }
      getschedule_odddual(data).then(res => {
        this.getTableData(res.data)
      })
    }
  },
  methods: {
    ConnectServer() {
      this.ws = new WebSocket('ws://127.0.0.1:8000/ws/chat/')
      if ('WebSocket' in window) {
        this.ws.onopen = function() {
          console.log('连接成功')
        }
        this.ws.onmessage = function(evt) {
          const received_msg = evt.data
          console.log(received_msg)
        }
        this.ws.onclose = function() {
          console.log('连接已关闭...')
        }
      } else {
        console.log('您的浏览器不支持 WebSocket!')
      }
    },
    SendMsg() {
      this.ws.send('patientid=100')
      console.log('发送的数据 ：patientid=100')
    },
    test: function() {
      return request({
        url: '/api-token-auth/',
        method: 'post',
        data: {
        }
      })
    },
    selectChange(val) {
      if (val === '单周') {
        this.odddual_week = '1'
        const data = { 'areaid': 1, 'odddual': this.odddual_week }
        getschedule_odddual(data).then(res => {
          this.getTableData(res.data)
        })
      } else {
        this.odddual_week = '2'
        const data = { 'areaid': 1, 'odddual': this.odddual_week }
        getschedule_odddual(data).then(res => {
          this.getTableData(res.data)
        })
      }
    },
    oddweek: function() {
      this.odddual_week = '1'
      const data = { 'areaid': 1, 'odddual': this.odddual_week }
      getschedule_odddual(data).then(res => {
        this.getTableData(res.data)
      })
    },
    dualweek: function() {
      this.odddual_week = '2'
      const data = { 'areaid': 1, 'odddual': this.odddual_week }
      getschedule_odddual(data).then(res => {
        this.getTableData(res.data)
      })
    },
    createschedule: function() {
      create_schedule().then(res => {
        alert('create schedual')
      })
    },
    createsdaychedule: function() {
      create_dayschedule().then(res => {
        alert('create day_schedual')
      })
    },
    returnpatient: function() {
      this.$router.push({ path: '/selectpatient' })
    },
    getTableData(TableDate) {
      const weekbase = [[['mon', 'morning'], ['mon', 'afternoon'], ['mon', 'evening']]
        ,[['tue', 'morning'], ['tue', 'afternoon'], ['tue', 'evening']]
        ,[['wed', 'morning'], ['wed', 'afternoon'], ['wed', 'evening']]
        ,[['thu', 'morning'], ['thu', 'afternoon'], ['thu', 'evening']]
        ,[['fri', 'morning'], ['fri', 'afternoon'], ['fri', 'evening']]
        ,[['sat', 'morning'], ['sat', 'afternoon'], ['sat', 'evening']]
        ,[['sun', 'morning'], ['sun', 'afternoon'], ['sun', 'evening']]
      ]

      let o = {}
      let i = 0, j = 0, m, dataobj = [], b = '', c = ''

      // 界面排班数据 周一到周六
      // let week = ['mon', 'tue', 'wed','thu','fri','sat','sun']
      for (i = 0; i < TableDate.length; i += 1) {
        o = {}
        o.roomno = TableDate[i].area.name
        o.bedno = TableDate[i].bed.name
        o.flag = TableDate[i].bed.flag
        for (j = 0; j < weekbase.length; j += 1) {
          for (m = 0; m < 3; m = m + 1) {
            b = 'o.' + weekbase[j][m][0] + '_' + weekbase[j][m][1] + '_patientid = TableDate[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.schedule_patientid'
            eval(b)
            c = ' if (TableDate[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.patientname != \"\") { o.' + weekbase[j][m][0] + '_' + weekbase[j][m][1] + ' = TableDate[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.patientname + ( TableDate[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.treat_project ) } else  o.' + weekbase[j][m][0] + '_' + weekbase[j][m][1] + ' = ""'
            eval(c)
          }
        }
        dataobj.push(o)
      }
      this.tableData = dataobj
    },
    getAxiosTableData(url) {
      //
      api.get_patient(url, 'type=top&key=123456')
        // api.get_patient(url, 'data:{a:1,b:2}')
        .then(res => {
          this.getTableData(res)
        })
    },
    // :row-style="rowClass"
    // rowClass: function (row, index) {
    //  return { "background-color": "red" }
    // },
    // /////////////////////////////////////////////////////

    // 处理排班表的右键菜单
    handleright(row, event, column) {
      //  week 保存当前点击哪个表格

      const week = column.property
      // 空床位不允许右键
      if ((typeof (row[week]) === 'undefined') || row[week] === '' || (week === 'bedno') || (week === 'roomno')) {
        event.preventDefault()
        return
      }
      this.x = event.clientX
      this.y = event.clientY
      this.layout()

      const s = week + '_patientid'
      // evil (fn) {
      // let Fn = Function // 一个变量指向Function，防止有些前端编译工具报错
      //  return new Fn('return ' + fn)()
      // }
      const schedule_patient = eval('row.' + s)

      self.patientname = row[week]
      const index = self.patientname.indexOf('(')
      if (index > 0) {
        self.patientname = self.patientname.substring(0, index)
      }
      self.roomno2 = row['roomno']
      self.bedno2 = row['bedno']
      // 星期几
      self.week2 = week
      // 单双周
      self.odddual = this.odddual_week
      self.patientid = row[week + '_patientid']
      self.schedule_patient = schedule_patient

      bus.$emit('msg_treat', event.clientX, event.clientY)
      event.preventDefault()
    },

    processSchedule(odddualid, patientid, odddual, treat_project) {
      let data = {
        odddualid: odddualid,
        patientid: patientid,
        data: {
          odddual: odddual,
          treat_project: treat_project,
        }
      }
      setschedule_patient(data).then(response => {
        this.updateSchudual = !this.updateSchudual
      })
    },
    treat_hd() {
      // copymsg 与右键弹出菜单函数同属一个对象， this 相同 ，右键菜单中赋值self.roomno2 ，本函数可以直接得到
      // copymsg 与 bus.$on('msg', (x,y)）不属于同一个对象 ，
      // bus.$on('msg', (x,y)）与table属于同一个对象，可以读取 data() {  定义的数据
      // console.log(`qqqqqqqqqqqqqqqqqqqq+${self.roomno2}+${self.bedno2}+${self.week2}+${self.patientname}`);
      this.isShow = false
      const str = schedule_patient.split(',')
      const odddualid = str[0]
      const patientid = str[1]
      this.processSchedule(odddualid, patientid, odddual, 'hd')

    },
    treat_hdf() {
      this.isShow = false
      const str = schedule_patient.split(',')
      const odddualid = str[0]
      const patientid = str[1]
      this.processSchedule(odddualid, patientid, odddual, 'hdf')
    },

    //  左键单击单元格 , 排班当前患者
    handlecell(row, column, cell, event) {

      let week = column.property
      if ((week === 'bedno') || (week === 'roomno'))
        return

      if ((typeof (row[week]) === 'undefined') ||
        (typeof (row[week]) === 'string') && (row[week] === '')) {
        const s = week + '_patientid'
        const schedule_patient = eval('row.' + s)
        const str = schedule_patient.split(',')
        const odddualid = str[0]

        this.processSchedule(odddualid, this.$store.state.schedule.patientid, this.$store.state.schedule.odddual_week, '')
      }
    },
    // 右键取消患者单双周排班
    resetschedule() {
      this.isShow = false
      const str = schedule_patient.split(',')
      const odddualid = str[0]
      this.processSchedule(odddualid, '', odddual, '')
    },
    //   右键选择当前患者
    setcurpatient() {

      this.isShow = false
      let str = schedule_patient.split(',')
      let patientid = str[1]

      this.$store.commit('panban_patient', {
        odddual_week: odddual,
        patient_week: `${self.week2}`,
        patient_roomno: `${self.bedno2}`,
        patient_bedno: `${self.roomno2}`,
        patientid: patientid,
        patientname: patientname,
      })
    },
    // 选择患者
    selectpatient() {

      this.isShow = false
      let str = schedule_patient.split(",")
      let odddualid = str[0]
      this.processSchedule(odddualid, '', odddual, '')
    },

    // 布局
    layout() {
      this.style = {
        left: this.x + 'px',
        top: this.y + 'px'
      }
    },
    ...mapMutations([
      //该 increment 来自 store.js 中导出的 actions 和 mutations 中的 increment
      'patient_week'
    ])
  },
  created() {　　　　
    let self = this

    let data = { "areaid": 1, "odddual": 1 }
      getschedule_odddual(data).then(res => {
      this.getTableData(res.data)
    })


    // bus 与 table 同属一个对象
    bus.$on('msg_treat', (x, y) => {
      self.isShow = !self.isShow
    })

  },
  computed: mapGetters([
    // 此处的 count 与以下 store.js 文件中 getters 内的 count 相对应
    'count', 'patientid', 'patientname', 'patientsex'
  ]),
}

</script>
