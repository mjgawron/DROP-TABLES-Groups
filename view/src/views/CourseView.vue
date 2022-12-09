<template>
  <div>
    <h1>{{ course_name }}</h1>
    <CourseTabs />
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
      course_name: "",
    }
  },
  beforeMount() {
    axios.get("/course/" + this.$router.currentRoute.value.params.course_id).then((response) => {
      this.course_name = response.data.name;
    });
  },
};
</script>
