<template>
  <div class="account">
    <span v-if="invalidChange" class="error">
      Invalid Name. Please try again.
    </span>
    <form @submit="changeName">
      <label for="name-field">Name</label>
      <input type="text" id="name-field" name="name" v-model="name" required />
      <button>Change Name</button>
    </form>
  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

export default {
  name: "AccountView",
  data() {
    return {
      name: "",
      invalidChange: false,
    };
  },
  methods: {
    changeName(e) {
      e.preventDefault();
      const accountData = {
        name: this.name,
      };
      axios
        .put("/account", accountData)
        .then(() => {
          this.$router.push("/");
        })
        .catch(() => {
          this.invalidChange = true;
        });
    },
  },
};
</script>

<style scoped>
.account {
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