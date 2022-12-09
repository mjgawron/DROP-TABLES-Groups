<template>
  <div class="member">
    <div class="info">
      <h1>Name: {{ student.name }}</h1>
      <h4>Username: {{ student.username }}</h4>
    </div>
  </div>
</template>

<script>
/* eslint-disable*/
export default {
  name: "RosterComp",
  props: {
    student: Object,
  },
}
</script>

<style scoped>
.member {
  width: 60%;
  padding: 20px;
  margin: 20px auto;
  border: 2px solid black;
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
}
.info {
  text-align: left;
}
</style>
