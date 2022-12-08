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
      // answer NON PLURAL  => {q_id:<num>,answer:"t/f/x", ...}
      // answers PLURAL     => [{q_id:<num>,answer:"t/f/x", ...}, ...]
      // grade   NON PLURAL => {student_id: <num>, answers:[{q_id:<num>,answer:"t/f/x", ...}, ...]}
      // grades  PLURAL     => [{student_id: <num>, answers:[{q_id:<num>,answer:"t/f/x", ...}, ...]}, ... ]
      grades: [{"student_id":10, "answers":[{"question_id":10,"answer":"t"},{"question_id":9,"answer":"t"},{"question_id":8,"answer":"t"},{"question_id":7,"answer":"t"},{"question_id":6,"answer":"t"}]},{"student_id":10, "answers":[{"question_id":10,"answer":"t"},{"question_id":9,"answer":"t"},{"question_id":8,"answer":"t"},{"question_id":7,"answer":"t"},{"question_id":6,"answer":"t"}]},{"student_id":10, "answers":[{"question_id":10,"answer":"t"},{"question_id":9,"answer":"t"},{"question_id":8,"answer":"t"},{"question_id":7,"answer":"t"},{"question_id":6,"answer":"t"}]},{"student_id":10, "answers":[{"question_id":10,"answer":"t"},{"question_id":9,"answer":"t"},{"question_id":8,"answer":"t"},{"question_id":7,"answer":"t"},{"question_id":6,"answer":"t"}]}]
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
