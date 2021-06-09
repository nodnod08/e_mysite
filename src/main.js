import Vue from "vue/dist/vue.js";

// Account
import loginPage from "./components/Pages/Account/Login";

const app = new Vue({
  el: "#app",
  components: {
    loginPage,
  },
});
