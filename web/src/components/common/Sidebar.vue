<template>
    <div class="sidebar">
       <el-scrollbar style="height: 100%;background: rgb(48,65,86)">
        <div style="width: 200px;height:70px;background: burlywood;">
          <div style="font-size:24px;color: white;padding: 20px 50px;">首泰医疗</div>
        </div>
        <el-menu
          :default-active="onRoutes"
          class="el-menu-vertical"
          style="background: rgb(48,65,86);margin-top: 20px;"
          :unique-opened="true"
          router
        >
              <template v-for="item in routes" v-if="!item.hidden&&item.children">
                <template v-if="item.children">
                    <el-submenu :index="item.path" style="background: rgb(48,65,86)">
                        <template slot="title">
                          <div style="color: white">
                            <svg-icon :icon-class="item.meta.icon" style="margin-right: 20px"/>
                            {{ item.meta.title }}
                          </div>
                        </template>
                          <el-menu-item-group style="background: rgb(48,65,86)">
                              <el-menu-item v-for="(subItem,i) in item.children" :key="i" :index="subItem.path">
                                {{ subItem.meta.title}}
                              </el-menu-item>
                          </el-menu-item-group>
                    </el-submenu>
                </template>
                <template v-else>
                  <router-link :to="item.path">{{ item.meta.title}}</router-link>
                </template>
            </template>
        </el-menu>
       </el-scrollbar>
    </div>
</template>

<script>
export default {
  name: 'vSidebar',
  props: {
    routes: {
      type: Array
    },
    isNest: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    onRoutes() {
      return this.$route.path.replace('/aaa', '')
    }
  }
}
</script>

<style>
    .sidebar{
        display: block;
        position: absolute;
        width: 200px;
        left: 0;
        top: 0px;
        bottom:0;
    }
    .sidebar > ul {
        height:100%;
    }
    .el-submenu .el-menu-item {
        height: 40px;
        line-height: 40px;
        padding: 0 20px;
        color: white;
        min-width: 200px;
    }
    .el-scrollbar__wrap {
       overflow: scroll;
       overflow-x:auto;
       overflow-y:auto;
    }
    .el-menu-item:hover{
        outline: 0 !important;
        color: white !important;
        background: #409EFF !important;
    }
    .el-menu-item.is-active {
        color: white !important;
        background: black !important;
    }
    .aa.el-submenu__title:focus, .el-submenu__title:hover{
        outline: 0 !important;
        color: white !important;
        background: #409EFF !important;
    }
    .el-submenu>.el-submenu__title .el-submenu__icon-arrow{
      -webkit-transform: rotateZ(-90deg);
      -ms-transform: rotate(-90deg);
      transform: rotateZ(-90deg);
      margin-right: 25px;
    }
    .el-submenu.is-opened>.el-submenu__title .el-submenu__icon-arrow{
      -webkit-transform: rotateZ(0deg);
      -ms-transform: rotate(0deg);
      transform: rotateZ(0deg);
      margin-right: 25px;
    }
</style>
