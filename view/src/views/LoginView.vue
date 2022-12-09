<template>
  <div class="login">
    <div class="image">
      <img alt="Jesse ballcap" src="../assets/propellerhat.jpg" />
    </div>
    <span v-if="invalidLogin" class="error">
      Unable to login. Please try again.
    </span>
    <form @submit="login">
      <label for="username-field">Username</label>
      <input
        type="text"
        id="username-field"
        name="username"
        v-model="username"
        required
      />
      <label for="password-field">Password</label>
      <input
        type="password"
        id="password-field"
        name="password"
        v-model="password"
        required
      />
      <button>Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      invalidLogin: false,
    };
  },
  methods: {
    login(e) {
      e.preventDefault();
      const loginData = {
        username: this.username,
        password: this.password,
      };
      axios
        .post("/account/login", loginData)
        .then(() => {
          this.$router.push("/");
        })
        .catch(() => {
          this.invalidLogin = true;
        });
    },
  },
};
</script>

<style scoped>
.login {
  display: inline-flex;
  flex-direction: column;
  min-width: 450px;
}
.error {
  color: red;
}
.image {
  justify-content: center;
}
form {
  display: inline-flex;
  flex-direction: column;
  text-align: left;
}
img {
  width: 200px;
}
</style>
