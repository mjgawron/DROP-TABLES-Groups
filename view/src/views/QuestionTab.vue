<template>
  <div class="tab">
    <!--In QuestionList, 'isInstructor' picks either 'InsQuestionComp' or 'QuestionComp' to be enumerated from the array-->
    <QuestionList :questions="questions" :isInstructor="isInstructor" />
  </div>
</template>

<script>
/* eslint-disable */
//import axios from "axios";
import QuestionList from "../components/QuestionList.vue";

export default {
  name: "QuestionTab",
  props: {
    isInstructor: Boolean,
  },
  components: {
    QuestionList,
  },
  data() {
    return {
      questions: [{"question_id":10,"question_detail":"asdasdasd"},{"question_id":9,"question_detail":"asdasdasd"}],
    };
  },
  // beforeMount() {
  //   axios.get("/course/" + this.course_id + "/questions").then((response) => {
  //     this.questions = response.data;
  //   });
  // },
};
</script>

<style scoped>
.tab {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>