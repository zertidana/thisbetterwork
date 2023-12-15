<template>
    <div class="h1">
      {{ title }}
    </div>
    <!--I am thinking idealy this would be  
    the page that once the user logs in, it has 
    his favourite categories and comments etc -->
  </template>
  
  <script lang="ts">
    import { defineComponent } from "vue";
    import { useUserStore } from "../stores/auth.ts";
    export default defineComponent({
        data() {
            return {
                title: "art Page",
            }
        },
        setup(){
          const userStore = useUserStore();
          return { userStore };
        }
    })
  </script>
  
  <style scoped>
  </style>
  