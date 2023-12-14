<template>
  <main class="container pt-4">
    <div id="app">
      <NavBar />
      <router-view />
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
});
</script>

<style scoped>
/* Your component styles */
</style>