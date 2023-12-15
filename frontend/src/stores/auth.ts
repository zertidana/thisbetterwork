import { defineStore } from 'pinia'
// store.js
export const useUserStore = defineStore('user', {
  state: () => ({
    isLoggedIn: false,
    username: '',
    favoriteCategories: []
  }),
  actions: {
    logIn(username) {
      this.isLoggedIn = true
      this.username = username
      // Additional login logic
    },
    logOut() {
      this.isLoggedIn = false
      this.username = ''
      // Additional logout logic
    },
    updateFavoriteCategories(categories) {
      this.favoriteCategories = categories
      // Additional logic to update categories
    }
  },
  getters: {
    isUserLoggedIn: (state) => state.isLoggedIn
  }
})
