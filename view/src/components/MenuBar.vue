<template>
  <div class="menubar">
    <img src="../assets/propellerhat.jpg" alt="jesse" width="50" height="50" />
    <h3>Welcome, {{ name }}</h3>
    <div class="dropdown">
      <button @click="onToggle" class="toolbar-button">{{ buttonChar }}</button>
      <router-link to="/join" v-if="toggle" class="toolbar-button"
        >Join</router-link
      >
      <router-link to="/create" v-if="toggle" class="toolbar-button"
        >Create</router-link
      >
    </div>
  </div>
</template>

<script>
/* eslint-disable */
export default {
    name: "MenuBar",
    data() {
      return {
        toggle: false,
        buttonChar: "+",
      }
    },
    props: {
      name: String,
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
  background-color: black;
  justify-content:space-evenly;
  align-items: center;
  align-self: center;
  width: 100%;
}
.dropdown {
  background-color: slategray;
}
.toolbar-button {
  padding: 5px;
}
</style>