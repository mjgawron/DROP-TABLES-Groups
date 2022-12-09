<template>
  <!--Simply shows the instructor the question_id and the 
  description of the question without buttons & WebSockets-->
  <div class="container">
    <h4>Question: {{ question.question_id }}</h4>
    <p>{{ question.question_detail }}</p>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "InsQuestionComp",
  props: {
    question: Object,
  },
}
</script>

<style scoped>
.container {
  width: 80%;
  padding: 20px;
  margin: 20px auto;
  border: 2px solid black;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
}
</style>