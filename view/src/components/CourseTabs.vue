<template>
  <nav>
    <router-link to="questions">Questions</router-link>
    <router-link to="chat">Chat</router-link>
    <router-link to="grades">Gradebook</router-link>
    <router-link to="roster">Roster</router-link>
  </nav>
</template>

<script>
/* eslint-disable */
export default {
  name: "CourseTabs",
};
</script>

<style scoped>
nav {
  padding: 30px;
  display: inline-flex;
  flex-direction: row;
  color: white;
  background-color: darkslategray;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  position: sticky;
  top: 78px;
}
nav a {
  font-weight: bold;
  color: white;
}
nav a.router-link-exact-active {
  color: #42b983;
}
</style>
