<template>
  <div class="questions">
    <CourseTabs />
    <div class="container">
      <CreateQuestion />
    </div>
  </div>
</template>

<script>
// import axios from "axios";
import CreateQuestion from "../components/CreateQuestion.vue";

export default {
  name: "InstructorQuestions",
  data() {
    return {
      //
    };
  },
  props: {
    //
  },
  components: {
    CourseTabs,
    CreateQuestion,
  },
  beforeMount() {
    axios.get("/course/" + this.course_id + "/questions").then((response) => {
      this.questions = response.data
    });
  }
};
</script>

<style scoped></style>
