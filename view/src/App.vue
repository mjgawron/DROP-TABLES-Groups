<template>
  <div>
    <nav class="mainmenu">
      <router-link to="/">Home</router-link>
      <router-link v-if="!loggedIn" to="/login">Login</router-link>
      <router-link v-if="!loggedIn" to="/register">Register</router-link>
      <a @click="logout" v-if="loggedIn">Logout</a>
    </nav>
    <div class="main">
      <router-view />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

export default {
  name: "App",
  data() {
    return {};
  },
  computed: {
    loggedIn() {
      return this.$route.name != "login" && this.$route.name != "register"
    },
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
.mainmenu {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  padding: 30px;
  color: white;
  background-color: darkslategray;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  width: 100%;
  box-sizing: border-box;
}
.main {
  margin-top: 120px;
}
</style>