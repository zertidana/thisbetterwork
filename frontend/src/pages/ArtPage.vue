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
  
      export default defineComponent({
          data() {
              return {
                  title: "Art Page",
              }
          }
      })
  </script>
  
  <style scoped>
  </style>
  