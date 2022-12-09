<template>
  <div class="grade">
    <h3>{{ grade.name }}</h3>
    <table class="table">
      <tr class="question_ids">
        <th :key="idx" v-for="idx in this.questionIncrement">
          <h4>Q{{ idx + 1 }}---</h4>
        </th>
        <th>Total:</th>
      </tr>
      <tr class="answers">
        <td :key="score.question_id" v-for="score in grade.score_list">
          {{ score.correctness }}
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
      questionIncrement: 0,
      score: 0,
    }
  },
  props: {
    grade: Object,
  },
  beforeMount() {
      var correct = 0;
      const numQuestions = this.grade.score_list.length;
      for (let score of this.grade.score_list) {
        if (score.correctness) {
          correct += 1;
        }
      }
      this.questionIncrement = Array.from(Array(numQuestions).keys())
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
