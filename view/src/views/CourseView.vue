<template>
  <div class="course">
    <h1>Course View</h1>
    <CourseTabs />
    <!--Here we have to figure out how to pass props through the router-view,
      We will pass isInstructor as a prop to QuestionView.vue, and QuestionView.vue will look
      at the boolean, and If its true, QuestionView.vue will show InstructorQuestionView.vue
      and otherwise (false) QuestionView.vue will show StudentQuestionView.vue-->
    <RouterView></RouterView>
  </div>
</template>

<script>
import axios from "axios";
import CourseTabs from "../components/CourseTabs.vue";

export default {
  name: "CourseView",
  components: {
    CourseTabs,
  },
  data() {
    return {
      course_id: "",
      isInstructor: false,
    };
  },
  beforeMount() {
    // api should return a boolean, true if the user is an instructor, false otherwise
    // if the user is an instructor, QuestionTab should display a list of questions they've created
    // if the user is a student, QuestionTab should open a WebSocket connection, and show questions and live timer.
    axios.get("/course/" + this.course_id + "/instructor").then((response)=> {
      this.isInstructor = response.data;
    });
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
