<template>
  <div class="course">
    <div class="info">
      <h2>{{ courseName }}</h2>
      <h4>{{ instructor }}</h4>
    </div>
    <div class="link">
      <a href="/">{{ action }}</a>
    </div>
  </div>
</template>

<script>
export default {
  name: "CourseComp",
  props: {
    courseName: String,
    instructor: String,
    action: String,
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
  display: flex;
  justify-content: space-between;
}
.info {
  text-align: left;
}
.link {
  text-align: right;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
