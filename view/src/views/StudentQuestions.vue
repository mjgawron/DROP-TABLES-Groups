<template>
  <div class="questions">
    <CourseTabs />
    <div class="container">
      <QuestionList :questions="questions" />
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import CourseTabs from "../components/CourseTabs.vue";
import QuestionList from "../components/QuestionList.vue";

export default {
  name: "StudentQuestions",
  data() {
    return {
      // questions: [{}],
    };
  },
  props: {
    course_id: Number,
  },
  components: {
    CourseTabs,
    QuestionList,
  },
  beforeMount() {
    axios.get("/course/" + this.course_id + "/questions").then((response) => {
      this.questions = response.data
    });
  }
};
</script>

<style scoped></style>
