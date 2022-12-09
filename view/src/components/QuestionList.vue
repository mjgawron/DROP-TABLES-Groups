<template>
  <div class="list">
    <!-- If the user is an instructor, populate an InsQuestionComp for every question in the array -->
    <div class="instructor" v-if="isInstructor">
      <div :key="question.question_id" v-for="question in questions">
        <InsQuestionComp :question="question" />
      </div>
    </div>
    <!-- If the user is a student, populate a QuestionComp for each question in the array -->
    <div class="student" v-else>
      <div :key="question.question_id" v-for="question in questions">
        <QuestionComp :question="question" />
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import QuestionComp from './QuestionComp.vue';
import InsQuestionComp from './InsQuestionComp.vue';

export default {
  name: "QuestionList",
  props: {
    isInstructor: Boolean,
    questions: Array,
  },
  components: {
    InsQuestionComp,
    QuestionComp,
  },
};
</script>

<style scoped>
.list {
  display: grid;
  align-items: center;
  grid-template-columns: minmax(150px, 25%) 1fr;
}
.instructor {
  display: inline-flex;
  flex-direction: column;
  min-width: 450px;
  text-align: left;
}
.student {
  display: inline-flex;
  flex-direction: column;
  min-width: 450px;
  text-align: left;
}
</style>
