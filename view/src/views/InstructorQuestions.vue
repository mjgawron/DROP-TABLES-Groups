<template>
  <div class="questions">
    <div class="container">
      <CreateQuestion :course_id="id" />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CreateQuestion from "../components/CreateQuestion.vue";

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
