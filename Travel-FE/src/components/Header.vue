<script setup lang="ts">
  import {RouterLink, RouterView} from 'vue-router';
  import SearchBar from "./SearchBar.vue";
</script>

<template>
    <div class="header">
      <img
        src="@/assets/ExplorerZ.jpg"
        class="logo-img"
      />
      <nav>
        <div class="searchDiv">
          <div class="search-bar">
            <SearchBar />
          </div>
        </div>
        <RouterLink class="header-text" to="/">Home</RouterLink>
        <div class="dropdown">
        <RouterLink class="header-text" to="/destinations">Destinations</RouterLink>
        <div class="dropdown-content">
          <RouterLink class="header-text" to="/destinations#discounts">Discounts</RouterLink>
        </div>
      </div>
        <RouterLink class="header-text" to="/contact">Contact</RouterLink>
        <RouterLink class="header-text" to="/login">Log in</RouterLink>
      </nav>
    </div>
  </template>
  
  
  
<style scoped>
.header {
background-color : white;
position : fixed;
top : 0;
justify-content : space-between;
align-self : center;
display : flex;
width : 100%;
max-width : 100%;
gap : 200px;
font-size : 16px;
color : #1e1e1e;
font-weight : 400;
line-height : 29px;
padding : 11px 0;
}
.searchDiv {
width : 25%;
}
.search-bar {
float : right;
width : 20%;
overflow : hidden;
transition : width 0.5s ease;
}
.search-bar:hover {
width : 100%;
}
@media (max-width: 991px) {
.div {
max-width : 100%;
flex-wrap : wrap;
}
}
.logo-img {
object-position : center;
width : 178px;
max-width : 100%;
animation : scaleImage 1s 1s ease-in-out forwards;
}
@keyframes scaleImage {
from {
transform : scale(0.5);
}
to {
transform : scale(1.0);
}
}
nav {
justify-content : space-between;
display : flex;
gap : 10px;
padding : 10px 20px;
margin : auto;
width : 35%;
margin-right : 1%;
align-items : center;
}
nav a.router-link-exact-active:hover {
background-color : transparent;
}
nav a {
display : inline-block;
padding : 0 1rem;
}
nav a:first-of-type {
border : 0;
}
.header-text {
font-size : 1.5rem;
font-family : Poppins, sans-serif;
}
.sticky {
position : fixed;
top : 0;
width : 100%;
}
.dropbtn {
background-color : transparent;
color : black;
padding : 16px;
font-size : 16px;
border : none;
cursor : pointer;
}
.dropdown-content {
display : none;
position : absolute;
background-color : #f9f9f9;
min-width : 160px;
box-shadow : 0 8px 16px 0 rgb(0, 0, 0, 0.2);
z-index : 1;
}
.dropdown-content a {
color : black;
padding : 12px 16px;
text-decoration : none;
display : block;
}
.dropdown-content a:hover {
background-color : #f1f1f1;
}
.dropdown:hover .dropdown-content {
display : block;
}
  </style>