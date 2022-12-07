<template>
  <div>
    <div class="head">
      <h2>{{ message }}</h2>
    </div>
    <div class="list" :key="grade.name" v-for="grade in grades">
      <GradeComp :gradeFixed="fixGrades(grade)" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import GradeComp from './GradeComp.vue';

export default {
    name: "GradeList",
    props: {
      // GradeList recieves an array of grade objects
      // and will render each as a GradeComp
      message: String,
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