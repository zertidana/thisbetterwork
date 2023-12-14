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

    <main class="container pt-4">
      <div id="app">
        <NavBar :isLoggedIn="isLoggedIn" />
        <router-view/>
        <div v-if="isLoggedIn">
          <!-- Display when user is logged in -->
          <p>You are logged in as {{ userInfo.username }} .</p>
        </div>
        <div v-else>
          <!-- Display when user is not logged in -->
          <p>You are not logged in.</p>
        </div>
      </div>
    </main>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, reactive, onMounted } from "vue";
  import { RouterView } from "vue-router";
  import NavBar from './pages/components/NavBar.vue';
  import axios from 'axios';
  
  export default defineComponent({
    components: {
      RouterView,
      NavBar
    },
    data() {
        return{
            sessionData: {},
        }
    },
    mounted() {
        this.fetchSessionData();
    },
    methods: {
        async fetchSessionData() {
            try {
                const response = await axios.get('/api/get_session_data/');
                this.sessionData = response.data;
            } catch (error) {
                console.error('Error fetching session data:', error);
            }
        },
    },
    setup() {
      const isLoggedIn = ref(false);
      
      const userInfo = reactive({
        username: '',
        email: '',
      });
  
      const checkLoginStatus = () => {
        fetch('http://127.0.0.1:8000/api/check_login_status', {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
            
            },
            credentials: 'include'
        })
        .then(response => response.json())
        .then(data => {
            console.log('Received login status:', data.loggedIn, 'User:', data.username);
            isLoggedIn.value = data.loggedIn;
            if (data.loggedIn) {
            userInfo.username = data.username;
            userInfo.email = data.email;
            }
            console.log('Updated state - isLoggedIn:', isLoggedIn.value, 'User:', userInfo.username);
        })
        .catch(error => {
            console.error('Error:', error);
        });
        };
  
      onMounted(() => {
        checkLoginStatus();
      });
  
      return { isLoggedIn, userInfo };
    },
  });
  </script>
  
  <style scoped>
  </style>
  