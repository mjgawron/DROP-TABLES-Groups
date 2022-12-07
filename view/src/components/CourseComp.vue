<template>
  <div class="course">
    <div class="info">
      <h2>{{ course.name }}</h2>
      <h4>{{ course.instructors[0].name }}</h4>
    </div>
    <div class="link">
      <a @click="enter">{{ action }}</a>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CourseComp",
  props: {
    course: Object,
    action: String,
  },
  methods: {
    enter() {
      if (this.action == "Join") {
        axios.post("/course/" + this.course.id + "/join").then(() => {
          console.log("CourseComp() => enter() => if{...}");
          this.$router.push("/course/" + this.course.id + "/");
        });
      } else {
        console.log("CourseComp() => enter() => else{...}");
        this.$router.push("/course/" + this.course.id + "/");
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
