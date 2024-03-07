<script setup>
import {defineProps} from 'vue';

const props = defineProps({
    imageSrc: String,
    cardTitle: String,
    cardDescription: String,
    cardBeginDate: String,
    cardEndDate: String,
    cardPrice: Number,
    cardDays: Number
})
</script>

<template>
  <div class="main-card">
    <v-card class="mx-auto" max-width="344" hover>
      <img :src="imageSrc" class="image"></img>
      <v-card-item>
        <v-card-title class="title">{{ cardTitle }}</v-card-title>
        <v-card-subtitle class="subtitle">Date: {{ cardBeginDate }} - {{ cardEndDate }}</v-card-subtitle>
      </v-card-item>

      <v-card-text>
        <p>
          {{ cardDescription }}
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's </p>
        <br>
        <div class="price-days">
          <span class="price">{{ cardPrice }}$</span>
          <span class="days">{{ cardDays }} days</span>
        </div>
      </v-card-text>
    </v-card>
  </div>
</template>


<style scoped>
.title{
  font-size: 30px;
}
.subtitle{
  font-size: 20px;
  color: black;
}
.image{
  width: 100%;
}
.main-card{
  margin-top: auto;
    display: block;
}
.price{
  float: left;
  margin-bottom: 20px;
}
.days{
  float: right;
  margin-bottom: 20px;
}
</style>