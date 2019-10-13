<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>
<style>
  @import "../static/css/main.css";
  @import "../static/css/paiban.css";   /*浅绿色主题*/
  @import "../static/css/theme-green/color-green.css";   /*浅绿色主题*/
  body .el-table th.gutter{
      display: table-cell!important;
  }
</style>

