import { createRouter, createWebHistory } from "vue-router";
import axios from "axios";
/* eslint-disable */
const routes = [
  {
    path: "/",
    name: "home",
    component: function () {
      return import(
        /* webpackChunkName: "home" */ "../views/HomeView.vue"
        );
    },
  },
  {
    path: "/login",
    name: "login",
    component: function () {
      return import(
        /* webpackChunkName: "login" */ "../views/LoginView.vue"
        );
    },
  },
  {
    path: "/register",
    name: "register",
    component: function () {
      return import(
        /* webpackChunkName: "register" */ "../views/RegisterView.vue"
      );
    },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  axios
    .get("/account/status")
    .then(() => {
      if (to.name !== "login" && to.name !== "register") next();
      else next("/");
    })
    .catch(() => {
      if (to.name !== "login" && to.name !== "register") next("login");
      else next();
    });
});

export default router;
