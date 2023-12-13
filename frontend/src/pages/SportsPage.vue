<template>
  <div class="sports-category-page">
    <h1>Sports News</h1>
    <div v-if="loading">Loading...</div>
    <div v-else>
      <div v-for="article in articles" :key="article.id">
        <h2>{{ article.title }}</h2>
        <img :src="article.imageUrl" :alt="article.title" />
        <p>{{ article.summary }}</p>
        <router-link :to="`/articles/${article.id}`">Read More</router-link>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';

export default defineComponent({
  setup() {
    const articles = ref([]);
    const loading = ref(true);

    onMounted(async () => {
      loading.value = true;
      const response = await fetch('/api/models.py'); 
      articles.value = await response.json();
      loading.value = false;
    });

    return { articles, loading };
  },
  async fetchSportsArticles() {
    const response = await fetch('/api/news/sports/');
    const data = await response.json();
    this.sportsArticles = data;
    }

});

</script>

<style scoped>
/* Your styles here */
</style>
