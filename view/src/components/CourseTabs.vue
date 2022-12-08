<template>
  <nav>
    <router-link to="questions">Questions</router-link>|
    <router-link to="chat">Chat</router-link>|
    <router-link to="grades">Gradebook</router-link>|
  </nav>
</template>

<script>
export default {
  name: "CourseTabs",
  props: {},
  methods: {},
};
</script>

<style>
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
