<template>
  <div>
    <h1>User Login</h1>
    <!-- The form submission is handled by the submitLogin method -->
    <form class="form-with-validation" @submit.prevent="submitLogin">
      <div class="form-group">
        <label for="username">Username:</label>
        <input 
          type="text" 
          id="username" 
          v-model="form.username" 
          required 
          class="form-control"
        />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input 
          type="password" 
          id="password" 
          v-model="form.password" 
          required 
          class="form-control"
        />
      </div>
      <!-- If you need to send a "next" parameter, you could include it as hidden input -->
      <button type="submit" class="form-submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'LoginPage',
  data() {
    return {
      form: {
        username: '',
        password: '',
      }
    };
  },
  methods: {
    async submitLogin() {
      try {
        const response = await axios.post('/users/api/login/', this.form);
        if (response.data.success) {
          console.log('Login successful:', response.data.message);
          await this.$store.dispatch('checkAuthStatus');
          this.$router.push({ name: 'Search' });
        } else {
          console.error('Login errors:', response.data.errors);
        }
      } catch (error) {
        console.error('Login error:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Component-specific styles can be added here, or rely on your global CSS */
</style>
