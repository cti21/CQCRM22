<template>
    <div class="dialog-container">
        <el-dialog
            title="title"
            :visible.sync="visible"
            @close="$emit('update:show', false)"
            :show="show">

          <el-select v-model="value" placeholder="请选择" filterable :filter-method="test">
            <el-option v-for="item in options"
                       :key="item.value"
                       :label="item.label"
                       :value="item.value">
            </el-option>
          </el-select>


          <el-table :data="gridData">
            <el-table-column property="date" label="日期" width="150"></el-table-column>
            <el-table-column property="name" label="姓名" width="200"></el-table-column>
            <el-table-column property="address" label="地址"></el-table-column>
          </el-table>
             <!--<el-button type="primary" @click="OnOK" >确定按钮</el-button>-->
          <el-pagination
            @current-change ="handleCurrentChange"
            @size-change="handleSizeChange"
            :page-size="pagesize"
            :total="totalCount"
            layout="prev, pager, next"
          >
          </el-pagination>

          <span slot="footer" class="dialog-footer">
            <el-button size="mini" type="primary" @click="OnOK">确 定</el-button>
            <el-button size="mini" @click="OnOK">取消</el-button>
          </span>

        </el-dialog>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                visible: this.show,
                patientid:'12142342342',
                totalCount:10,
              pagesize:1,

                gridData : [
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"},
                  {  "date":"A0","name":"01","address":"01"},
                  {"date":"AAA","name":"01","address":"01"}
              ],
              options: [{       //v-model数组
                value: '选项1',
                label: '黄金糕'
              }, {
                value: '选项2',
                label: '双皮奶'
              }, {
                value: '选项3',
                label: '蚵仔煎'
              }, {
                value: '选项4',
                label: '龙须面'
              }, {
                value: '选项5',
                label: '北京烤鸭'
              }],
              backUpArr:[{   //备份数组
                value: '选项1',
                label: '黄金糕'
              }, {
                value: '选项2',
                label: '双皮奶'
              }, {
                value: '选项3',
                label: '蚵仔煎'
              }, {
                value: '选项4',
                label: '龙须面'
              }, {
                value: '选项5',
                label: '北京烤鸭'
              }]
            };
        },
        methods:  {

          handleSizeChange()
          {
            alert("size chg")
          },
          handleCurrentChange()
          {
             alert("page chg")
          },
          OnOK: function(){
            // this.$emit('update:show', false)
            this.$emit('hidePanel');
            this.$emit('patientid', this.patientid)

          },
          test(val){
            if (val) { //val存在
              this.options = this.backUpArr.filter((item) => {
                if (!!~item.label.indexOf(val) || !!~item.value.indexOf(val)) {
                  return true
                }
              })
            } else { //val为空时，还原数组
              this.options = this.backUpArr
            }
          }
      },
        props: {
            show: {
                type: Boolean,
                default: false
            }
        },
        watch: {
            show() {
                this.visible = this.show;
            }
        }
    };
</script>
