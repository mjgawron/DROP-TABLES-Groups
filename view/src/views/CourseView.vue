<template>
  <div>
    <CourseTabs />
    <RouterView></RouterView>
  </div>
</template>

<script>
import CourseTabs from "../components/CourseTabs.vue";

export default {
  name: "CourseView",
  components: {
    CourseTabs,
  },
};
</script>
