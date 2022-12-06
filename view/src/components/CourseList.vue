<template>
  <div class="head">
    <h2>Your Courses:</h2>
  </div>
  <div class="list" :key="course.courseName" v-for="course in courses">
    <CourseComp :course="course" />
  </div>
</template>

<script>
/* eslint-disable */
import CourseComp from './CourseComp.vue';

export default {
    name: "CourseList",
    props: {
      // CourseList recieves an array of course objects
      // and will render each as a CourseComp
      courses: Array,
    },
    components: {
      CourseComp,
    },
};
</script>

<style scoped>
.head {
  width: 100%;
  margin-left: 40px;
  text-align: left;
}
.list {
  width: 90%;
  padding:5px;
  margin: 5px auto;
  border: 2px solid black;
  border-radius: 8px;
  justify-content: space-between;
  align-items: center;
}
</style>