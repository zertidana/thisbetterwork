<template>
  <div class="container sports-page">
    <h3 class="mb-4">{{ title }}</h3>
    <div class="row">
      <div class="col-md-6 mb-3">
        <div class="card">
          <img >
          <div class="card-body">
            <h5 class="card-title"></h5>
            <p class="card-text"></p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

  
<script lang="ts">
import { defineComponent, onMounted } from 'vue';

export default defineComponent({
  setup() {

  },
  data() {
    return {
      title: "Art News",
    };
  },
  methods: {
    
  }
});
</script>

  
  <style scoped>
  .sports-page {
      width: 80%;
      margin: auto;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .article {
      margin-top: 20px;
      border: 1px solid #ddd;
      padding: 20px;
  }
  
  .article img {
      max-width: 100%;
      height: auto;
      margin-bottom: 20px;
  }
  
  .article img {
    width: 800px;
    height: 450px;
    object-fit: cover;
    margin-bottom: 20px;
  }

  .article button {
      background-color: #007bff;
      color: white;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
      border-radius: 5px;
      margin-bottom: 20px;
  }
  
  .article button:hover {
      background-color: #0056b3;
  }
  
  .comment-section textarea {
      width: 100%;
      padding: 10px;
      margin-bottom: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
  }
  
  .comment-section button {
      background-color: #28a745;
      color: white;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
      border-radius: 5px;
  }
  
  .comment-section button:hover {
      background-color: #218838;
  }
  </style>