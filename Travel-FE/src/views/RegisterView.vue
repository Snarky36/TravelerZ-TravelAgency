<template>
  <div class="background">
    <div class="register-page">
      <div class="register-container">
        <div class="image-background">
          <img src="../assets/register-image.jpg" alt="Travel Image" />
        </div>
        <div class="register-form">
          <h1>Create an Account</h1>
          <p v-if="error" class="error-message">{{ error }}</p>
          <form @submit.prevent="register">
            <div class="form-group">
              <v-text-field class="register-field" label="Full Name" v-model="username"
                @input="resetError"></v-text-field>
            </div>
            <div class="form-group">
              <v-text-field class="register-field" label="Email" v-model="email" @input="resetError"></v-text-field>
            </div>
            <div class="form-group">
              <v-text-field class="register-field" type="password" label="Password" v-model="password"
                @input="resetError"></v-text-field>
            </div>
            <div class="form-group">
              <v-text-field class="register-field" type="password" label="Repeat Password" v-model="repeatPassword"
                @input="resetError"></v-text-field>
            </div>
            <v-btn class="button" size="large" type="submit" block elevation="4">
              Register
            </v-btn>
            <p>Already have an account? <router-link class="router-link" to="/login">Log in here</router-link></p>
          </form>

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
const username = ref('');
const password = ref('');
const repeatPassword = ref('');
const error = ref('');

const resetError = () => {
  if (error.value !== '') {
    error.value = '';
  }
};

const register = () => {
  const regex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  if (password.value !== repeatPassword.value) {
    error.value = 'Passwords do not match! Please try again.';
    showToast("error", "Passwords do not match! Please try again.");
    return;
  }
  if (email.value.match(regex) === null) {
    error.value = 'Invalid email address! Please try again.';
    showToast("error", "Invalid email address! Please try again.");
    return;
  }
  if (username.value === '' || password.value === '' || repeatPassword.value === '' || email.value === '') {
    error.value = 'All fields are required!';
    showToast("error", "All fields are required!");
    return;
  }

  axios.post(appStore.getRootUrl() + '/register', {
    name: username.value,
    email: email.value,
    password: password.value
  })
    .then(response => {
      if (response.status === 200) {
        saveInformations(response.data.token);
        showToast("success", "You have successfully registered!");
        router.push('login');
      }
    })
    .catch(error => {
      error.value = 'An error occurred during registration. Please try again.';
    });
  
  function showToast(errorType:string, message = '') {
      $toast.open({
        message: message,
        type: errorType,
        position: 'top-right',
      });
  }

  function saveInformations(token:string) {
    console.log(token);
    const decoded = VueJwtDecode.decode(token);
    console.log(decoded.role);
    console.log(decoded.guid);
    
    sessionStorage.setItem('token', token);
    sessionStorage.setItem('role', decoded.role);
    sessionStorage.setItem('guid', decoded.guid);

    appStore.setToken(token);
    appStore.setRole(decoded.role);
    appStore.setGuid(decoded.guid);
  }
};
</script>


<style scoped>
p {
  margin-top: 5%;
}

form {
  margin-top: 5%;
}

.router-link {
  color:  #5bb0c4;
}

.register-page {
  background: linear-gradient(to bottom, #5bb0c4, transparent);
  backdrop-filter: blur(10px);
  margin-bottom: 2%;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.register-form {
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

.register-container {
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

.register-field {
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