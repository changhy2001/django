import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    isAuthenticated: false,
    user: null,
    loading: false,
  },
  mutations: {
    SET_AUTH(state, payload) {
      state.isAuthenticated = payload.isAuthenticated;
      state.user = payload.user;
    },
    SET_LOADING(state, loading) {
      state.loading = loading;
    }
  },
  actions: {
    async checkAuthStatus({ commit }) {
      commit('SET_LOADING', true);
      try {
        const response = await axios.get('/users/api/auth-status/');
        console.log("Auth status response:", response.data);
        if (response.data.authenticated) {
          commit('SET_AUTH', { isAuthenticated: true, user: response.data.username });
          // Save to local storage
          localStorage.setItem('auth', JSON.stringify({
            isAuthenticated: true,
            user: response.data.username
          }));
        } else {
          commit('SET_AUTH', { isAuthenticated: false, user: null });
          localStorage.removeItem('auth');
        }
      } catch (error) {
        console.error('Auth status error:', error.response ? error.response.data : error);
        commit('SET_AUTH', { isAuthenticated: false, user: null });
        localStorage.removeItem('auth');
      } finally {
        commit('SET_LOADING', false);
      }
    },
    async login({ dispatch }, credentials) {
      try {
        const response = await axios.post('/users/api/login/', credentials);
        if (response.data.success) {
          // After successful login, update auth state (by calling checkAuthStatus, for example)
          await dispatch('checkAuthStatus');
          return true;
        } else {
          console.error('Login errors:', response.data.errors);
          return false;
        }
      } catch (error) {
        console.error('Login error:', error.response ? error.response.data : error);
        return false;
      }
    },
    async logout({ commit }) {
      try {
        const response = await axios.post('/users/api/logout/');
        if (response.data.success) {
          commit('SET_AUTH', { isAuthenticated: false, user: null });
          localStorage.removeItem('auth');
          return true;
        }
        return false;
      } catch (error) {
        console.error('Logout error:', error.response ? error.response.data : error);
        return false;
      }
    },
    // Load stored auth state on app startup
    loadAuthFromLocalStorage({ commit }) {
      const auth = localStorage.getItem('auth');
      if (auth) {
        const data = JSON.parse(auth);
        commit('SET_AUTH', { isAuthenticated: data.isAuthenticated, user: data.user });
      }
    }
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    user: (state) => state.user,
    loading: (state) => state.loading,
  }
});
