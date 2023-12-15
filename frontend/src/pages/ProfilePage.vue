<template>
  <div class="title">
    <h1>{{ title }}</h1>
  </div>
  <div class="profile-container">
    
    <div class="username-section">
      <h2>{{ userStore.username }}</h2>
    </div>
    <div class="profile-image-section">
      <img :src="profileImage" alt="Profile Image" />
      <button class="edit-button" @click="edit">Edit</button>
    </div>
    <div class="input-section">
      <label for="email" class="input-label">Email:</label>
      <input type="text" v-model="email" name="email">
      <button class="save-button" @click="saveemail">Save</button>
    </div>
    <div class="input-section">
      <label for="dob" class="input-label">Date of Birth:</label>
      <input type="date" v-model="dob" name="dob">
      <button class="save-button" @click="saveDob">Save</button>
    </div>
    <div class="favorite-category-section">
      <label v-for="(category, index) in categories" :key="index">
    <input type="checkbox" v-model="selectedCategories" :value="category"> {{ category }}
    </label>

    <button class="save-button" @click="saveCategory">Save</button>
  </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useUserStore } from "../stores/auth.ts";
export default defineComponent ({
  setup()
  {
    const userStore = useUserStore();
    return { userStore };
  },

  data() {
    return {
      username: '',
      email: '',
      dob: '',
      profileImage: '', 
      favoriteCategory: '',
      title: "Profile Page",
      selectedCategories: [] as string[],
      categories: ['Sports', 'Fashion', 'Education', 'Art', 'World News', 'Finance']

    };
  },
  methods: {
    async saveCategory(){
      
    },
    async saveDob(){
      
    },
    async saveemail() {
    
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Authorization": `Token ${this.userStore.token}` // If authentication is required
        },
        body: JSON.stringify({ 
          username: this.userStore.username, 
          email: this.email
        })
      };

      try {
        const response = await fetch('http://127.0.0.1:8000/api/update-email/', requestOptions);

        if (!response.ok) {
          throw new Error('Failed to save email.');
        }

        alert('Email saved successfully!');
      } catch (error) {
        console.error('Error saving email:', error);
        alert('Failed to save email.');
      }
    },
    async edit(){
      
    },


    
  }
})
</script>

<style scoped>

.title {
   text-align: center;
 }
.profile-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.username-section h2 {
    margin-bottom: 20px;
}

.profile-image-section {
    position: relative;
    display: inline-block;
    margin-bottom: 20px;
}

.profile-image-section img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 3px solid #333;
}

.edit-button {
    position: absolute;
    bottom: 10px;
    left: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 12px;
}

.edit-button:hover {
    background-color: #0056b3;
}

.input-section {
    text-align: left;
    margin-bottom: 20px;
    width: 80%;
    margin-left: auto;
    margin-right: auto;
}

.input-section .input-label {
    display: block;
}

input[type="text"], input[type="date"] {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-top: 5px;
}

input[type="text"]:focus, input[type="date"]:focus {
    outline: none;
    border-color: #007bff;
}

.save-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    margin-top: 10px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
}

.save-button:hover {
    background-color: #0056b3;
}

.favorite-category-section {
    margin-bottom: 20px;
    text-align: center;
}

.favorite-category-section label {
    margin-right: 10px;
}

#favoriteCategory {
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.save-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
    font-size: 16px;
}

.save-button:hover {
    background-color: #0056b3;
}
</style>
