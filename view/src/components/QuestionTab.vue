<template>
  <div class="tab">
    <div class="bar"></div>
    <div class="question">
      <!-- <RouterView></RouterView> -->
      <QuestionList :questions="questions" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
//import axios from "axios";
import axios from "axios";
import QuestionList from "./QuestionList.vue";

export default {
  name: "QuestionTab",
  components: {
    QuestionList,
  },
  data() {
    return {
      questions: [],
    };
  },
  methods: {},
  beforeMount() {
    axios.get("/question").then((response) => {
      // recieve a list of questions
      this.questions = [{},{},{},{}]
    });
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
