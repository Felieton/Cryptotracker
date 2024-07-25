import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import Dashboard from "../views/Dashboard.vue";
import CurrencyDetails from "../views/CurrencyDetails";
import Hot from "../views/Hot.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/hot",
    name: "Hot",
    component: Hot,
  },
  {
    path: "/crypto/:code",
    name: "CurrenyDetails",
    component: CurrencyDetails,
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;