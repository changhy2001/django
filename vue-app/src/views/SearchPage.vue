<template>
  <div>
    <h2>Search</h2>
    <!-- Search Form -->
    <form @submit.prevent="performSearch">
      <!-- Search Query -->
      <div class="form-row">
        <div class="form-group col-12">
          <div class="input-group">
            <input
              class="form-control py-2 border-right-0 border"
              type="search"
              v-model="query.q"
              placeholder="Search users or questions..."
            />
          </div>
        </div>
      </div>

      <!-- Filter Options -->
      <div class="form-row">
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.username_contains" placeholder="Username contains...">
        </div>
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.credentials_contains" placeholder="User credentials...">
        </div>
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.questions_contains" placeholder="Question contains...">
        </div>
        <div class="form-group col-md-3">
          <input type="text" class="form-control" v-model="query.session_info_contains" placeholder="Session info contains...">
        </div>
      </div>

      <!-- Date Range Filters -->
      <div class="form-row">
        <div class="form-group col-md-3">
          <label for="created_at_min" class="small-label">Created At (Min)</label>
          <input type="date" class="form-control" id="created_at_min" v-model="query.created_at_min">
        </div>
        <div class="form-group col-md-3">
          <label for="created_at_max" class="small-label">Created At (Max)</label>
          <input type="date" class="form-control" id="created_at_max" v-model="query.created_at_max">
        </div>
        <div class="form-group col-md-3">
          <label for="updated_at_min" class="small-label">Updated At (Min)</label>
          <input type="date" class="form-control" id="updated_at_min" v-model="query.updated_at_min">
        </div>
        <div class="form-group col-md-3">
          <label for="updated_at_max" class="small-label">Updated At (Max)</label>
          <input type="date" class="form-control" id="updated_at_max" v-model="query.updated_at_max">
        </div>
      </div>

      <!-- Search Button -->
      <button type="submit" class="btn btn-primary btn-block">Search</button>
    </form>

    <!-- Search Results -->
    <div v-if="results.length > 0">
      <div class="small-break"></div>
      <p>Results: {{ results.length }}</p>
      <div class="small-break"></div>
      <div class="row">
        <div v-for="(meta, index) in results" :key="index" class="col-md-6 col-lg-4">
          <div class="card mb-4">
            <div class="card-body">
              <h5 class="card-title">
                <router-link :to="{ name: 'SearchDetail', params: { username: meta.user_username } }">
                  User: {{ meta.user_username }}
                </router-link>
              </h5>
              <p class="card-text">
                <strong>Credentials:</strong> {{ formatCredentials(meta.credentials) }}
              </p>
              <p class="card-text">
                <strong>Questions:</strong> {{ meta.questions.join(', ') }}
              </p>
              <p class="card-text">
                <strong>Session Info:</strong> {{ meta.session_info }}
              </p>
              <p class="card-text">
                <small class="text-muted">Last Updated: {{ meta.updated_at }}</small>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div v-else>
      <p>No results found.</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "SearchPage",
  data() {
    return {
      query: {
        q: "",
        username_contains: "",
        credentials_contains: "",
        questions_contains: "",
        session_info_contains: "",
        created_at_min: "",
        created_at_max: "",
        updated_at_min: "",
        updated_at_max: ""
      },
      results: []
    }
  },
  mounted() {
    Object.assign(this.query, this.$route.query);
    this.performSearch();
  },
  methods: {
    performSearch() {
      axios.get('/search/api/', { params: this.query })
        .then(response => {
          this.results = response.data;
          this.$router.push({ query: this.query });
        })
        .catch(error => {
          console.error('Error during search:', error);
        });
    },
    formatCredentials(credentials) {
      if (Array.isArray(credentials)) {
        return credentials.join(', ');
      } else if (typeof credentials === 'object') {
        return JSON.stringify(credentials);
      }
      return credentials;
    }
  }
};
</script>

<style scoped>
/* Add component-specific styles if needed */
</style>