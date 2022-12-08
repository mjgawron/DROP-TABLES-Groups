<template>
  <div class="grade">
    <table class="table">
      <tr
        class="tableRow"
        v-bind:key="score.question_id"
        v-for="score in grade.answers"
      >
        <th>asd</th>
        <th>asd</th>
        <th>asd</th>
        <!-- but ignore question_id and instead count up Q1, Q2, just used for uniqueness
        <th class trueBox v-if="score.correctness == 'T'">+</th>
        <th class falseBox v-if="score.correctness == 'F'">-</th>
        <th class unansweredBox v-if="score.correctness == 'X'">?</th> -->
      </tr>
    </table>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: "GradeComp",
  props: {
    grade: Object,
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

.tableRow{

}

.truebox{
  background: #0e0;
  max-height: 40px;
  max-width: 40px;
  min-height: 40px;
  margin: 0px;
}
.falseBox{
  background: #e00;
  max-width: 40px;
  max-height: 40px;
  min-width: 40px;
  min-height: 40px;
  margin: 0px;
}

.unansweredBox{
  background: #777;
  max-width: 40px;
  max-height: 40px;
  min-width: 40px;
  min-height: 40px;
  margin: 0px;
}

</style>
