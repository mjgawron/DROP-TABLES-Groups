<template>
  <div class="questions">
    <div class="container">
      <QuestionList :questions="questions" />
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import QuestionList from "../components/QuestionList.vue";

export default {
  name: "StudentQuestions",
  data() {
    return {
      // questions: [{}],
      id: "",
    };
  },
  props: {
    course_id: Number,
  },
  components: {
    QuestionList,
  },
  beforeMount() {
    this.id = this.$router.currentRoute.value.params.course_id;
    axios.get("/course/" + this.course_id + "/questions").then((response) => {
      this.questions = response.data
    });
  }
};
</script>

<style scoped></style>
