import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import './index.css'

const app = createApp(App)

// Axios
import axios from "axios";
axios.defaults.baseURL = 'https://moonquake-map-back-end.vercel.app/'

app.use(router)

app.mount('#app')
