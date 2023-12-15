<template>
    <div class="container mt-5">
      <form @submit.prevent="submit()" class="border p-4 bg-light">
        <h2 class="mb-4 text-center">Sign Up!</h2>
  
        <!-- Username Field -->
        <div class="form-group mb-3">
          <label for="usernameInput" class="form-label">Username</label>
          <input type="text" v-model="username" class="form-control" id="usernameInput" placeholder="Enter username" required>
        </div>
  
        <!-- Password Field -->
        <div class="form-group mb-4">
          <label for="passwordInput" class="form-label">Password</label>
          <input type="password" v-model="password" class="form-control" id="passwordInput" placeholder="Password" required>
        </div>

        <div class="form-group mb-4">
          <label for="passwordInput2" class="form-label">Confirm Password</label>
          <input type="password" v-model="password2" class="form-control" id="passwordInput2" placeholder="Password" required>
        </div>
        <div v-if="passwordError" class="alert alert-danger">
            Passwords do not match.
        </div>
        <div v-if="userExistsError" class="alert alert-danger">
            Username already exists.
        </div>
        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary w-100">Submit</button>
      </form>
    </div>
  </template>
  
  
  <script lang="ts">
      import { defineComponent } from "vue";
      import router from '../router/index'
      import { useUserStore } from '../../stores/auth';


      export default defineComponent({
          data() {
              return {
                  username: '',
                  password: '',
                  password2: '',
                  token: '',
                  passwordError: false,
                  userExistsError: false,
              }
          },
          methods: {
            async submit() {
                this.passwordError = false;
                this.userExistsError = false;

                if (this.password != this.password2) {
                    this.passwordError = true;
                    return;
                }

              console.log(this.password)
              console.log(this.username)
              const requestOptions = {
                method: "POST",
                headers: {
                  "Content-type": "application/json",
                },
                body: JSON.stringify({ "username": this.username, "password": this.password })
              }
  
              const response = await fetch('http://127.0.0.1:8000/accounts/signup', requestOptions)
              const requestOptions2 = {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({ "username": this.username, "password": this.password})
                }

                if (response.status === 400) { 
                    this.userExistsError = true;
                    return;
                }


                const signup = await fetch('http://127.0.0.1:8000/accounts/login', requestOptions2)
                var data = await signup.json() 
                const userStore = useUserStore();
                
                if (response.ok) {
                    userStore.login(data.user.username, data.token);
                    
                } else {
                    
                }

                this.token = data.token // Global store this
                router.push({ path: '/MainPage'})
            },
  
          },
      })
  </script>
  
  <style scoped>
  </style>
  