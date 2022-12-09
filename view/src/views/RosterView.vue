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
  data() {
    return {
      students: [],
    }
  },
  beforeMount() {
    axios.get("/course/" + this.$router.currentRoute.value.params.course_id + "/roster").then((response)=> {
        this.students = response.data;
    });
  },
}
</script>
