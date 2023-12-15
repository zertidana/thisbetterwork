<template>
    <div class="container mt-5">
      <form @submit.prevent="login()" class="border p-4 bg-light">
        <h2 class="mb-4 text-center">Log In!</h2>
  
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

        <!-- Submit Button -->
        <button type="submit" class="btn btn-primary w-100">Submit</button>
      </form>
    </div>
  </template>

<script lang="ts">
    import { defineComponent } from "vue";

    export default defineComponent({
        data() {
            return {
                username: '',
                password: '',
                token: ''
            }
        },
        methods: {
          async login() {
            const requestOptions = {
              method: "POST",
              headers: {
                "Content-type": "application/json",
              },
              body: JSON.stringify({ "username": this.username, "password": this.password})
            }

            const signup = await fetch('http://127.0.0.1:8000/accounts/login', requestOptions)
            var data = await signup.json() 
            this.token = data.token // Global store this
          },
        },
    })
</script>

<style scoped>
</style>
