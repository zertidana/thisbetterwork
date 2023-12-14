<template>
  <main class="container pt-4">
    <div id="app">
      <NavBar/>
      <router-view />
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useAuthStore } from "@/stores/auth"; // Assuming you have a store folder with an auth.ts file
import NavBar from './pages/components/NavBar.vue';

export default defineComponent({
  components: {
    NavBar
  },
  setup() {
    const authStore = useAuthStore();

    // Check if the user is authenticated, and if not, authenticate
    if (!authStore.isAuthenticated) {
      authenticateUser();
    }

    return {};
  }
});

async function authenticateUser() {
  try {
    // Make a Fetch API call to authenticate the user and get the token
    const response = await fetch('http://127.0.0.1:8000/api/authenticate/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        // You may need to include additional headers here, like credentials or others
      },
      body: JSON.stringify({
        // Include any authentication data you need here
      }),
    });

    if (!response.ok) {
      throw new Error('Authentication failed');
    }

    const data = await response.json();

    // Assuming your Pinia store has a mutation to set the token
    useAuthStore().setAuthToken(data.token);
  } catch (error) {
    console.error('Authentication error:', error);
  }
}
</script>
