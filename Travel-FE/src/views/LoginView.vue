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
              <v-text-field class="login-field" label="Username"></v-text-field>
            </div>
            <div class="form-group">
              <v-text-field class ="login-field" type="password" label="Password"></v-text-field>
            </div>
            <v-btn class="button"
                :loading="loading"
                size="large"
                type="submit"
                block
                elevation="4"
                >
                Log in
                </v-btn>
                <br><br>
            <p>Don't you have an account already? Register here</p>
          </form>
          <p v-if="error" class="error-message">{{ error }}</p>
          </div>
        </div>
    </div>
</div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: '',
        error: ''
      };
    },
    methods: {
      login() {
        
        if (this.username === 'example' && this.password === 'password') {
          // Successful login, redirect to dashboard or home page
          this.$router.push('/dashboard');
        } else {
          // Failed login, display error message
          this.error = 'Invalid username or password';
        }
      }
    }
  };
  </script>
  
  <style scoped>

form{
    margin-top: 5%;
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
  object-fit: cover; /* Cover the entire container */
  overflow: hidden;
}

.login-container {
  z-index: 10;
  background-color: #fff;
  display: flex;
  flex-direction: row;
  width: 50%;
  border: 1px solid #ccc;
  border-radius: 10px; /* Add rounded corners */
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* Add box shadow */
}

h1{
    font: 30 40px Poppins, sans-serif;
}
.login-field{
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
  padding: 15px 30px; /* Increase padding for a bigger button */
  background-color: var(--TravelTheme, #5bb0c4); /* Change background color */
  color: #fff; /* Change text color to white */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px; /* Adjust font size */
  }
  
  .button:hover {
  background-color: var(--TravelTheme, #1a9bb8); /* Change background color */
  }
  .error-message {
    color: red;
    margin-top: 10px;
  }
  </style>
  