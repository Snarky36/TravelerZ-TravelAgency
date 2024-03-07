<script setup lang="ts">
import {RouterLink, RouterView} from 'vue-router'
</script>

<template>
    <div class="header">
      <img
        src="@/assets/ExplorerZ.jpg"
        class="logo-img"
      />
      <nav>
        <RouterLink class="header-text" to="/">Home</RouterLink>
        <RouterLink class="header-text" to="/destinations">Destinations</RouterLink>
        <RouterLink class="header-text" to="/contact">Contact</RouterLink>
        <RouterLink class="header-text" to="/login">Log in</RouterLink>
      </nav>
    </div>
  </template>
  
  
  
  <style scoped>
  .header {
    background-color: white;
    position: fixed;
    top:0;
    justify-content: space-between;
    align-self: center;
    display: flex;
    width: 100%;
    max-width: 100%;
    gap: 500px;
    font-size: 16px;
    color: #1e1e1e;
    font-weight: 400;
    line-height: 29px;
    padding: 11px 0;
  }
  @media (max-width: 991px) {
    .div {
      max-width: 100%;
      flex-wrap: wrap;
    }
  }
  .logo-img {
    aspect-ratio: 2;
    object-fit: auto;
    object-position: center;
    width: 178px;
    max-width: 100%;
  }

  
  nav {
    justify-content: space-between;
    display: flex;
    gap: 20px;
    margin: auto 0;
    padding: 10px 20px;
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

  .header-text {
    font-size: 1.5rem;
    font-family: Poppins, sans-serif;
  }
  .sticky {
  position: fixed;
  top: 0;
  width: 100%;
}
  </style>