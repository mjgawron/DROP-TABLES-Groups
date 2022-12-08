<template>
  <div class="grade">
    <h3>SID # {{ grade.student_id }}</h3>
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
          {{ total }}
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
      total: 0,
    }
  },
  props: {
    grade: Object,
  },
  methods: {
    total() {
      this.total = 12;
    },
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
.table {

}
</style>
