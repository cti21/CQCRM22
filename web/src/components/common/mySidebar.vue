<template>
    <div class="sidebar">
        <el-menu  default-active="2"  class="el-menu-vertical-demo"  @open="handleOpen"  @close="handleClose" router>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>统计分析</span>
            </template>
            <div style="margin-left: 100px"><i class="el-icon-location"></i></div>
            <el-menu-item index="/countTxTypeByYear">透析方式按年分析</el-menu-item>
            <el-menu-item index="/countTxTypeBymonth">透析方式按月分析</el-menu-item>
            <el-menu-item index="/deviceByYear">透析器按年分析</el-menu-item>
            <el-menu-item index="/deviceBymonth">透析器按月分析</el-menu-item>
            <el-menu-item index="/operateByYear">手术分析</el-menu-item>
            <el-menu-item index="/analyseBykind">分类分析</el-menu-item>
            <el-menu-item index="/analyseFirstTx">首次透析分析</el-menu-item>
            <el-menu-item index="/analyseBfzBymonth">并发症分析</el-menu-item>
            <el-menu-item index="/analyseBloodPressure">血压异常分析</el-menu-item>
            <el-menu-item index="/analyseByYuanfa">原发病分析</el-menu-item>
            <el-menu-item index="/analyseZhuangui">转归分析</el-menu-item>
            <el-menu-item index="/analyseZhengzhuang">症状分析</el-menu-item>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>药品耗材分析</span>
            </template>
            <el-menu-item index="/analyseDrugByyear">药品使用量分析</el-menu-item>
            <el-menu-item index="/analyseMaterialByyear">耗材使用量分析</el-menu-item>
            <el-menu-item index="/analysedrug">药品明细汇总</el-menu-item>
            <el-menu-item index="/analysematerial">耗材明细汇总</el-menu-item>
            <el-menu-item index="/analyseDrugstock">药品出入库分析</el-menu-item>
            <el-menu-item index="/analyseMaterialstock">耗材出入库分析</el-menu-item>
            <el-menu-item index="/analyseDeptCharge">科室收费分析</el-menu-item>
            <el-menu-item index="/deptChargeBymonth">科室收费按月分析</el-menu-item>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-document"></i>
              <span>检验分析</span>
            </template>
            <el-menu-item index="/analysePTH">甲状旁腺分析</el-menu-item>
            <el-menu-item index="/analyseCaP">钙磷乘积分析</el-menu-item>
            <el-menu-item index="/AlarmLab">检验预警分析</el-menu-item>
          </el-submenu>
        </el-menu>
    </div>
</template>

<script>
export default {
  name: 'mySidebar',
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
}
</script>

<style scoped>
    .sidebar{
        display: block;
        position: absolute;
        width: 250px;
        left: 0;
        top: 70px;
        bottom:0;
        background: #2E363F;
    }
    .sidebar > ul {
        height:100%;
    }
    .el-submenu .el-menu-item {
        height: 30px;
        line-height: 30px;
        padding: 0 45px;
        min-width: 200px;
    }
</style>
