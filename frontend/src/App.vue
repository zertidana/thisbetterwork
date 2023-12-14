<template>
  <main class="container pt-4">
    <div id="app">
      <NavBar/>
      <router-view />
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent,} from "vue";
import { RouterView } from "vue-router";
import NavBar from './pages/components/NavBar.vue';


//import { defineStore } from 'pinia'



export default defineComponent({
  components: {
    RouterView,
    NavBar
  },
  mounted(){
    
  },
  data(){
    return{
      
    }
  },
  methods:{

  }

});
</script>