import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import Scrip from "../views/Scrip.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/scrip",
    name: "Scrip",
    component: Scrip,
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;
