<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  imageSrc: String,
  cardTitle: String,
  cardLocation: String,
  cardDescription: String,
  cardBeginDate: String,
  cardEndDate: String,
  cardPrice: Number,
  cardDays: Number,
  displayButton: Boolean
})
</script>

<template>
  <div class="main-card">
    <v-card class="mx-auto" max-width="344" hover>
      <img :src="imageSrc" class="image"></img>
      <v-card-item>
        <v-card-title class="title">{{ cardTitle }}, {{ cardLocation }}</v-card-title>
        <v-card-subtitle class="subtitle">Date: {{ cardBeginDate }} - {{ cardEndDate }}</v-card-subtitle>
      </v-card-item>

      <v-card-text>
        <p>
          {{ cardDescription }}
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's
        </p>
        <br>
        <div class="price-days">
          <span class="price">{{ cardPrice }}$</span>
          <span class="days">{{ cardDays }} days</span>
        </div>
      </v-card-text>
      <v-btn v-if="displayButton" class="cardBtn">See more</v-btn>
    </v-card>
  </div>
</template>


<style scoped>
.cardBtn {
  margin-left: 20%;
  background-color: turquoise;
  margin-top: 10px;
  margin-bottom: 10px;
}

.title {
  font-size: 30px;
}

.subtitle {
  font-size: 20px;
  color: black;
}

.image {
  width: 100%;
  transition: transform 0.5s ease-in-out;
  /* Add transition for width */
}

.image:hover {
  transform: scale(1.1);
}

.main-card {
  margin-top: auto;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.price {
  float: left;
  margin-bottom: 20px;
}

.days {
  float: right;
  margin-bottom: 20px;
}
</style>