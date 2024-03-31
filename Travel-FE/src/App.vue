<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'
import { useAppStore } from './stores/appStore'
import { createApp, watch } from "vue";
import axios from 'axios';

// Add a request interceptor
axios.interceptors.request.use(
  function (config) {
    const token = sessionStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

const appStore = useAppStore();
console.log("App",sessionStorage.getItem('token'));

appStore.setUserIsLoggedIn(sessionStorage.getItem('token') ? true : false);
appStore.setRootUrl('http://localhost:5000');
</script>

<template>
<div class="app">
  <div class="header">
    <Header />
  </div>
  <div class="pages">
    <RouterView />
  </div>
  <div class="footer">
    <Footer />
  </div>
</div>
</template>

<style scoped>
.footer{
  margin-top: 2%;
  width: 100%;
  margin-bottom: 0px;
}

.pages{
  margin-top: 100px;
  z-index: 0;
}

.app{
  display: grid;
  width: 99vw;
  max-width: 100%;
}

.header {
  z-index: 1;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
