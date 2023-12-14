<template>
  <div>
    <!-- Content shown to logged-in users -->
    <div v-if="isLoggedIn">
      Welcome, {{ username }}!
    </div>
    <!-- Content shown to guests -->
    <div v-else>
      Please log in.
    </div>
  </div>
</template>

<script lang="ts">

export default {
    data() {
        return {
        isLoggedIn: false,
        username: ''
        }
    },
    mounted() {
        this.checkLoginStatus();
    },
    methods: {
        async checkLoginStatus(){
        let response = await fetch("http://127.0.0.1:8000/api/check_login_status/")
        let data = await response.json()
        this.isLoggedIn = data.LoggedIn
        }



    // async checkLoginStatus() {
    //   await fetch('/api/check_login_status')
    //   .then(data =>{
    //     console.log(data)
    //   })
      // const data = await response.json();
      // console.log(response);
      // this.isLoggedIn = data.LoggedIn;
      // this.username = data.username; // Set username if logged in
      
    }
  }

</script>

<style scoped>

</style>