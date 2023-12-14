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

// stores/counter.js
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => {
    return { count: 0 }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    increment() {
      this.count++
    },
  },
})


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