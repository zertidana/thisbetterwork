<template>
  <form onsubmit="return false">
    <div class="form-group">
      <label for="exampleInputEmail1">Username</label>
      <input type="text" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter username">
    </div>

    <div class="form-group">
      <label for="exampleInputPassword1">Password</label>
      <input type="password" v-model="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
    </div>
    <button @click="login()"  class="btn btn-primary">Submit</button>
  </form>

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
