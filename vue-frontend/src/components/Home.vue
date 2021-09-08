<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions complete="complete"/>

    <!-- PART 4: Modify the Show component to accept all of these props -->
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />
    <input type="text" v-model="input">
    <button type="button" @click="addShow(input)">Add a new Show</button>
  </div>



</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ]
    };
  },
  methods: {
  addShow(input) {
    if(!input){
      return;
    }
    this.shows.push({ id:(this.shows.length + 1), name: input, episodes_seen: 0 });
    this.name = '';
  }
}
};
</script>

<style>
</style>


