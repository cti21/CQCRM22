<template>
    <div class="wrapper">
        <v-head></v-head>
        <my-sidebar></my-sidebar>
        <div class="content">
            <transition name="move" mode="out-in">
              <router-view></router-view>
            </transition>
        </div>
    </div>
</template>

<script>
    import vHead from './Header.vue'
    import mySidebar from './mySidebar.vue'
    import store from '@/store'
    export default {
      components: {
        vHead, mySidebar
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
