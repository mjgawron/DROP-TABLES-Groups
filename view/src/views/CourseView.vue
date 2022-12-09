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
  // Need to also get the course_id, right now it is blank
  beforeMount() {
    // api should return a boolean, true if the user is an instructor, false otherwise
    axios.get("/course/" + this.course_id + "/instructor").then((response) => {
      this.isInstructor = response.data;
      // push params/state to the Vue Router Here
    });
  },
};
</script>
