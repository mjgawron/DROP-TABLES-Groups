<template>
  <div class="join">
    <h1>Available Courses</h1>
    <hr style="width: 65%" />
    <CourseList :courses="courses" action="Join" />
  </div>
</template>

<script>
// @ is an alias to /src
import CourseList from "@/components/CourseList.vue";
import axios from "axios";

export default {
  name: "JoinView",
  components: {
    CourseList,
  },
  data() {
    return {
      courses: [],
    };
  },
  beforeMount() {
    // make api req
    axios.get("course/user/joinable").then((response) => {
      this.courses = response.data;
    });
  },
};
</script>
