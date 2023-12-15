<template>
    <div class="h3">
      {{ title }}
    </div>
  </template>
  
  <script lang="ts">
    import { defineComponent } from "vue";
    import { useUserStore } from "../stores/auth.ts";
    export default defineComponent({
        data() {
            return {
                title: "Main Page",
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