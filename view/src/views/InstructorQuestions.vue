<template>
  <div class="questions">
    <CourseTabs />
    <div class="container">
      <CreateQuestion :course_id="id" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CreateQuestion from "../components/CreateQuestion.vue";
import CourseTabs from "../components/CourseTabs.vue";

export default {
  name: "InstructorQuestions",
  data() {
    return {
      id: "",
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
    this.id = this.$router.currentRoute.value.params.course_id;
    axios.get("/course/" + this.course_id + "/questions").then((response) => {
      this.questions = response.data;
    });
  },
};
</script>

<style scoped></style>
