<template>
  <div class="course">
    <h1>Course View</h1>
    <CourseTabs />
    <RouterView></RouterView>
  </div>
</template>

<script>
// import axios from "axios";
import CourseTabs from "../components/CourseTabs.vue";

export default {
  name: "CourseView",
  components: {
    CourseTabs,
  },
  data() {
    return {
      id: "",
    };
  },
};
</script>

<style scoped>
.login {
  display: inline-flex;
  flex-direction: column;
  min-width: 450px;
}
.error {
  color: red;
}
form {
  display: inline-flex;
  flex-direction: column;
  text-align: left;
}
</style>
