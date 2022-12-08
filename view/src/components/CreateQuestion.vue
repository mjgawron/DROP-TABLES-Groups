<template>
  <div class="container">
    <form @submit="makeQuestion">
      <label for="username-field">Question: </label>
      <input
        type="text"
        id="question_detail"
        name="question"
        v-model="question.question_detail"
        required
      />
      <br />
      <label for="answer_a">Choice A: </label>
      <input
        type="text"
        id="answer_a"
        name="answer_a"
        v-model="question.answer_a"
        required
      />
      <br />
      <label for="answer_b">Choice B: </label>
      <input
        type="text"
        id="answer_b"
        name="answer_b"
        v-model="question.answer_b"
        required
      />
      <br />
      <label for="answer_c">Choice C: </label>
      <input
        type="text"
        id="answer_c"
        name="answer_c"
        v-model="question.answer_c"
        required
      />
      <br />
      <label for="answer_d">Choice D: </label>
      <input
        type="text"
        id="answer_d"
        name="answer_d"
        v-model="question.answer_d"
        required
      />
      <br />
      <label for="time-field">Time (sec): </label>
      <input
        type="number"
        id="time"
        name="time"
        v-model="sock.time"
        required
      />
      <!---------------------------------------------->
      <p>Correct Answer:</p>
      <label for="radio_a">A</label>
      <input
        type="radio"
        id="answer_a"
        name="answer_a"
        v-model="question.answer"
        value="a"
      />
      <label for="radio_b">B</label>
      <input
        type="radio"
        id="answer_b"
        name="answer_b"
        v-model="question.answer"
        value="b"
      />
      <label for="radio_c">C</label>
      <input
        type="radio"
        id="answer_c"
        name="answer_c"
        v-model="question.answer"
        value="c"
      />
      <label for="radio_d">D</label>
      <input
        type="radio"
        id="answer_d"
        name="answer_d"
        v-model="question.answer"
        value="d"
      />
      <br />
      <button>Post Question</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "InstructorQuestionsTab",
  data() {
    return {
      question: Object,
      sock: Object,
    };
  },
  prop: {
    course_id: String,
  },
  methods: {
    makeQuestion(e) {
      e.preventDefault();
      // set field inside question object to the prop that was passed
      this.question.course_id = this.course_id;
      axios
        .post("/question", this.question)
        .then(() => {
          this.$router.push("/course/" + this.course_id);
        })
        .catch(() => {});
      sock.action = "start"
      const socket = new WebSocket('');
      socket.send(JSON.stringify(sock));
    },
  },
};
</script>

<style scoped>
.container {
  width: 100%;
  display: flex;
  flex-direction: column;
}
</style>
