<template>
  <div>
    <h1>Course View</h1>
    <CourseTabs />
    <!--Here we have to pass props through the router into QuestionTab.vue-->
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
  // NEED TO GET THE COURSE ID, RIGHT NOW ITS THE EMPTY STRING
  beforeMount() {
    // api should return a boolean, true if the user is an instructor, false otherwise
    // if the user is an instructor, QuestionTab should display a list of questions they've created
    // if the user is a student, QuestionTab should open a WebSocket connection, and show questions and live timer.
    axios.get("/course/" + this.course_id + "/instructor").then((response) => {
      this.isInstructor = response.data;
      // push params/state to the Vue Router Here
    });
  },
};
</script>
