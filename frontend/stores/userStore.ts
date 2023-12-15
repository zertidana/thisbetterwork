import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
    // State
    state: () => ({
        username: '',
        isLoggedIn: false,
    }),

    // Actions
    actions: {
        login(username) {
            this.username = username;
            this.isLoggedIn = true;
        },

        logout() {
            this.username = '';
            this.isLoggedIn = false;
        }
    }
});
