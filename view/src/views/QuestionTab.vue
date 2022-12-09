<template>
  <div>
    <div v-if="isInstructor">
      <!--If the user is an instructor, show InstructorQuestionView inside the current Tab-->
      <InstructorQuestionView :isInstructor="isInstructor" />
    </div>
    <div v-else="isInstructor">
      <!--OTHERWISE, show StudentQuestionView inside the Tab-->
      <StudentQuestionView :isInstructor="isInstructor" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import StudentQuestionView from "./StudentQuestionView.vue";
import InstructorQuestionView from "./InstructorQuestionView.vue";

export default {
  name: "QuestionTab",
  props: {
    isInstructor: Boolean,
  },
  components: {
    InstructorQuestionView,
    StudentQuestionView,
  },
  data() {
    return {
      questions: [],
    };
  },
  beforeMount() {
    axios.get("/course/" + this.course_id + "/questions").then((response) => {
      this.questions = response.data;
    });
  },
};
</script>

