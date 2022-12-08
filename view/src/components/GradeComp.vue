<template>
  <div class="grade">
    <table class="table">
      <tr
        class="tableRow"
        v-bind:key="score.question_id"
        v-for="score in grade.scoreList"
      >
        <!-- but ignore question_id and instead count up Q1, Q2, just used for uniqueness-->
        <th v-if="score.correctness == true">+</th>
        <th v-if="score.correctness == false">-</th>
      </tr>
    </table>
  </div>
</template>

<script>
/* eslint-disable */
//import axios from "axios";
// grade is an array containing one object
// once we iterate
export default {
  name: "GradeComp",
  props: {
    grade: Object,
  },
  methods: {},
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
</style>
