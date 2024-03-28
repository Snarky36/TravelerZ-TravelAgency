<template>
  <div class="header">
    <img src="@/assets/ExplorerZ.jpg" class="logo-img" />
    <nav>
      <div class="searchDiv">
        <div class="search-bar">
          <SearchBar @search="getSearchFilter" />
        </div>
      </div>
      <RouterLink class="header-text" to="/">Home</RouterLink>
      <div class="dropdown">
        <RouterLink class="header-text" to="/destinations">Destinations</RouterLink>
        <div class="dropdown-content">
          <RouterLink class="header-text button" to="/destinations#discounts">Discounts</RouterLink>
        </div>
      </div>
      <RouterLink class="header-text" to="/contact">Contact</RouterLink>
      <RouterLink v-if="!appStore.userIsLoggedIn" class="header-text" to="/login">Log in</RouterLink>
      <div v-if="appStore.userIsLoggedIn" class="dropdown">
        <i class="pi pi-user" style="font-size: 2.5rem; cursor: pointer;"></i>
        <div class="dropdown-content-user">
          <h3>Username: {{ userName }}</h3>
          <button class="header-text button" @click="logOutUser">Log out</button>
          <button v-if="isAdmin" class="header-text button" @click="goToManageDestinations">Manage Destinations</button>
        </div>
      </div>
    </nav>
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router';
import router from '@/router';
import SearchBar from "./SearchBar.vue";
import { useAppStore } from '@/stores/appStore';
import 'primeicons/primeicons.css'
import { ref, watch, watchEffect} from 'vue';
import SearchFilter from '@/DataTypes/SearchFilter';
import { couldStartTrivia } from 'typescript';
getUserLocation();

const userIsLoggedIn = ref<Boolean>(sessionStorage.getItem('token') !== null);
const appStore = useAppStore();
const userName = ref('');
const userEmail = appStore.email ? appStore.email : sessionStorage.getItem('email') ? sessionStorage.getItem('email') : null;
const userRole = ref(appStore.role ? appStore.role : sessionStorage.getItem('role') ? sessionStorage.getItem('role') : null);
const isAdmin = ref(userRole.value === 'admin');

watchEffect(() => {
  if (sessionStorage.getItem('token')) {
    userIsLoggedIn.value = true;
    console.log('User is logged in');
  } else {
    userIsLoggedIn.value = false;
    console.log('User is not logged in');
  }
});


function getSearchFilter(place: string) {
  console.log('Place:', place);
  router.push({ name: 'destinations', query: { filterKey: place } });
}

if (userEmail !== null) {
  userName.value = userEmail.substring(0, userEmail.indexOf('@'));
  if (userName.value.length > 10) {
    userName.value = userName.value.substring(0, 10) + '...';
  }
} else {
  userName.value = 'Unknown';
}

function getUserLocation() {
  if ('geolocation' in navigator) {
    navigator.geolocation.getCurrentPosition(
      function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        console.log('Latitude:', latitude);
        console.log('Longitude:', longitude);
      },
      function (error) {
        console.error('Error getting user location:', error.message);
      }
    );
  } else {
    console.error('Geolocation is not supported by your browser.');
  }
}
const goToManageDestinations = () => {
  router.push('/manage-destinations');
};
const logOutUser = () => {
  appStore.logOutUser();
  sessionStorage.removeItem('token');
  sessionStorage.removeItem('guid');
  sessionStorage.removeItem('role');
  sessionStorage.removeItem('email');

  userIsLoggedIn.value = false;
  appStore.setUserIsLoggedIn(false);
  router.push('/login');
};
</script>

<style scoped>
.button {
  color: #5f9ea0;
}

.button:hover {
  color: black;
}

.header {
  background-color: white;
  position: fixed;
  top: 0;
  justify-content: space-between;
  align-self: center;
  display: flex;
  width: 100%;
  max-width: 100%;
  gap: 200px;
  font-size: 16px;
  color: #1e1e1e;
  font-weight: 400;
  line-height: 29px;
  padding: 11px 0;
}

.searchDiv {
  width: 25%;
}

.search-bar {
  float: right;
  width: 20%;
  overflow: hidden;
  transition: width 0.5s ease;
}

.search-bar:hover {
  width: 100%;
}

@media (max-width: 991px) {
  .div {
    max-width: 100%;
    flex-wrap: wrap;
  }
}

.logo-img {
  object-position: center;
  width: 178px;
  max-width: 100%;
  animation: scaleImage 1s 1s ease-in-out forwards;
}

@keyframes scaleImage {
  from {
    transform: scale(0.5);
  }

  to {
    transform: scale(1.0);
  }
}

nav {
  justify-content: space-between;
  display: flex;
  gap: 10px;
  padding: 10px 20px;
  margin: auto;
  width: 35%;
  margin-right: 1%;
  align-items: center;
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
}

nav a:first-of-type {
  border: 0;
}

.header-text {
  font-size: 1.5rem;
  font-family: Poppins, sans-serif;
  color: #5f9ea0;
}

.sticky {
  position: fixed;
  top: 0;
  width: 100%;
}

.dropbtn {
  background-color: transparent;
  color: black;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0 8px 16px 0 rgb(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #f1f1f1;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.header-dropdown {
  position: relative;
  display: inline-block;
}


.dropdown-content-user button, .dropdown-content-user h3 {
  display: block;
  padding: 10px;
  text-align: left;
}

.dropdown-content-user {
  display: none;
  position: absolute;
  margin-left: -3%;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0 8px 16px 0 rgb(0, 0, 0, 0.2);
  z-index: 1;
}
.dropdown:hover .dropdown-content-user {
  display: block;
}
</style>