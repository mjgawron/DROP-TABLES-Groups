<template>
  <div class="menubar">
    <img src="../assets/propellerhat.jpg" alt="jesse" width="50" height="50" />
    <p>Welcome {{ user }}</p>
    <div id="dropdown">
      <button @click="onToggle">{{ buttonChar }}</button>
      <button @click="onJoin" v-if="toggle">Join</button>
      <button @click="onCreate" v-if="toggle">Create</button>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import axios from 'axios';

export default {
    name: "MenuBar",
    data() {
      return {
        user: "",
        toggle: false,
        buttonChar: "+",
      }
    },
    methods: {
      onToggle() {
        this.buttonChar = this.buttonChar == "+" ? "-" : "+";
        this.toggle = !this.toggle;
      },

      onJoin() {
        //this.$router.push("/course-join")
      },

      onCreate() {
        //this.$router.push("/course-create")
      },

      // /account/status returns an object with username, name, and id
      isAuthentic() {
        axios.get("/account/status")
        .then((response) => {
          this.user = response.data.username
        })
        .catch(() => { 
          console.log("user is NOT authentic")
        });
      },
    },
};
</script>

<style scoped>
.menubar {
  display: flex;
  color: white;
  background-color: darkslategray;
  justify-content:space-evenly;
  align-items: center;
  align-self: center;
  width: 100%;
}
</style>