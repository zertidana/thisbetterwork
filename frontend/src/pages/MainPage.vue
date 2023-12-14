<template>
  <div class="h1">
    {{ title }}
  </div>
  <div>
    {{ counter.count }}
  </div>
  <!--I am thinking idealy this would be  
  the page that once the user logs in, it has 
  his favourite categories and comments etc -->
</template>

<script lang="ts">
    import { defineComponent, ref } from "vue";
    import { defineStore } from "pinia";
    
    export const useCounterStore = defineStore('counter', () => {
      const count = ref(0)
      function increment() {
        count.value++
      }

      return { count, increment }
    })

    export default defineComponent({
        data() {
            return {
                title: "Main Page",
            }
        }
    })
</script>

<style scoped>
</style>
