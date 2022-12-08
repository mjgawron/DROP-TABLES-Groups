<template>
  <div class="tab">
    <div class="bar">
      <div class="questions" :key="question.id" v-for="question in questions">
        <QuestionComp :question="question" />
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
//import axios from "axios";

export default {
  name: "QuestionList",
  props: {
    questions: Array,
  },
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
