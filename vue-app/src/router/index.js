import { createRouter, createWebHistory } from 'vue-router';
import HomePage from '../views/HomePage.vue'; // your Home component
import AboutPage from '../views/AboutPage.vue'; // your About component
import SearchPage from '../views/SearchPage.vue';
import SearchDetail from '../views/SearchDetail.vue';
import LoginPage from '../views/LoginPage.vue'; // if needed
import RegisterPage from '../views/RegisterPage.vue'; // if needed

const routes = [
  { path: '/', name: 'Home', component: HomePage },
  { path: '/about', name: 'About', component: AboutPage },
  { path: '/search', name: 'Search', component: SearchPage },
  { path: '/search/detail/:username', name: 'SearchDetail', component: SearchDetail },
  { path: '/login', name: 'Login', component: LoginPage },
  { path: '/register', name: 'Register', component: RegisterPage }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
