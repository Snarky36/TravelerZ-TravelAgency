<template>
    <div class="search-box">
      <v-menu class="calendar"
        v-model="menu"
        :close-on-content-click="false"
        :return-value.sync="selectedDate"
        offset-y
        min-width="290px"
      >
        <template v-slot:activator="">
          <v-text-field class="date-picker"
            v-model="formattedDate"
            label="Select Date"
            readonly
            v-on="on"
            @click="menu = !menu"
          ></v-text-field>
        </template>
        <v-date-picker v-model="selectedDate" no-title></v-date-picker>
      </v-menu>
      <v-text-field class="search-bar" v-model="searchText" label="Search"></v-text-field>
      <v-btn class="search-button" @click="search">Search</v-btn>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, computed } from 'vue';
  
  const selectedDate = ref<Date | null>(null);
  const on = ref<Boolean>(false);
  const searchText = ref<string>('');
  const menu = ref<boolean>(false);
  
  const formattedDate = computed(() => selectedDate.value ? selectedDate.value.toDateString() : '');
  
  const search = () => {
    // Perform search based on selectedDate and searchText
    console.log('Searching...');
  };
  </script>
  
  <style scoped>
  .date-picker{
    background-color: rgb(230, 230, 230);
    margin-left: 5%;
    margin-right: 10px;
    height: 38%;
    color: black;
    font-size: 15px;
  }
  .search-bar{
    margin-left: 10px;
    margin-right: 10px;
    background-color: rgb(230, 230, 230);
    height: 38%;
    color: black;
    font-size: 15px;
  }
  .calendar{
    z-index: 1;
    margin-left: 32%;
    margin-top: 45%;
  }
  .search-box {
    margin-top: 35%;
    display: flex;
    flex-wrap: wrap; 
    align-items: center;
    height: 150px;
    width: 50%;
    background-color: rgba(255, 255, 255, 0.795);
    z-index: 1; 
    border-radius: 5px;
  }
  .search-button{
    height: 60px;
    width: 150px;
    
    margin-left: 10px;
    margin-right: 30px;
    background-color:black;
    color: white;
  }
  </style>
  