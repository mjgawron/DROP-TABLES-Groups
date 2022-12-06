<template>
  <div class="menubar">
    <img src="../assets/propellerhat.jpg" alt="jesse" width="50" height="50" />
    <p>Welcome {{ name }}!</p>
    <div id="dropdown">
      <button @click="onToggle">{{ buttonChar }}</button>
      <button @click="onJoin" v-if="toggle">Join</button>
      <button @click="onCreate" v-if="toggle">Create</button>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
//import axios from 'axios';

export default {
    name: "MenuBar",
    data() {
      return {
        toggle: false,
        buttonChar: "+",
      }
    },
    props: {
      name: String
    },
    methods: {
      onToggle() {
        this.buttonChar = this.buttonChar == "+" ? "-" : "+";
        this.toggle = !this.toggle;
      },

      onJoin() {
        this.$router.push("/join")
      },

      onCreate() {
        this.$router.push("/create")
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