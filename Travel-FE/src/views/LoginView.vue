<template>
  <div class="background">
    <div class="login-page">
      <div class="login-container">
        <div class="image-background">
          <img src="../assets/Login.jpg" alt="Travel Image" />
        </div>
        <div class="login-form">
          <h1>Welcome back, Traveler!</h1>
          <form @submit.prevent="login">
            <div class="form-group">
              <v-text-field class="login-field" label="Email" v-model="email"></v-text-field>
            </div>
            <div class="form-group">
              <v-text-field class="login-field" type="password" label="Password" v-model="password"></v-text-field>
            </div>
            <v-btn class="button" size="large" type="submit" block elevation="4">
              Log in
            </v-btn>
            <br><br>
            <p>Don't you have an account already? <router-link class="router-link" to="/register">Register here</router-link></p>
          </form>
          <p v-if="error" class="error-message">{{ error }}</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref } from 'vue';
import { useToast } from 'vue-toast-notification';
import axios from 'axios';
import { useAppStore } from '@/stores/appStore'
import router from '@/router';
import VueJwtDecode from 'vue-jwt-decode';

const appStore = useAppStore();
const $toast = useToast();
const email = ref('');
const password = ref('');
const error = ref('');
const login = () => {
  if (email.value === '' || password.value === '') {
    error.value = 'Email and password are required!';
    showToast("error", "Email and password are required!");
    return;
  }

  axios.post(appStore.getRootUrl() + '/login', {
    email: email.value,
    password: password.value
  })
    .then(response => {
      if (response.status === 200) {
        saveInformations(response.data.token);
        showToast("success", "You have successfully logged in!");
        router.push('/');
      }
    })
    .catch(error => {
      error.value = 'Invalid email or password. Please try again.';
      showToast("error", "Invalid email or password. Please try again.");
    });
};
function showToast(errorType:string, message = '') {
  $toast.open({
    message: message,
    type: errorType,
    position: 'top-right',
  });
}

function saveInformations(token:string) {
  const decoded = VueJwtDecode.decode(token);

  sessionStorage.setItem('token', token);
  sessionStorage.setItem('role', decoded.role);
  sessionStorage.setItem('guid', decoded.guid);
  sessionStorage.setItem('email', email.value);
  
  appStore.setToken(token);
  appStore.setRole(decoded.role);
  appStore.setGuid(decoded.guid);
  appStore.setUserIsLoggedIn(true);
  appStore.setEmail(email.value);
}
</script>



<style scoped>
form {
  margin-top: 5%;
}

.router-link {
  color: #5bb0c4;
}

.login-page {
  background: linear-gradient(to bottom, #5bb0c4, transparent);
  backdrop-filter: blur(10px);
  margin-bottom: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.login-form {
  width: 40%;
  padding: 20px;
  text-align: center;
}

.image-background {
  width: 60%;
  position: relative;
}

.image-background img {
  width: 100%;
  height: 100%;
  position: relative;
  object-fit: cover;
  /* Cover the entire container */
  overflow: hidden;
}

.login-container {
  z-index: 10;
  background-color: #fff;
  display: flex;
  flex-direction: row;
  width: 50%;
  border: 1px solid #ccc;
  border-radius: 10px;
  /* Add rounded corners */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  /* Add box shadow */
}

h1 {
  font: 30 40px Poppins, sans-serif;
}

.login-field {
  margin-bottom: 5%;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 8px;
  border-radius: 3px;
  border: 1px solid #ccc;
}

.button {
  padding: 15px 30px;
  /* Increase padding for a bigger button */
  background-color: var(--TravelTheme, #5bb0c4);
  /* Change background color */
  color: #fff;
  /* Change text color to white */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  /* Adjust font size */
}

.button:hover {
  background-color: var(--TravelTheme, #1a9bb8);
  /* Change background color */
}

.error-message {
  color: red;
  margin-top: 10px;
}
</style>