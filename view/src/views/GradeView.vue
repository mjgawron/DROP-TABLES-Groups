<template>
  <div class="tabs">
    <CourseTabs />
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
      // answers NON PLURAL => {q_id:"t/f/x"}
      // answers PLURAL     => [{q_id:"t/f/x"}, ...]
      // grade   NON PLURAL => {student_id: <num>, answers:[{q_id:"t/f/x"}, ...]}
      // grades  PLURAL     => [{student_id: <num>, answers:[{q_id:"t/f/x"},...]}, ... ]
      grades: [{"student_id":10, "answers":[{"1":"t"}]}]
    }
  },
  props: {
    course_id: Number,
  },
  components: {
    CourseTabs,
    GradeList,
  },
}
</script>
