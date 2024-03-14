<template>
  <div class="destination-page">
    <div class="title-div">
      <img alt="BackgroundImage" class="img" src="@/assets/TravelDestinations3.jpg" />
      <SearchBox :boxDisplayTitle=true boxTitle="Help Us Find You A Destination" @search="getSearchFilter" />
    </div>
    <div id="searched" class="home-content">
      <DestinationManager Title="All Destinations in one place" :DisplaySeeMoreButton="true" :ItemsPerRaw="3"
        :Filters="searchFilter" />
    </div>
    <div id="discounts" class="home-content">
      <DestinationManager Title="Discounted Destinations" :DisplaySeeMoreButton="true" :ItemsPerRaw="4" />
    </div>
  </div>

</template>

<script setup lang="ts">
import DestinationManager from '@/components/DestinationManager.vue';
import SearchBox from '../components/SearchBox.vue';
import { ref, computed } from 'vue';
import router from '@/router';
import SearchFilter from '@/DataTypes/SearchFilter';

const searchFilter = ref(new SearchFilter());

function getSearchFilter(place: string) {
  searchFilter.value = new SearchFilter(place);
  router.push("/destinations#searched");
}

</script>

<style scoped>
.destination-page {
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
  height: 1000px;
  width: 100%;
  justify-content: center;
  align-items: center;
  padding: 50px 60px;
}

.title-div .img {
  position: absolute;
  inset: 0;
  height: 100%;
  width: 100%;

  object-fit: cover;
  object-position: center;
}

.home-content {
  background-color: #ffffff;
  /* Card background color */
  border-radius: 10px;
  /* Adjust the border radius as needed */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  /* Card shadow */
  padding: 20px;
  padding-bottom: 3%;
  /* Padding inside the card */
  justify-content: center;
  align-content: center;
  display: flex;
  margin-top: 2%;
}
</style>