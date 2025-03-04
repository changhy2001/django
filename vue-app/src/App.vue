<template>
  <div id="app">
    <nav>
      <!-- Navigation using Vue Router -->
      <router-link to="/" aria-label="Home" title="Home">🏠</router-link> |
      <router-link to="/about" aria-label="About" title="About">🗒️</router-link> |
      <!-- Render based on authentication state -->
      <template v-if="isAuthenticated">
        <router-link to="/search" aria-label="Search" title="Search">🔍</router-link> |
        <button @click="handleLogout" class="logout-button" aria-label="Logout" title="Logout">👋</button>
      </template>
      <template v-else>
        <router-link to="/register" aria-label="Register" title="Register">🔏</router-link> |
        <router-link to="/login" aria-label="Login" title="Login">🔐</router-link>
      </template>
    </nav>
    <main>
      <router-view />
    </main>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isAuthenticated', 'user'])
  },
  methods: {
    ...mapActions(['logout']),
    async handleLogout() {
      const success = await this.logout();
      if (success) {
        this.$router.push({ name: 'Home' });
      }
    }
  }
};
</script>

<style>
@import "@/assets/css/style.css";

nav {
  padding: 1rem;
  background-color: var(--primary-color);
  color: var(--white);
  font-size: 2.5rem;
}
.logout-button {
  background: transparent;
  border: none;
  cursor: pointer;
}
</style>
