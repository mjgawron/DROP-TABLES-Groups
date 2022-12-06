<template>
  <div class="tab">
    <div class="bar"></div>
    <div class="question">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script>
//import axios from "axios";

export default {
  name: "QuestionsTab",
  data() {
    return {
      questions: [],
    };
  },
  methods: {},
};
</script>

<style scoped>
.bar {
  display: inline-flex;
  flex-direction: column;
  min-width: 450px;
  text-align: left;
}
.question {
  display: inline-flex;
  flex-direction: column;
}
.tab {
  display: grid;
  grid-template-columns: minmax(150px, 25%) 1fr;
}
</style>
