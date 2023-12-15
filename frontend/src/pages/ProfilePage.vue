<template>
  <div class="profile-container">
    <div class="username-section">
      <h2>{{ username }}</h2>
    </div>
    <div class="profile-image-section">
      <img :src="profileImage" alt="Profile Image" />
      <button class="edit-button">Edit</button>
    </div>
    <div class="input-section">
      <label for="email" class="input-label">Email:</label>
      <input type="text" v-model="email" name="email">
      <button class="save-button">Save</button>
    </div>
    <div class="input-section">
      <label for="dob" class="input-label">Date of Birth:</label>
      <input type="date" v-model="dob" name="dob">
      <button class="save-button">Save</button>
    </div>
    <div class="favorite-category-section">
    <label for="favoriteCategory">Favorite Category:</label>
    <select v-model="selectedCategory" name="favoriteCategory" id="favoriteCategory">
      <option value="Sports">Sports</option>
      <option value="Fashion">Fashion</option>
      <option value="Education">Education</option>
      <option value="Art">Art</option>
      <option value="World News">World News</option>
      <option value="Finance">Finance</option>
    </select>
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
      username: 'Aqib',
      email: 'aqib@coolguy.com',
      dob: '2002-01-01',
      profileImage: 'https://ih0.redbubble.net/image.777653777.6638/raf,360x360,075,t,fafafa:ca443f4786.jpg', // Replace with actual image path
      favoriteCategory: 'Sports',
      title: "art Page",
      selectedCategory: '',
    };
  },
  methods: {
    saveCategory(){

    },
  }
})
</script>

<style scoped>
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
