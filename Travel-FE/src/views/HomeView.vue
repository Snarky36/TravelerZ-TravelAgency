<script setup lang="ts">
  import TopDestinationsView from '@/views/TopDestinationsView.vue';
  import SearchBox from '../components/SearchBox.vue';
</script>

<template>
  <div class="home-page">
    <div class="title-div">
      <div class="title-text">
        <p>A happy life is a life</p>
        <p class="off-word">OF</p>
      </div>
      <img alt="BackgroundImage" class="img" src="@/assets/Travel-home-background.png"/>
      <SearchBox />
    </div>
    <div class="home-content">
      <TopDestinationsView />
    </div>
  </div>
  
</template>

<style scoped>
.title-div .title-text{
  color: var(--TitleColor, #f5f5f5);
  white-space: nowrap;
  font: 700 72px/120% Poppins, sans-serif;
  z-index: 1;
  margin-top: -40%;
  position: absolute;
}

.title-div .title-text .off-word{
  font: 700 90px/120% Poppins, sans-serif;
  justify-content: center;
  margin-left: 40%;
  margin-top: 10%;
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
.title-text-search {
  position: relative;
  justify-content: space-between;
  display: flex;
  width: 991px;
  max-width: 100%;
  flex-direction: column;
  margin: 86px 0 33px;
  padding: 0 80px;
}
@media (max-width: 991px) {
  .title-text-search {
    margin-top: 40px;
    padding: 0 20px;
  }
}

.home-content{
  justify-content: center;
  align-content: center;
  display: flex;
  margin-top: 30px;
}

</style>