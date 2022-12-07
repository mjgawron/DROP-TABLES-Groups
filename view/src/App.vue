<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/login">Login</router-link> |
    <router-link to="/register">Register</router-link> |
    <a @click="logout">Logout</a>
  </nav>
  <router-view />
  <br />
  <CourseTabs />
  <CourseView />
  <QuestionTab />
  <QuestionList />
  <QuestionComp />
  <GradeComp />
  <GradeList />
  <GradeView />
</template>

<script>
/* eslint-disable */
import axios from "axios";
import CourseTabs from "./components/CourseTabs.vue";
import CourseView from "./views/CourseView.vue";
import QuestionTab from "./components/QuestionTab.vue";
import QuestionComp from "./components/QuestionComp.vue";
import QuestionList from "./components/QuestionList.vue";
import GradeComp from "./components/GradeComp.vue";
import GradeList from "./components/GradeList.vue";
import GradeView from "./views/GradeView.vue";

export default {
  name: "App",
  components: {
    CourseView,
    CourseTabs,
    QuestionList,
    QuestionComp,
    QuestionTab,
    GradeComp,
    GradeList,
  },
  methods: {
    logout() {
      axios.post("/account/logout").then(() => {
        this.$router.push("/login");
      });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
nav {
  padding: 30px;
  display: inline-flex;
  flex-direction: row;
  color: white;
  background-color: darkslategray;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  width: 95%;
}
nav a {
  font-weight: bold;
  color: white;
}
nav a.router-link-exact-active {
  color: #42b983;
}
</style>