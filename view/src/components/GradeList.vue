<template>
  <div>
    <div class="head">
      <h2>{{ message }}</h2>
    </div>
    <div class="list" :key="grade.student_id" v-for="grade in grades">
      <GradeComp :grade="grade" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import GradeComp from './GradeComp.vue';

export default {
  name: "GradeList",
  props: {
    // answer NON PLURAL  => {q_id:"t/f/x", ...}
    // answers PLURAL     => [{q_id:"t/f/x", ...}, ...]
    // grade   NON PLURAL => {student_id: <num>, answers:[{q_id:"t/f/x"}, ...]}
    // grades  PLURAL     => [{student_id: <num>, answers:[{q_id:"t/f/x"},...]}, ... ]
    grades: Array,
  },
  components: {
    GradeComp,
  },
};
</script>

<style scoped>
.head {
  width: 100%;
  margin-left: 40px;
  text-align: left;
}
</style>