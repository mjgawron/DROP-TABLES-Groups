<template>
  <div class="home">
    <MenuBar :name="name" />
    <div class="container">
      <CourseList :courses="courses" action="Enter" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";
import MenuBar from "../components/MenuBar.vue";
import CourseList from "../components/CourseList.vue";

export default {
  name: "HomeView",
  data() {
    return {
      name: "",
      courses: []
    }
  },
  components: {
    MenuBar,
    CourseList,
  },
  beforeMount() {
    axios.get("/course/member")
      .then((response) => {
        this.courses = response.data
      })
      .catch(() => { 
        console.log("HomeView.vue => beforeMount() => catch ERROR")
    });
    axios.get("/account/status")
      .then((response) => {
        this.name = response.data.name
      })
      .catch(() => {
        console.log("HomeView.vue => beforeMount() => catch ERROR")
    });
  },
};
</script>