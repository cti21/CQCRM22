<template>
    <div>
       <el-breadcrumb separator-class="el-icon-arrow-right" class="breadcrumb">
         <!--<el-breadcrumb-item><a href="/">首页</a></el-breadcrumb-item>-->
         <el-breadcrumb-item v-for="item in breadList" :key="item.path" :to="item.path">
           {{ item.meta.title }}
         </el-breadcrumb-item>
       </el-breadcrumb>
    </div>
</template>

<script>
export default {
  name: 'vbreadCrumb',
  data() {
    return {
      breadList: []
    }
  },
  watch: {
    $route() {
      this.getBreadcrumb()
    }
  },
  methods: {
    getBreadcrumb() {
      let matched = this.$route.matched.filter(item => item.name)
      const first = matched[0]
      // console.log('matched', matched)
      // console.log('first', first)
      if (matched.length === 1) {
        if (first.parent.meta !== 'undefined') {
          if (first.parent.meta.title === '医疗管理') {
            matched = [
              {
                path: '/permission',
                meta: {
                  title: '医疗管理'
                }
              }
            ].concat(matched)
          }
          if (first.parent.meta.title === '排班') {
            matched = [
              {
                path: '/schedule',
                meta: {
                  title: '排班'
                }
              }
            ].concat(matched)
          }
        }
      }
      this.breadList = matched
    }
  },
  created() {
    this.getBreadcrumb()
  }
}
</script>
