<template>
  <v-card-title v-if="props.boxDisplayTitle" class="title-text-search">{{ props.boxTitle }}</v-card-title>
    <div class="search-box" :style="{ marginTop: props.marginTop }">
      <VueDatePicker 
      v-model="selectedDate" 
      range 
      :enable-time-picker="false" 
      modeHeight="60px"
      class="calendar"/>
      <v-text-field class="search-bar" v-model="searchText" label="Search"></v-text-field>
      <v-btn class="search-button" @click="search">Search</v-btn>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, computed, defineProps } from 'vue';
  const emit = defineEmits(['search', 'submit'])


  const selectedDate = ref<Date | null>(null);
  const on = ref<Boolean>(false);
  const searchText = ref<string>('');
  const menu = ref<boolean>(false);

  const props = defineProps({
    boxTitle: String,
    boxDisplayTitle: Boolean,
    boxFullSearchMode: Boolean,
    marginTop: String
  });
  
  const formattedDate = computed(() => selectedDate.value ? selectedDate.value.toDateString() : '');
  
  const search = () => {
    emit('search', searchText.value);
    console.log('Searching...');
  };
  </script>
  
  <style>
    .dp__input{
      height: 60px;
    }
    .v-field__field{
      background-color: white;
    }
  </style>

  <style scoped>
  .date-picker-popup{
    position: absolute;
    margin-top:50%;
    z-index: 1;
  }
  .title-text-search{
    color: rgb(0, 0, 0);
    font-size: 50px;
    margin-bottom: 10px;
    z-index: 1;
  }
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
    background-color: rgb(255, 255, 255);
    height: 38%;
    color: black;
    font-size: 15px;
  }
  .calendar{
    z-index: 1;
    margin-left:5%;
    width: 30%;
  }
  .search-box {
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
  