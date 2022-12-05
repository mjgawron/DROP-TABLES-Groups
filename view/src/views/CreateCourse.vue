<template>
  <div class="course_create">
    <form @submit="createCourse">
      <label for="name-field">Course Name:</label>
      <input type="text" id="name-field" name="name" v-model="name" required />
      <label for="description-field">Course Description:</label>
      <input
        type="text"
        id="description-field"
        name="description"
        v-model="description"
        required
      />
      <button>Register Course</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CreateCourse",
  data() {
    return {
      name: "",
      description: "",
    };
  },
  methods: {
    createCourse(e) {
      e.preventDefault();
      const courseData = {
        name: this.name,
        description: this.description,
      };
      axios.post("/course", courseData).then((r) => {
        const response = JSON.parse(r);
        const id = toString(response[0]);
        this.$router.push("/course/" + id);
      });
    },
  },
};
</script>

<style scoped>
.course_create {
  display: inline-flex;
  flex-direction: column;
  text-align: left;
}
form {
  display: inline-flex;
  flex-direction: column;
  text-align: left;
}
</style>
