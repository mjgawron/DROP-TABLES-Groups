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
  props: {
    id: Number,
  },
  components: {
    CourseTabs,
    GradeList,
  },
  beforeMount() {
    // Before this component is mounted GET the grades for this user
    // answer  NON PLURAL => {q_id:<num>,answer:"t/f/x", ...}
    // answers PLURAL     => [{q_id:<num>,answer:"t/f/x", ...}, ...]
    // grade   NON PLURAL => {student_id: <num>, answers:[{q_id:<num>,answer:"t/f/x"}, ...]}
    // grades  PLURAL     => [{student_id: <num>, answers:[{q_id:<num>,answer:"t/f/x"}, ...]}, ... ]
    axios.get("/submission/" + this.id + "/grades").then((response) => {
      grades = response.data
    });
  },
}
</script>
