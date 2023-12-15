import { defineStore } from 'pinia';
export const useUserStore = defineStore('user', {
    state: () => ({
        username: null,
        token: null,
    }),
    actions: {
        login(username: string,token: token) {
            this.username = username;
            this.token = token;
        },
        logout() {
            this.username = 'null';
            this.token = '';
        }
    }
});