<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <router-link class="navbar-brand" to="/">Home</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              All Categories
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><router-link class="dropdown-item" to="/SportsPage">Sports</router-link></li>
              <li><router-link class="dropdown-item" to="/FashionPage">Fashion</router-link></li>
              <li><router-link class="dropdown-item" to="/EducationPage">Education</router-link></li>
              <li><router-link class="dropdown-item" to="/ArtPage">Art</router-link></li>
              <li><router-link class="dropdown-item" to="/WorldPage">World News</router-link></li>
              <li><router-link class="dropdown-item" to="/FinancePage">Finance</router-link></li>
            </ul>

          </li>
          <li><router-link class="" to="/ProfilePage">Profile Page</router-link></li>
        </ul>
        <ul class="navbar-nav">
          <li class="nav-item"><a class="nav-link active" href="http://127.0.0.1:8000/accounts/login/">Login</a></li>
          <li class="nav-item"><a class="nav-link" href="http://127.0.0.1:8000/accounts/signup/">Sign Up</a></li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">

</script>

