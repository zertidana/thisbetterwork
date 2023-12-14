<template>
  <nav class="navbar">
    <ul>
      <li><router-link to="/App.vue">Home</router-link></li>

            
            <li class="dropdown"><router-link
                class="dropbtn"
                :to="{name: 'All Categories'}"
            >
                All Categories
            </router-link>
                <div class="dropdown-content">
                    <router-link to="/SportsPage.vue">Sports</router-link>
                    <router-link to="/FashionPage.vue">Fashion</router-link>
                    <router-link to="/EducationPage.vue">Education</router-link>
                    <router-link to="/ArtPage.vue">Art</router-link>
                    <router-link to="/WorldPage.vue">World News</router-link>
                    <router-link to="/FinancePage.vue">Finance</router-link>
                </div></li>

            <li style="float:right"><a class="active" href="http://127.0.0.1:8000/accounts/logout/"> Logout</a></li>
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
  position: sticky;
  top: 0;
}

li {
  display: inline;
  float: left;
  border-right: 1px solid #bbb;
}
/*
a {
  display: block;
  padding: 8px;
  background-color: #dddddd;
}
*/
li a:hover, .dropdown:hover .dropbtn  {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  background-color: #111;
}

.active {
  background-color: #0439aa;
}

li a, .dropbtn {
  display: inline-block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #f1f1f1;}

.dropdown:hover .dropdown-content {
  display: block;
}




</style>

