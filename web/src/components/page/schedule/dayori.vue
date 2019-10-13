<template>

  <div>
    <span>当前患者id{{patientid}}</span>
    <span>当前患者姓名{{patientname}}</span>
    <span>当前患者性别{{patientsex}}</span>
    <span>{{odddual_week==1 ? "单周":"双周"}}</span>
    <br></br>
  <el-button-group>
  <!--<el-button type="primary" icon="el-icon-edit"   @click.native="lastweek">上周</el-button>-->
  <el-button size="mini" type="primary" icon="el-icon-share"  @click.native="thisweek">本周</el-button>
  <el-button size="mini" type="primary" icon="el-icon-delete" @click.native="nextweek">下周</el-button>
  <!--<el-button type="primary" icon="el-icon-delete" @click.native="next2week">下两周</el-button>-->
</el-button-group>

 <!--<el-button type="primary" icon="el-icon-delete" @click.native="returnpatient">确定（返回排班）</el-button>-->

 <el-button size="mini" type="primary" icon="el-icon-delete" @click.native="returnpatient">选择患者</el-button>

  <div :style="style" v-show="isShow" class="right-menu" >
      <a href="javascript:;" @click="treat_hd">hd</a>
      <a href="javascript:;" @click="treat_hdf">hdf</a>
      <a href="javascript:;" @click="treat_hp">hp</a>
      <a href="javascript:;" @click="treat_hf">hf</a>
      <!--<a href="javascript:;" @click="treat_crrt">CRRT</a>-->
      <a href="javascript:;" @click="selectpatient">设为当前患者</a>
      <a href="javascript:;" @click="resetschedule">取消排班</a>
  </div>

  <el-table
    :data="tableData"
    stripe
    style="width: 100% ;margin-left: 5px ;margin-top: 5px"
    header-row-class-name="center"
    @cell-click='handlecell'
    @row-contextmenu='handleright'
    class = "aaa"
    >
  <el-table-column  label="病区"
  prop="roomno"
       width="40"
    >
  </el-table-column>
 <el-table-column  label="床号"
 prop="bedno"
     width="30" >
  </el-table-column>
 <el-table-column :label="mon"  >
    <el-table-column
     :width = "colwidth"
      prop="mon_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="mon_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="mon_evening"
      label="晚">
    </el-table-column>
  </el-table-column>
 <el-table-column :label="tue">
    <el-table-column
    :width = "colwidth"
      prop="tue_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="tue_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="tue_evening"
      label="晚">
    </el-table-column>
  </el-table-column>
  <el-table-column :label="wed">
    <el-table-column
    :width = "colwidth"
      prop="wed_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="wed_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="wed_evening"
      label="晚">
    </el-table-column>
  </el-table-column>
  <el-table-column :label="thu">
    <el-table-column
    :width = "colwidth"
      prop="thu_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="thu_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="thu_evening"
      label="晚">
    </el-table-column>
  </el-table-column>
  <el-table-column :label="fri">
    <el-table-column
    :width = "colwidth"
      prop="fri_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="fri_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="fri_evening"
      label="晚">
    </el-table-column>
  </el-table-column>
  <el-table-column :label="sat">
    <el-table-column
    :width = "colwidth"
      prop="sat_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="sat_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="sat_evening"
      label="晚">
    </el-table-column>
  </el-table-column>

  <el-table-column :label="sun">
    <el-table-column
    :width = "colwidth"
      prop="sun_morning"
      label="早"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="sun_afternoon"
      label="中"
      >
    </el-table-column>
    <el-table-column
    :width = "colwidth"
      prop="sun_evening"
      label="晚">
    </el-table-column>
  </el-table-column>

  </el-table>
</div>
</template>

<style  type="text/css" >
   .el-table .cell {
    /*background:#f5b5a1 !important;*/
    font-size: small;
  }
   .el-table .cell,child .cell {
     padding-left: 5px;
     padding-right: 5px;
   }
</style>

<script>
  import bus from "./bus.js"
  import api from './api.js'
  // import mockTableData from './table1Data.js'
  // 准备与个人治疗方案对照，1.0版暂不加入
  // import patientTreat from './table1patientData.js'
  import {mapGetters,mapActions} from 'vuex'
  import { setschedule_day, getschedule_day } from './schedule.js'

  export default {
    data() {
      return {
        style: {},
        tabledataObj:Object(),
        mon:'',
        tue:'',
        wed:'',
        thu:'',
        fri:'',
        sat:'',
        sun:'',
        isShow :false,
        tableData:[],
        // days:[],
        colwidth:55,
        updateSchudual: 0,
        curselweek:0
       }
    },

    methods: {
timeFormat:function (date) {
      if (!date || typeof(date) === "string") {
          this.error("参数异常，请检查...");
     }
     var y = date.getFullYear(); //年
     var m = date.getMonth() + 1; //月
      m = m < 10 ? '0' + m : m;
     var d = date.getDate(); //日
   d =d < 10 ? '0' + d : d;
     return y + "-" + m + "-" + d;
 },
//获取本周的周一
 getFirstDayOfThisWeek:function  (date) {

     var weekday = date.getDay()||7; //获取星期几,getDay()返回值是 0（周日） 到 6（周六） 之间的一个整数。0||7为7，即weekday的值为1-7

     date.setDate(date.getDate()-weekday+1);//往前算（weekday-1）天，年份、月份会自动变化
     return this.timeFormat(date);
 },

// 获取下周的周一

 getFirstDayOfNextWeek:function  (date) {

     var weekday = date.getDay()||7; //获取星期几,getDay()返回值是 0（周日） 到 6（周六） 之间的一个整数。0||7为7，即weekday的值为1-7

     date.setDate(date.getDate()-weekday+1+7);//往前算（weekday-1）天，年份、月份会自动变化

     return this.timeFormat(date);
 },

    dateToString: function(date){
  var year = date.getFullYear();
  var month =(date.getMonth() + 1).toString();
  var day = (date.getDate()).toString();
  if (month.length == 1) {
      month = "0" + month;
  }
  if (day.length == 1) {
      day = "0" + day;
  }
  var dateTime = year + "-" + month + "-" + day;
  return dateTime;
  },
    getCurWeekList: function () {
    var new_Date = new Date()
    var timesStamp = new_Date.getTime();
    var currenDay = new_Date.getDay();
    var dates = [];
    for(var i = 0; i < 7; i++) {
        dates.push(this.dateToString(new Date(timesStamp + 24 * 60 * 60 * 1000 * (i - (currenDay + 6) % 7))));
    }
    return dates
    },

      getNextWeekList: function (date) {
        var dateTime = date.getTime(); // 获取现在的时间
        var dateDay = date.getDay();
        var oneDayTime = 24 * 60 * 60 * 1000;
        var proWeekList = [];

        for(var i = 0; i < 7; i++){
          var time = dateTime + (dateDay + (7 - i)) * oneDayTime;
          proWeekList[i] = this.dateToString(new Date(time)); //date格式转换为yyyy-mm-dd格式的字符串
        }
        return proWeekList;
    },
  getProWeekList: function (date) {
        var dateTime = date.getTime(); // 获取现在的时间
        var dateDay = date.getDay();
        var oneDayTime = 24 * 60 * 60 * 1000;
        var proWeekList = [];

        for(var i = 0; i < 7; i++){
          var time = dateTime - (dateDay + (7 - 1 - i)) * oneDayTime;;
          proWeekList[i] = this.dateToString(new Date(time)); //date格式转换为yyyy-mm-dd格式的字符串
        }
        return proWeekList;
},

      getWeek: function (j) {

            var wdays=[],mon='',firstDay;
            var now = new Date();
            if (j==0)
              firstDay = this.getFirstDayOfThisWeek(now);
            else
              firstDay = this.getFirstDayOfNextWeek(now);

            this.mon = firstDay
            var newdate = new Date(firstDay)
            for (var i=0;i<6;i++)
            {
                newdate.setDate(newdate.getDate() + 1);
                // mon = Number(firstDay.getMonth()) + 1;
                // wdays.push(now.getFullYear() + "-" + mon + "-" + firstDay.getDate())
                wdays.push(this.dateToString(newdate))
            }

                this.tue = wdays[0]
                this.wed = wdays[1]
                this.thu = wdays[2]
                this.fri = wdays[3]
                this.sat = wdays[4]
                this.sun = wdays[5]
                firstDay = this.mon
                // alert(this.mon+','+wdays)
       //      var week = new Date().getDay();
       //      if (j==0) {
       //          // 本周
       //        if (week == 0)
       //        {
       //          // 本周星期日,js函数视为上周，国内习惯看做本周
       //          wdays = this.getProWeekList(now)
       //          firstDay = wdays[0]
       //        }
       //        else
       //        {
       //          day = getCurWeekList()
       //          alert(day)
       //          // firstDay = new Date(now - (now.getDay() - 1 ) * 86400000);
       //          // for (var i=0;i<7;i++)
       //          // {

       //          //   firstDay.setDate(firstDay.getDate() + i);
       //          //   mon = Number(firstDay.getMonth()) + 1;
       //          //   wdays.push(now.getFullYear() + "-" + mon + "-" + firstDay.getDate())
       //          // }
       //          // this.mon = wdays[0]
       //          // this.tue = wdays[1]
       //          // this.wed = wdays[2]
       //          // this.thu = wdays[3]
       //          // this.fri = wdays[4]
       //          // this.sat = wdays[5]
       //          // this.sun = wdays[6]
       //          // firstDay = this.mon

       //        }
       //      // //只传本周第一天
       //      // let data = { "date": firstDay, "area": 1,"patientid":"" }
       //      // getschedule_day(data).then(res => {
       //      // this.getTableData(res.data)
       //  // })
       //  }
       //  else
       //  {
       // //  下周
       //       if (week == 0)
       //        {
       //          // 本周星期日
       //          wdays = this.getNextWeekList(now)
       //          // alert(wdays)
       //          firstDay = wdays[6]
       //        }
       //        else {
       //          wdays = this.getNextWeekList(now)
       //          // alert(wdays)
       //          firstDay = wdays[0]

       //        }

       //  }

         //只传本周第一天
            let data = { "date": firstDay, "area": 1,"patientid":"" }
            getschedule_day(data).then(res => {
              // alert("aaaaaaaaaaaaaa");
            this.getTableData(res.data)
          })
        },

    thisweek: function () {
               this.curselweek = 0
               this.getWeek(0)
            },
    lastweek: function () {
               this.curselweek = 1
               this.getWeek(1)
            },
    nextweek: function () {
               this.getWeek(7)
            },
    next2week: function () {
               this.getWeek(14)
            },
    returnpatient: function () {
      this.$router.push({ path: '/selectpatient' })
            },
     getTableData: function(TableData){

       let weekbase = [[['mon','morning'],['mon','afternoon'],['mon','evening']]
         ,[['tue','morning'],['tue','afternoon'],['tue','evening']]
         ,[['wed','morning'],['wed','afternoon'],['wed','evening']]
         ,[['thu','morning'],['thu','afternoon'],['thu','evening']]
         ,[['fri','morning'],['fri','afternoon'],['fri','evening']]
         ,[['sat','morning'],['sat','afternoon'],['sat','evening']]
         ,[['sun','morning'],['sun','afternoon'],['sun','evening']]
       ]

       let o = {}
       let i = 0, j = 0, m,  dataobj = [] ,  b="", c=""

       // 界面排班数据 周一到周六
       for (i = 0; i < TableData.length; i += 1) {
         o = { }
         o.roomno = TableData[i].area.name
         o.bedno = TableData[i].bed.name

         for (j =0;j < weekbase.length ;j += 1)
         {
             for ( m=0;m<3;m=m+1) {

             b = 'o.' + weekbase[j][m][0] + '_' + weekbase[j][m][1] + '_patientid = TableData[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.schedule_patientid'
             eval(b)

             c = ' if (TableData[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.patientname != \"\") { o.' + weekbase[j][m][0] + '_' + weekbase[j][m][1] + ' = TableData[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.patientname + ( TableData[' + i + '].' + weekbase[j][m][0] + weekbase[j][m][1] + '.treat_project ) } else  o.' + weekbase[j][m][0] + '_' + weekbase[j][m][1] + ' = ""'
             eval(c)
           }
         }
         dataobj.push(o)
       }
       this.tableData = dataobj
    },
      handlecell(row, column, cell, event) {

      let week = column.property
      if ((week == 'bedno') || (week == 'roomno'))
        return

      if ((typeof(row[week]) == "undefined") ||
        (typeof(row[week]) == "string") && (row[week] == "")) {
        let  s = week + '_patientid';
        let schedule_patient = eval('row.' + s)
        let str = schedule_patient.split(",")
        let scheduleid = str[0]

        this.processSchedule(scheduleid, this.$store.state.schedule.patientid, '')
        }
      },
      processSchedule(scheduleid, patientid, treat_project) {

        let data = {
          patientid: patientid,
          scheduleid: scheduleid,
          data: {
            treat_project: treat_project,
          }
        }
        setschedule_day(data).then(response => {
          this.updateSchudual = !this.updateSchudual
        })
      },
       // 处理table的右键菜单
      handleright(row, event,column) {
          // 周几
        let week = column.property
        // 空床位不允许右键
        if ((typeof(row[week]) == "undefined") || row[week] == '' || (week == 'bedno') || (week == 'roomno')) {
          event.preventDefault()
          return
        }

        this.x = event.clientX
           this.y = event.clientY
           this.layout()

        let s = week + '_patientid';
        let schedule_patient = eval('row.' + s)

           self.roomno2 = row['roomno']
           self.bedno2  = row['bedno']
           self.patientname = row[week]
           self.week2 = week

           self.patientname = row[week]

           let index = self.patientname.indexOf("(")
           if (index>0) {
             self.patientname = self.patientname.substring(0,index)
             // self.patientname = self.patientname.replace(")", "")
           }
           self.schedule_patient = schedule_patient

           if ((week != 'bedno') && (week != 'roomno'))
            bus.$emit('msg_treat',event.clientX,event.clientY)

           event.preventDefault()
           console.log(column.property);
      },

      resetschedule() {

        this.isShow = false
        let str = schedule_patient.split(",")
        let scheduleid = str[0]

        this.processSchedule(scheduleid, '','')
      },

      //   右键选择当前患者
      selectpatient() {

        this.isShow = false
        let str = schedule_patient.split(",")
        let patientid = str[1]

        this.$store.commit('panban_patient', {
          patientid: patientid,
          patientname: patientname,
        })
      },
      treat_hd() {
      this.isShow = false
      let str = schedule_patient.split(",")
      let scheduleid = str[0]
      let patientid = str[1]
      this.processSchedule(scheduleid, patientid, 'HD')
    },
    treat_hdf () {
      this.isShow = false
      let str = schedule_patient.split(",")
      let scheduleid = str[0]
      let patientid = str[1]
      this.processSchedule(scheduleid, patientid, 'HDF')
    },
     treat_hp () {
      this.isShow = false
      let str = schedule_patient.split(",")
      let scheduleid = str[0]
      let patientid = str[1]
      this.processSchedule(scheduleid, patientid, 'HP')
    },
     treat_hf() {
      this.isShow = false
      let str = schedule_patient.split(",")
      let scheduleid = str[0]
      let patientid = str[1]
      this.processSchedule(scheduleid, patientid, 'HP+HD')
    },
    treat_crrt () {
      // alert('delete')
      this.isShow = false
    },
// 布局
    layout () {
      this.style = {
        left: this.x + 'px',
        top: this.y + 'px'
      }
    },

  },
    watch: {


      updateSchudual(curVal, oldVal) {
        // let data = { "date": '2018-10-15', "area": 1,"patientid":"111111111111111" }
        // getschedule_day(data).then(res => {
        //   this.getTableData(res.data)
        // })
         this.thisweek(this.curselweek);
      }
    },
    created() {
　　　　let self = this
       self.thisweek()
       // bus 与 table 同属一个对象
       bus.$on('msg_treat', (x,y) => {
       self.isShow = !self.isShow
        }),
        bus.$on('msg_getdata', (x) => {
          // 更新数据
       self.getTableData()
       }),
      // 前一个页面选择患者排班
      bus.$on('msg_patient_panban', (x) => {
          // 1向后台更新数据
          // 2从后台取数据
          self.getTableData()
       })
     },
      computed:mapGetters([
    //此处的 count 与以下 store.js 文件中 getters 内的 count 相对应
        'count', 'patientid', 'patientname', 'patientsex'
       ]),
}
</script>

