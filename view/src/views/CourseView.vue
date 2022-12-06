<template>
  <div class="course">
    <h1>Course View</h1>
    <RouterView></RouterView>
  </div>
</template>

<script>
// import axios from "axios";

export default {
  name: "CourseView",
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
