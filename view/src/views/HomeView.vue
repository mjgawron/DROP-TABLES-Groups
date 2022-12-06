<template>
  <div class="home">
    <MenuBar username="" />
    <div class="container">
      <!-- Here we want to set courses equal to the method call of getCourses() -->
      <CourseList :courses="courses" />
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
      username: "",
      courses: []
    }
  },
  components: {
    MenuBar,
    CourseList,
  },
  beforeMount() {
    axios.get("/api/course")
      .then((response) => {
        this.courses = response.data
      })
      .catch(() => { 
        console.log("HomeView.vue => getCourses() => catch ERROR")
    });
    axios.get("/account/status")
      .then((response) => {
        this.username = response.data.name
      })
      .catch(() => { 
        console.log("HomeView.vue => getCourses() => catch ERROR")
    });
  },
  // methods: {
  //   getCourses() {
  //     axios.get("/api/course")
  //     .then((response) => {
  //       this.courses = response.data
  //     })
  //     .catch(() => { 
  //       console.log("HomeView.vue => getCourses() => catch ERROR")
  //     });
  //   },
  // },
};
</script>

<style scoped>
.home {
  display: inline-flex;
  flex-direction: column;
  color: white;
  background-color: darkslategray;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  width: 95%;
}
.container {
  display: inline-flex;
  flex-direction: column;
  color: white;
  background-color: gray;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  width: 100%;
}
</style>