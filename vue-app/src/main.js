import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from 'axios';

import './assets/css/style.css';

axios.defaults.withCredentials = true;

const app = createApp(App);
app.use(router);
app.use(store);
app.mount('#app');

// Load auth state from local storage and then check auth status from backend
store.dispatch('loadAuthFromLocalStorage');
store.dispatch('checkAuthStatus');