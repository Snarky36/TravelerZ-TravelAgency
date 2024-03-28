<template>
  <div class="home-page">
    <div class="title-div">
      <div class="title-text">
        <p>A happy life is a life</p>
        <p class="off-word">OF</p>
      </div>
      <img alt="BackgroundImage" class="img" src="@/assets/Travel-home-background.png" />
      <SearchBox :boxDisplayTitle=false marginTop="35%" @search="getSearchFilter" />

    </div>
    <div class="home-content">
      <DestinationManager Title="Destination Packs" :DisplaySeeMoreButton="true" :ItemsPerRaw="3"/>
    </div>
  </div>

</template>

<script setup lang="ts">
import { ref } from 'vue';
import DestinationManager from '../components/DestinationManager.vue';
import SearchBox from '../components/SearchBox.vue';
import SearchFilter from '@/DataTypes/SearchFilter';
import router from '@/router';

const searchFilter = ref(new SearchFilter());

function getSearchFilter(place: string) {
  searchFilter.value = new SearchFilter(place);
  router.push("/destinations#searched");
}

</script>

<style scoped>
.title-div .title-text {
  color: var(--TitleColor, #f5f5f5);
  white-space: nowrap;
  font: 700 72px/120% Poppins, sans-serif;
  z-index: 1;
  margin-top: -33%;
  position: absolute;
}

.title-div .title-text .off-word {
  font: 700 90px/120% Poppins, sans-serif;
  justify-content: center;
  margin-left: 40%;
  margin-top: 7%;
  position: absolute;
}

.home-page {
  justify-content: center;
  align-content: center;
  flex-wrap: wrap;
  background-color: #fff;
  display: flex;
  flex-direction: column;
}

.title-div {
  flex-direction: column;
  overflow: hidden;
  position: relative;
  display: flex;
  min-height: 728px;
  height: 1100px;
  width: 100%;
  justify-content: center;
  align-items: center;
  padding: 50px 60px;
}

@media (max-width: 991px) {
  .title-div {
    max-width: 100%;
    padding: 0 20px;
  }
}

.img {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;

  object-fit: cover;
  object-position: center;
}

@media (max-width: 991px) {
  .title-text-search {
    margin-top: 40px;
    padding: 0 20px;
  }
}

.home-content {
  justify-content: center;
  align-content: center;
  display: flex;
  margin-top: 30px;
}
</style>