<template>
  <div class="register">
    <div class="image">
      <img alt="Jesse ballcap" src="../assets/propellerhat.jpg" />
    </div>
    <span v-if="invalidRegistration" class="error">
      Invalid registration. Please try again.
    </span>
    <form @submit="register">
      <label for="name-field">Name</label>
      <input type="text" id="name-field" name="name" v-model="name" required />
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
      <button>Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterView",
  data() {
    return {
      username: "",
      password: "",
      name: "",
      invalidRegistration: false,
    };
  },
  methods: {
    register(e) {
      e.preventDefault();
      const registerData = {
        username: this.username,
        password: this.password,
        name: this.name,
      };
      axios
        .post("/account/register", registerData)
        .then(() => {
          this.$router.push("/");
        })
        .catch(() => {
          this.invalidRegistration = true;
        });
    },
  },
};
</script>

<style scoped>
.register {
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
