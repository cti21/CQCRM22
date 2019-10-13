<template>
    <div>
        <el-row>
            <el-select v-model="searchname" clearable style="width: 200px" class="myInput" placeholder="中心">
                <el-option v-for="item in centerSelect" :key="item.id" :value="item.id" :label="item.name">
                </el-option>
            </el-select>
            <el-input
              v-model="searchClientname"
              class="myInput"
              style="width: 220px;margin-right: 20px"
              clearable
              @keyup.enter.native="handleFilter"
              suffix-icon="el-icon-search"
              placeholder="请输入名称">
            </el-input>
            <el-button size="small" type="primary"  @click="handleFilter" icon="el-icon-search">搜索</el-button>
            <el-button size="small" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
            <!--<el-button size="small" style="margin-left: 10px;" @click="toggleSelection([list[1],list[3]])" type="primary" icon="el-icon-plus">选中</el-button>-->
            <!--<el-button size="small" style="margin-left: 10px;" @click="toggleSelection()" type="primary" icon="el-icon-plus">取消</el-button>-->
        </el-row>
        <el-row style="margin:20px;">
          <el-table
            ref="multipleTable"
            :data="list"
            :header-cell-style="{background:'#F8F8F8'}"
            v-loading="listLoading"
            stripe
          >
            <!--<el-table-column  type="selection" width="55"></el-table-column>-->
            <el-table-column type="index" label="序号"  width="60">
            </el-table-column>
            <el-table-column prop="name" label="姓名" width="120">
            </el-table-column>
            <el-table-column prop="sex" label="性别" width="60">
            </el-table-column>
            <el-table-column prop="birthDate" label="出生日期" width="120">
            </el-table-column>
            <el-table-column prop="phone1" label="手机" width="120">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column label="操作" fixed="right" align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
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

        <!--客户档案新增、修改-->
        <div>
          <el-dialog  title="客户档案" width="58%" :visible.sync="dialogFormVisible">
                  <el-form  :model="customer" ref="dataForm" :rules="rules"  label-position="left" label-width="70px" style='width:90%; margin-left:60px;'>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="名称"  prop="name">
                              <el-input v-model="customer.name" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="性别"  prop="sex">
                              <el-select v-model="customer.sex" clearable style="width: 80%" class="myInput">
                                <el-option v-for="item in sexSelect" :key="item.id" :value="item.name" :label="item.name">
                                </el-option>
                              </el-select>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="出生日期"  prop="birthDate">
                              <el-date-picker
                                v-model="customer.birthDate"
                                style="width:80%"
                                class="myInput"
                                type="date"
                                placeholder="出生日期"
                                value-format="yyyy-MM-dd">
                              </el-date-picker>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="年龄">
                              <el-input v-model="age" readonly style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="手机"  prop="phone1">
                              <el-input v-model="customer.phone1" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                         <el-col :span="12">
                            <el-form-item label="家长手机"  prop="phone2">
                              <el-input v-model="customer.phone2" style="width: 80%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <el-row>
                         <el-col :span="12">
                            <el-form-item label="家庭住址"  prop="address">
                              <el-input v-model="customer.address" style="width: 90%;" class="myInput"></el-input>
                            </el-form-item>
                         </el-col>
                       </el-row>
                       <!--<el-row>-->
                         <!--<el-col>-->
                            <!--<el-form-item label="备注"  prop="comment">-->
                              <!--<el-input v-model="customer.comment" style="width: 90%;" class="myInput"></el-input>-->
                            <!--</el-form-item>-->
                         <!--</el-col>-->
                       <!--</el-row>-->
                       <el-row>
                     <el-button size="small" @click="register_handleCreate" type="primary" icon="el-icon-plus">新增</el-button>
                   </el-row>
                   <el-row>
                     <el-table
                        :data="registerList"
                        :header-cell-style="{background:'#F8F8F8'}"
                        stripe
                      >
                        <el-table-column type="index" label="序号"  width="60">
                        </el-table-column>
                        <el-table-column prop="registerdate" label="登记日期" width="120">
                        </el-table-column>
                        <el-table-column prop="clienttype" label="客户类型" width="100">
                        </el-table-column>
                        <el-table-column prop="registerdeptname" label="登记科室" width="100">
                        </el-table-column>
                        <el-table-column label="操作" fixed="right" align="center">
                          <template slot-scope="scope">
                              <el-button type="text" size="small" @click="register_handleUpdate(scope.row)">修改</el-button>
                              <el-button type="text" size="small" @click="register_handleDelete(scope.row)">删除</el-button>
                          </template>
                        </el-table-column>
                     </el-table>
                   </el-row>
                  </el-form>
                <div slot="footer" class="dialog-footer">
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
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="updateData">保存
                  </el-button>
                </div>
          </el-dialog>
        </div>

        <!--客户登记新增、修改-->
        <div>
           <el-dialog  title="客户登记" width="55%" :visible.sync="dialogRegisterVisible">
              <el-form :model="register" ref="registerForm" :rules="registerRules" label-position="left" style='width:90%; margin-left:50px;'>
                  <el-row>
                     <el-col :span="8">
                        <el-form-item label="登记科室" prop="dept">
                          <el-select v-model="register.dept" style="width: 60%" class="myInput" @change="deptChange">
                            <el-option v-for="item in deptSelect" :key="item.deptname" :label="item.deptname" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8">
                       <el-form-item label="客户类型" prop="client_type">
                          <el-select v-model="register.client_type" style="width: 60%" class="myInput" @change="clienttypeChange">
                            <el-option v-for="item in clienttypeSelect" :key="item.clienttype_name"
                                       :label="item.clienttype_name" :value="item.clienttype_id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8">
                       <el-form-item label="登记日期" prop="registerdate">
                          <el-date-picker
                            v-model="register.registerdate" type="date" value-format="yyyy-MM-dd"
                            format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'fenmiandate')">
                        <el-form-item label="分娩日期" prop="fenmiandate">
                          <el-date-picker v-model="register.fenmiandate" type="date" value-format="yyyy-MM-dd"
                                        format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'fenmiantype')">
                        <el-form-item label="分娩方式" prop="fenmiantype">
                          <el-select v-model="register.fenmiantype" style="width: 60%" class="myInput">
                            <el-option v-for="item in fenmianfsSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>

                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'burutype')">
                      <el-form-item label="哺乳方式" prop="burutype">
                        <el-select v-model="register.burutype" style="width: 60%" class="myInput">
                          <el-option v-for="item in burufsSelect" :key="item.name" :label="item.name" :value="item.id">
                          </el-option>
                        </el-select>
                      </el-form-item>
                    </el-col>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'weight')">
                        <el-form-item label="体重" prop="weight">
                          <el-input v-model="register.weight" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                    </el-col>

                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'shoushudate')">
                        <el-form-item label="手术日期" prop="shoushudate">
                          <el-date-picker v-model="register.shoushudate" type="date" value-format="yyyy-MM-dd"
                                        format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'shoushuype')">
                        <el-form-item label="手术方式" prop="shoushuype">
                          <el-select v-model="register.shoushuype" style="width: 60%" class="myInput" placeholder="分成类型">
                            <el-option v-for="item in shoushufsSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                         </el-form-item>
                     </el-col>

                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'lastyuejing')">
                        <el-form-item label="末次月经" prop="lastyuejing">
                          <el-date-picker v-model="register.lastyuejing" type="date" value-format="yyyy-MM-dd"
                                        format="yyyy-MM-dd" clearable style="width: 60%" class="myInput">
                          </el-date-picker>
                        </el-form-item>
                     </el-col>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'taishu')">
                        <el-form-item label="胎数" prop="taishu">
                          <el-select v-model="register.taishu" style="width: 60%" class="myInput" placeholder="分成类型">
                            <el-option v-for="item in taishuSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                         </el-form-item>
                     </el-col>

                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'height')">
                        <el-form-item label="身高" prop="height">
                          <el-input v-model="register.height" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'preweight')">
                        <el-form-item label="孕前体重" prop="preweight">
                          <el-input v-model="register.preweight" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>

                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'BMI')">
                        <el-form-item label="BMI" prop="BMI">
                          <el-input v-model="register.BMI" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>

                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'workqiangdu')">
                        <el-form-item label="工作强度" prop="workqiangdu">
                          <el-select v-model="register.workqiangdu" style="width: 60%" class="myInput">
                            <el-option v-for="item in workqdSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'sportttime')">
                       <el-form-item label="运动时间" prop="sportttime">
                          <el-select v-model="register.sportttime" style="width: 60%" class="myInput">
                            <el-option v-for="item in sportsjSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'frequency')">
                       <el-form-item label="运动频率" prop="frequency">
                          <el-select v-model="register.frequency" style="width: 60%" class="myInput">
                            <el-option v-for="item in sportplSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'yunci')">
                        <el-form-item label="孕次" prop="yunci">
                          <el-input v-model="register.yunci" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'chanci')">
                        <el-form-item label="产次" prop="chanci">
                          <el-input v-model="register.chanci" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'yunzhou')">
                        <el-form-item label="孕周" prop="yunzhou">
                          <el-input v-model="register.yunzhou" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'chanhouzhouqi')">
                        <el-form-item label="产后周期" prop="chanhouzhouqi">
                          <el-input v-model="register.chanhouzhouqi" style="width: 50%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'ganyutype')">
                        <el-form-item label="干预方式" prop="ganyutype">
                          <el-select v-model="register.ganyutype" style="width: 60%" class="myInput">
                            <el-option v-for="item in ganyufsSelect" :key="item.deptname" :label="item.deptname" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'sourcedept')">
                       <el-form-item label="科室来源" prop="sourcedept">
                          <el-select v-model="register.sourcedept" style="width: 60%" class="myInput">
                            <el-option v-for="item in deptlySelect" :key="item.name"
                                       :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                    <el-col :span="8" v-if="displayField(deptName,clientTypeName,'preBMI')">
                        <el-form-item label="孕前BMI" prop="preBMI">
                          <el-input v-model="register.preBMI" style="width: 60%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                     <el-col :span="8" v-if="displayField(deptName,clientTypeName,'sporttype')">
                        <el-form-item label="运动类型" prop="sporttype">
                          <el-select v-model="register.sporttype" style="width: 60%" class="myInput">
                            <el-option v-for="item in sportlxSelect" :key="item.name" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col v-if="displayField(deptName,clientTypeName,'healthtype')">
                        <el-form-item label="健康类型">
                          <el-select
                            multiple
                            value-key="id"
                            v-model="register.healths" style="width: 60%" class="myInput">
                            <el-option v-for="item in healthlxSelect" :key="item.id" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col v-if="displayField(deptName,clientTypeName,'jinjizheng')">
                        <el-form-item label="禁忌症" prop="jinjizheng">
                          <el-select multiple
                                     value-key="id"
                                     v-model="register.jinjizheng"
                                     style="width: 80%" class="myInput">
                            <el-option v-for="(item,index) in jinjizhengSelect" :key="item.id" :label="item.name" :value="item.id">
                            </el-option>
                          </el-select>
                        </el-form-item>
                     </el-col>
                  </el-row>
                  <el-row>
                    <el-col>
                        <el-form-item label="备注" prop="comment">
                          <el-input v-model="register.comment" style="width: 80%;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                  </el-row>

              </el-form>
              <div slot="footer" class="dialog-footer">
                  <el-button
                    size="small"
                    icon="el-icon-close"
                    @click="dialogRegisterVisible = false"
                  >关闭
                  </el-button>
                  <el-button
                    size="small"
                    type="primary"
                    icon="el-icon-check"
                    v-if="register_dialogStatus=='create'"
                    @click="register_createData">保存
                  </el-button>
                  <el-button
                    size="small"
                    v-else
                    type="primary"
                    icon="el-icon-check"
                    @click="register_updateData">保存
                  </el-button>
              </div>
           </el-dialog>
         </div>


    </div>
</template>

<script>
import { depts } from '@/api/system'
import { clients, createClient, updateClient, deleteClient, dept_client_types, jinjizhengs,
  client_registers, createClient_register, updateClient_register, deleteClient_register} from '@/api/client'
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
    ElCol
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
        sort: '+id'
      },
      registerList: [],
      searchname: '',
      searchClientname: '',
      dialogFormVisible: false,
      dialogRegisterVisible: false,
      dialogStatus: '',
      register_dialogStatus: '',
      deptName: '',
      clientTypeName: '',
      deptSelect: [],
      jinjizhengSelect: [],
      sexSelect: [
        { id: 1, name: '男' },
        { id: 2, name: '女' }
      ],
      taishuSelect: [
        { id: 1, name: '单胎' },
        { id: 2, name: '二胎' },
        { id: 1, name: '多胎' }
      ],
      shoushufsSelect: [
        { id: 1, name: '无痛人流' },
        { id: 2, name: '普通人流' },
        { id: 3, name: '剖宫' },
        { id: 4, name: '引产' }
      ],
      clienttypeSelect: [],
      fenmianfsSelect: [
        { id: 1, name: '顺' },
        { id: 2, name: '剖' }
      ],
      ganyufsSelect: [
        { id: 1, name: '沙盘' },
        { id: 2, name: '生物反馈训练' },
        { id: 3, name: '心理咨询' }
      ],
      deptlySelect: [],
      burufsSelect: [
        { id: 1, name: '母乳' },
        { id: 2, name: '人工' },
        { id: 3, name: '混合' }
      ],
      workqdSelect: [
        { id: 1, name: '无劳动' },
        { id: 2, name: '轻体力劳动' },
        { id: 3, name: '中体力劳动' },
        { id: 4, name: '重体力劳动' }
      ],
      sportlxSelect: [
        { id: 1, name: '无' },
        { id: 2, name: '散步' },
        { id: 3, name: '瑜伽' },
        { id: 4, name: '体操舞蹈' },
        { id: 5, name: '游泳' },
        { id: 6, name: '其他' }
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
      sportplSelect: [
        { id: 1, name: '不到2次/周' },
        { id: 2, name: '2-4次/周' },
        { id: 3, name: '4-6次/周' },
        { id: 4, name: '7次以上/周' }
      ],
      sportsjSelect: [
        { id: 1, name: '0min' },
        { id: 2, name: '0-15min' },
        { id: 3, name: '15-30min' },
        { id: 4, name: '30-45min' },
        { id: 4, name: '45min以上' }
      ],
      centerSelect: [
        { id: 2, name: '綦江中心' },
        { id: 3, name: '永川中心' }
      ],
      rules: {
        name: [{ required: true, message: '请输入名称', trigger: 'blur' }],
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }]
      },
      registerRules: {},
      customer: {
        id: null,
        name: '',
        sex: '',
        birthDate: null,
        phone1: '',
        phone2: '',
        address: '',
        hrmdepartment: null,
        username: '',
        comment: ''
      },
      register: {
        id: null,
        client_id: null,
        dept: null,
        client_type: '',
        registerdate: null,
        lastyuejing: null,
        taishu: null,
        height: '',
        preweight: '',
        weight: '',
        workqiangdu: '',
        sportttime: null,
        healthtype: '',
        yunci: '',
        chanci: '',
        preBMI: '',
        sporttype: '',
        frequency: '',
        fenmiandate: null,
        fenmiantype: '',
        burutype: null,
        yunzhou: '',
        chanhouzhouqi: '',
        ganyutype: '',
        sourcedept: '',
        jinjizheng: [],
        shoushudate: null,
        shoushuype: '',
        BMI: '',
        comment: ''
      }
    }
  },
  computed:{
    age() {
      let val = ''
      if ( this.customer.birthDate !== null) {
        const birthdays = new Date(this.customer.birthDate.replace(/-/g, '/'))
        const d = new Date()
        val =
          d.getFullYear() -
          birthdays.getFullYear() -
          (d.getMonth() < birthdays.getMonth() ||
          (d.getMonth() === birthdays.getMonth() &&
          d.getDate() < birthdays.getDate()) ? 1 : 0)
      }
      return val
    }
  },
  methods: {
    getClients(data) {
      clients(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getClient_registers(data) {
      client_registers(data).then(response => {
        this.registerList = response.data.results
      })
    },
    getDepts(data) {
      depts(data).then(response => {
        this.deptSelect = response.data.results
      })
    },
    displayField(sdept, sclienttype, sfield) {
      let arr = []
      let num = false
      if (sdept === '营养') {
        switch (sclienttype) {
          case '孕妇':
            arr = ['lastyuejing', 'yunci', 'chanci', 'taishu', 'height', 'preweight', 'preBMI',
              'workqiangdu', 'sporttype', 'sportttime', 'frequency', 'healthtype', 'comment']
            num = arr.some((item) => { return item === sfield  })
            break
          case '产妇':
            arr = ['fenmiandate', 'yunci', 'chanci', 'taishu', 'height', 'preweight', 'preBMI',
              'workqiangdu', 'sporttype', 'sportttime', 'frequency', 'healthtype', 'comment']
            num = arr.some((item) => { return item === sfield })
            break
          case '备孕':
            arr = ['yunci', 'chanci', 'height', 'weight', 'BMI', 'workqiangdu', 'sporttype', 'sportttime',
              'frequency', 'healthtype', 'comment']
            num = arr.some((item) => { return item === sfield })
            break
          case '婴幼儿':
            arr = ['height', 'preweight', 'sporttype', 'sportttime', 'frequency', 'healthtype', 'comment']
            num = arr.some((item) => { return item === sfield })
            break
          case '疾病人群':
            arr = ['height', 'weight', 'BMI', 'workqiangdu', 'sporttype', 'sportttime', 'frequency', 'healthtype', 'comment']
            num = arr.some((item) => { return item === sfield })
        }
      } else if (sdept === '产后门诊') {
        if (sclienttype === '产妇') {
          arr = ['fenmiandate', 'taishu', 'yunci', 'chanci', 'jinjizheng', 'fenmiantype', 'burutype', 'comment']
          num = arr.some((item) => { return item === sfield })
        }
      } else if (sdept === '人流室') {
        arr = ['shoushudate', 'shoushuype', 'comment']
        num = arr.some((item) => { return item === sfield })
      } else if (sdept === '中心') {
        arr = ['comment']
        num = arr.some((item) => { return item === sfield })
      } else if (sdept === '心理门诊') {
        console.log('sdept', sdept, 'sclienttype', sclienttype)
        arr = ['yunci', 'chanci', 'yunzhou', 'chanhouzhouqi', 'ganyutype', 'sourcedept', 'comment']
        num = arr.some((item) => { return item === sfield })
      }
      return num
    },
    deptChange(val) {
      let obj = {}
      obj = this.deptSelect.find(item => {
        return item.id === val
      })
      this.deptName = obj.deptname
      const par = { dept_id: val }
      this.clienttypeSelect = []
      dept_client_types(par).then(response => {
        this.clienttypeSelect = response.data.results
      })
    },
    clienttypeChange(val) {
      let obj = {}
      obj = this.clienttypeSelect.find(item => {
        return item.clienttype_id === val
      })
      this.clientTypeName = obj.clienttype_name
    },
    Dept_ClenttypeChange(sdept,sclienttype) {
      let obj = {}
      obj = this.deptSelect.find(item => {
        return item.id === sdept
      })
      this.deptName = obj.deptname
      const par = { dept_id: sdept }
      this.clienttypeSelect = []
      dept_client_types(par).then(response => {
        this.clienttypeSelect = response.data.results
        this.clienttypeChange(sclienttype)
      })
    },
    resetCustomer() {
      this.customer = {
        id: '',
        name: '',
        sex: '',
        birthDate: null,
        phone1: '',
        phone2: '',
        address: '',
        username: '',
        comment: ''
      }
    },
    resetRegister() {
      this.register = {
        id: null,
        client_id: null,
        dept: null,
        client_type: '',
        registerdate: null,
        lastyuejing: null,
        taishu: null,
        height: null,
        preweight: null,
        weight: null,
        workqiangdu: null,
        sportttime: null,
        healthtype: null,
        yunci: null,
        chanci: null,
        preBMI: null,
        sporttype: null,
        frequency: null,
        fenmiandate: null,
        fenmiantype: null,
        burutype: null,
        yunzhou: null,
        chanhouzhouqi: null,
        ganyutype: null,
        sourcedept: null,
        jinjizheng: [],
        healths: [],
        shoushudate: null,
        shoushuype: null,
        BMI: null,
        comment: ''
      }
    },
    handleReset() {
      this.listQuery.page = 1
      this.listQuery.name = ''
      this.searchname = ''
      this.getClients(this.listQuery)
    },
    handleCreate() {
      this.resetCustomer()
      const par = { name: this.searchname}
      this.getDepts(par)
      this.registerList = []
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      this.$refs.dataForm.validate((valid) => {
        if (valid) {
          this.customer.id = parseInt(Math.random() * 100) + 1024
          createClient(this.customer).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getClients(this.listQuery)
          })
        }
      })
    },
    handleUpdate(row) {
      const para = { name: this.searchname }
      this.getDepts(para)
      const par = { clientid: row.id }
      this.getClient_registers(par)
      this.customer = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.customer)
          updateClient(tempData).then(() => {
            this.dialogFormVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            this.listQuery.page = 1
            this.getClients(this.listQuery)
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
        deleteClient(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          this.listQuery.page = 1
          this.getClients(this.listQuery)
        })
      })
    },
    register_handleCreate() {
      this.resetRegister()
      if (this.customer.id === '') {
        this.$refs['dataForm'].validate((valid) => {
          if (valid) {
            createClient(this.customer).then((res) => {
              this.customer = res.data
              // ------------------------------
              this.dialogStatus = 'update'
              this.dialogRegisterVisible = true
              this.register_dialogStatus = 'create'
              this.$nextTick(() => {
                this.$refs['registerForm'].clearValidate()
              })
              // -------------------------------
              this.listQuery.page = 1
              this.getClients(this.listQuery)
            })
          }
        })
      } else {
        this.dialogRegisterVisible = true
        this.register_dialogStatus = 'create'
        this.$nextTick(() => {
          this.$refs['registerForm'].clearValidate()
        })
      }
    },
    register_createData() {
      this.displayField(this.deptName, this.clientTypeName, 'fenmiandate')
      // console.log('deptName', this.deptName, 'clientTypeName', this.clientTypeName)
      // console.log('displayField', this.displayField(this.deptName, this.clientTypeName, 'fenmiandate'))
      this.$refs.registerForm.validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.register)
          tempData.client_id = this.customer.id
          tempData.healthtype = tempData.healths.join(',')
          createClient_register(tempData).then(() => {
            this.dialogRegisterVisible = false
            this.$notify({
              title: '成功',
              message: '创建成功',
              type: 'success',
              duration: 2000
            })
            const par = { clientid: this.customer.id }
            this.getClient_registers(par)
          })
        }
      })
    },
    register_handleUpdate(row) {
      this.register = Object.assign({}, row)
      const myjinjizhengs = row.jinjizheng
      if (row.healthtype !== null) {
        const health_type = row.healthtype.split(',')
        this.register.healths = health_type.map(x => Number(x))
      }
      this.register.jinjizheng = []
      this.register.jinjizheng = myjinjizhengs.map(v => v.jinjizheng_id)
      this.register_dialogStatus = 'update'
      this.dialogRegisterVisible = true
      this.$nextTick(() => {
        this.$refs['registerForm'].clearValidate()
        this.Dept_ClenttypeChange(row.dept, row.client_type)
      })
    },
    register_updateData() {
      this.$refs['registerForm'].validate((valid) => {
        if (valid) {
          const tempData = Object.assign({}, this.register)
          console.log('tempData', tempData)
          updateClient_register(tempData).then(() => {
            this.dialogRegisterVisible = false
            this.$notify({
              title: '成功',
              message: '更新成功',
              type: 'success',
              duration: 2000
            })
            const par = { clientid: this.customer.id }
            this.getClient_registers(par)
          })
        }
      })
    },
    register_handleDelete(row) {
      this.$confirm('确认删除该记录吗?', '提示', {
        type: 'warning'
      }).then(() => {
        this.register = Object.assign({}, row)
        const tempData = Object.assign({}, this.register)
        deleteClient_register(tempData).then(() => {
          this.$notify({
            title: '成功',
            message: '删除成功',
            type: 'success',
            duration: 2000
          })
          const par = { clientid: this.customer.id }
          this.getClient_registers(par)
        })
      })
    },
    toggleSelection(rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row);
        });
      } else {
        this.$refs.multipleTable.clearSelection();
      }
    },
    handleFilter() {
      this.listQuery.page = 1
      this.listQuery.name = this.searchname
      this.getClients(this.listQuery)
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.listQuery.offset = (val - 1) * this.listQuery.limit
      this.getClients(this.listQuery)
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
    jinjizhengs(this.listQuery).then(response => {
      this.jinjizhengSelect = []
      this.jinjizhengSelect = response.data.results
    })
    this.listQuery.page = 1
    this.listQuery.name = ''
    this.getClients(this.listQuery)
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
