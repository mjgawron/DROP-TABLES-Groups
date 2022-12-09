<template>
  <div class="head">
    <div class="list" :key="student.username" v-for="student in students">
      <RosterComp :student="student" />
    </div>
  </div>
</template>

<script>
/* eslint-disable*/
import RosterComp from "./RosterComp.vue";

export default {
  name: "RosterList",
  props: {
    students: Array,
  },
  components: {
    RosterComp,
  },
}
</script>

<style scoped>
.head {
  width: 100%;
  margin-left: 40px;
  text-align: left;
}
</style>
