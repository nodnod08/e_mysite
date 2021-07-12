import Vue from "vue/dist/vue.js";

window.axios = require("axios");

axios.defaults.xsrfHeaderName = "X-CSRFToken";

// Account
import loginPage from "./components/Pages/Account/Login";

const app = new Vue({
  el: "#app",
  components: {
    loginPage,
  },
});
