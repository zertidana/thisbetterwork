// stores/counter.js
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => {
    return { count: 0 }
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    increment() {
      this.count++
    },
  },
})


interface AuthState {
  isAuthenticated: boolean;
  authToken: string | null;
}

export const useAuthStore = defineStore('auth', {
  state: (): AuthState => ({
    isAuthenticated: false,
    authToken: null,
  }),
  getters: {
    // You can add getters here if needed
  },
  actions: {
    setAuthToken(token: string): void {
      this.authToken = token;
      this.isAuthenticated = true;
    },
    clearAuthToken(): void {
      this.authToken = null;
      this.isAuthenticated = false;
    },
  },
  
});