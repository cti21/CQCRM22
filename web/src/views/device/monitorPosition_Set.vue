<template>
    <div>
        <div style="float: right;margin-right: 40px">
            <el-button
              size="small"
              type="primary"
              icon="el-icon-plus"
              @click="handleCreate"
            >新增
            </el-button>
        </div>
        <div>
          <el-select
            v-model="devicetype"
            clearable
            style="width: 280px"
            class="myInput"
            @change="handleChange"
            placeholder="请选择设备类型">
              <el-option label="透析机" value="0" >
              </el-option>
              <el-option label="水处理" value="1" >
              </el-option>
              <el-option label="浓缩液" value="2" >
              </el-option>
          </el-select>
        </div>
        <el-table
          :data="list"
          v-loading="listLoading"
          :header-cell-style="{background:'#F8F8F8'}"
          stripe
          @row-click="rowClick">
            <el-table-column type="index" label="序号"  width="200" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false">
            </el-table-column>
            <el-table-column prop="position" label="检查位置" width="300" align="center">
            </el-table-column>
            <el-table-column  label="操作"  align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete(scope.row)">删除</el-button>
              </template>
            </el-table-column>
        </el-table>
        <div style="margin-top: 10px">
            <label style="float: left">监测点</label>
            <el-button
              size="small"
              style="float: right;margin-right: 40px"
              type="primary"
              icon="el-icon-plus"
              @click="handleCreate_mpd"
            >新增
            </el-button>
        </div>
        <el-table
          :data="mpd_list"
          :header-cell-style="{background:'#F8F8F8'}"
          stripe
          style="margin-bottom: 20px;">
            <el-table-column type="index" label="序号"  width="200" align="center">
            </el-table-column>
            <el-table-column prop="id" v-if="false" width="160">
            </el-table-column>
            <el-table-column prop="specific" label="监测点" width="300" align="center">
            </el-table-column>
            <el-table-column  label="操作"  align="center">
              <template slot-scope="scope">
                  <el-button type="text" size="small" @click="handleUpdate_mpd(scope.row)">修改</el-button>
                  <el-button type="text" size="small" @click="handleDelete_mpd(scope.row)">删除</el-button>
              </template>
            </el-table-column>
        </el-table>

        <div>
          <el-dialog  title="监测位置" width="35%" :visible.sync="dialogFormVisible" append-to-body>
              <el-form  :model="mp" ref="dataForm" label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
                   <el-row>
                     <el-col>
                        <el-form-item label="名称"  prop="position">
                          <el-input v-model="mp.position" style="width: 350px;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  icon="el-icon-close"
                  @click="dialogFormVisible = false"
                >关闭
                </el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogStatus=='create'"
                  @click="createData">保存
                </el-button>
                <el-button
                  size="small"
                  icon="el-icon-check"
                  v-else type="primary"
                  @click="updateData">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

        <div>
          <el-dialog  title="监测点" width="35%" :visible.sync="dialogDetailVisible" append-to-body>
              <el-form  :model="mpd" ref="detailForm" label-position="left" label-width="70px" style='width:90%; margin-left:30px;'>
                   <el-row>
                     <el-col>
                        <el-form-item label="名称"  prop="position">
                          <el-input v-model="mpd.specific" style="width: 350px;" class="myInput"></el-input>
                        </el-form-item>
                     </el-col>
                   </el-row>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button
                  size="small"
                  icon="el-icon-close"
                  @click="dialogDetailVisible = false"
                >关闭
                </el-button>
                <el-button
                  size="small"
                  type="primary"
                  icon="el-icon-check"
                  v-if="dialogDetailStatus=='create'"
                  @click="createData_mpd">保存
                </el-button>
                <el-button
                  size="small"
                  icon="el-icon-check"
                  v-else type="primary"
                  @click="updateData_mpd">保存
                </el-button>
              </div>
          </el-dialog>
        </div>

    </div>
</template>

<script>
import { mps, mpds, createmps, updatemps, deletemps, creatempds, updatempds, deletempds } from '@/api/device'
export default {
  props: ['clickcount'],
  data() {
    return {
      count: 0,
      list: [],
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 5,
        offset: 0,
        type: 100,
        sort: '+id'
      },
      detailid: null,
      mp: {
        id: null,
        type: null,
        position: null
      },
      mpd: {
        id: null,
        specific: null,
        mp: null
      },
      dialogFormVisible: false,
      dialogStatus: '',
      dialogDetailVisible: false,
      dialogDetailStatus: '',
      mpd_list: [],
      mpd_total: null,
      devicetype: ''
    }
  },
  methods: {
    getMonitorPosition(data) {
      this.list = []
      this.mpd_list = []
      mps(data).then(response => {
        this.listLoading = true
        this.list = response.data.results
        this.total = response.data.count
        this.listLoading = false
      })
    },
    getMpdList(data) {
      mpds(data).then(response => {
        this.mpd_list = response.data.results
        this.mpd_total = response.data.count
      })
    },
    handleCreate() {
      this.dialogFormVisible = true
      this.dialogStatus = 'create'
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    createData() {
      if (this.devicetype !== '' ) {
        this.mp.id = parseInt(Math.random() * 100) + 1024 // mock a id
        this.mp.type = this.devicetype
        createmps(this.mp).then(() => {
          this.getMonitorPosition(this.listQuery)
          this.$notify({
            title: '提示',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogFormVisible = false
        })
      }
    },
    handleUpdate(row) {
      this.mp = Object.assign({}, row) // copy obj
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    updateData() {
      updatemps(this.mp).then(() => {
        this.getMonitorPosition(this.listQuery)
        this.$notify({
          title: '提示',
          message: '保存成功',
          type: 'success',
          duration: 2000
        })
        this.dialogFormVisible = false
      })
    },
    handleDelete(row) {
      this.mp = Object.assign({}, row) // copy obj
      const tempData = Object.assign({}, this.mp)
      deletemps(tempData).then(() => {
        this.getMonitorPosition(this.listQuery)
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    handleCreate_mpd() {
      this.dialogDetailVisible = true
      this.dialogDetailStatus = 'create'
      this.$nextTick(() => {
        this.$refs['detailForm'].clearValidate()
      })
    },
    createData_mpd() {
      if (this.mpd.specific !== '') {
        this.mpd.id = parseInt(Math.random() * 100) + 1024 // mock a id
        this.mpd.mp = this.detailid
        creatempds(this.mpd).then(() => {
          const params = {
            id: this.detailid
          }
          this.getMpdList(params)
          this.$notify({
            title: '提示',
            message: '新增成功',
            type: 'success',
            duration: 2000
          })
          this.dialogDetailVisible = false
        })
      }
    },
    handleUpdate_mpd(row) {
      this.mpd = Object.assign({}, row) // copy obj
      this.dialogDetailStatus = 'update'
      this.dialogDetailVisible = true
      this.$nextTick(() => {
        this.$refs['detailForm'].clearValidate()
      })
    },
    updateData_mpd() {
      updatempds(this.mpd).then(() => {
        const params = {
          id: this.detailid
        }
        this.getMpdList(params)
        this.$notify({
          title: '提示',
          message: '保存成功',
          type: 'success',
          duration: 2000
        })
        this.dialogDetailVisible = false
      })
    },
    handleDelete_mpd(row) {
      this.mpd = Object.assign({}, row) // copy obj
      const tempData = Object.assign({}, this.mpd)
      deletempds(tempData).then(() => {
        const params = {
          id: this.detailid
        }
        this.getMpdList(params)
        this.$notify({
          title: '成功',
          message: '删除成功',
          type: 'success',
          duration: 2000
        })
      })
    },
    handleChange(val) {
      this.listQuery.type = val
      this.getMonitorPosition(this.listQuery)
    },
    rowClick(row, event, column) {
      this.detailid = row.id
      const params = {
        id: row.id
      }
      this.getMpdList(params)
    }
  },
  watch: {
    clickcount: function() {
      this.getMonitorPosition(this.listQuery)
    }
  },
  created: function() {
    this.getMonitorPosition(this.listQuery)
  }
}
</script>
