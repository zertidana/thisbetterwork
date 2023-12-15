import { defineStore } from 'pinia';
import axios from 'axios'; 

export const useArticleStore = defineStore('article', {
  state: () => ({
    categories: [],
    articles: []
  }),
  actions: {
    async fetchCategories() {
      try {
        const response = await axios.get('/api/categories/');
        this.categories = response.data;
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    },
    async fetchArticlesByCategoryName(categoryName: string) {
        try {
            const response = await axios.get(`/api/articles?categoryName=${categoryName}`);
            this.articles = response.data;
            console.log("Articles fetched:", this.articles); 
        } catch (error) {
            console.error('Error fetching articles by category name:', error);
        }
    }
  }
});
