<template>
  <div class="h3">
    {{ title }}
  </div>
</template>

<script lang="ts">
  import { defineComponent } from "vue";
  import { useUserStore } from "../../stores/auth";
  export default defineComponent({
      data() {
          return {
              title: "Art Page",
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
