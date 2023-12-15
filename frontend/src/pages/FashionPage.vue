<template>
  <div class="sports-page">
    <h3>{{ title }}</h3>
    <div class="article" v-for="(article, index) in articles" :key="index">
      <h1>{{ article.title }}</h1>
      <img :src="article.image" :alt="article.title" />
      <p v-if="!article.showFullArticle">{{ article.preview }}</p>
      <p v-else>{{ article.fullText }}</p>
      <button v-if="!article.showFullArticle" @click="article.showFullArticle = true">View more</button>
      <div class="comment-section" v-if="article.showFullArticle">
        <textarea v-model="article.comment" placeholder="Add a comment..."></textarea>
        <button @click="(index)">Submit</button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({

  // setup() {
  //   const articles = ref([]);
  //   const loading = ref(true);
  //   onMounted(async () => {
  //     loading.value = true;
  //     const response = await fetch('/api/models.py'); 
  //     articles.value = await response.json();
  //     loading.value = false;
  //   });
  //   return { articles, loading };
  // },
  //   async fetchSportsArticles() {
  //     const response = await fetch('/api/news/sports/');
  //     const data = await response.json();
  //     this.sportsArticles = data;
  //     },
    data() {
        return {
            title: "World New Page Page",
            articles: [
              {
                title: "Shipping firm pauses Red Sea journeys over attacks",
                image: "https://ichef.bbci.co.uk/news/976/cpsprodpb/1488/production/_132065250_gettyimages-166399156-1.jpg.webp",
                preview: "Danish shipping company Maersk has said it is pausing all journeys through the Red Sea....",
                fullText: "Danish shipping company Maersk has said it is pausing all journeys through the Red Sea.The decision comes after a spate of attacks on vessels launched from a part of Yemen controlled by the Houthis - an Iran-backed rebel movement....",
                showFullArticle: false,
                comment: ''
              },
              {
                title: "Beijing subway crash leaves 102 with broken bones",
                image: "https://ichef.bbci.co.uk/news/976/cpsprodpb/14497/production/_132059038_1bd5a112-43fa-4211-bce3-a5bc284fdfaa.jpg.webp",
                preview: "Tottenham defender Destiny Udogie has signed a new contract until 2030...",
                fullText: "Tottenham defender Destiny Udogie has signed a new contract until 2030. Udogie joined Spurs from Udinese for £15m on a five-year deal in the summer of 2022 before immediately returning to the Serie A club on a season-long loan...",
                showFullArticle: false,
                comment: ''
              },
              {
                title: "Yemen Houthi rebels claim attacks on two Red Sea cargo ships",
                image: "https://ichef.bbci.co.uk/news/976/cpsprodpb/E174/production/_132061775_gettyimages-1841988533.jpg.webp",
                preview: "Two cargo ships in the Red Sea have been attacked by missiles fired from territory in Yemen, the US says....",
                fullText: "Two cargo ships in the Red Sea have been attacked by missiles fired from territory in Yemen, the US says.One was hit with a drone and another by missiles, both launched from a part of Yemen controlled by the Houthis - a rebel movement backed by Iran....",
                showFullArticle: false,
                comment: ''
              }
            ]
        }
    },
    methods: {
      
    }
})
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