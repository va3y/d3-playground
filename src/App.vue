<template>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
  
  <Selector />
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import Selector from './components/Selector.vue'



export default {
  name: 'App',
  components: {
    HelloWorld,
    Selector
  },
  data() {
    return {
      loadData: {}
    }
  },
  mounted() {
    console.log("App loaded");
  },
  methods: {
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
