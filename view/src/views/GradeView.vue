<template>
  <div class="tabs">
    <div class="list">
      <GradeList :grades="grades" />
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios"
import GradeList from "../components/GradeList.vue";
import CourseTabs from "../components/CourseTabs.vue";

export default {
  name: "GradeView",
  data() {
    return {
      grades: [],
    }
  },
  components: {
    CourseTabs,
    GradeList,
  },
  beforeMount() {
    axios.get("/submission/" + this.$router.currentRoute.value.params.course_id + "/grades").then((response) => {
      this.grades = response.data;
    });
  },
}
// answer  NON PLURAL => {question_id:<num>,correctness:t/f, ...}
// answers PLURAL     => [{question_id:<num>,correctness:t/f, ...}, ...]
// grade   NON PLURAL => {student_id: <num>, score_list:[{question_id:<num>,correctness:t/f, ...}, ...]}
// grades  PLURAL     => [{student_id: <num>, score_list:[{question_id:<num>,correctness:t/f, ...},...]}, ... ]
</script>

