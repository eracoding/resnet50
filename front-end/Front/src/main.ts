import { createApp } from "vue";
import { createPinia } from "pinia";
// import Vuesax from 'vuesax3'
import "./index.css";
// @ts-ignore
import axios from "axios";
import VueAxios from "vue-axios";
import App from "./App.vue";
import router from "./router";
import "vuesax3/dist/vuesax.css";

import "./assets/main.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(VueAxios, axios);
// app.use(Vuesax);

app.mount("#app");
