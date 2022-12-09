<template>
  <div class="question">
    <div class="info">
      <h4>Question #{{ index }}</h4>
      <p>{{ question.question_detail }}</p>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "InsQuestionComp",
  props: {
    index: Number,
    question: Object,
  },
}
</script>

<style scoped>
.question {
  width: 60%;
  padding: 20px;
  margin: 20px auto;
  border: 2px solid black;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
}
.info {
  text-align: left;
}
</style>
