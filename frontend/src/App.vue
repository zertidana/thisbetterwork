<template>
  <main class="container pt-4">
    <div id="app">
      <NavBar :loggedIn="sessionData.user_id !== null" />
      <router-view />
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent, reactive, onMounted } from "vue";
import { RouterView } from "vue-router";
import NavBar from './pages/components/NavBar.vue';

export default defineComponent({
  components: {
    RouterView,
    NavBar
  },
  setup() {
    // Define a reactive property to store session data
    const sessionData = reactive({
      user_id: null,
      // Add other session data properties here
    });

    // Fetch session data on component mount
    onMounted(async () => {
      try {
        const response = await fetch("/api/get_session_data");
        const data = await response.json();

        // Update sessionData with the received data
        Object.assign(sessionData, data);
      } catch (error) {
        console.error("Error fetching session data:", error);
      }
    });

    return {
      sessionData,
    };
  },
});
</script>