<template>
  <div class="grade">
    <div class="info">
      <h2>{{ course.name }}</h2>
      <h4>{{ course.instructors.values[0] }}</h4>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

export default {
  name: "GradeComp",
  props: {
    course: Object,
  },
  methods: {
    enter() {
      if (this.action == "Join") {
        axios.post("/course/" + this.course.id + "/join").then(() => {
          this.$router.push("/course/" + this.id);
        });
      } else {
        this.$router.push("/course/" + this.id);
      }
    },
  },
};
</script>

<!--GET   /api/course             gets all courses-->
<!--GET   /api/coursse/<id>       gets specific course-->
<!--POST  /api/course/<id>/join   join specific course-->

<style scoped>
.course {
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
.link {
  text-align: right;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
a {
  cursor: pointer;
  color: blue;
  text-decoration: underline;
}
</style>