<template>
  <div class="grade">
    <h3>{{ grade.name }}</h3>
    <table class="table">
      <tr class="question_ids">
        <th :key="answer.question_id" v-for="answer in grade.answers">
          <h4>Q{{ answer.question_id }},</h4>
        </th>
        <th>Tot:</th>
      </tr>
      <tr class="answers">
        <td :key="answer.question_id" v-for="answer in grade.answers">
          {{ answer.answer }}
        </td>
        <td>
          {{ score }}
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "GradeComp",
  data() {
    return {
      score: 0,
    }
  },
  props: {
    grade: Object,
  },
  beforeMount() {
      var correct = 0;
      const numQuestions = this.grade.answers.length;
      for (let answer of this.grade.answers) {
        if (answer.answer === "t") {
          correct += 1;
        }
      }
      this.score = Intl.NumberFormat('default', {style: 'percent', minimumFractionDigits: 2, maximumFractionDigits: 2,}).format((correct / numQuestions));
    },
};
</script>

<style scoped>
.grade {
  width: 80%;
  padding: 20px;
  margin: 20px auto;
  border: 2px solid black;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
}
</style>
