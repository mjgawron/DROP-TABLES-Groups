<template>
  <div class="grade">
    <table class="table">
      <tr>
        <th>Company</th>
        <th>Contact</th>
        <th>Country</th>
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
</style>
