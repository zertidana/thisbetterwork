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
            title: "Education News Page",
            articles: [
              {
                title: "Uproar as after-school Satan club forms at Tennessee elementary school",
                image: "https://i.guim.co.uk/img/media/18481d9a6a188757ca691d925dac3e736d7d80f2/0_0_6650_3992/master/6650.jpg?width=620&dpr=1&s=none",
                preview: "Reading print texts improves comprehension more than reading digital materials does, according to a new study.....",
                fullText: " Community members in a Tennessee school district want to banish Satan from their children’s halls after the formation of a new club was announced. The After School Satan Club (ASSC) wants to establish a branch in Chimneyrock elementary school in the Memphis-Shelby county schools (MSCS) district.",
                showFullArticle: false,
                comment: ''
              },
              {
                title: "Reading print improves comprehension",
                image: "https://i.guim.co.uk/img/media/e1ce36c36f11035f5de41c21443e9575b9dd32fb/0_141_2121_1273/master/2121.jpg?width=620&dpr=1&s=none",
                preview: "Reading print improves comprehension far more than looking at digital text, say researchers...",
                fullText: "Reading print texts improves comprehension more than reading digital materials does, according to a new study. Researchers at the University of Valencia analysed more than two dozen studies on reading comprehension published between 2000 and 2022, which assessed nearly 470,000 participants. Their findings suggest that print reading over a long period of time could boost comprehension skills by six to eight times more than digital reading does....",
                showFullArticle: false,
                comment: ''
              },
              {
                title: "David Cameron defends UK’s decision not to vote for UN resolution",
                image: "https://i.guim.co.uk/img/media/7346aa8ed426f15621aa9ff3ca19a278132d92a9/0_97_3500_2101/master/3500.jpg?width=620&dpr=1&s=none",
                preview: "Cameron defends UK's decision not to vote for UN resolution demanding immediate ceasefire in Gaza...",
                fullText: "Cameron defends UK's decision not to vote for UN resolution demanding immediate ceasefire in Gaza Lady Blackstone (Lab) asks about Gaza.Cameron says he does not want the fighting to go on for any longer than necessary.But, if there is a ceasefire, it has to be sustainable. There should not be an opportunity for Hamas to launch another 7 October-type attack.He says the UN resolution was asking for an immediate ceasefire, and a two-state solution....",
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