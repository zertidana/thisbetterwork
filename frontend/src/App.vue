<template>
    <main class="container pt-4">
      <div id="app">
        <NavBar />
        <router-view/>
        <div >
          
        </div>
        <div >
        
        </div>
      </div>
    </main>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, reactive, onMounted } from "vue";
  import { RouterView } from "vue-router";
  import NavBar from './pages/components/NavBar.vue';

  
  export default defineComponent({
    components: {
      RouterView,
      NavBar
    },
    data() {
        return{
            
        }
    },
    mounted() {
        
    },
    methods: {
        
    },
    setup() {
      
    },
  });
  </script>
  
  <style scoped>
  </style>
  