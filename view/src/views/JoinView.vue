<template>
  <div class="join">
    <h1>Available Courses</h1>
    <hr style="width: 65%" />
    <CourseList :courses="courses" />
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
      courses: [
        // { courseName: "CSE-312", instructor: "J.Hartloff", action: "Join" },
        // { courseName: "CSE-370", instructor: "A.Hunt", action: "Join" },
      ],
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
