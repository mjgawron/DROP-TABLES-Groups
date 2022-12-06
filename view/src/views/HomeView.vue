<template>
  <div class="home">
    <MenuBar :name="name" />
    <div class="container">
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
      name: "",
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

<style scoped>
.home {
  display: inline-flex;
  flex-direction: column;
  color: white;
  background-color: black;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  width: 95%;
}
.container {
  display: inline-flex;
  flex-direction: column;
  color: white;
  background-color: lightslategray;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  width: 100%;
}
</style>