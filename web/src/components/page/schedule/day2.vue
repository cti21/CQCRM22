<template>
    <div>
        <el-row>
            <span class="el-form-item__label">当前患者编号:{{patientid}}</span>
            <span class="el-form-item__label">当前患者姓名:{{patientname}}</span>
            <span class="el-form-item__label">当前患者性别:{{patientsex}}</span>
        </el-row>
        <el-row>
            <el-radio-group v-model="weektype" style="margin-left: 10px;" @change="selectChange">
                <el-radio label="本周">本周</el-radio>
                <el-radio label="下周">下周</el-radio>
            </el-radio-group>
            <el-button size="small" type="primary" style="margin-left: 50px;" icon="el-icon-check" @click.native="returnpatient">选择患者
            </el-button>
        </el-row>
        <div :style="style" v-show="isShow2" class="right-menu" id='dvmenu'></div>
        <el-table :data="tableData" stripe style="width: 100%" header-row-class-name="center" :header-cell-style="{background:'#F8F8F8'}" @cell-click='handlecell' @row-contextmenu='handleright' :row-style="{height: '40px', fontSize: '14px'}">
            <el-table-column label="病区" prop="roomno" width="40px"></el-table-column>
            <el-table-column label="床号" prop="bedno" width="35px"></el-table-column>
            <el-table-column :label="mon">
                <el-table-column :width="colwidth" prop="mon_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="mon_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="mon_evening" label="晚"></el-table-column>
            </el-table-column>
            <el-table-column :label="tue">
                <el-table-column :width="colwidth" prop="tue_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="tue_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="tue_evening" label="晚"></el-table-column>
            </el-table-column>
            <el-table-column :label="wed">
                <el-table-column :width="colwidth" prop="wed_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="wed_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="wed_evening" label="晚"></el-table-column>
            </el-table-column>
            <el-table-column :label="thu">
                <el-table-column :width="colwidth" prop="thu_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="thu_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="thu_evening" label="晚"></el-table-column>
            </el-table-column>
            <el-table-column :label="fri">
                <el-table-column :width="colwidth" prop="fri_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="fri_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="fri_evening" label="晚"></el-table-column>
            </el-table-column>
            <el-table-column :label="sat">
                <el-table-column :width="colwidth" prop="sat_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="sat_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="sat_evening" label="晚"></el-table-column>
            </el-table-column>
            <el-table-column :label="sun">
                <el-table-column :width="colwidth" prop="sun_morning" label="早"></el-table-column>
                <el-table-column :width="colwidth" prop="sun_afternoon" label="中"></el-table-column>
                <el-table-column :width="colwidth" prop="sun_evening" label="晚"></el-table-column>
            </el-table-column>
        </el-table>
    </div>
</template>
<style>
.el-table .cell {
    font-size: 14px;
}
</style>
<script>
import bus from './bus.js'
import api from './api.js'

import { mapGetters, mapMutations } from 'vuex'
import { setschedule_day, getschedule_day, getpatient_txtype } from './schedule.js'
import Vue from 'vue'
export default {
    data() {
        return {
            style: {},
            tabledataObj: Object(),
            mon: '',
            tue: '',
            wed: '',
            thu: '',
            fri: '',
            sat: '',
            sun: '',
            tableData: [],
            colwidth: 54,
            updateSchudual: 0,
            curselweek: 0,
            weektype: ''
        }
    },
    methods: {
        destorymenu(obj) {
            self.$store.commit('setpopmenu', {
                isShow2: false,
            })
        },
        selectChange(val) {
            if (val === '本周') {
                this.curselweek = 0
                this.getWeek(0)
            } else {
                this.getWeek(7)
            }
        },
        treat_f(hd, f) {
            const obj = document.getElementById('dvmenu')
            // self = this
            const MyComponent = Vue.extend({
                template: "<a href='javascript:;' @click=" + f + '>' + hd + '</a>',
                methods: {
                    hd() {
                        const str = self.schedule_patient2.split(',')
                        const scheduleid = str[0]
                        const patientid = str[1]
                        self.processSchedule(scheduleid, patientid, 'hd')
                        self.destorymenu(obj)
                    },
                    hdf() {
                        const str = self.schedule_patient2.split(',')
                        const scheduleid = str[0]
                        const patientid = str[1]
                        self.processSchedule(scheduleid, patientid, 'hdf')
                        self.destorymenu(obj)
                    },
                    hp() {
                        const str = self.schedule_patient2.split(',')
                        const scheduleid = str[0]
                        const patientid = str[1]
                        self.processSchedule(scheduleid, patientid, 'hp')
                        self.destorymenu(obj)
                    },
                    hdp() {
                        const str = self.schedule_patient2.split(",")
                        const scheduleid = str[0]
                        const patientid = str[1]
                        self.processSchedule(scheduleid, patientid, 'hdp')
                        self.destorymenu(obj)
                    },
                    selectpatient() {
                        const str = self.schedule_patient2.split(',')
                        const patientid = str[1]
                        let patientname2 = str[2]
                        let result
                        patientname2 = patientname2 + 'abc'
                        const reg = /[a-zA-Z]+/ // [a-zA-Z]表示匹配字母，g表示全局匹配
                        while (result === patientname2.match(reg)) { // 判断str.match(reg)是否没有字母了
                            patientname2 = patientname2.replace(result[0], '') //替换掉字母  result[0] 是 str.match(reg)匹配到的字母
                        }
                        self.$store.commit('panban_patient', {
                            patientid: patientid,
                            patientname: patientname2
                        })
                        self.destorymenu(obj)
                    },
                    resetschedule() {
                        const str = self.schedule_patient2.split(',')
                        const scheduleid = str[0]
                        self.processSchedule(scheduleid, ',')
                        self.destorymenu(obj)
                    }
                },
                ...mapMutations([
                    'setpopmenu'
                ])
            })
            const component = new MyComponent().$mount()
            obj.appendChild(component.$el)
        },
        timeFormat: function(date) {
            if (!date || typeof(date) === 'string') {
                this.error('参数异常，请检查...')
            }
            const y = date.getFullYear() // 年
            let m = date.getMonth() + 1 // 月
            m = m < 10 ? '0' + m : m
            let d = date.getDate() // 日
            d = d < 10 ? '0' + d : d
            return y + '-' + m + '-' + d
        },
        // 获取本周的周一
        getFirstDayOfThisWeek: function(date) {

            var weekday = date.getDay() || 7; //获取星期几,getDay()返回值是 0（周日） 到 6（周六） 之间的一个整数。0||7为7，即weekday的值为1-7

            date.setDate(date.getDate() - weekday + 1); //往前算（weekday-1）天，年份、月份会自动变化
            return this.timeFormat(date);
        },

        // 获取下周的周一

        getFirstDayOfNextWeek: function(date) {

            var weekday = date.getDay() || 7; //获取星期几,getDay()返回值是 0（周日） 到 6（周六） 之间的一个整数。0||7为7，即weekday的值为1-7

            date.setDate(date.getDate() - weekday + 1 + 7); //往前算（weekday-1）天，年份、月份会自动变化

            return this.timeFormat(date);
        },

        dateToString: function(date) {
            var year = date.getFullYear();
            var month = (date.getMonth() + 1).toString();
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
        getCurWeekList: function() {
            var new_Date = new Date()
            var timesStamp = new_Date.getTime();
            var currenDay = new_Date.getDay();
            var dates = [];
            for (var i = 0; i < 7; i++) {
                dates.push(this.dateToString(new Date(timesStamp + 24 * 60 * 60 * 1000 * (i - (currenDay + 6) % 7))));
            }
            return dates
        },

        getNextWeekList: function(date) {
            var dateTime = date.getTime(); // 获取现在的时间
            var dateDay = date.getDay();
            var oneDayTime = 24 * 60 * 60 * 1000;
            var proWeekList = [];

            for (var i = 0; i < 7; i++) {
                var time = dateTime + (dateDay + (7 - i)) * oneDayTime;
                proWeekList[i] = this.dateToString(new Date(time)); //date格式转换为yyyy-mm-dd格式的字符串
            }
            return proWeekList;
        },
        getProWeekList: function(date) {
            var dateTime = date.getTime(); // 获取现在的时间
            var dateDay = date.getDay();
            var oneDayTime = 24 * 60 * 60 * 1000;
            var proWeekList = [];

            for (var i = 0; i < 7; i++) {
                var time = dateTime - (dateDay + (7 - 1 - i)) * oneDayTime;;
                proWeekList[i] = this.dateToString(new Date(time)); //date格式转换为yyyy-mm-dd格式的字符串
            }
            return proWeekList;
        },

        getWeek(j) {
            const wdays = []
            const mon = ''
            let firstDay = ''
            const now = new Date()
            if (j === 0) {
                firstDay = this.getFirstDayOfThisWeek(now)
            } else {
                firstDay = this.getFirstDayOfNextWeek(now)
            }

            this.mon = firstDay
            const newdate = new Date(firstDay)
            for (let i = 0; i < 6; i++) {
                newdate.setDate(newdate.getDate() + 1)
                wdays.push(this.dateToString(newdate))
            }
            this.tue = wdays[0]
            this.wed = wdays[1]
            this.thu = wdays[2]
            this.fri = wdays[3]
            this.sat = wdays[4]
            this.sun = wdays[5]
            firstDay = this.mon
            // 只传本周第一天
            const data = { 'date': firstDay, 'area': 1, 'patientid': '' }
            getschedule_day(data).then(res => {
                this.getTableData(res.data)
            })
        },

        thisweek() {
            this.curselweek = 0
            this.getWeek(0)
        },
        lastweek() {
            this.curselweek = 1
            this.getWeek(1)
        },
        nextweek() {
            this.getWeek(7)
        },
        next2week() {
            this.getWeek(14)
        },
        returnpatient() {
            this.$router.push({ path: '/selectpatient' })
        },
        getTableData(TableData) {
            const weekbase = [
                [
                    ['mon', 'morning'],
                    ['mon', 'afternoon'],
                    ['mon', 'evening']
                ],
                [
                    ['tue', 'morning'],
                    ['tue', 'afternoon'],
                    ['tue', 'evening']
                ],
                [
                    ['wed', 'morning'],
                    ['wed', 'afternoon'],
                    ['wed', 'evening']
                ],
                [
                    ['thu', 'morning'],
                    ['thu', 'afternoon'],
                    ['thu', 'evening']
                ],
                [
                    ['fri', 'morning'],
                    ['fri', 'afternoon'],
                    ['fri', 'evening']
                ],
                [
                    ['sat', 'morning'],
                    ['sat', 'afternoon'],
                    ['sat', 'evening']
                ],
                [
                    ['sun', 'morning'],
                    ['sun', 'afternoon'],
                    ['sun', 'evening']
                ]
            ]

            let o = {}
            let i = 0,
                j = 0,
                m, dataobj = [],
                b = '',
                c = ''

            // 界面排班数据 周一到周六
            for (i = 0; i < TableData.length; i += 1) {
                o = {}
                o.roomno = TableData[i].area.name
                o.bedno = TableData[i].bed.name

                for (j = 0; j < weekbase.length; j += 1) {
                    for (m = 0; m < 3; m = m + 1) {
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

            let obj = document.getElementById('dvmenu')
            this.$store.commit('setpopmenu', {
                isShow2: false,
            })

            var childs = obj.childNodes;
            let len = childs.length
            while (childs.length > 0) {
                obj.removeChild(childs[0]);
            }

            let week = column.property
            if ((week == 'bedno') || (week == 'roomno'))
                return

            if ((typeof(row[week]) == "undefined") ||
                (typeof(row[week]) == "string") && (row[week] == "")) {
                let s = week + '_patientid';
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
        handleright(row, event, column) {
            //  清空右键菜单
            let obj = document.getElementById('dvmenu')
            this.$store.commit('setpopmenu', {
                isShow2: false,
            })

            const childs = obj.childNodes
            let len = childs.length
            while (childs.length > 0) {
                obj.removeChild(childs[0]);
            }
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
            let schedule_patient = eval('row.' + s) + "," + eval('row.' + week)

            self.roomno2 = row['roomno']
            self.bedno2 = row['bedno']
            self.patientname2 = eval('row.' + week)
            self.week2 = week


            self.schedule_patient = schedule_patient

            if ((week != 'bedno') && (week != 'roomno')) {
                //  确定当前患者透析方式

                let data = { "patientid": schedule_patient.split(",")[1] }
                getpatient_txtype(data).then(resdata => {
                    let i = 0,
                        len;
                    len = resdata.data.tx_type.length

                    for (i = 0; i < len; i++) {
                        if (resdata.data.tx_type[i].name == '血液透析滤过')
                            this.treat_f('hdf', 'hdf')
                        else if (resdata.data.tx_type[i].name == '血液透析')
                            this.treat_f('hd', 'hd')
                        else if (resdata.data.tx_type[i].name == '血液灌流')
                            this.treat_f('hp', 'hp')
                        else if (resdata.data.tx_type[i].name == '血液滤过')
                            this.treat_f('hf', 'hf')
                    }

                    this.treat_f('设为当前患者', 'selectpatient')
                    this.treat_f('取消排班', 'resetschedule')
                })

                this.$store.commit('setpopmenu', {
                    isShow2: true,
                    schedule_patient2: schedule_patient,
                })
            }
            event.preventDefault()
            console.log(column.property);
        },

        // 布局
        layout() {
            this.style = {
                left: this.x + 'px',
                top: this.y + 'px'
            }
        },

    },
    watch: {
        updateSchudual(curVal, oldVal) {
            this.thisweek(this.curselweek);
        }
    },
    created() {
        let self = this
        self.thisweek()
        // bus.$on('msg_treat', (x,y) => {
        //    self.isShow = !self.isShow
        //  }),
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
    computed: mapGetters([
        //此处的 count 与以下 store.js 文件中 getters 内的 count 相对应
        'count', 'patientid', 'patientname', 'patientsex', 'isShow2', 'schedule_patient2'
    ]),
    ...mapMutations([
        'setpopmenu'
    ])
}
</script>