<template>
    <div>
        <el-row>
          <el-card style="margin-left: 15px;margin-right: 10px">
            <el-row>
                <el-col :span="6">
                  <label class="el-form-item__label">日期从</label>
                  <el-date-picker
                    v-model="listQuery.begindate"
                    style="width:50%;margin-left: 20px"
                    class="myInput"
                    type="date"
                    placeholder="日期开始"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
                <el-col :span="1">
                  <label class="el-form-item__label">到</label>
                </el-col>
                <el-col :span="5">
                  <el-date-picker
                    v-model="listQuery.enddate"
                    style="width:60%"
                    class="myInput"
                    type="date"
                    placeholder="日期结束"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">客户姓名</label>
                  <el-input
                    v-model="listQuery.name"
                    class="myInput"
                    style="width: 180px;margin-right: 20px"
                    clearable
                    placeholder="请输入姓名">
                  </el-input>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">回访项目</label>
                  <el-select v-model="listQuery.project" clearable style="width:60%" class="myInput">
                      <el-option v-for="item in projectSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
            </el-row>
            <el-row>
                <el-col :span="6">
                  <label class="el-form-item__label">回访人员</label>
                  <el-select v-model="listQuery.handleman" clearable style="width:60%" class="myInput">
                      <el-option v-for="item in userSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">回访状态</label>
                  <el-select v-model="listQuery.isfinish" clearable style="width:40%" class="myInput">
                      <el-option v-for="item in statusSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">回访类型</label>
                  <el-select v-model="listQuery.callbacktype" clearable style="width:40%" class="myInput">
                      <el-option v-for="item in typeSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
                <el-col :span="6">
                  <label class="el-form-item__label">回院状态</label>
                  <el-select v-model="listQuery.ishospital" clearable style="width:40%" class="myInput">
                      <el-option v-for="item in hospitalSelect" :key="item.id" :value="item.id" :label="item.name">
                      </el-option>
                  </el-select>
                </el-col>
            </el-row>
            <el-row>
              <el-col :span="6">
                  <el-checkbox style="margin-left20px;margin-top:15px;" v-model="listQuery.todaycallback">今天要回访</el-checkbox>
              </el-col>
              <el-col :span="6">
                <el-select v-model="searchname" clearable style="width: 200px" class="myInput" placeholder="中心">
                    <el-option v-for="item in centerSelect" :key="item.id" :value="item.id" :label="item.name">
                    </el-option>
                </el-select>
              </el-col>
               <el-col :span="6">
                  <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">查询</el-button>
               </el-col>
            </el-row>
          </el-card>
        </el-row>
        <!--<el-row style="margin-top: 20px;margin-left: 10px;">-->
            <!--<el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>-->
        <!--</el-row>-->
        <el-row style="margin-left: 15px;margin-right: 15px;margin-top: 20px">
          <el-table
            ref="multipleTable"
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <el-table-column type="index" label="序号"  width="50">
            </el-table-column>
            <el-table-column prop="begindate" label="日期" width="110">
            </el-table-column>
            <el-table-column prop="clientname" label="客户姓名" width="100">
            </el-table-column>
            <el-table-column prop="hftype" label="回访类型" width="100">
            </el-table-column>
            <el-table-column prop="handlemanname" label="回访人" width="90">
            </el-table-column>
            <el-table-column prop="hytype" label="是否回院" width="100">
            </el-table-column>
            <el-table-column prop="hospitaldate" label="回院日期" width="110">
            </el-table-column>
            <el-table-column prop="ordertype" label="开单方式" width="100">
            </el-table-column>
            <el-table-column prop="hfstatus" label="回访状态" width="100">
            </el-table-column>
            <el-table-column label="操作" fixed="right">
              <template slot-scope="scope">
                  <el-button type="text" size="small" v-if="scope.row.isfinish===0" @click="handleCallback(scope.row)">回访</el-button>
                  <el-button type="text" size="small" v-if="scope.row.ishospital===0" @click="handleHospital(scope.row)">回院</el-button>
                  <!--<el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>-->
                  <el-button type="text" size="small" @click="handleInfo(scope.row)">档案</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
          </el-table>
          <div class="pagination-container" style="margin-top: 5px" align="right">
                <el-pagination background
                               @current-change="handleCurrentChange"
                               :current-page="listQuery.page"
                               :page-size="listQuery.limit"
                               layout="total, prev, pager, next"
                               :total="total">
                </el-pagination>
          </div>
        </el-row>

        <!--回访信息-->
        <div>
          <el-dialog  title="回访信息" width="58%" :visible.sync="dialogFormVisible">
            <el-form  :model="callback" ref="dataForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:20px;'>
               <el-row>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                    <label class="el-form-item__label">哺乳方式</label>
                    <el-select v-model="callback.burufs" clearable style="width:60%" class="myInput">
                        <el-option v-for="item in burufsSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                      <label class="el-form-item__label">乳房情况</label>
                      <el-select v-model="callback.breast" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in breastSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                      <label class="el-form-item__label">乳汁情况</label>
                      <el-select v-model="callback.milk" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in milkSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                    <label class="el-form-item__label">乳头情况</label>
                    <el-select v-model="callback.rutou" clearable style="width:60%" class="myInput">
                        <el-option v-for="item in rutouSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                      <label class="el-form-item__label">恶露情况</label>
                      <el-select v-model="callback.elu" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in eluSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                    <label class="el-form-item__label">饮食情况</label>
                    <el-select v-model="callback.yinshi" clearable style="width:60%" class="myInput">
                        <el-option v-for="item in yinshiSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                      <label class="el-form-item__label">睡眠情况</label>
                      <el-select v-model="callback.sleep" clearable style="width:60%" class="myInput">
                        <el-option v-for="item in sleepSelect" :key="item.id" :value="item.id" :label="item.name">
                        </el-option>
                    </el-select>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='产康回访'">
                      <label class="el-form-item__label">伤口会阴</label>
                      <el-select v-model="callback.huiyin" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in huiyinSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                 </el-col>

                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='营养回访'">
                    <label class="el-form-item__label">年龄</label>
                    <el-input v-model="callback.age" style="width: 60%;" class="myInput"></el-input>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='营养回访'">
                      <label class="el-form-item__label">胎数</label>
                      <el-input v-model="callback.taishu" style="width: 60%;" class="myInput"></el-input>
                 </el-col>
                 <el-col :span="8"  style="margin-top: 10px" v-if="callback.hftype==='营养回访'">
                      <label class="el-form-item__label">孕前BMI</label>
                      <el-input v-model="callback.preBMI" style="width: 60%;" class="myInput"></el-input>
                 </el-col>
               </el-row>
               <el-row v-if="callback.hftype==='营养回访'">
                 <el-col :span="12" style="margin-top: 10px">
                      <label class="el-form-item__label">健康类型</label>
                      <el-select
                        multiple
                        value-key="id"
                        v-model="callback.healths" style="width: 80%" class="myInput">
                        <el-option v-for="item in healthlxSelect" :key="item.id" :label="item.name" :value="item.id">
                        </el-option>
                      </el-select>
                 </el-col>
                 <el-col :span="12" style="margin-top: 10px">
                      <label class="el-form-item__label">建议</label>
                      <el-select
                        multiple
                        value-key="id"
                        v-model="callback.guides" style="width: 80%" class="myInput">
                        <el-option v-for="item in guideSelect" :key="item.id" :label="item.name" :value="item.id">
                        </el-option>
                      </el-select>
                 </el-col>
               </el-row>
               <el-row v-if="callback.hftype==='营养回访'">
                  <el-col :span="8" style="margin-top: 10px">
                      <label class="el-form-item__label">诊断</label>
                      <el-select v-model="callback.diagnosis" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in diagnosisSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                 </el-col>
                 <el-col :span="8" style="margin-top: 10px">
                      <label class="el-form-item__label">执行情况</label>
                      <el-select v-model="callback.zhixing" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in executeSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                 </el-col>
                 <el-col :span="8" style="margin-top: 10px">
                      <label class="el-form-item__label">体重</label>
                      <el-input v-model="callback.weight" style="width: 60%;" class="myInput"></el-input>
                 </el-col>
               </el-row>
               <el-row style="margin-top: 10px;margin-bottom: 20px">
                <label class="el-form-item__label">备注</label>
                <el-input v-model="callback.comment" style="width: 80%;" class="myInput"></el-input>
             </el-row>
            </el-form>
             <el-row>
               <el-table
                  :data="historyList"
                  :header-cell-style="{background:'#F8F8F8'}"
                  stripe
                >
                  <el-table-column type="index" label="序号"  width="60">
                  </el-table-column>
                  <el-table-column prop="begindate" label="开始日期" width="100">
                  </el-table-column>
                  <el-table-column prop="enddate" label="结束日期" width="100">
                  </el-table-column>
                  <el-table-column prop="handledate" label="回访日期" width="100">
                  </el-table-column>
                  <!--<el-table-column prop="handlemanname" label="回访人" width="80">-->
                  <!--</el-table-column>-->
                  <el-table-column prop="execute" label="执行情况" width="100">
                  </el-table-column>
                  <el-table-column prop="weight" label="体重" width="60">
                  </el-table-column>
                  <el-table-column prop="comment" label="备注" width="100" show-overflow-tooltip>
                  </el-table-column>
                  <el-table-column label="操作" fixed="right" align="center">
                    <template slot-scope="scope">
                        <el-button type="text" size="small" @click="register_handleUpdate(scope.row)">修改</el-button>
                        <el-button type="text" size="small" @click="register_handleDelete(scope.row)">删除</el-button>
                    </template>
                  </el-table-column>
               </el-table>
             </el-row>
             <el-row style="margin-top: 10px;margin-left: 30px"  v-if="callback.hftype==='产康回访'">
               <el-col :span="12">
                  <label class="el-form-item__label">预约回访日期</label>
                  <el-date-picker
                    v-model="callback.nextbegindate"
                    style="width:50%;margin-left: 20px"
                    class="myInput"
                    type="date"
                    placeholder="日期开始"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
                <el-col :span="2">
                  <label class="el-form-item__label">到</label>
                </el-col>
                <el-col :span="10">
                  <el-date-picker
                    v-model="callback.nextenddate"
                    style="width:60%"
                    class="myInput"
                    type="date"
                    placeholder="日期结束"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
             </el-row>
             <el-row style="margin-top: 10px;margin-left: 30px">
               <el-col :span="12">
                  <label class="el-form-item__label">预约治疗日期</label>
                  <el-date-picker
                    v-model="callback.s_treat"
                    style="width:50%;margin-left: 20px"
                    class="myInput"
                    type="date"
                    placeholder="日期开始"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
                <el-col :span="2">
                  <label class="el-form-item__label">到</label>
                </el-col>
                <el-col :span="10">
                  <el-date-picker
                    v-model="callback.e_treat"
                    style="width:60%"
                    class="myInput"
                    type="date"
                    placeholder="日期结束"
                    value-format="yyyy-MM-dd">
                  </el-date-picker>
                </el-col>
             </el-row>
              <div slot="footer" class="dialog-footer">
                <el-select
                  v-model="callback.finish" clearable
                  style="width:150px;margin-right: 30px"
                  class="myInput">
                    <el-option v-for="item in finishSelect" :key="item.id" :value="item.id" :label="item.name">
                    </el-option>
                </el-select>
                <el-button
                  size="small"
                  @click="dialogFormVisible = false"
                  icon="el-icon-close"
                >关闭</el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogStatus=='create'"
                  @click="createData">保存
                </el-button>
                <el-button
                  size="small"
                  style="margin-right: 50px"
                  v-else
                  type="primary"
                  icon="el-icon-check"
                  @click="updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

        <!--回院信息-->
        <div>
          <el-dialog  title="回院信息" width="40%" :visible.sync="dialogHospitalVisible">
              <el-form  :model="callback" ref="hospitalForm" :rules="rules"  label-position="left" label-width="120px" style='width:90%; margin-left:20px;'>
                <el-row>
                 <el-col>
                    <el-form-item label="是否回院"  prop="ishospital">
                      <el-select v-model="callback.ishospital" clearable style="width:60%" class="myInput">
                          <el-option v-for="item in hospitalSelect" :key="item.id" :value="item.id" :label="item.name">
                          </el-option>
                      </el-select>
                    </el-form-item>
                 </el-col>
                </el-row>
                <el-row>
                 <el-col>
                    <el-form-item label="回院日期"  prop="hospitaldate">
                      <el-date-picker
                        v-model="callback.hospitaldate"
                        style="width:60%"
                        class="myInput"
                        type="date"
                        placeholder="回院日期"
                        value-format="yyyy-MM-dd">
                      </el-date-picker>
                    </el-form-item>
                 </el-col>
               </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  @click="dialogHospitalVisible = false"
                  icon="el-icon-close"
                >关闭</el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  @click="hospital_updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

        <!--员工档案-->
        <div>
          <el-dialog  title="员工档案" width="50%" :visible.sync="dialogArchiveVisible">
            <archive :client_id="clientid"></archive>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { depts } from '@/api/system'
import { callbacks, createCallback, updateCallback, deleteCallback } from '@/api/service'
import { getOrderSelectData } from '@/api/order'
import archive from '@/views/client/archives.vue'
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

export default {
  components: {
    ElInput,
    ElCheckbox,
    ElCheckboxGroup,
    ElRadioGroup,
    ElFormItem,
    ElSlPanel,
    ElTabPane,
    ElRow,
    ElCol,
    archive
  },
  data: function() {
    return {
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 10000,
        offset: 0,
        name: '',
        begindate: null,
        enddate: null,
        project: null,
        handleman: null,
        isfinish: null,
        callbacktype: null,
        ishospital: null,
        todaycallback: null,
        hrmdepartment_id: this.hrmdepartment_id,
        sort: '+id'
      },
      historyList: [],
      searchname: '',
      clientid: null,
      dialogArchiveVisible: false,
      hrmdepartment_id: 2,
      dialogFormVisible: false,
      dialogHospitalVisible: false,
      dialogStatus: '',
      deptName: '',
      clientTypeName: '',
      deptSelect: [],
      userSelect: [],
      projectSelect: [],
      statusSelect: [
        { id: 0, name: '未回访' },
        { id: 1, name: '已回访' }
      ],
      typeSelect: [
        { id: 0, name: '营养回访' },
        { id: 1, name: '心理回访' },
        { id: 2, name: '产康回访' }
      ],
      hospitalSelect: [
        { id: 0, name: '未回院' },
        { id: 1, name: '已回院' }
      ],
      healthlxSelect: [
        { id: 1, name: '正常' },
        { id: 2, name: '甲亢' },
        { id: 3, name: '甲减' },
        { id: 4, name: '妊娠糖尿病' },
        { id: 5, name: '缺铁性贫血' },
        { id: 6, name: '地中海贫血' },
        { id: 7, name: '巨幼红细胞性贫血' },
        { id: 8, name: '胎儿生长受限' },
        { id: 9, name: '高血压' },
        { id: 10, name: '子痫前期' },
        { id: 11, name: '其他' }
      ],
      diagnosisSelect: [
        { id: 1, name: '正常' },
        { id: 2, name: '体重增长过快' },
        { id: 3, name: '体重增长过慢' },
        { id: 4, name: '高体脂率' }
      ],
      centerSelect: [
        { id: 2, name: '綦江中心' },
        { id: 3, name: '永川中心' }
      ],
      guideSelect: [
        { id: 1, name: '普通饮食' },
        { id: 2, name: '糖尿病膳食' },
        { id: 3, name: '低脂膳食' },
        { id: 4, name: '低蛋白膳食' },
        { id: 5, name: '高蛋白膳食' },
        { id: 6, name: '低胆固醇膳食' },
        { id: 7, name: '低嘌呤膳食' },
        { id: 8, name: '钙磷代谢膳食' },
        { id: 9, name: '低价膳食' },
        { id: 10, name: '低盐、无盐膳食' },
        { id: 11, name: '流质饮食' },
        { id: 12, name: '半流质饮食' }
      ],
      executeSelect: [
        { id: 1, name: '好' },
        { id: 2, name: '一般' },
        { id: 3, name: '差' },
        { id: 4, name: '完全未执行' }
      ],
      finishSelect: [
        { id: 1, name: '完成随访' },
        { id: 0, name: '未完成随访' }
      ],
      burufsSelect: [
        { id: 1, name: '母乳' },
        { id: 2, name: '人工' },
        { id: 3, name: '混合' }
      ],
      sleepSelect: [
        { id: 1, name: '入睡快睡眠深沉无梦' },
        { id: 2, name: '入睡困难' },
        { id: 3, name: '易醒无梦' },
        { id: 4, name: '易醒多梦' }
      ],
      breastSelect: [
        { id: 1, name: '乳房肿胀' },
        { id: 2, name: '乳腺炎' }
      ],
      milkSelect: [
        { id: 1, name: '无奶' },
        { id: 2, name: '乳汁通畅' },
        { id: 3, name: '乳涨' },
        { id: 4, name: '乳涨并乳房肿块' }
      ],
      rutouSelect: [
        { id: 1, name: '乳头正常' },
        { id: 2, name: '乳头凹陷' },
        { id: 3, name: '乳头短平' },
        { id: 4, name: '乳头较大' },
        { id: 5, name: '乳头皲裂' }
      ],
      huiyinSelect: [
        { id: 1, name: '会阴无红肿' },
        { id: 2, name: '会阴红肿' },
        { id: 3, name: '敷料干燥(剖)' },
        { id: 4, name: '敷料有渗血(剖)' }
      ],
      eluSelect: [
        { id: 1, name: '干净' },
        { id: 2, name: '未干净' }
      ],
      yinshiSelect: [
        { id: 1, name: '禁食' },
        { id: 2, name: '流食' },
        { id: 3, name: '半流食' },
        { id: 4, name: '正常饮食' }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }]
      },
      callback: {
        id: null,
        age: null,
        taishu: null,
        preBMI: null,
        healthtype: null,
        healths: [],
        guide: null,
        guides: [],
        diagnosis: null,
        zhixing: null,
        weight: null,
        burufs: null,
        breast: null,
        milk: null,
        rutou: null,
        elu: null,
        yinshi: null,
        sleep: null,
        huiyin: null,
        hrmdepartment: null,
        nextbegindate: null,
        nextenddate: null,
        s_treat: null,
        e_treat: null,
        finish: null,
        treat_id: null,
        order_id: null,
        ishospital: null,
        hospitaldate: null,
        comment: '',
        action: ''
      }
    }
  },
  methods: {
    getCallbacks(data) {
      callbacks(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        console.log('list', this.list)
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getCallbackDetail(data) {
      this.historyList = []
      callbacks(data).then(response => {
        this.historyList = response.data.results
      })
    },
    getDepts(data) {
      depts(data).then(response => {
        this.deptSelect = response.data.results
      })
    },
    handleInfo(row) {
      this.clientid = row.client
      this.dialogArchiveVisible = true
      this.$nextTick(() => {
      })
    },
    resetCallback() {
      this.callback = {
        id: null,
        age: null,
        taishu: null,
        preBMI: null,
        healthtype: null,
        healths: [],
        guide: null,
        guides: [],
        diagnosis: null,
        zhixing: null,
        weight: null,
        burufs: null,
        breast: null,
        milk: null,
        rutou: null,
        elu: null,
        yinshi: null,
        sleep: null,
        huiyin: null,
        hrmdepartment: null,
        nextbegindate: null,
        nextenddate: null,
        s_treat: null,
        e_treat: null,
        finish: null,
        treat: null,
        order: null,
        ishospital: null,
        hospitaldate: null,
        comment: '',
        action: ''
      }
    },
    handleCallback(row) {
      this.resetCallback()
      const par = {
        hrmdepartment_id: this.hrmdepartment_id,
        order_id: row.order
      }
      this.callback = Object.assign({}, row)
      this.callback.action = 0 // 0为点击回访1为回院2修改
      if (row.healthtype !== null) {
        const health_type = row.healthtype.split(',')
        this.callback.healths = health_type.map(x => Number(x))
      }
      if (row.guide !== null) {
        const foodguide = row.guide.split(',')
        this.callback.guides = foodguide.map(x => Number(x))
      }
      this.getCallbackDetail(par)
      this.dialogFormVisible = true
      this.dialogStatus = 'update'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    handleHospital(row) {
      this.resetCallback()
      this.callback = Object.assign({}, row)
      this.callback.action = 1 // 0为点击回访1为回院2修改
      this.dialogHospitalVisible = true
      this.$nextTick(() => {
        this.$refs['hospitalForm'].clearValidate()
      })
    },
    handleCreate() {
      this.resetCallback()
      const par = { name: this.searchname}
      this.getDepts(par)
      this.historyList = []
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.callback.id = parseInt(Math.random() * 100) + 1024
          createCallback(this.callback).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getCallbacks(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      this.callback = Object.assign({}, row)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          console.log('callback', this.callback)
          const tempData = Object.assign({}, this.callback)
          if (tempData.healthtype !== null) {
            tempData.healthtype = tempData.healths.join(',')
          }
          if (tempData.guide !== null) {
            tempData.guide = tempData.guides.join(',')
          }
          updateCallback(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getCallbacks(this.listQuery)
          })
        }
      })
    },
    hospital_updateData() {
      this.$refs['hospitalForm'].validate((valid) => {
        if (valid) {
          console.log('callback', this.callback)
          const tempData = Object.assign({}, this.callback)
          updateCallback(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '设置回院成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getCallbacks(this.listQuery)
          })
        }
      })
    },
    handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.customer = Object.assign({}, row) // copy obj
        const tempData = Object.assign({}, this.customer)
        deleteCallback(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getCallbacks(this.listQuery)
        })
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getCallbacks(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getCallbacks(this.listQuery)
    },
    dateFormat: function(row, column) {
      var date = row[column.property]
      if (date === undefined) {
        return ''
      }
      return moment(date).format('YYYY-MM-DD HH:mm:ss')
    }
  },
  created: function() {
    this.listQuery.hrmdepartment_id = this.hrmdepartment_id
    this.getCallbacks(this.listQuery)
    const param = { hrmdepartment_id: this.hrmdepartment_id }
    getOrderSelectData(param).then(res => {
      this.userSelect = res.data.users
      this.projectSelect = res.data.projects
    })
  }
}
</script>

<style>
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
