<template>
  <div>
    <div class="head">
      <h2>{{ message }}</h2>
    </div>
    <div class="list" :key="course.courseName" v-for="course in courses">
      <CourseComp :course="course" :id="id" />
    </div>
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
      message: String,
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
</style>