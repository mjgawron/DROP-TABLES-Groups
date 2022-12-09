<template>
  <div>
    <h3>Question:</h3>
    <p>{{ question.question_detail }}</p>
    <div class="submissionForm">
      <form @submit="sendChoice">
        <div class="a">
          <input
            type="radio"
            :id="'radio_a' + question.id"
            name="a"
            v-model="choice"
            value="a"
          />
          <label :for="'radio_a' + question.id">A: {{ question.answer_a }}</label>
        </div>

        <div class="b">
          <input
            type="radio"
            :id="'radio_b'+ question.id"
            name="b"
            v-model="choice"
            value="b"
          />
          <label :for="'radio_b' + question.id">B: {{ question.answer_b }}</label>
        </div>

        <div class="c">
          <input
            type="radio"
            :id="'radio_c' + question.id"
            name="c"
            v-model="choice"
            value="c"
          />
          <label :for="'radio_c' + question.id">C: {{ question.answer_c }}</label>
        </div>

        <div class="d">
          <input
            type="radio"
            :id="'radio_d' + question.id"
            name="d"
            v-model="choice"
            value="d"
          />
          <label :for="'radio_d' + question.id">D: {{ question.answer_d }}</label>
        </div>

        <button>Submit Answer</button>
      </form>
    </div>
    <div class="timer">Time Remaining: {{ timeRemaining }}</div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

export default {
  name: "QuestionComp",
  data() {
    return {
      choice: "",
      timeRemaining: 0,
    };
  },
  props: {
    question: Object(),
  },
  methods: {
    sendChoice(e) {
      e.preventDefault();
      const submissionData = {
        choice: this.choice,
        action: "submit",
      };
      this.socket.send(JSON.stringify(submissionData));
    },
  },
  mounted() {

    this.socket = new WebSocket(
      'ws://' + window.location.host + '/api/ws/' + this.question.id
      );
    this.socket.onmessage = (ws_message) => {
      const message = JSON.parse(ws_message.data);
      const messageType = message.action;

      switch (messageType) {
        case 'timer':
          this.timeRemaining = message.timeRemaining;
      }
    }
  },
};
</script>

<style scoped>
.submissionForm {
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
