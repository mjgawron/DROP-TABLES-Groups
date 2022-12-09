<template>
  <div class="tabs">
    <div class="list">
      <GradeList :grades="grades" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
//import axios from "axios"
import GradeList from "../components/GradeList.vue";
import CourseTabs from "../components/CourseTabs.vue";

export default {
  name: "GradeView",
  data() {
    return {
      grades: [],
    }
  },
  props: {
    course_id: String,
  },
  components: {
    CourseTabs,
    GradeList,
  },
  beforeMount() {
    // Before this component is mounted get the grade of this user,
    // OR if you are an instructor; the grades of all enrolled students.
    axios.get("/submission/" + this.course_id + "/grades").then((response) => {
      grades = response.data;
    });
  },
}
// answer  NON PLURAL => {q_id:"t/f/x", ...}
// answers PLURAL     => [{q_id:"t/f/x", ...}, ...]
// grade   NON PLURAL => {student_id: <num>, answers:[{q_id:"t/f/x", ...}, ...]}
// grades  PLURAL     => [{student_id: <num>, answers:[{q_id:"t/f/x", ...},...]}, ... ]
</script>

