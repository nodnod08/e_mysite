import Vue from "vue/dist/vue.js";
import JQuery from "jquery";
window.$ = JQuery;

window.axios = require("axios");

axios.defaults.xsrfHeaderName = "X-CSRFToken";

// Account
import loginPage from "./components/Pages/Account/Login";

// Dashboard
import dashboardPage from "./components/Pages/Dashboard";

// Product
import productPage from "./components/Pages/Products";
import productImportPage from "./components/Pages/Products/Import";

const app = new Vue({
  el: "#app",
  components: {
    loginPage,
    dashboardPage,
    productPage,
    productImportPage
  }
});
