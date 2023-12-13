<template>
    <div class="profile">
      <div class="profile-picture"></div>
      <h2 class="profile-name">{{ profileName }}</h2>
      <p class="date-of-birth">Date of Birth: {{ dateOfBirth }}</p>
      <p class="email">Email: {{ email }}</p>
    </div>
  </template>

  <script>
  export default {
    name: 'ProfilePage',
    data() {
      return {
        profileName: 'John Doe',
        dateOfBirth: 'January 1, 1990',
        email: 'johndoe@example.com' // Replace with dynamic email data
      };
    }
  }
  </script>

  <style>
 

  .profile {
      text-align: center;
      border: 1px solid #ddd;
      padding: 20px;
      border-radius: 10px;
      width: 300px;
  }

  .profile-picture {
      width: 100px;
      height: 100px;
      background-color: grey;
      border-radius: 50%;
      margin: 0 auto 20px;
  }

  .profile-name {
      margin: 10px 0;
  }

  .date-of-birth, .email {
      color: #555;
      margin: 5px 0;
  }
  </style>
