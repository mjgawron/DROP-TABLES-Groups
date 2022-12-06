<template>
  <div class="course">
    <div class="info">
      <h2>{{ course.courseName }}</h2>
      <h4>{{ course.instructor }}</h4>
    </div>
    <div class="link">
      <a href="/">{{ course.action }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseComp",
  props: {
    course: Object,
  },
};
</script>

<style scoped>
.course {
  width: 60%;
  padding: 20px;
  margin: 20px auto;
  border: 2px solid black;
  border-radius: 8px;
}
.info {
  text-align: left;
}
.link {
  text-align: right;
}
</style>
