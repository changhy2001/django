<template>
  <div>
    <section v-if="meta">
      <h1>{{ meta.user_username }}</h1>
      <p>
        <strong>Credentials:</strong>
        <!-- Assume credentials is an array or object; adjust display accordingly -->
        {{ meta.credentials }}
      </p>
      <p>
        <strong>Questions:</strong>
        {{ meta.questions }}
      </p>
      <p>
        <strong>Session Info:</strong>
        {{ meta.session_info }}
      </p>
      <p>
        <small class="text-muted">Last Updated: {{ meta.updated_at }}</small>
      </p>
    </section>
    <section v-else>
      <p>Loading user details...</p>
    </section>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SearchDetail',
  data() {
    return {
      meta: null,
      error: null
    };
  },
  mounted() {
    // Retrieve the username from route params
    const username = this.$route.params.username;
    axios.get(`/search/api/${username}/`)
      .then(response => {
        this.meta = response.data;
      })
      .catch(error => {
        console.error('Error fetching user detail:', error.response ? error.response.data : error);
        this.error = "Error loading user details.";
      });
  }
};
</script>

<style scoped>
/* Add component-specific styles as needed */
</style>
