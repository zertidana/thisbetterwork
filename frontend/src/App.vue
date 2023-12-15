<template>
  <main class="container pt-4">
    <div id="app">
      <div v-if="userStore.username">
        <NavBar />
      </div>
      
      <router-view/>
    </div>
  </main>
</template>

<script lang="ts">

import { defineComponent } from "vue";
import { RouterView } from "vue-router";
import NavBar from './pages/components/NavBar.vue';
import { useUserStore } from "./stores/auth.ts";


export default defineComponent({
  components: {
    RouterView,
    NavBar
  },
  setup(){
          const userStore = useUserStore();
          return { userStore };
        }

  
});
</script>

<style scoped>
</style>
