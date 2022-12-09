<template>
  <div class="tab">
    <!--In QuestionList, 'isInstructor' picks either 'InsQuestionComp' or 'QuestionComp' to be enumerated from the array-->
    <QuestionList :questions="questions" :isInstructor="isInstructor" />
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import QuestionList from "../components/QuestionList.vue";

export default {
  name: "QuestionTab",
  components: {
    QuestionList,
  },
  data() {
    return {
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