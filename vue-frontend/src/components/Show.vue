<template>
  <!-- PART 4: Add your code here -->
  <div>
    <p>Name of the Show : {{ name }}</p>
    <p>ID of the Show : {{ id }}</p>
    <Counter v-bind:number="episodes_seen"/>
</div>
</template>

<script>
// PART 4: Add your code here
import Counter from "./Counter.vue";
export default {
  components:{
      Counter
    },
  props: {
    "id": Number, 
    "name": String, 
    "episodes_seen": Number
    }
    
};
</script>

<style>
</style>
