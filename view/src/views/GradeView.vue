<template>
  <div>
    <GradeList :grades="grades" />
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios"
export default {
  name: "GradeView",
  props: {
    course_id: Number,
  },
  data() {
    return {
      path: this.course_id,
    }
  },
  beforeMount() {
    path = "/" + this.course_id + "/grades"
    axios.get(path).then((response) => {
      
    });
  },
}
</script>
