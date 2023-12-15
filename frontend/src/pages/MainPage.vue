<template>
  <div class="h1">
    {{ title }}
  </div>
  <div v-if="userStore.username">
    Logged in as: {{ userStore.username }}
  </div>
  <div v-else>
    Not logged in.
  </div>
  <!--I am thinking idealy this would be  
  the page that once the user logs in, it has 
  his favourite categories and comments etc -->
</template>

<script lang="ts">
    import { defineComponent } from "vue";
    import { useUserStore } from "../../stores/auth";

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
