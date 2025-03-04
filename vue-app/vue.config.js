const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false, // Disable ESLint during build
  devServer: {
    proxy: {
      '/users/api': {
        target: 'http://localhost:8000', // Django server URL for user endpoints
        changeOrigin: true,
      },
      '/search/api': {
        target: 'http://localhost:8000', // Django server URL for search endpoints
        changeOrigin: true,
      },
    }
  },
  chainWebpack: config => {
    if (config.has('eslint')) {
      config.plugin('eslint').tap(args => {
        if (args && args[0] && args[0].extensions) {
          delete args[0].extensions;
        }
        return args;
      });
    }
  }
});
