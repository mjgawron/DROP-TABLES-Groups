<template>
  <!--QuestionList needs 'isInstructor' to pick the component that is enumerated-->
  <div class="list">
    <!-- If the user is an instructor, populate an InsQuestionComp for every question in the array -->
    <div class="instructor" v-if="isInstructor">
      <div :key="question.id" v-for="question in questions">
        <InsQuestionComp :question="question" />
      </div>
    </div>
    <!-- If the user is a student, populate a QuestionComp for each question in the array -->
    <div class="student" v-else="isInstructor">
      <div :key="question.id" v-for="question in questions">
        <QuestionComp :question="question" />
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "QuestionList",
  props: {
    isInstructor: Boolean,
    questions: Array,
  },
};
</script>

<style scoped>
.list {
  display: grid;
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
