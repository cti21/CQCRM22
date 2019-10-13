<template>
    <div class="wrapper">
      <el-container >
        <el-aside style="width: 200px">
          <v-sidebar :routes="routes"></v-sidebar>
        </el-aside>
        <el-container>
          <el-header style="padding: 0px">
            <v-head></v-head>
          </el-header>
          <el-main>
            <div class="content">
                <v-bread-crumb style="margin-bottom: 20px;"></v-bread-crumb>
                <transition name="move" mode="out-in">
                  <router-view></router-view>
                </transition>
            </div>
          </el-main>
        </el-container>
      </el-container>
    </div>
</template>

<script>
    import vHead from './Header.vue'
    import vSidebar from './Sidebar.vue'
    import vBreadCrumb from './BreadCrumb.vue'
    import store from '@/store'
    export default {
      components: {
        vHead, vSidebar, vBreadCrumb
      },
      computed: {
        routes() {
          // let c = store.getters.routers
          return store.getters.routers
          // return this.$router.options.routes
        }
      }
    }
</script>
<style>
  div .content {
    left: 200px;
  }
</style>
