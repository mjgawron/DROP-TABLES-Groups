<template>
  <div class="tab">
    <div class="chat-history" v-for="chat of chatHistory" v-bind:key="chat.id">
      <div class="chat">
        <span class="user"> {{ chat.user }}: </span>
        <span class="message"> {{ chat.message }} </span>
      </div>
    </div>
    <form @submit="sendMessage" class="send-chat">
      <input type="text" class="message-input" v-model="newMessage" />
      <button>Send</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "ChatTab",
  data() {
    return {
      newMessage: "",
      chatHistory: [],
      id: "",
    };
  },
  beforeMount() {
    this.id = this.$router.currentRoute.value.params.course_id;
    this.fetchMessages();
  },
  methods: {
    fetchMessages() {
      axios.get("/course/" + this.id + "/chat").then((response) => {
        this.chatHistory = response.data;
      });
    },
    sendMessage(e) {
      e.preventDefault();
      const messageData = {
        message: this.newMessage,
      };
      this.newMessage = "";
      axios.post("/course/" + this.id + "/chat", messageData).then(() => {
        this.fetchMessages();
      });
    },
  },
};
</script>

<style scoped>
.chat-history {
  text-align: left;
}
.send-chat {
  display: flex;
}

.message-input {
  width: 100%;
}
</style>
