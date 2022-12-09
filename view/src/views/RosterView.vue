<template>
  <div class="container">
    <RosterList :students="students" />
  </div>
</template>

<script>
/* eslint-disable*/
import axios from "axios";
import RosterList from "../components/RosterList.vue";

export default {
  name: "RosterView",
  components: {
    RosterList,
  },
  props: {
    course_id: String,
  },
  data() {
    return {
      students: [],
    }
  },
  beforeMount() {
    axios.get("/course/" + this.course_id + "/roster").then((response)=> {
        this.students = response.data;
    });
  },
}
</script>
