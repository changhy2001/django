<template>
  <div>
    <h1>Register a New User</h1>
    <form class="form-with-validation" @submit.prevent="submitRegister">
      <!-- Username Field -->
      <div class="form-group">
        <label for="username">Username:</label>
        <p class="helptext">
          Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
        </p>
        <input
          type="text"
          id="username"
          v-model="form.username"
          required
          class="form-control"
        />
      </div>

      <!-- Password Field -->
      <div class="form-group">
        <label for="password">Password:</label>
        <p class="helptext">
          Your password can't be too similar to your other personal information.<br />
          Your password must contain at least 8 characters.<br />
          Your password can't be a commonly used password.<br />
          Your password can't be entirely numeric.
        </p>
        <input
          type="password"
          id="password"
          v-model="form.password"
          required
          class="form-control"
        />
      </div>

      <!-- Password Confirmation Field -->
      <div class="form-group">
        <label for="confirmPassword">Password confirmation:</label>
        <p class="helptext">
          Enter the same password as before, for verification.
        </p>
        <input
          type="password"
          id="confirmPassword"
          v-model="form.confirmPassword"
          required
          class="form-control"
        />
      </div>

      <!-- Submit Button -->
      <button type="submit" class="form-submit">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      form: {
        username: '',
        password: '',
        confirmPassword: ''
      }
    };
  },
    methods: {
      async submitRegister() {
        // Basic client-side check to ensure passwords match
        if (this.form.password !== this.form.confirmPassword) {
          console.error('Passwords do not match');
          return;
        }

        // Prepare data for the API to match UserCreationForm fields
        const requestData = {
          username: this.form.username,
          password1: this.form.password,
          password2: this.form.confirmPassword
        };

        try {
          const response = await axios.post('/users/api/register/', requestData);
          if (response.data.success) {
            console.log('Registration successful:', response.data.message);
            await this.$store.dispatch('checkAuthStatus');
            this.$router.push({ name: 'Search' });
          } else {
            console.error('Registration errors:', response.data.errors);
          }
        } catch (error) {
          if (error.response) {
            console.error('Registration error:', error.response.data);
          } else {
            console.error('Registration error:', error);
          }
        }
      }
    }
};
</script>

<style scoped>
/* Component-specific styles can be added here, or rely on your global CSS */
</style>
