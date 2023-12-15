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
          <button @click="submitComment(index)">Submit</button>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from "vue";
  import { useUserStore } from "../stores/auth.ts";
  export default defineComponent({
    setup(){
          const userStore = useUserStore();
          return { userStore };
        },
      data() {
          return {
              title: "Sports Page",
              articles: [
                {
                  title: "Tottenham 4-1 Newcastle",
                  image: "https://imgresizer.tntsports.io/unsafe/2560x1440/filters:format(jpeg)/origin-imgresizer.tntsports.io/2023/12/10/3842157-78076068-2560-1440.jpg",
                  preview: "Tottenham ended their recent slump in emphatic style as they convincingly overpowered a leg-weary Newcastle United...",
                  fullText: "Tottenham ended their recent slump in emphatic style as they convincingly overpowered a leg-weary Newcastle United. Spurs had lost four of their previous five games and had not won since the victory at Crystal Palace on 27 October, but, once Destiny Udogie put them ahead from Son Heung-min's pass, there was only one winner...",
                  showFullArticle: false,
                  comment: ''
                },
                {
                  title: "Destiny Udogie: Tottenham defender signs new contract until 2030",
                  image: "https://ichef.bbci.co.uk/onesport/cps/800/cpsprodpb/0DF0/production/_131986530_gettyimages-1845190575.jpg",
                  preview: "Tottenham defender Destiny Udogie has signed a new contract until 2030...",
                  fullText: "Tottenham defender Destiny Udogie has signed a new contract until 2030. Udogie joined Spurs from Udinese for £15m on a five-year deal in the summer of 2022 before immediately returning to the Serie A club on a season-long loan...",
                  showFullArticle: false,
                  comment: ''
                },
                {
                  title: "Man City 3-3 Tottenham",
                  image: "https://ichef.bbci.co.uk/news/976/cpsprodpb/1f30/live/37075280-9280-11ee-952c-5f8de97ee99b.jpg.webp",
                  preview: "Former Tottenham defender Stephen Kelly says a relentlessness helped Spurs to a stunning 3-3 draw at Manchester City on Sunday...",
                  fullText: "Former Tottenham defender Stephen Kelly says a relentlessness helped Spurs to a stunning 3-3 draw at Manchester City on Sunday. Ange Postecoglou’s side twice came from behind to level at the Etihad Stadium after initially taking an early lead through captain Son Heung-min...",
                  showFullArticle: false,
                  comment: ''
                }
              ]
          }
      },
      methods: {
          submitComment(articleIndex) {
              // Logic to handle comment submission for a specific article
              // Placeholder for frontend functionality
          }
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