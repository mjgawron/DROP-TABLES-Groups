<template>
  <div class="tab">
    <div class="bar"></div>
    <div class="question">
      <!-- <RouterView></RouterView> -->
      <QuestionList :questions="questions" :course_id="course_id" />
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
      course_id: "",
    };
  },
  methods: {},
  beforeMount() {
    this.course_id = this.$router.currentRoute.value.params.course_id;
    axios.get("/course/" + this.course_id + "/questions").then((response) => {
      this.questions = response.data;
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
