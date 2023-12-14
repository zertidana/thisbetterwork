<template>
  <div class="h1">
    {{ title }}
  </div>
  <div>
    {{ counter.count }}
  </div>
  <!--I am thinking ideally this would be  
  the page that once the user logs in, it has 
  his favourite categories and comments etc -->
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import { useCounterStore } from "@/stores/auth";

export default defineComponent({
  data() {
    return {
      title: "Main Page",
    };
  },
  setup() {
    const counter = useCounterStore();

   
    onMounted(() => {
      counter.increment();
    });
    
    return { counter };
  },
});
</script>

<style scoped>
</style>
