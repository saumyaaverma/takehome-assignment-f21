<template>
<div>
  <button v-on:click="count += 1">increment</button>
  <button v-on:click="count -= 1">decrement</button>
  <br><br>
  <p>Episodes seen are : {{ count }}</p>
  <br>
</div>  
</template>

<script>
export default {
  props:{
    number: {
      default: 0,
      type: Number}
  },
  data() {
    return {
      count: this.number
    };
  }
};
</script>

<style>
</style>