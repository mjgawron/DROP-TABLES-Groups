<template>
  <div class="tab">
    <!--If the user is an instructor, show them a question submission form and the questions they've made-->
    <div class="instructor" v-if="isInstructor">
      <CreateQuestion :course_id="course_id" />
      <QuestionList :questions="questions" :isInstructor="isInstructor" />
    </div>
    <!--If the user is a student, open the component that uses WebSockets-->
    <div class="student" v-else>
      <QuestionList :questions="questions" :isInstructor="isInstructor" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import QuestionList from "../components/QuestionList.vue";
import CreateQuestion from "../components/CreateQuestion.vue";

export default {
  name: "QuestionTab",
  components: {
    CreateQuestion,
    QuestionList,
  },
  data() {
    return {
      course_id: "",
      isInstructor: false,
      questions: [],
    };
  },
  beforeMount() {
    axios.get("/course/" + this.$router.currentRoute.value.params.course_id + "/questions").then((response) => {
      this.questions = response.data;
    });
    axios.get("/course/" + this.$router.currentRoute.value.params.course_id + "/instructor").then((response) => {
      this.isInstructor = response.data;
    });
    this.course_id = this.$router.currentRoute.value.params.course_id;
  },
};
</script>

<style scoped>
.tab {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>