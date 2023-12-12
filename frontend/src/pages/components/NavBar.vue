<template>
  <nav class="navbar">
    <ul>
      <li><router-link to="/App.vue">Home</router-link></li>
            <li><router-link
                class=""
                :to="{name: 'Main Page'}"
            >
                Home
            </router-link></li>
            
            <li><router-link
                class=""
                :to="{name: 'Sports Page'}"
            >
                Sports
            </router-link></li>
            <li style="float:right"><a class="active" href="http://127.0.0.1:8000/accounts/login/"> Login</a></li>
            <li style="float:right"><a class="active" href="http://127.0.0.1:8000/accounts/signup/"> Sign Up</a></li>
    </ul>
  </nav>
</template>

<script lang="ts">

</script>

<style scoped>
ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #333;
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 0;
}

li {
  display: inline;
  float: left;
  border-right: 1px solid #bbb;
}

a {
  display: block;
  padding: 8px;
  background-color: #dddddd;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

/* Change the link color to #111 (black) on hover */
li a:hover {
  background-color: #111;
}

.active {
  background-color: #04AA6D;
}



</style>

